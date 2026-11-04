# Assistance IA — règles de ce dépôt

À lire **avant toute intervention** (rédaction, découpage, code, assets).
Ce document complète le template maison (architecture, codage,
assistance IA) : **en cas de conflit, le template prime**. Tout ce qui
suit est spécifique au projet « Ira à toi ».

## 1. Le projet en bref (pour ne pas dénaturer)

- **« Ira à toi »** est l'app ; **« Le Cabinet Noir »** est le nom
  de la *collection*. « Le Cabinet Noir » ne désigne jamais un
  abonnement, un plan ou un paywall.
- Jamais le mot **« Lagardère »** (le serment vient du *Bossu*, mais le
  nom appartient au groupe Hachette) : la citation complète et correcte
  est « Si tu ne viens pas à Lagardère… » ; dans l'app, on ne nomme
  que la collection et l'app.
- **Gratuité intégrale côté lecteur** : aucun paywall, aucun écran qui
  parle d'argent, aucune mécanique d'engagement marchand. Le
  financement (FAJV/CNC, mécénat, licences B2B, patrimoine) vit hors
  de l'app, dans les documents, jamais dans l'interface.
- Une seule app ; chaque œuvre est un monde plein écran. Le texte
  source est sacré, l'ordonnancement est sacré, la marge est jouable.

## 2. Interdits absolus (aucune exception, aucune « amélioration »)

1. **Ne jamais réécrire le texte source.** Toute retouche, correction
   typographique ou « clarification » d'un fragment casse la CI
   anti-altération (diff au caractère près + sha256). Si la source
   semble fautive, c'est la source qui fait foi.
2. **Ne jamais inventer.** Pas de citation, de date, d'URL, de fait
   historique, d'année de mort, de licence sans vérification. Chaque
   affirmation sourcée doit être vérifiable (Gallica, Wikisource,
   archive.org, Commons). En cas de doute : vérifier ou s'abstenir.
3. **Ne jamais analyser le carnet du joueur.** Les gestes `ecriture`
   sont conservés mot pour mot, jamais envoyés à un LLM, jamais
   instrumentés. Le Horla simule la surveillance, il ne l'instrumente pas.
4. **Ne jamais coder une mécanique dans le moteur.** Une mécanique se
   *déclare* dans le pack (geste, état joueur, état de rendu,
   condition). Le moteur interprète, il ne contient rien.
5. **Ne jamais ajouter une dépendance** exigée par la CI ou les tests :
   la vérification anti-altération en dicts purs ne doit reposer sur
   aucun modèle qui décrit (pydantic est optionnel).
6. **Ne jamais renommer un id publié.** Slugs immuables une fois un
   pack publié sur le CDN. Une correction = une nouvelle version à côté
   (les versions cohabitent : `…-1886`, `…-1887`).
7. **Ne jamais mentir à l'utilisateur sur l'œuvre** : horloge
   personnelle (due_at = g(lu_à, règle, contraintes)) ; absence =
   pause structurelle, au plus une entrée attendue ; « la fiction
   recule, jamais elle ne ment ».

## 3. Domaine public : la preuve voyage avec chaque chose

La règle unique : **toute chose intégrée prouve elle-même son statut**,
dans les fichiers du pack, avec créateur, dates et source.

- **Textes** : auteur mort depuis plus de 70 ans (prorogations de guerre
  françaises vérifiées au cas par cas, dont +30 ans « mort pour la
  France »). Partir **des sources d'origine** (Gallica, Wikisource) ;
  jamais d'une traduction, préface, note ou édition critique récente.
- **Illustrations** : c'est le **créateur de l'image** qui compte
  (illustrateur, graveur, photographe), pas l'auteur de l'œuvre :
  mort depuis plus de 70 ans. Attention aux éditions illustrées du
  XXᵉ siècle, souvent protégées — préférer les éditions originales
  et les illustrateurs morts avant ~1956.
- **Musique — deux couches** : la *composition* (compositeur mort +
  70 ans, partitions comprises) ET l'*enregistrement* (droits voisins :
  70 ans à compter du 1ᵉʳ janvier suivant la publication du
  phonogramme — donc publiés avant 1956 = domaine public dans l'UE).
  Pour la distribution mondiale, viser avant 1923 (règle US) ou des
  enregistrements expressément libres (Musopen, CC).
- **Sons d'époque** : aucun enregistrement avant ~1890 ; utiliser des
  sons « un peu postérieurs » (1900-1955, tous PD) ou des
  réenregistrements CC0. Le cliché de surface (sous le 78 tours) est
  un atout, pas un défaut.

## 4. Où chercher (sources vérifiables, dans l'ordre de préférence)

| Quoi | Où | Condition d'usage |
|---|---|---|
| Textes sources | [Gallica](https://gallica.bnf.fr), [Wikisource](https://fr.wikisource.org) | toujours la source d'origine ; créditer la transcription |
| Illustrations | [Wikimedia Commons](https://commons.wikimedia.org), [Internet Archive](https://archive.org), [Europeana](https://www.europeana.eu) | vérifier la fiche : créateur + année de mort + licence |
| Illustrations (2ᵉ choix) | [Gallica](https://gallica.bnf.fr) | gratuit **non commercial** avec mention « Source gallica.bnf.fr / BnF » ; la réutilisation commerciale est payante → pour la B2B, préférer une copie Commons/Archive du même objet |
| Musique (partitions) | [IMSLP](https://imslp.org) | compositeur mort + 70 ans |
| Musique (enregistrements PD) | [Great 78 Project](https://archive.org/details/georgeblood), [Gallica audio](https://gallica.bnf.fr) | publié avant 1956 (UE) ; avant 1923 pour le monde entier |
| Musique (enregistrements libres) | [Musopen](https://musopen.org) | enregistrements expressément placés dans le domaine public |
| Sons | [Freesound](https://freesound.org) (filtre CC0), archives sonores [Internet Archive](https://archive.org) | CC0 pour ce qui est réenregistré |

Chaque asset retenu est documenté dans le pack : créateur, année de
mort (ou de publication du phonogramme), licence, URL de la source,
et — dès qu'il est embarqué — son hash. Un asset non prouvé n'embarque pas.

## 5. Vérifications avant tout commit

```bash
python ci/valider_pack.py oeuvres/<slug>     # doit finir par « PRÊT POUR PUBLICATION »
python -m unittest discover -s tests         # doit finir par OK
```

- Toute modification du pack Horla ou l'ajout d'un pack relit la sortie
  complète de la CI (7 sections) — pas seulement le code de retour.
- Tout nouvel invariant du schéma s'accompagne d'un **test négatif**
  (le cas qui doit échouer) ; le schéma se versionne sans rupture
  (ajouts optionnels : v1 → v1.1 est le modèle à suivre).
- Après tout ajout d'asset : relire le §3 et la table du §4 de ce
  document ; la preuve (créateur, †, licence, source) est dans le pack.

## 6. Méthode de travail avec une IA

- L'IA propose, l'humain décide : tout choix éditorial (découpage,
  cadence, geste, corruption, angle d'une œuvre) est présenté comme
  une proposition avec sa raison, jamais comme un acquis.
- L'IA ne « corrige » jamais seule : pour le texte source, la CI est
  l'arbitre ; pour le code, les tests sont l'arbitre.
- Quand une demande contredit un interdit du §2, l'IA le dit
  explicitement plutôt que de contourner.
