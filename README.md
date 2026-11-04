# Ira à toi — le nécessaire pour le dépôt

À poser sur le template Git + Python maison. **Les règles du template
priment** (architecture, codage, assistance IA) : cette arborescence est
indicative, à replacer selon vos conventions. Ce qui doit rester vrai,
quoi que vous déplaciez : le module de contrat, le dossier d'œuvre, la
CI et les tests se référencent par chemin relatif, sans installation.

```
ira-a-toi/
├── ASSISTANCE_IA.md               règles pour toute IA intervenant sur le dépôt
├── contrat/
│   └── pack.py                    le contrat d'œuvre (schéma v1.1, Pydantic)
├── ci/
│   └── valider_pack.py            la CI : valider un pack avant publication CDN
├── oeuvres/
│   └── le-horla-maupassant-1887/  la première œuvre (extrait de démonstration)
│       ├── manifeste.json         identité & édition (fait la fiche)
│       ├── source.txt             le texte intégral de référence (haché)
│       ├── fragments.json         le texte découpé + états de rendu
│       ├── publication.json       les cadences (règles d'envoi)
│       ├── interactions.json      états joueur, gestes, fins
│       └── enrichissements.json   fiches, lexique — tracés « généré puis validé »
└── tests/
    └── test_contrat.py            21 tests : invariants + négatifs + rendu
```

## Commandes

```bash
python ci/valider_pack.py oeuvres/le-horla-maupassant-1887   # la CI d'un pack
python -m unittest discover -s tests -v                       # la suite de tests
```

Sans pydantic, tout fonctionne en **mode CI mécanique** (invariants en
dicts purs) ; les modèles Pydantic se valident dès que la dépendance
est présente — le test correspondant s'ignore proprement sinon.

## Les invariants du contrat

La CI refuse (code de sortie non nul, le build casse) :

1. **Anti-altération** — la concaténation des fragments reproduit
   `source.txt` au caractère près, et le sha256 du manifeste correspond :
   le LLM ne réécrit jamais Maupassant ;
2. **Identité** — l'id du pack est un slug `<titre>-<auteur>-<année>`
   (le cas réel existe : `…-1886` et `…-1887` sont deux textes distincts) ;
3. **Ancrage des états** — chaque mot à corrompre existe dans le fragment ;
4. **Couverture des cadences** — chaque fragment a une règle d'envoi dans
   chaque cadence : aucun fragment orphelin, aucun envoi sans fragment ;
5. **Références** — gestes, fins, enrichissements pointent vers des
   objets du pack ;
6. **Micro-interactions** — toute condition, tout effet référence un état
   joueur *déclaré* ; le miroir renvoie vers un geste d'écriture ; le geste
   `trouver` vise un mot corrompu déclaré.

## Ce que contient le Horla de démonstration

Cinq entrées authentiques (8 → 25 mai, source : [Wikisource — Ollendorff
1895](https://fr.wikisource.org/wiki/Le_Horla_(recueil,_Ollendorff_1895)/Le_Horla)),
deux cadences (`standard` et `sprint` pour la QA), et la mécanique
signature complète :

- **corruption** — au second affichage de l'entrée du 18 mai,
  *« je ne pouvais plus dormir »* devient *« je ne pouvais plus me
  réveiller »* (état de rendu conditionné `relu`, jamais une réécriture) ;
- **choix** — saluer le trois-mâts brésilien ;
- **écriture** — le carnet de la nuit du 16 mai (jamais analysé) ;
- **miroir** — l'entrée du 25 mai rend le carnet en annotation
  (`a-ecrit`) : le Horla ne vous lit pas, il vous rend ce que vous lui
  avez confié ;
- **trouver** — repérer le mot changé (conditionné `relu`).

## À produire ensuite (hors périmètre de ce paquet)

- `assets/` de l'œuvre (couverture, papiers, cachets, sons — référencés
  par le manifeste, non inclus ici). Sources autorisées, preuves de
  domaine public et vérifications : voir `ASSISTANCE_IA.md` (§3-§5) ;
- l'ordonnanceur (`due_at = g(lu_à, règle, contraintes)`) côté serveur ;
- le découpage complet du Horla (les ~60 entrées de mai à septembre —
  l'extrait s'arrête au 25 mai).

## Conventions internes au contrat

- ids en slugs ASCII (`le-horla-maupassant-1887`, `entree-18-mai`,
  `a-vu-la-corruption`) — immuables une fois publiés ;
- conditions : `<état>`, `!<état>`, ou le mot-clé `relu` (fragment déjà lu) ;
- le corps de lecture est partagé par la collection ; le manifeste ne
  déclare que des polices **display** (licence OFL) ;
- horloge personnelle (Horla, Liaisons) : règles relatives à la dernière
  lecture ; horloge commune (Feuilleton) : calendrier de saison à dates
  absolues — jamais les deux dans la même cadence.
