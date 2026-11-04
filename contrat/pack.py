"""
contrat.pack — le contrat d'œuvre de « Ira à toi » (schéma v1.1).

Une œuvre est un dossier Git publié tel quel sur le CDN (immuable) ;
le serveur n'enregistre que sa version, le client télécharge ce dont il
a besoin. Ce module sert trois usages :

1. la CI (ci/valider_pack.py) vérifie le pack avant publication ;
2. le serveur (FastAPI) y type la version enregistrée — jamais le texte ;
3. l'atelier de validation du designer narratif rend le même schéma.

Règles fondatrices du projet :
- le moteur interprète, il ne contient rien ;
- le LLM ne réécrit jamais le texte source (diff CI au caractère près) ;
- l'horloge diégétique n'avance qu'avec son lecteur ;
- la fiction recule, jamais elle ne ment ;
- le corps de lecture est partagé ; la peau typographique est de la
  mise en scène (display uniquement, licences OFL) ;
- rien n'analyse le téléphone : le Horla simule la surveillance,
  il ne l'instrumente jamais.

v1.1 (ajouts optionnels, sans rupture) : micro-interactions —
registre d'états du joueur, gestes (action / choix / ecriture /
trouver), grammaire des conditions (<état>, !<état>, relu), états de
rendu (corruption au second affichage) et miroir (écho mot pour mot
du carnet — jamais analysé).
"""

from __future__ import annotations

import hashlib
import re
from datetime import date, datetime, time
from enum import StrEnum
from typing import Literal, Self

try:
    from pydantic import BaseModel, Field, model_validator

    PYDANTIC = True
except ImportError:
    # Mode CI mécanique : vérifier un pack sans les modèles.
    # La vérification anti-altération ne doit dépendre d'aucun modèle —
    # les définitions deviennent inertes, seul le contrôle pur fonctionne.
    PYDANTIC = False

    BaseModel = object  # type: ignore[assignment,misc]

    def Field(*_args, **_kwargs):  # type: ignore[misc]
        return None

    def model_validator(*_args, **_kwargs):  # type: ignore[misc]
        def _identity(fn):
            return fn

        return _identity


_SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

MOT_CLE_RELU = "relu"  # condition intégrée : le fragment a déjà été lu


# ------------------------------------------------------------------ #
# Lignes & horloges                                                   #
# ------------------------------------------------------------------ #


class Ligne(StrEnum):
    """Une ligne de collection par canal d'origine de la littérature."""

    cabinet_fantastique = "cabinet-fantastique"  # le journal intime
    correspondances = "correspondances"  # la lettre
    feuilleton = "feuilleton"  # le roman-feuilleton


class Horloge(StrEnum):
    """Sémantique d'ancrage du temps d'une partie."""

    personnelle = "personnelle"  # due_at = g(lu_à, règle, contraintes)
    commune = "commune"  # calendrier de saison, partagé par tous


# ------------------------------------------------------------------ #
# Manifeste : identité & édition                                      #
# ------------------------------------------------------------------ #


class Auteur(BaseModel):
    slug: str
    nom: str
    naissance: date
    mort: date  # plus de 70 ans : la preuve de domaine public voyage avec l'œuvre


class SourceOriginelle(BaseModel):
    support: str  # "Recueil Le Horla, P. Ollendorff (mai 1887)"
    publication: date
    url: str  # Gallica / Wikisource — la source transcrite


class PoliceDisplay(BaseModel):
    """Police de mise en scène — display uniquement, licence OFL.

    Le corps de lecture n'apparaît jamais ici : il est partagé par
    toute la collection (« une seule police de lecture, mille polices
    de mise en scène »).
    """

    usage: str  # "dates", "titres", "cachets"
    fichier: str  # "assets/fonts/…"
    licence: str = "OFL"


class PeauTypographique(BaseModel):
    display: list[PoliceDisplay] = []
    palette: dict[str, str] = {}  # {"encre": "#1f1a15", "papier": "#f2e9d8"}


class Sensibilites(BaseModel):
    push_nuit: bool = False  # Horla : opt-in explicite, prévisualisé
    avertissement: str | None = None
    public: str = "tous"


class Manifeste(BaseModel):
    """Identité & édition. Le manifeste fait la fiche : la vitrine web,
    le cabinet et le dossier de financement lisent le même fichier."""

    schema_version: Literal[1] = 1
    id: str  # <titre>-<auteur>-<année> : le-horla-maupassant-1887
    titre: str
    edition: str  # "Version définitive (1887)" / "Gil Blas (1886)"
    ligne: Ligne
    horloge: Horloge
    auteur: Auteur
    source: SourceOriginelle
    annee_originelle: int = Field(ge=1400, le=2100)
    pitch: str  # « Si tu ne vas pas au Horla, le Horla ira à toi. »
    sensibilites: Sensibilites = Sensibilites()
    peau: PeauTypographique = PeauTypographique()
    couverture: str  # "assets/couverture.png"
    credits: list[str] = []
    hash_source: str = Field(pattern=r"^[0-9a-f]{64}$")  # sha256 de source.txt
    separateur_fragments: str = "\n\n"  # joint par la CI pour le diff anti-altération

    @model_validator(mode="after")
    def _id_est_un_slug(self) -> Self:
        if not _SLUG.match(self.id):
            raise ValueError(f"id de pack invalide (slug attendu) : {self.id!r}")
        return self


# ------------------------------------------------------------------ #
# Micro-interactions : registre d'états, gestes, conditions            #
# ------------------------------------------------------------------ #


class EtatJoueur(BaseModel):
    """Un état du joueur — le seul registre d'interaction de la partie.

    Les états sont posés par des gestes et consommés par des
    conditions ; toute référence à un état non déclaré fait échouer
    la CI (aucune faute de frappe silencieuse).
    """

    id: str
    description: str = ""


def condition_satisfaite(condition: str | None, etats: set[str], relu: bool = False) -> bool:
    """Grammaire des conditions : `<état>`, `!< état>` (négation), ou le
    mot-clé `relu` (le fragment a déjà été lu au moins une fois).
    `None` = toujours vrai.

    La fiction répond par conditions, jamais par scripts : « le cœur du
    récit est inamovible, la marge est jouable » devient une grammaire.
    """
    if condition is None:
        return True
    if condition == MOT_CLE_RELU:
        return relu
    if condition.startswith("!"):
        return condition[1:] not in etats
    return condition in etats


def _refs_condition(condition: str | None) -> list[str]:
    """Les états référencés par une condition (le mot-clé `relu` n'en réfère aucun)."""
    if condition is None or condition == MOT_CLE_RELU:
        return []
    return [condition[1:]] if condition.startswith("!") else [condition]


class Ecriture(BaseModel):
    """Le carnet : ce que le joueur écrit n'est jamais analysé — ni LLM,
    ni capteur. Conservé mot pour mot avec la partie ; au besoin, le
    miroir le rend en annotation (voir Etat.miroir)."""

    max_caracteres: int = Field(default=500, ge=1, le=2000)


class Choix(BaseModel):
    id: str
    libelle: str
    effets: list[str] = []  # ids d'états joueur


class Geste(BaseModel):
    """Mécanique signature — déclarée dans le pack, jamais codée dans le moteur.

    `condition` règle la disponibilité (grammaire des conditions) ;
    `effets` pose les états. Les conséquences vivent dans les états de
    rendu conditionnés des fragments suivants : la fiction recule,
    jamais elle ne ment — sans état, le texte original s'affiche.
    """

    id: str
    fragment_id: str
    type: Literal["action", "choix", "ecriture", "trouver"] = "action"
    condition: str | None = None
    invite: str
    choix: list[Choix] = []
    cible: str | None = None  # type trouver : le mot corrompu à repérer
    ecriture: Ecriture | None = None  # type ecriture
    effets: list[str] = []


class Remplacement(BaseModel):
    """Un mot du texte original et sa version corrompue, rendue à l'écran.

    Le texte source n'est jamais altéré : la corruption est un état de
    rendu, calculé depuis les états du joueur. CI : `cherche` doit
    exister dans le fragment ; `remplace_par` peut être la cible d'un
    geste `trouver`.
    """

    cherche: str
    remplace_par: str


class Etat(BaseModel):
    """Un état de rendu d'un fragment.

    `condition` active l'état (grammaire des conditions — typiquement
    `relu` pour la corruption au second affichage, ou un état joueur).
    `miroir` rend, en annotation jamais mêlée au texte source, les
    propres mots du joueur confiés au geste d'écriture référencé :
    le Horla ne vous lit pas, il vous rend ce que vous lui avez confié.
    """

    id: str
    condition: str | None = None
    remplacements: list[Remplacement] = []
    miroir: str | None = None


class AncrageFictif(BaseModel):
    """Où le fragment vit dans la fiction (le journal n'utilise pas ISO)."""

    date_fictive: str | None = None  # "8 mai"
    lettre: str | None = None  # Correspondances : "lettre-71"
    chapitre: int | None = None  # Feuilleton : 117 chapitres

    @model_validator(mode="after")
    def _au_moins_un(self) -> Self:
        if self.date_fictive is None and self.lettre is None and self.chapitre is None:
            raise ValueError("ancrage fictif manquant (date, lettre ou chapitre)")
        return self


class Fragment(BaseModel):
    id: str  # "entree-08-mai"
    ancrage_fictif: AncrageFictif
    texte: str  # découpe exacte de source.txt
    duree_lecture_s: int = Field(ge=10)  # estimation, pour l'atelier
    etats: list[Etat] = []
    enrichissements: list[str] = []  # ids vers Enrichissement


# ------------------------------------------------------------------ #
# Publication : les horaires diégétiques                              #
# ------------------------------------------------------------------ #


class PlageHoraire(BaseModel):
    debut: time
    fin: time


class RegleEnvoi(BaseModel):
    """Règle d'envoi relative — horloge personnelle.

    due_at(next) = g(lu_à(courant), règle, contraintes du lecteur).
    La règle donne le delta de l'œuvre ; l'ancre (la dernière lecture)
    et les contraintes (fuseau, opt-in nuit) appartiennent à la partie.
    « La fiction recule, jamais elle ne ment » : si l'heure diégétique
    est déjà passée, l'ordonnanceur prend le prochain créneau plausible.
    """

    ancre: Literal["t0", "lecture-precedente"] = "lecture-precedente"
    decalage_jours: int = Field(default=0, ge=0, le=7)
    heure: time | None = None  # heure diégétique précise : 23:12
    plage: PlageHoraire | None = None  # ou fenêtre : 08:00–10:00
    jitter_minutes: int = Field(default=0, ge=0, le=30)  # l'heure ne se sent pas mécanique
    repli_sans_optin_nuit: PlageHoraire | None = None  # 08:00–10:00
    push: bool = True  # False : disponible in-app seulement
    titre_notification: str | None = None  # bandeau non spoilant

    @model_validator(mode="after")
    def _heure_ou_plage(self) -> Self:
        if self.heure is not None and self.plage is not None:
            raise ValueError("règle d'envoi : `heure` et `plage` sont exclusifs")
        if self.push and self.heure is None and self.plage is None:
            raise ValueError("règle d'envoi : un push demande `heure` ou `plage`")
        return self


class EnvoiCommun(BaseModel):
    """Horloge commune (Feuilleton) : 17 h précises pour toute la communauté."""

    fragment_id: str
    moment: datetime  # UTC — le salon n'attend personne


class Cadence(BaseModel):
    """Une cadence nommée du pack : standard, sprint, 1844…

    Choisir un rythme, c'est choisir une cadence — les rythmes sont des
    données, pas du code.
    """

    id: str
    description: str = ""
    regles: dict[str, RegleEnvoi] = {}  # horloge personnelle : fragment_id → règle
    calendrier: list[EnvoiCommun] = []  # horloge commune

    @model_validator(mode="after")
    def _regles_ou_calendrier(self) -> Self:
        if bool(self.regles) == bool(self.calendrier):
            raise ValueError(f"cadence {self.id!r} : `regles` OU `calendrier`, jamais les deux ni aucune")
        return self


# ------------------------------------------------------------------ #
# Fins & enrichissements                                              #
# ------------------------------------------------------------------ #


class Fin(BaseModel):
    id: str
    libelle: str
    fragment_id: str
    authenticite: str | None = None  # « Véritable fin de la version 1886 (Gil Blas) »
    desinstallation: bool = False  # le geste novateur : brûler le journal
    cendre: str | None = None  # asset de l'épitaphe partageable


class Enrichissement(BaseModel):
    """Note, fiche ou lexique — traçable : « généré puis validé »."""

    id: str
    type: Literal["fiche-personnage", "lexique", "note"] = "note"
    titre: str
    contenu: str
    genere_par_ia: bool = False
    valide_par: str | None = None


# ------------------------------------------------------------------ #
# Le pack                                                              #
# ------------------------------------------------------------------ #


class Pack(BaseModel):
    """Le dossier d'œuvre complet, validé par la CI avant publication CDN."""

    manifeste: Manifeste
    fragments: list[Fragment] = Field(min_length=1)
    cadences: list[Cadence] = Field(min_length=1)
    etats_joueur: list[EtatJoueur] = []
    gestes: list[Geste] = []
    fins: list[Fin] = []
    enrichissements: list[Enrichissement] = []

    @model_validator(mode="after")
    def _invariants_pack(self) -> Self:
        ids = [f.id for f in self.fragments]
        frag = {f.id: f for f in self.fragments}
        if len(ids) != len(set(ids)):
            doublons = sorted({i for i in ids if ids.count(i) > 1})
            raise ValueError(f"fragments en doublon : {doublons}")

        # Chaque cadence respecte l'horloge de l'œuvre et couvre exactement
        # les fragments : aucun fragment orphelin, aucun envoi sans fragment.
        for c in self.cadences:
            if bool(c.regles) != (self.manifeste.horloge is Horloge.personnelle):
                raise ValueError(
                    f"cadence {c.id!r} : incohérente avec l'horloge "
                    f"{self.manifeste.horloge.value!r} du manifeste"
                )
            if c.regles:
                orphelins = set(c.regles) - set(frag)
                manquants = set(frag) - set(c.regles)
                if orphelins or manquants:
                    raise ValueError(
                        f"cadence {c.id!r} : envois sans fragment {sorted(orphelins)} ; "
                        f"fragments sans envoi {sorted(manquants)}"
                    )
            else:
                cal = [e.fragment_id for e in c.calendrier]
                if len(cal) != len(set(cal)) or set(cal) != set(frag):
                    raise ValueError(f"cadence {c.id!r} : le calendrier ne couvre pas exactement les fragments")

        # On ne réécrit pas Maupassant : les mots à corrompre existent dans le fragment.
        for f in self.fragments:
            for et in f.etats:
                for r in et.remplacements:
                    if r.cherche not in f.texte:
                        raise ValueError(
                            f"état {et.id!r} : le mot {r.cherche!r} n'existe pas dans "
                            f"le fragment {f.id!r} — la corruption est un état de rendu, pas une réécriture"
                        )

        registre = {e.id for e in self.etats_joueur}
        ecritures = {g.id for g in self.gestes if g.type == "ecriture"}

        # Conditions et effets pointent vers des états déclarés — jamais de faute de frappe silencieuse.
        for f in self.fragments:
            for et in f.etats:
                for ref in _refs_condition(et.condition):
                    if ref not in registre:
                        raise ValueError(f"état {et.id!r} (fragment {f.id!r}) : état joueur inconnu {ref!r}")
        for g in self.gestes:
            for ref in _refs_condition(g.condition) + list(g.effets):
                if ref not in registre:
                    raise ValueError(f"geste {g.id!r} : état joueur inconnu {ref!r}")
            for ch in g.choix:
                for ref in ch.effets:
                    if ref not in registre:
                        raise ValueError(f"geste {g.id!r}, choix {ch.id!r} : état joueur inconnu {ref!r}")

        # Le miroir renvoie du texte confié à un geste d'écriture.
        for f in self.fragments:
            for et in f.etats:
                if et.miroir is not None and et.miroir not in ecritures:
                    raise ValueError(
                        f"état {et.id!r} : le miroir doit référencer un geste d'écriture, pas {et.miroir!r}"
                    )

        # Le geste `trouver` vise un mot corrompu déclaré dans le fragment.
        for g in self.gestes:
            if g.type == "trouver":
                f = frag.get(g.fragment_id)
                cibles = {r.remplace_par for et in f.etats for r in et.remplacements} if f else set()
                if g.cible not in cibles:
                    raise ValueError(
                        f"geste {g.id!r} : la cible {g.cible!r} n'est pas un mot corrompu du fragment {g.fragment_id!r}"
                    )

        for g in self.gestes:
            if g.fragment_id not in frag:
                raise ValueError(f"geste {g.id!r} : fragment inconnu {g.fragment_id!r}")
        for fin in self.fins:
            if fin.fragment_id not in frag:
                raise ValueError(f"fin {fin.id!r} : fragment inconnu {fin.fragment_id!r}")
        ids_enr = {e.id for e in self.enrichissements}
        for f in self.fragments:
            for eid in f.enrichissements:
                if eid not in ids_enr:
                    raise ValueError(f"fragment {f.id!r} : enrichissement inconnu {eid!r}")
        return self

    def texte_reconstitue(self) -> str:
        """Concaténation des fragments — doit reproduire source.txt au caractère près."""
        sep = self.manifeste.separateur_fragments
        return sep.join(f.texte for f in self.fragments)


# ------------------------------------------------------------------ #
# Le rendu : texte affiché = texte source + états actifs              #
# ------------------------------------------------------------------ #


def rendre_fragment(fragment: dict, *, etats: set[str], relu: bool = False) -> dict:
    """Rendu client — pure fonction, partagée par la PWA et l'atelier :
    ce qu'on valide à l'atelier est exactement ce que voit le joueur.

    Applique les remplacements des états actifs (conditions satisfaites)
    et signale les miroirs à rendre en annotation. Le texte source, lui,
    ne change jamais.
    """
    texte = fragment["texte"]
    miroirs: list[str] = []
    for etat in fragment.get("etats", []):
        if not condition_satisfaite(etat.get("condition"), etats, relu):
            continue
        for r in etat.get("remplacements", []):
            if r["cherche"] not in texte:
                raise ErreurCI(
                    f"état {etat['id']!r} : {r['cherche']!r} absent du fragment {fragment['id']!r} — la CI l'aurait refusé"
                )
            texte = texte.replace(r["cherche"], r["remplace_par"], 1)
        if etat.get("miroir"):
            miroirs.append(etat["miroir"])
    return {"texte": texte, "miroirs": miroirs}


# ------------------------------------------------------------------ #
# La CI mécanique — dicts purs, zéro dépendance                       #
# ------------------------------------------------------------------ #


class ErreurCI(Exception):
    """Un invariant du pack est violé : le build échoue."""


def invariants_ci(pack: dict, source_txt: str) -> list[str]:
    """Les contrôles mécaniques de la CI, sur dicts purs.

    La vérification anti-altération ne dépend d'aucun modèle : elle est
    mécanique, au caractère près. (Les mêmes règles sont redondamment
    portées par le modèle Pack — la ceinture et les bretelles.)
    """
    man = pack["manifeste"]
    fragments = pack["fragments"]
    sep = man.get("separateur_fragments", "\n\n")
    rapport: list[str] = []

    # 1. Anti-altération : concaténation == source, au caractère près.
    reconstitue = sep.join(f["texte"] for f in fragments)
    if reconstitue != source_txt:
        raise ErreurCI("ALTÉRATION : la concaténation des fragments != source.txt")
    rapport.append("anti-altération : la concaténation des fragments reproduit la source au caractère près")

    digest = hashlib.sha256(source_txt.encode("utf-8")).hexdigest()
    if digest != man["hash_source"]:
        raise ErreurCI(f"HASH SOURCE : manifeste={man['hash_source']} réel={digest}")
    rapport.append(f"hash source : sha256 vérifié ({digest[:12]}…)")

    # 2. Identité : un id est un slug, pas un titre.
    if not _SLUG.match(man["id"]):
        raise ErreurCI(f"id de pack invalide (slug attendu) : {man['id']!r}")
    rapport.append(f"identité : {man['id']} (slug valide, immuable une fois publié)")

    # 3. Fragments uniques ; les mots à corrompre existent dans le texte.
    ids = [f["id"] for f in fragments]
    if len(ids) != len(set(ids)):
        raise ErreurCI(f"fragments en doublon : {sorted({i for i in ids if ids.count(i) > 1})}")
    for f in fragments:
        for et in f.get("etats", []):
            for r in et.get("remplacements", []):
                if r["cherche"] not in f["texte"]:
                    raise ErreurCI(
                        f"état {et['id']!r} : le mot {r['cherche']!r} n'existe pas dans le fragment {f['id']!r}"
                    )
    rapport.append(f"fragments : {len(ids)} ids uniques ; états de rendu ancrés dans le texte")

    # 4. Chaque cadence couvre exactement les fragments.
    for c in pack["cadences"]:
        if c.get("regles"):
            manquants = set(ids) - set(c["regles"])
            orphelins = set(c["regles"]) - set(ids)
            if manquants or orphelins:
                raise ErreurCI(
                    f"cadence {c['id']!r} : fragments sans envoi {sorted(manquants)} ; envois sans fragment {sorted(orphelins)}"
                )
        else:
            cal = [e["fragment_id"] for e in c["calendrier"]]
            if len(cal) != len(set(cal)) or set(cal) != set(ids):
                raise ErreurCI(f"cadence {c['id']!r} : le calendrier ne couvre pas exactement les fragments")
    rapport.append(f"cadences : {len(pack['cadences'])} cadences couvrent exactement les {len(ids)} fragments")

    # 5. Gestes, fins et enrichissements pointent vers des objets existants.
    for g in pack.get("gestes", []):
        if g["fragment_id"] not in ids:
            raise ErreurCI(f"geste {g['id']!r} : fragment inconnu {g['fragment_id']!r}")
    for fin in pack.get("fins", []):
        if fin["fragment_id"] not in ids:
            raise ErreurCI(f"fin {fin['id']!r} : fragment inconnu {fin['fragment_id']!r}")
    ids_enr = {e["id"] for e in pack.get("enrichissements", [])}
    for f in fragments:
        for eid in f.get("enrichissements", []):
            if eid not in ids_enr:
                raise ErreurCI(f"fragment {f['id']!r} : enrichissement inconnu {eid!r}")
    rapport.append("références : gestes, fins et enrichissements pointent vers des objets du pack")

    # 6. Micro-interactions : conditions et effets pointent vers des états déclarés ;
    #    le miroir renvoie vers un geste d'écriture ; `trouver` vise un mot corrompu.
    registre = {e["id"] for e in pack.get("etats_joueur", [])}
    if len(registre) != len(pack.get("etats_joueur", [])):
        raise ErreurCI("registre d'états joueur : ids en doublon")
    ecritures = {g["id"] for g in pack.get("gestes", []) if g.get("type") == "ecriture"}
    frag_by_id = {f["id"]: f for f in fragments}

    def _refs(cond: str | None) -> list[str]:
        return _refs_condition(cond)

    for f in fragments:
        for et in f.get("etats", []):
            for ref in _refs(et.get("condition")):
                if ref not in registre:
                    raise ErreurCI(f"état {et['id']!r} : état joueur inconnu {ref!r}")
            if et.get("miroir") and et["miroir"] not in ecritures:
                raise ErreurCI(f"état {et['id']!r} : le miroir doit référencer un geste d'écriture, pas {et['miroir']!r}")
    for g in pack.get("gestes", []):
        for ref in _refs(g.get("condition")) + list(g.get("effets", [])):
            if ref not in registre:
                raise ErreurCI(f"geste {g['id']!r} : état joueur inconnu {ref!r}")
        for ch in g.get("choix", []):
            for ref in ch.get("effets", []):
                if ref not in registre:
                    raise ErreurCI(f"geste {g['id']!r}, choix {ch['id']!r} : état joueur inconnu {ref!r}")
        if g.get("type") == "trouver":
            frag = frag_by_id[g["fragment_id"]]
            cibles = {r["remplace_par"] for et in frag.get("etats", []) for r in et.get("remplacements", [])}
            if g.get("cible") not in cibles:
                raise ErreurCI(
                    f"geste {g['id']!r} : la cible {g.get('cible')!r} n'est pas un mot corrompu du fragment {g['fragment_id']!r}"
                )
    rapport.append(f"micro-interactions : {len(registre)} états joueur déclarés ; conditions, effets et miroirs référencés")

    return rapport
