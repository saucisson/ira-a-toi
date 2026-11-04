"""Tests du contrat d'œuvre (schéma v1.1) — unittest, zéro dépendance.

Lancement :  python -m unittest discover -s tests -v
(ou : python tests/test_contrat.py)

Les invariants mécaniques tournent partout ; les tests des modèles
Pydantic s'ignorent proprement si pydantic est absent.
"""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "contrat"))
sys.path.insert(0, str(RACINE / "ci"))

from pack import (  # noqa: E402
    ErreurCI,
    PYDANTIC,
    condition_satisfaite,
    invariants_ci,
    rendre_fragment,
)
from valider_pack import charger_pack  # noqa: E402

DOSSIER_HORLA = RACINE / "oeuvres" / "le-horla-maupassant-1887"


class TestChargeur(unittest.TestCase):
    """Le dossier d'œuvre s'assemble et ses invariants tiennent."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.pack, cls.source = charger_pack(DOSSIER_HORLA)

    def test_invariants_ok(self) -> None:
        rapport = invariants_ci(self.pack, self.source)
        self.assertEqual(len(rapport), 7)

    def test_slug_valide(self) -> None:
        self.assertEqual(self.pack["manifeste"]["id"], "le-horla-maupassant-1887")


class TestInvariantsNegatifs(unittest.TestCase):
    """Chaque invariant doit mordre — sinon il ne sert à rien."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.pack, cls.source = charger_pack(DOSSIER_HORLA)

    def _refuse(self, mutation, fragment_msg="") -> None:
        pack = copy.deepcopy(self.pack)
        mutation(pack)
        with self.assertRaises(ErreurCI):
            invariants_ci(pack, self.source)

    def test_alteration_d_un_caractere(self) -> None:
        def m(p):  # noqa: ANN001
            p["fragments"][0]["texte"] = p["fragments"][0]["texte"].replace("admirable", "ADMIRABLE", 1)

        self._refuse(m)

    def test_hash_mensonger(self) -> None:
        def m(p):  # noqa: ANN001
            p["manifeste"]["hash_source"] = "0" * 64

        self._refuse(m)

    def test_cadence_incomplete(self) -> None:
        def m(p):  # noqa: ANN001
            del p["cadences"][0]["regles"]["entree-18-mai"]

        self._refuse(m)

    def test_mot_a_corrompre_absent(self) -> None:
        def m(p):  # noqa: ANN001
            p["fragments"][3]["etats"][0]["remplacements"][0]["cherche"] = "orthographe"

        self._refuse(m)

    def test_id_non_slug(self) -> None:
        def m(p):  # noqa: ANN001
            p["manifeste"]["id"] = "Le Horla (Ollendorff)"

        self._refuse(m)

    def test_condition_vers_etat_inconnu(self) -> None:
        def m(p):  # noqa: ANN001
            p["gestes"][2]["condition"] = "nuit-troublee"

        self._refuse(m)

    def test_effet_vers_etat_inconnu(self) -> None:
        def m(p):  # noqa: ANN001
            p["gestes"][1]["effets"] = ["a-pleure"]

        self._refuse(m)

    def test_miroir_vers_non_ecriture(self) -> None:
        def m(p):  # noqa: ANN001
            p["fragments"][4]["etats"][0]["miroir"] = "saluer-le-brésilien"

        self._refuse(m)

    def test_trouver_vers_mot_non_corrompu(self) -> None:
        def m(p):  # noqa: ANN001
            p["gestes"][2]["cible"] = "navire"

        self._refuse(m)

    def test_geste_orphelin(self) -> None:
        def m(p):  # noqa: ANN001
            p["gestes"][0]["fragment_id"] = "entree-99-juin"

        self._refuse(m)


class TestConditions(unittest.TestCase):
    """La grammaire des conditions : <état>, !<état>, relu, None."""

    def test_none_toujours_vrai(self) -> None:
        self.assertTrue(condition_satisfaite(None, set(), relu=False))

    def test_etat_present(self) -> None:
        self.assertTrue(condition_satisfaite("a-ecrit", {"a-ecrit"}, relu=False))
        self.assertFalse(condition_satisfaite("a-ecrit", set(), relu=False))

    def test_negation(self) -> None:
        self.assertTrue(condition_satisfaite("!a-ecrit", set(), relu=False))
        self.assertFalse(condition_satisfaite("!a-ecrit", {"a-ecrit"}, relu=False))

    def test_releu(self) -> None:
        self.assertTrue(condition_satisfaite("relu", set(), relu=True))
        self.assertFalse(condition_satisfaite("relu", set(), relu=False))


class TestRendu(unittest.TestCase):
    """texte_affiché = texte_source + états actifs — corruption et miroir."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.pack, cls.source = charger_pack(DOSSIER_HORLA)
        cls.frag = {f["id"]: f for f in cls.pack["fragments"]}

    def test_premiere_lecture_intacte(self) -> None:
        rendu = rendre_fragment(self.frag["entree-18-mai"], etats=set(), relu=False)
        self.assertIn("je ne pouvais plus dormir", rendu["texte"])
        self.assertEqual(rendu["miroirs"], [])

    def test_corruption_au_second_affichage(self) -> None:
        rendu = rendre_fragment(self.frag["entree-18-mai"], etats=set(), relu=True)
        self.assertIn("je ne pouvais plus me réveiller", rendu["texte"])
        self.assertNotIn("dormir", rendu["texte"])
        self.assertEqual(rendu["miroirs"], [])

    def test_miroir_actif_si_ecrit(self) -> None:
        rendu = rendre_fragment(self.frag["entree-25-mai"], etats={"a-ecrit"}, relu=False)
        self.assertEqual(rendu["miroirs"], ["ecrire-la-nuit"])
        # le texte source, lui, ne change jamais
        self.assertEqual(rendu["texte"], self.frag["entree-25-mai"]["texte"])

    def test_miroir_inactif_sans_ecriture(self) -> None:
        rendu = rendre_fragment(self.frag["entree-25-mai"], etats=set(), relu=False)
        self.assertEqual(rendu["miroirs"], [])


@unittest.skipUnless(PYDANTIC, "pydantic absent — validation des modèles ignorée")
class TestModelesPydantic(unittest.TestCase):
    """Le pack de démonstration passe Pack.model_validate()."""

    def test_validation(self) -> None:
        pack, source = charger_pack(DOSSIER_HORLA)
        from pack import Pack  # noqa: PLC0415

        Pack.model_validate(pack)


if __name__ == "__main__":
    unittest.main(verbosity=2)
