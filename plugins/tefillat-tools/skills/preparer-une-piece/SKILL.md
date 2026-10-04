---
name: preparer-une-piece
description: >-
  Préparer une pièce liturgique hébraïque pour la projection en synagogue :
  translittérer l'hébreu vocalisé selon les règles séfarades jointes, proposer
  une traduction française, découper l'alignement hébreu / translittération /
  français, contrôler le tout, et produire le fichier d'import (.json) — pour
  un chant, une prière de l'office ou une lecture. À charger dès qu'il est
  question de translittérer, vocaliser, transcrire, traduire, aligner, découper
  ou segmenter un texte hébreu, de « préparer un chant », « préparer une
  prière », « faire un fichier d'import », ou quand quelqu'un colle de l'hébreu
  ou une translittération en demandant d'en faire une pièce — même sans nommer
  ce skill : « translittère ce psaume », « fais-moi le fichier pour ce chant »,
  « découpe cette berakha » suffisent. Sert aussi à **reconstituer l'hébreu**
  d'une translittération — dans n'importe quel standard (`ch`, `tz`, `'h`…),
  avec ou sans traduction — et à la **retranslittérer selon la norme** :
  « retrouve l'hébreu de ce chant », « remets cette translittération dans la
  norme ». Ne sert pas à relire une pièce déjà chargée dans une base, et
  n'écrit jamais dans une base.
---

# Préparer une pièce : de l'hébreu au fichier d'import

## 0. Ce que tu ne fais jamais — lis ceci d'abord

Ce skill touche du **texte sacré**. Ses interdits ne sont pas des précautions
de style : ce sont eux qu'on partage, plus encore que la norme.

1. **Jamais changer les mots.** Ni l'hébreu, ni une translittération, ni un
   français que l'on t'a donnés. Une forme douteuse se **signale** dans le
   rapport, elle ne se réécrit pas. *Y compris quand tu découpes* : le
   découpage recopie le texte à l'identique, même fautif.
2. **Jamais deviner sans le dire.** Un hébreu sans voyelles ne se translittère
   pas (§1). Un hébreu tiré d'une translittération est **cité** si tu as
   ouvert sa source, **reconstitué** sinon — et une reconstitution porte ses
   choix ambigus, mot par mot (§10). **Hors réseau, rien n'est cité.**
3. **Le rapport distingue le mesuré du supposé.** Ce que tu as compté — les
   atomes, les mots, le recollage, les longueurs — est marqué *mesuré* ; ta
   translittération, ta traduction et tes frontières sont des *propositions*.
   Un rapport qui mélange les deux n'est pas contestable.
4. **Six exemples ne sont pas une règle.** Leçon chèrement acquise : l'ayin
   final a été cru `'` sur six cas ; il s'écrit `"` **156 fois contre 6**.
   Tout constat chiffré se compte, il ne se raisonne pas.
5. **Une pièce se nomme, elle ne se numérote pas.** Tout tableau, tout
   signalement porte le titre de la pièce.
6. **L'humain tranche.** Chaque rapport se termine par ce qui attend son
   arbitrage. Rien de ce que tu produis ne sera projeté sans qu'une personne
   de la communauté l'ait relu (§7).

## 1. Qu'est-ce que tu as ? — la question qui ouvre tout

Demande-le, ou regarde, **avant** de commencer. La réponse change le travail.

| Entrée | Ce que tu fais | Ce que tu **ne peux pas** faire |
|---|---|---|
| **Hébreu vocalisé** | translittérer selon la norme, proposer une traduction, découper | — |
| **Hébreu non vocalisé** | **t'arrêter et le dire** : la vocalisation décide de la translittération | deviner les voyelles |
| **Translittération seule** | proposer une traduction et un découpage ; **à la demande, reconstituer l'hébreu** (§10) | rendre l'hébreu **sans le marquer** : la translittération perd la graphie — plein ou défectif, qamats ou patah, gémination —, donc toute reconstitution porte son rang et ses ambiguïtés |
| **Translittération + traduction** | le mode « reconstituer » **avec contrôle de sens** (§10.6) — **le meilleur cas pour reconstituer** | — |
| **Les deux** | vérifier l'un par l'autre (§4, règle 1) — **c'est le cas le plus sûr** | — |

Un hébreu « vocalisé » porte ses voyelles (`ַ ָ ֵ ֶ ִ ֹ ֻ ְ`). Des lettres seules
— `ברוך אתה` — ne le sont pas. Une ligne vocalisée à moitié se signale.

## 2. La norme

La translittération suit **`REGLES-translitteration-sefarade.md`**, livré
dans ce dossier. **Lis-le en entier avant de translittérer** ; ne travaille
pas de mémoire. Les points qui cassent le plus souvent : `'` = aleph et
`"` = ayin, en ASCII (§4) ; l'aleph initial muet (§4.2) ; le trait d'union
réservé au Nom divin préfixé (§7.3) ; le maqaf rendu par une espace (§7.4) ;
`'Adonaï` contre `Adonai` (§8).

| | |
|---|---|
| Version copiée | version du 2026-10-04, 312 lignes, §1 à §13 |
| Empreinte | `sha256 9586359a8904538e7d9e0fe55440e9f5b140730c12643237b23102067255ba53` |
| Copie | à l'octet près — **ne la modifie pas** : elle est comparée à l'original |

> **§13 — l'implémentation de référence n'est pas livrée avec ce skill.** Le
> §13 de la norme décrit un `translit.py` ; il ne fait pas partie de ce
> paquet. Tu translittères **par lecture des règles**, mot par mot.

## 3. Les étapes

1. **Établis l'entrée** (§1). Si l'hébreu n'est pas vocalisé, arrête-toi là.
2. **Découpe l'hébreu en atomes** : un atome est séparé par une espace **ou
   par un maqaf** `־`. Un signe de ponctuation isolé n'est pas un atome.
3. **Translittère atome par atome**, en citant le § de la norme quand le cas
   n'est pas trivial. Un atome donne **un** mot : ne fusionne ni ne scinde.
4. **Propose une traduction** française, ligne par ligne. Marque-la comme
   proposition. Le Tétragramme se traduit **YHWH**, le mot `אֲדֹנָי` **Seigneur**,
   `יָהּ` **Yah** (§8 de la norme). **Puis reviens aux majuscules** : elles vont
   au premier mot de chaque **phrase** (§9), et l'hébreu ne ponctue pas la
   phrase — c'est ta traduction et le sens qui disent où elle commence.
5. **Découpe** la ligne en segments selon le §4.
6. **Contrôle** avec la liste du §6, et rends son verdict.
7. **Rends le fichier** (§5) et **le rapport** (§8).

## 4. Le découpage — quatre règles, dans cet ordre

Un *segment* est une paire `[translittération, français]` : un morceau de
translittération et le français qui lui correspond. Les chiffres viennent
d'une mesure du 2026-10-03 sur un corpus liturgique réel — **21 755 segments,
11 224 lignes** ; ils se remesurent, ils ne se récitent pas.

1. **L'invariant d'alignement** (§10 de la norme) — sur une ligne qui porte
   hébreu et translittération, **nombre d'atomes hébreux = nombre de mots
   translittérés**, la ponctuation isolée ne comptant ni d'un côté ni de
   l'autre. **Vérifie-le en comptant, pas à l'œil.** Il est rompu sur **1 %**
   des lignes du corpus — et sur 5 % si l'on compte un `!` isolé comme un mot :
   c'est l'erreur de comptage la plus fréquente.
2. **Le recollage** — recoller les segments d'une ligne, séparés par une
   espace, doit rendre **exactement** la ligne d'avant, caractère pour
   caractère. Donc : aucune espace en bord de segment, aucune espace double
   dans un segment. Un découpage qui perd ou ajoute une espace a modifié le
   texte.
3. **Les frontières suivent le sens**, pas les mots un à un. **Vise 2 à 4
   segments sur une ligne longue.** 44 % des lignes du corpus n'en ont qu'un,
   et c'est très bien : une ligne courte ne se découpe pas pour faire joli.
   Médiane : 2 segments par ligne ; 93 % des lignes en ont 1 à 3.
4. **La cohérence avec la traduction, mesurée** — le français d'un segment
   fait en médiane **1,3 fois** la longueur de sa translittération (p90 : 2,0 ;
   p99 : 3,3). **Au-delà de 3,0 ou en deçà de 0,33, tu es dans les extrêmes**
   (1,3 % et 0,2 % du corpus). C'est un **signal, pas un verdict** : tu le
   signales et tu demandes ; tu ne redécoupes jamais de toi-même.

## 5. Le fichier produit

Un objet JSON, une pièce par fichier :

```json
{
  "structure": "table",
  "format": "htf",
  "titre_he": "דּוֹר הֹלֵךְ",
  "titre_translit": "Dor holékh",
  "titre_fr": "Une génération s'en va",
  "source": "Qohélet 1:4-5",
  "slug_propose": "dor-holekh",
  "lignes": [
    { "genre": "liturgie",
      "hebreu": "דּוֹר הֹלֵךְ וְדוֹר בָּא …",
      "texte": null,
      "segments": [ ["Dor holékh", "Une génération s'en va,"],
                    ["vedor ba'", "une génération vient,"] ] }
  ]
}
```

| Clé | Valeurs |
|---|---|
| `structure` | `table` (hébreu, translittération, français) · `libre` |
| `format` | `htf` (hébreu-translittération-français) · `fr` (français seul) |
| `genre` d'une ligne | `liturgie` (texte dit ou chanté) · `rubrique` (indication : « Le hazan : », texte dans `texte`) · `source` (référence) |
| `rendu` (facultatif, pièce ou ligne) | `multi` · `mono` · absent |
| `apres` (facultatif — **voir §7**) | le slug de la pièce qui précède |
| `slug_propose` | le titre translittéré en minuscules, sans accents ni signes, mots joints par `-` |
| `provenance` (par ligne — **mode « reconstituer »**, §10.7) | d'où vient l'hébreu : rang, standard d'entrée, référence, ambiguïtés, verdict de sens |

**La sortie est du texte.** Si tu peux écrire un fichier, écris-le. Sinon —
et c'est le cas dans bien des environnements —, **rends le JSON entier dans ta
réponse**, dans un bloc de code, prêt à être copié dans un fichier `.json`. Ne
suppose jamais que tu peux écrire sur un disque.

Trois exemples sont joints : `exemples/piece-exemple.json` (bien formé),
`exemples/piece-cassee.json` (fautif, pour voir le contrôle parler) et
`exemples/piece-reconstituee.json` (mode « reconstituer », avec `provenance`).

## 6. La liste de contrôle — le verdict

**Tu l'appliques en lisant, à chaque fichier, et tu rends son verdict dans le
rapport.** Elle ne demande aucun programme. Là où du code peut s'exécuter,
`valider_feed.py` (joint) confirme mécaniquement le même verdict — **les deux
doivent concorder** ; s'ils divergent, dis-le.

### 6.1 Refus — la chaîne d'import ne chargera pas le fichier

| # | Contrôle |
|---|---|
| R1 | le fichier est **un objet JSON** `{ … }` |
| R2 | `structure` vaut `table` ou `libre` |
| R3 | `format` vaut `htf` ou `fr` |
| R4 | `rendu` de la pièce, s'il est présent et non vide, vaut `multi` ou `mono` |
| R5 | `apres`, s'il est présent, est un texte non vide |
| R6 | `lignes` est une liste, et chaque ligne un objet |
| R7 | chaque `genre` de ligne vaut `liturgie`, `rubrique` ou `source` |
| R8 | chaque `rendu` de ligne, s'il est présent et non vide, vaut `multi` ou `mono` |
| R9 | `segments` est une liste ; chaque segment est **une paire** `[translittération, français]`, deux textes (ou `null`), ni plus ni moins |
| R10 | **pièce de liturgie** (§7) qui porte au moins une ligne : `apres` est présent — sinon le lot entier est refusé |

### 6.2 Signalements — le fichier est importable, un humain doit regarder

| # | Contrôle |
|---|---|
| S1 | `titre_he`, `titre_translit`, `titre_fr`, `slug_propose` présents et non vides ; au moins une ligne |
| S2 | ligne `liturgie` : son champ `hebreu`, s'il est rempli, porte des lettres hébraïques |
| S3 | ligne `liturgie` : son hébreu porte des **voyelles** |
| S4 | ligne `liturgie` : aucun segment dont les deux côtés sont vides |
| S5 | **§10** : atomes hébreux = mots translittérés (maqaf = espace, ponctuation isolée exclue) |
| S6 | **recollage** : aucun segment bordé d'espaces, aucune espace double dans un segment |
| S7 | **rapport de longueur** : pour chaque segment plein des deux côtés, français ÷ translittération entre 0,33 et 3,0 |
| S8 | **invariants absolus** de la translittération : pas de `c` (§1.1), pas de `è` (§1.4), pas d'apostrophe ni de guillemet typographique `’ ʼ ʻ “ ”` (§4) |
| S9 | **provenance** (si présente) : rang `cité`, `attesté` ou `reconstitué` ; un `cité`/`attesté` a sa référence **et** son adresse ; le standard d'entrée est déclaré ; le sens vaut `concordant`, `nuance`, `désaccord` ou `non contrôlé` — **un désaccord, ou un reconstitué non contrôlé, se signale** |
| S10 | **aller-retour** (si la provenance porte la translittération d'entrée) : chaque mot d'entrée a le même squelette consonantique que le mot de retour — sinon **INEXPLIQUÉ**, et la ligne ne devait pas être proposée |

**Verdict** : un seul refus → **REFUSÉ**. Aucun refus mais des signalements →
**IMPORTABLE, à relire** (le script sort 2). Ni l'un ni l'autre →
**IMPORTABLE** (le script sort 0).

```bash
python3 valider_feed.py ma-piece.json                    # chant ou lecture
python3 valider_feed.py ma-piece.json --corpus liturgie  # ajoute R10
```

## 7. Après toi — ce que devient le fichier

**Tu ne charges rien.** Charger le fichier est un geste de la communauté, par
sa chaîne d'import, après une sauvegarde de sa base. Dis-le à l'utilisateur, et
dis-lui aussi ceci, qui doit le rassurer :

> **Tout ce qui entre par ce fichier arrive en quarantaine.** Chaque ligne
> importée est marquée « à relire », quoi que le fichier déclare ; quelqu'un de
> la communauté la relira avant qu'elle soit projetée. Une erreur de bonne foi
> sur un mot d'hébreu ne passe pas à l'écran.

**Le même fichier sert aux trois corpus** — chant, liturgie, lecture — à deux
réserves près, que tu écris **en tête** du rapport quand elles s'appliquent :

- **Liturgie : le rang.** Une prière de l'office prend sa place dans l'ordre
  de l'office. Le fichier doit dire après quelle pièce elle entre :
  `"apres": "<slug de la pièce qui la précède>"`. **Tu ne connais pas ce slug
  et tu ne l'inventes jamais.** Laisse `apres` absent et écris en tête du
  rapport : *« cette pièce est de la liturgie : son rang doit être posé avant
  l'import, sinon la chaîne refusera le lot entier. »* Si l'utilisateur te
  donne le slug, pose-le.
- **Lecture : la porte d'entrée.** Les lectures hebdomadaires arrivent
  d'ordinaire dans un autre format, propre à leur outil de préparation, et
  l'écran d'import des lectures **refuse** ce fichier-ci. Il entre par la
  **chaîne d'import des pièces**, et la personne qui l'importe **doit**
  nommer la section : sans elle, la chaîne s'arrête. Dis-le, pour que le
  fichier ne soit pas présenté à la mauvaise porte.

La **section** où la pièce sera rangée n'est pas dans le fichier : c'est la
personne qui importe qui la choisit. Ne t'en occupe pas.

## 8. La forme du rapport

Dans cet ordre :

1. **En tête** — le titre de la pièce ; le corpus ; les réserves du §7 qui
   s'appliquent ; le verdict de la liste de contrôle.
2. **La translittération, atome par atome**, pour chaque ligne :
   `hébreu → translittération (§ invoqué)`, et les atomes douteux marqués, avec
   leur raison.
3. **Le découpage**, en tableau `ligne | translittération | français`, les
   segments séparés par `·`.
4. **Le contrôle** — chaque contrôle de la liste avec son résultat, en
   distinguant **mesuré** (compté) et **proposé** (jugé). Le §10 se donne en
   chiffres : `n atomes / n mots`.
5. **Ce qui attend un arbitrage humain**, par ordre d'importance. Il y a
   toujours au moins la traduction, qui est une proposition.
6. **Le fichier**, en bloc de code ou écrit sur le disque.

## 9. Ce que ce skill ne fait pas

Il ne charge rien dans une base · il **n'invente jamais un slug de rang** · il
ne présente jamais un hébreu reconstitué comme cité · il ne reconstitue pas les
paroles d'une œuvre protégée · il ne vocalise pas un hébreu nu · il ne produit
pas de présentation · il ne connaît ni les sections, ni les rangs, ni les
offices d'une communauté · **il ne corrige jamais le texte sacré, il le
signale** · il ne sert pas à relire une pièce déjà chargée.

## 10. Le mode « reconstituer » — de la translittération à l'hébreu

**À utiliser quand on te donne une translittération et qu'on te demande
l'hébreu**, ou une translittération à remettre dans la norme. La traduction
française est facultative ; **avec elle, le contrôle de sens devient
possible**, et c'est le meilleur cas.

### 10.1 Ce que tu refuses, avant tout

Tu t'arrêtes, tu nommes la raison, et tu ne proposes rien :

- **une œuvre protégée** — paroles d'un auteur identifiable et récent :
  écrire en hébreu les paroles d'une chanson, c'est les reproduire ;
- **une entrée déjà en hébreu** : il n'y a rien à reconstituer (§1).

### 10.2 Le standard d'entrée — déclaré, à défaut détecté, et toujours dit

Le même `ch` est un ḥet chez l'un, un khaf chez l'autre, un shin chez un
troisième. **Tout dépend du standard**, donc :

1. **Si l'utilisateur le déclare** — « c'est la norme », « c'est de
   l'ashkénaze », « je ne sais pas » —, sa déclaration gagne.
2. **Sinon tu le détectes** par indices (`ch`, `tz`, `''`, un circonflexe,
   `'h`, « Hashem ») et **tu annonces ce que tu as retenu, avec les indices**.
3. **Dans le doute, tu demandes.** Sans réponse, tu traites toutes les
   lectures possibles comme ambiguës (§10.5).

Le standard retenu s'écrit **dans le rapport et dans la `provenance`**.

### 10.3 La chaîne : on passe par l'hébreu

```
translittération d'entrée  →  hébreu (cité | attesté | reconstitué)  →  translittération selon la norme
```

On ne convertit **jamais** une translittération en une autre par
substitution : `ch` ne devient `ḥ` que si la lettre est un ח. **La
translittération de sortie hérite du rang de l'hébreu dont elle vient** :
sûre sur une ligne citée, **proposition appuyée sur une proposition** sur
une ligne reconstituée. Dis-le, ligne par ligne.

### 10.4 Les trois rangs — et celui qui gouverne

| Rang | Ce que c'est | Ce qu'il exige |
|---|---|---|
| **cité** | un verset biblique | la référence (livre, chapitre, verset), une **adresse qu'un tiers peut ouvrir**, et le texte **repris de cette source, pas récité** |
| **attesté** | un texte liturgique connu (siddour, piyyout) | la source nommée, son édition, son adresse |
| **reconstitué** | tout le reste | les ambiguïtés (§10.5), l'aller-retour (§10.6) |

- **Repris, pas récité.** Si tu peux ouvrir la source (un site de textes
  bibliques), copie le texte **depuis elle**. Sinon, **demande à
  l'utilisateur** de coller le verset de son édition. **Hors réseau et sans
  texte fourni, aucune ligne n'est citée** : elle est reconstituée, quelle
  que soit ta certitude. Un verset récité de mémoire peut être faux sur une
  seule voyelle.
- **Le rang le plus faible gouverne la ligne.** Une ligne qui reprend trois
  mots d'un verset en omettant le quatrième **n'est pas le verset** : elle est
  reconstituée, le verset devient un indice.

### 10.5 Les ambiguïtés, mot par mot

`conventions.json` (joint) dit, pour chaque forme d'entrée, les lettres
possibles — `ch` : ח, כ ou ש ; `h` : ה ou ח ; `'` : א, et ע si la source
confond. S'y ajoutent **quatre ambiguïtés qui demeurent même en norme
parfaite** : **plein ou défectif**, **qamats ou patah**, **gémination**,
**`ḥ` de la source pour ח ou כ**.

Pour chaque ligne reconstituée, liste les choix : *le mot, ce que tu as
retenu, les autres candidats.* C'est la moitié du travail : on tranche en
regardant une liste au lieu de relire tout l'hébreu.

### 10.6 L'aller-retour et le contrôle de sens

**L'aller-retour, toujours.** Retranslittère ton hébreu selon la norme et
compare **mot à mot** à l'entrée. Chaque écart doit s'expliquer par une
famille — convention étrangère, aleph initial, h/ḥ/kh, gémination, voyelle,
casse. **Un mot inexpliqué** (les consonnes dures diffèrent) veut dire que
ton hébreu ne rend pas l'entrée : **la ligne est signalée et tu ne proposes
pas son hébreu.** Là où du code s'exécute : `python3 aller_retour.py
ma-piece.json`.

**Le contrôle de sens, si une traduction est fournie.**

1. Traduis **ton propre hébreu**, sans relire la traduction fournie.
2. Compare. Trois verdicts par ligne : **concordant** · **nuance** ·
   **désaccord**.
3. **Un désaccord se met en tête du rapport** : un hébreu qui ne dit pas ce
   que dit la traduction connue est probablement faux. La ligne reste
   proposée, avec sa marque — l'information est trop utile pour être tue.
4. **Sans traduction fournie**, chaque ligne porte **« sens non contrôlé »**.
   Une ligne non contrôlée n'est pas une ligne validée.

Les segments portent la translittération **de sortie** et le français
**fourni**, recopié sans changer un mot ; à défaut, ta traduction, marquée
comme proposition.

### 10.7 La provenance, dans le fichier

Chaque ligne reconstituée ou citée porte :

```json
"provenance": {
  "rang": "cité | attesté | reconstitué",
  "reference": "Qohélet 1:4", "url": "<adresse de la source ouverte>",
  "standard": { "retenu": "français (ch, tz)", "declare": false, "indices": ["ch", "tz"] },
  "translit_entree": "la translittération telle qu'on te l'a donnée",
  "ambiguites": [ { "mot": "…", "choix": "…", "candidats": ["…"] } ],
  "sens": "concordant | nuance | désaccord | non contrôlé"
}
```

**Limite à dire à l'utilisateur** : la chaîne d'import accepte cette clé mais
**ne la charge pas** — la provenance ne survit pas à l'import. **Le rapport
doit accompagner le fichier** jusqu'à la personne qui importe, et tout ce
qui est importé arrive de toute façon en quarantaine (§7).

### 10.8 Le rapport du mode « reconstituer »

En plus du §8, et **en tête** : le standard retenu et ses indices ; **les
désaccords de sens** ; les lignes non proposées (aller-retour inexpliqué).
Puis, pour chaque ligne : rang et référence · hébreu · translittération
d'entrée → de retour, écarts et familles · ambiguïtés · verdict de sens.
