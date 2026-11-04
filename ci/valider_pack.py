"""CI : valider un pack d'œuvre avant publication CDN.

Usage :
    python ci/valider_pack.py <dossier-du-pack>

Exemple :
    python ci/valider_pack.py oeuvres/le-horla-maupassant-1887

Le dossier du pack contient : manifeste.json, source.txt,
fragments.json, publication.json, interactions.json,
enrichissements.json. La sortie non nulle casse le build :
aucun pack invalide ne part sur le CDN.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "contrat"))

from pack import ErreurCI, Pack, PYDANTIC, invariants_ci  # noqa: E402


def charger_pack(dossier: Path) -> tuple[dict, str]:
    """Assemble le dossier d'œuvre en un `pack` (dict) + son texte source."""
    manifeste = json.loads((dossier / "manifeste.json").read_text(encoding="utf-8"))
    fragments = json.loads((dossier / "fragments.json").read_text(encoding="utf-8"))
    publication = json.loads((dossier / "publication.json").read_text(encoding="utf-8"))
    interactions = json.loads((dossier / "interactions.json").read_text(encoding="utf-8"))
    enrichissements = json.loads((dossier / "enrichissements.json").read_text(encoding="utf-8"))
    source_txt = (dossier / "source.txt").read_text(encoding="utf-8")

    pack = {
        "manifeste": manifeste,
        "fragments": fragments["fragments"],
        "cadences": publication["cadences"],
        "etats_joueur": interactions.get("etats_joueur", []),
        "gestes": interactions.get("gestes", []),
        "fins": interactions.get("fins", []),
        "enrichissements": enrichissements["enrichissements"],
    }
    return pack, source_txt


def main(argv: list[str]) -> int:
    """Entry point for the CI validation script."""
    expected_arg_count = 2
    if len(argv) != expected_arg_count:
        print(__doc__)
        return 2
    dossier = Path(argv[1])
    if not dossier.is_dir():
        print(f"dossier introuvable : {dossier}")
        return 2

    pack, source_txt = charger_pack(dossier)

    try:
        rapport = invariants_ci(pack, source_txt)
    except ErreurCI as erreur:
        print(f"✗ {dossier.name} REFUSÉ : {erreur}")
        return 1

    print(f"CI — {dossier.name}")
    print("=" * 78)
    for ligne in rapport:
        print(f"  OK — {ligne}")

    if PYDANTIC:
        Pack.model_validate(pack)
        print("  OK — modèles Pydantic : Pack.model_validate() passe")
    else:
        print("  ·   pydantic absent : CI mécanique seule (le pack reste vérifié)")

    print("=" * 78)
    print(f"✓ {dossier.name} PRÊT POUR PUBLICATION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
