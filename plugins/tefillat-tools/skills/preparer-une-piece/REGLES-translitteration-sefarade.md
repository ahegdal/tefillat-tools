# Translittération séfarade de l'hébreu ponctué — règles canoniques

Document autoportant, destiné à être partagé entre projets.
Cible : un lecteur francophone lisant à voix haute en synagogue. La
translittération est **fidèle mais non académique** — elle sert la lecture
fluide, pas l'analyse linguistique.

Source : `Règles de translitération v2.docx` + `Liste complète des règles de
translittération.docx`, arbitrées par le corpus réellement produit
(8 lectures hebdomadaires, 15 437 occurrences, 5 251 mots distincts).
Là où les documents et l'usage divergent, **l'usage attesté fait foi** et
la divergence est signalée au §12.

---

## 1. Invariants absolus

1. **La lettre `c` n'est jamais utilisée.** `שׁ`=sh (jamais « ch »), `ח`=ḥ,
   `כ/ך`=kh, `צ`=ts, `ק`=q.
2. **Aucune marque de longueur vocalique** — pas de macron, pas de point
   suscrit, pas de distinction bref/long.
3. **`'` (apostrophe) = aleph** et **`"` (guillemet droit) = ayin**, partout,
   sans exception. Ces deux signes ne servent à rien d'autre.
4. **Pas de `è`.** Le segol s'écrit `e`. (Zéro occurrence de `è` dans le corpus.)
5. **Le trait d'union `-` est réservé** au seul cas du §7.3.

---

## 2. Consonnes

| Hébreu | → | Hébreu | → | Hébreu | → |
|---|---|---|---|---|---|
| `א` | `'` (voir §4) | `י` | `y` / `i` (§5) | `ס` | `s` |
| `ב` | `v` | `כ` `ך` | `kh` | `ע` | `"` (voir §4) |
| `בּ` | `b` | `כּ` | `k` | `פ` `ף` | `f` |
| `ג` | `g` | `ל` | `l` | `פּ` | `p` |
| `ד` | `d` | `מ` `ם` | `m` | `צ` `ץ` | `ts` |
| `ה` | `h` (§6) | `נ` `ן` | `n` | `ק` | `q` |
| `ו` | `v` (§5) | `ז` | `z` | `ר` | `r` |
| `ח` | `ḥ` | `ט` | `t` | `שׁ` | `sh` |
| | | | | `שׂ` | `s` |
| | | | | `ת` | `t` |

**Pas de distinction entre lettres proches** : `ט`/`ת` → tous deux `t` ;
`ס`/`שׂ` → tous deux `s`. Pas de `h'` artificiel pour `ח` : simplement `ḥ`.

**Begadkefat** : le daguesh léger durcit uniquement `ב`→`b`, `כ`→`k`, `פ`→`p`.
En séfarade `ג` `ד` `ת` restent inchangés.

---

## 3. Voyelles

| Signe | | → |
|---|---|---|
| tsere | `ֵ` | `é` |
| segol | `ֶ` | `e` |
| hiriq | `ִ` | `i` |
| holam | `ֹ` `וֹ` | `o` |
| qamats / patah | `ָ` `ַ` | `a` |
| qubuts / shuruk | `ֻ` `וּ` | `ou` |
| qamats qatan | `ׇ` | `o` |

**Hataf** (voyelles brèves) : `ֱ`→`e`, `ֲ`→`a`, `ֳ`→`o`.

**Sheva** : mobile → `e` ; quiescent → non transcrit.
Un sheva est mobile en début de mot, après un sheva quiescent, ou sous une
consonne géminée ; sinon quiescent. Dans le doute, suivre la lecture séfarade
courante.

**Il est mobile aussi sous la première de deux consonnes identiques** :
`הַלְלִי`→`Haleli`, `הַלְלוּ`→`halelou`, `אָהַלְלָה`→`Ahalela` (et non `Halli`,
`hallou`, `Ahalla`). *Arbitré le 2026-10-04.*

---

## 4. Les deux apostrophes — `א` et `ע`

C'est le point le plus facile à casser dans un portage. Ce sont **deux
caractères ASCII distincts** :

- `'` U+0027 APOSTROPHE — **aleph**
- `"` U+0022 QUOTATION MARK — **ayin**

**Ne jamais** les remplacer par des apostrophes typographiques (`’`), des
demi-anneaux (`ʼ` `ʻ`) ou des guillemets courbes : cela casse l'égalité de
chaîne et l'alignement (§10).

### 4.1 `ע` ayin = `"` — toujours

Quelle que soit la voyelle, quelle que soit la position.

```
עָשָׂה      → "asa
שִׁמְעוּ     → Shim"ou
יְהוֹשֻׁעַ    → Yehoshou"a
עַמָּלֵק     → "Amaléq
```

### 4.2 `א` aleph = `'` — sauf en début de mot

- **Début de mot : muet**, non transcrit. `אֱלֹהִים`→`Elohim`, `אֲשֶׁר`→`asher`,
  `אֵת`→`et`, `אִשָּׁה`→`Ishsha`.
- **Partout ailleurs : `'`**, y compris quiescent en milieu ou fin de mot.

```
לֹא        → lo'          (et non « lo »)
רִאשׁוֹנִים  → ri'shonim     (et non « rishonim »)
רֹאשׁ       → ro'sh
וַיִּקְרָא    → Vayyiqra'
מוֹאָב      → Mo'av
כַּאֲשֶׁר     → ka'asher
```

---

## 5. `ו` et `י` — matres lectionis et diphtongues

**Vav**
- `וֹ` holam malé → `o` ; `וּ` shuruk → `ou` — mais seulement quand le vav ne
  porte pas d'autre voyelle et ne suit pas une voyelle.
- Consonantique partout ailleurs → `v`.

**Yod**
- Consonantique (début de syllabe) → `y` : `יוֹם`→`yom`.
- hiriq + yod → `i` long, déjà couvert par le `i` (pas de `iy`).
- tsere/segol + yod → **`éy`** en milieu de mot, **`é`** en finale.
  Le segol est relevé en `é` devant yod.

```
בֵּית      → béyt
אֱלֹהֶיךָ    → Elohéykha
לִפְנֵי     → lifné        (finale : é, pas éy)
```
- patah/qamats + yod → `ai` : `יָדַי`→`yadai`.
- `יו` → `yo` ; `יי` → `yy`.

---

## 6. `ה` final

Sans mappiq et sans voyelle : **muet**, non transcrit — `תּוֹרָה`→`tora`.
Avec mappiq (`הּ`) : transcrit `h` — `אַרְצָהּ`→`artsah`.

---

## 7. Gémination et jonctions

### 7.1 Daguesh fort

**Doublé entre deux voyelles.** Non doublé en début de mot ou au contact
direct d'une autre consonne (pas de redoublement artificiel : `בְּ` = `be`,
jamais `bbe`).

```
מַסָּע      → massa"
פִּקּוּד     → piqqoud
נָגִיד      → naggid
```

**Deux exceptions de lisibilité :**

| | → | exemple |
|---|---|---|
| `שּׁ` | `shsh` | `הַשָּׁמַיִם` → `hashshamayim` |
| `צּ` | `tts` | `נִצָּבִים` → `nittsavim` |

### 7.2 Préfixes — soudés, sans trait d'union

Les préfixes inséparables (`וְ` `לְ` `בְּ` `מִ` `כְּ` `הַ`) s'écrivent **collés**,
et la gémination de l'article se rend par un simple doublement, **sans
séparateur** :

```
הַתּוֹרָה    → hattora        (et non « hat-tora »)
הַדֶּרֶךְ     → hadderekh
הַגּוֹיִם     → haggoyim
בַּכֶּסֶף     → bakkesef
וְקֹלוֹ       → veqolo
מֵאֶרֶץ      → mé'erets
```

**Un nom propre garde sa majuscule après le préfixe** :

```
וְלֵוִי       → veLévi
לְיִצְחָק     → leYitsḥaq
וּלְיַעֲקֹב    → oulYa"aqov
לִיהוֹשֻׁעַ    → liHoshou"a
מִבָּצְרָה    → miBotsra
```

### 7.3 Le seul emploi du trait d'union

**Préposition inséparable + Nom divin.** C'est le seul cas, sans exception,
dans tout le corpus (41 occurrences, 7 formes) :

```
בַּיהֹוָה  → ba-'Adonaï
לַיהֹוָה  → la-'Adonaï
וַיהֹוָה  → va-'Adonaï
כַּיהֹוָה  → ka-'Adonaï
```
Idem sur le mot `אֲדֹנָי` : `וַאדֹנָי` → `va-Adonai`.

### 7.4 Maqaf `־`

Rendu par une **espace**, jamais par un trait d'union.
`כׇּל־הָאָרֶץ` → `kol ha'arets` (deux mots).

---

## 8. Noms divins — trois cas distincts

| Hébreu | Translittération | Traduction (fr) |
|---|---|---|
| `יהוה` Tétragramme | `'Adonaï` | **YHWH** |
| `יהוה` préfixé | `ba-` / `la-` / `va-` / `ka-'Adonaï` | à / pour / et / comme YHWH |
| `אֲדֹנָי` le *mot* (apostrophe d'adresse) | `Adonai` *(sans apostrophe)* | **Seigneur** |

Le troisième cas n'est **pas** le Tétragramme. Il faut regarder les consonnes,
pas la vocalisation : `אֲדֹנָי` s'écrit aleph-dalet-noun-yod.
Les deux peuvent cohabiter dans un même verset — p. ex. Isaïe 61:11
`אֲדֹנָי יֱהֹוִה` → `Adonai 'Adonaï` → « le Seigneur YHWH ».

**`יָהּ` n'est pas le Tétragramme** : il s'écrit `Yah` et se traduit **Yah**,
jamais « YHWH ». `הַלְלוּ־יָהּ` → `halelou Yah` → « louez Yah ».
*Arbitré le 2026-10-04.*

---

## 9. Majuscules

- Premier mot de chaque **phrase** — donc aussi de chaque verset, et d'une
  strophe quand elle ouvre une phrase. L'hébreu ne ponctue pas la phrase : sa
  frontière **se déduit de la traduction et du sens**. *Arbitré le 2026-10-04 ;
  la règle disait auparavant « premier mot de chaque verset ».*
- Noms propres (personnes, peuples, lieux) — y compris après un préfixe (§7.2).
- Épithètes divines : `Elohéykha`, `Qadosh`, `Eloah`.

Quand un mot commence par un ayin ou un aleph consonantique, la majuscule
porte sur la **première lettre latine**, le signe restant devant :
`"Amaléq`, `"Og`, `Ha'ish`.

---

## 10. Invariant d'alignement (si la sortie est consommée par un programme)

**Un mot translittéré ↔ un atome hébreu**, où un « atome » est une unité
séparée par une espace **ou par un maqaf** (puisque le maqaf devient une
espace, §7.4).

C'est cette égalité de comptage qui permet de redécouper l'hébreu ligne par
ligne. Si elle est rompue pour un verset, l'alignement du verset entier est
perdu — silencieusement. Toute chaîne de traitement devrait la vérifier :

```
nombre de mots de la translittération du verset
  == nombre d'atomes hébreux du verset
```

Corollaire : ne jamais fusionner ni scinder un mot dans la translittération
pour des raisons de mise en page.

---

## 11. Exemples complets

```
אַתֶּם נִצָּבִים הַיּוֹם כֻּלְּכֶם לִפְנֵי יְהֹוָה אֱלֹהֵיכֶם
Attem nittsavim hayyom koullekhem lifné 'Adonaï elohéykhem

וְהָיָה כִּי־תָבוֹא אֶל־הָאָרֶץ אֲשֶׁר יְהֹוָה אֱלֹהֶיךָ נֹתֵן לְךָ
Vehaya ki tavo' el ha'arets asher 'Adonaï elohéykha notén lekha

הַנִּסְתָּרֹת לַיהֹוָה אֱלֹהֵינוּ וְהַנִּגְלֹת לָנוּ וּלְבָנֵינוּ
Hannistarot la-'Adonaï elohéynou vehanniglot lanou oulvanéynou

קוּמִי אוֹרִי כִּי בָא אוֹרֵךְ וּכְבוֹד יְהֹוָה עָלַיִךְ זָרָח
Qoumi ori ki va' orékh oukhvod 'Adonaï "alayikh zaraḥ
```

---

## 12. Divergences avec les sources écrites — arbitrages

Les points suivants sont tranchés **contre** la lettre d'un des documents
sources, sur la foi de l'usage attesté. À reprendre tels quels.

| Point | Ce que dit un document | Usage retenu | Preuve |
|---|---|---|---|
| segol | `אֶ = è` | **`e`** | 0 occurrence de `è` sur 15 437 |
| aleph quiescent | « `לֹא`→`lo` », « `רִאשׁוֹן`→`rishon` » | **`lo'`, `ri'shonim`** — l'aleph n'est muet qu'à l'initiale | `lo'` parmi les 5 mots les plus fréquents |
| préfixes | « préfixes avec trait d'union : `ve-`, `le-`, `be-`… » | **soudés** | 0 occurrence hors §7.3 |
| article géminé | « `הַדֶּרֶךְ`→`had-derekh` » | **`hadderekh`** | `hattora`, `haggoyim`, `bakkesef`… |
| trait d'union | usage général comme séparateur de préfixe | **réservé** au Nom divin préfixé | 41/41 occurrences |

---

## 13. Implémentation de référence

`translit.py` (≈ 200 lignes, sans dépendance) implémente mécaniquement les
§2, §3, §5, §6, §7.1 et le Tétragramme simple. Il produit une **ébauche**, pas
un résultat final : il faut ensuite reprendre à la main ou par modèle

- les majuscules de noms propres et d'épithètes (§9),
- les noms divins préfixés (§7.3, §8) — l'ébauche sort `laihova`, `vaihova`,
- l'ambiguïté sheva mobile / quiescent dans les cas non tranchés (§3),
- le mot `אֲדֹנָי` face au Tétragramme (§8).

Ces quatre catégories sont **les seules** à corriger systématiquement ; le
reste de la sortie mécanique est fiable.
