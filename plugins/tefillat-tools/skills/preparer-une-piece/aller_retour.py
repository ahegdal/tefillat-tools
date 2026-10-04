# -*- coding: utf-8 -*-
"""L'aller-retour : la translittération d'entrée contre la translittération de
retour (celle que la norme donne de l'hébreu proposé), mot à mot.

    python3 aller_retour.py <piece.json>

Bibliothèque standard seule. Lit un fichier d'import dont les lignes portent une
`provenance` avec `translit_entree` ; la translittération de retour est celle des
segments. Mesure, ne juge pas.

**Expliqué** : les deux mots ont le même **squelette dur** — les consonnes
qu'aucune source ne confond. Ce qui reste est de la graphie : accents, casse,
aleph/ayin, h/ḥ/kh, b/v, gémination, voyelles, ou une **convention étrangère**
(`ch`, `tz`, `''`, circonflexe — voir `conventions.json`).
**Inexpliqué** : le squelette diffère — l'hébreu proposé ne rend pas l'entrée.
Une ligne qui laisse un mot inexpliqué est signalée et **ne doit pas être
proposée**.

Sortie 0 = aucun mot inexpliqué. Sortie 1 = au moins un. Sortie 2 = rien à comparer.
"""
import json
import re
import sys
import unicodedata

MAQAF = '־'
PONCT = re.compile(r'^[!?;:,.…«»"\'\-—–׃()]+$')


def atomes(he):
    return [x for x in (he or '').replace(MAQAF, ' ').split() if not PONCT.match(x)]


def mots(tr):
    return [w.strip('.,;:!?«»…()') for w in (tr or '').split() if not PONCT.match(w)]


def sans_accents(w):
    return ''.join(c for c in unicodedata.normalize('NFD', w) if not unicodedata.combining(c))


def _normaliser(w):
    """Minuscules, sans accents (le circonflexe s'en va avec), et les
    conventions étrangères sans ambiguïté ramenées à la norme."""
    s = sans_accents(w.lower()).replace("''", '"').replace('tz', 'ts')
    return s.replace("'h", 'h')


def squelettes(w):
    """Les squelettes durs possibles d'un mot. Un `ch` en a deux : il peut
    noter un ḥet ou un khaf (retirés, comme tout son h) ou un shin."""
    s = _normaliser(w)
    lectures = {s.replace('ch', ''), s.replace('ch', 'sh')} if 'ch' in s else {s}
    out = set()
    for x in lectures:
        # §7.1 : le tsadi géminé s'écrit « tts » — une seule lettre, pas t + ts.
        x = x.replace('tts', 'ts')
        x = x.replace('sh', 'S').replace('ts', 'C').replace('kh', '')
        x = re.sub(r"['\"\-]", '', x).replace('f', 'p').replace('q', 'k')
        x = re.sub(r'[hbvaeiouyw]', '', x)
        out.add(re.sub(r'(.)\1+', r'\1', x))
    return out


def familles(a, b):
    """Ce qui distingue deux mots au même squelette, chaque famille par un test isolé."""
    x, y = a.lower(), b.lower()
    if x == y:
        return ['casse']
    f = []
    if re.search(r"ch|tz|''|[îôâêû]|'h", x):
        f.append('convention étrangère (ch, tz, \'\', circonflexe)')
    x2, y2 = _normaliser(a), _normaliser(b)
    if x2.startswith("'") != y2.startswith("'"):
        f.append('aleph initial (§4.2)')
    if re.findall(r"['\"]", x2.lstrip("'")) != re.findall(r"['\"]", y2.lstrip("'")):
        f.append('aleph / ayin (§4)')
    sons_h = lambda w: re.findall(r'kh|ḥ|ch|(?<![sct])h', w)
    if sons_h(x) != sons_h(y):
        f.append('h / ḥ / kh (§2)')
    if re.sub(r'[^kq]', '', x2) != re.sub(r'[^kq]', '', y2) or \
            re.sub(r'[^fp]', '', x2) != re.sub(r'[^fp]', '', y2):
        f.append('k / q, f / p (§2)')
    doubles = lambda w: len(re.findall(r'([b-df-hj-np-tv-z])\1', sans_accents(w)))
    if doubles(x2) != doubles(y2):
        f.append('gémination (§7.1)')
    if ('ei' in x or 'éy' in x) and ('ei' in y or 'éy' in y) and ('ei' in x) != ('ei' in y):
        f.append('diphtongue éy (§5)')
    if ('è' in x) != ('è' in y):
        f.append('è / e (§1.4)')
    voy = lambda w: re.sub(r'[^aeiou]', '', sans_accents(w.replace('ei', 'é').replace('éy', 'é')))
    if voy(x) != voy(y):
        f.append('voyelle (§3)')
    return f or ['accent']


def comparer(depart, retour, hebreu):
    """{'s10': (atomes, mots d'entrée), 'ecarts': [(a, b, familles)], 'inexpliques': [...]}"""
    d, r = mots(depart), mots(retour)
    out = {'s10': (len(atomes(hebreu)), len(d)), 'ecarts': [], 'inexpliques': []}
    if len(d) != len(r):
        out['inexpliques'].append('compte de mots : entrée %d, retour %d' % (len(d), len(r)))
        return out
    for a, b in zip(d, r):
        if a == b:
            continue
        if squelettes(a).isdisjoint(squelettes(b)):
            out['inexpliques'].append('%s → %s' % (a, b))
        else:
            out['ecarts'].append((a, b, familles(a, b)))
    return out


def lignes_a_comparer(data):
    lot = data['chants'] if isinstance(data, dict) and 'chants' in data else [data]
    for d in lot:
        for n, l in enumerate(d.get('lignes') or [], 1):
            p = l.get('provenance') or {}
            if p.get('translit_entree') and (l.get('hebreu') or '').strip():
                retour = ' '.join((s[0] or '') for s in l.get('segments') or [])
                yield n, p['translit_entree'], retour, l['hebreu']


def main(argv):
    if len(argv) != 1:
        print(__doc__.strip().splitlines()[3].strip())
        return 2
    data = json.load(open(argv[0], encoding='utf-8'))
    total = inex = ecarts = s10 = 0
    for n, dep, ret, he in lignes_a_comparer(data):
        c = comparer(dep, ret, he)
        total += 1
        s10 += c['s10'][0] == c['s10'][1]
        ecarts += len(c['ecarts'])
        inex += len(c['inexpliques'])
        print('ligne %d — entrée : %s' % (n, dep))
        print('          retour : %s   (§10 : %d atomes / %d mots)' % (ret, c['s10'][0], c['s10'][1]))
        for a, b, f in c['ecarts']:
            print('          expliqué   %s → %s : %s' % (a, b, ', '.join(f)))
        for x in c['inexpliques']:
            print('          INEXPLIQUÉ %s' % x)
    if not total:
        print('rien à comparer : aucune ligne ne porte provenance.translit_entree et un hébreu')
        return 2
    print('lignes %d · §10 conformes %d · mots expliqués %d · inexpliqués %d' % (total, s10, ecarts, inex))
    return 1 if inex else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
