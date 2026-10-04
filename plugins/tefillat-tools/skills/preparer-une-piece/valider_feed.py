# -*- coding: utf-8 -*-
"""Valide un fichier d'import de pièce (feed .json), hors ligne.

    python3 valider_feed.py <piece.json> [--corpus chant|liturgie|lecture]

Bibliothèque standard seule. Ne lit aucune base, n'appelle aucun service,
n'écrit rien : il lit un fichier et parle.

Deux niveaux, qui ne se confondent pas :

  REFUS         — ce que la chaîne d'import refuserait. Mêmes règles qu'elle.
  SIGNALEMENTS  — ce qu'un humain doit regarder avant l'import : l'invariant
                  d'alignement, le recollage, le rapport de longueur, l'hébreu
                  sans voyelles, les invariants absolus de la norme. Un
                  signalement n'est pas un verdict : le fichier reste importable.

Sortie 0 = importable, aucun signalement.
Sortie 2 = importable, avec signalements — à relire avant de l'envoyer.
Sortie 1 = refusé — la chaîne d'import ne le chargera pas.

Ce script **confirme** la liste de contrôle du SKILL.md ; il ne la remplace
pas. Les deux doivent rendre le même verdict.
"""
import json
import re
import sys

STRUCTURES = ('table', 'libre')
FORMATS = ('htf', 'fr')
RENDUS = (None, '', 'multi', 'mono')
GENRES = ('liturgie', 'rubrique', 'source')
CORPUS = ('chant', 'liturgie', 'lecture')
ATTENDUES = ('titre_he', 'titre_translit', 'titre_fr', 'slug_propose')

HEBREU = re.compile(r'[א-ת]')              # une lettre hébraïque
NIQQUD = re.compile(r'[ְ-ׇֻ]')          # une voyelle (hors daguesh)
MAQAF = '־'
PONCT = re.compile(r'^[!?;:,.…«»"\'\-—–׃]+$')        # un signe isolé n'est pas un mot

RAPPORT_HAUT = 3.0          # au-delà : les 1,3 % extrêmes du corpus mesuré
RAPPORT_BAS = 1 / 3.0       # en deçà : les 0,2 % extrêmes


def atomes(he):
    """Les atomes hébreux : le maqaf vaut une espace, la ponctuation isolée ne
    compte pas (sans quoi un `!` fabrique un mot fantôme)."""
    return [x for x in (he or '').replace(MAQAF, ' ').split() if not PONCT.match(x)]


def mots(tr):
    return [w for w in (tr or '').split() if not PONCT.match(w)]


def _texte(v):
    return v if isinstance(v, str) else ''


def refus_extrait(d, corpus=None):
    """La liste des refus d'un extrait. Vide = la chaîne d'import l'accepte."""
    if not isinstance(d, dict):
        return ["le fichier doit être un objet JSON { … }, pas %s" % type(d).__name__]
    r = []
    if d.get('structure') not in STRUCTURES:
        r.append("« structure » doit valoir table ou libre — reçu %r" % d.get('structure'))
    if d.get('format') not in FORMATS:
        r.append("« format » doit valoir htf ou fr — reçu %r" % d.get('format'))
    if d.get('rendu') not in RENDUS:
        r.append("« rendu » de la pièce doit valoir multi, mono ou être absent — reçu %r"
                 % d.get('rendu'))
    apres = d.get('apres')
    if apres is not None and not (isinstance(apres, str) and apres.strip()):
        r.append("« apres » doit nommer le slug d'une pièce — reçu %r" % apres)
    lignes = d.get('lignes', [])
    if not isinstance(lignes, list):
        return r + ["« lignes » doit être une liste — reçu %s" % type(lignes).__name__]
    for n, l in enumerate(lignes, 1):
        if not isinstance(l, dict):
            r.append("ligne %d : doit être un objet { … }" % n)
            continue
        if l.get('genre') not in GENRES:
            r.append("ligne %d : « genre » doit valoir liturgie, rubrique ou source — reçu %r"
                     % (n, l.get('genre')))
        if l.get('rendu') not in RENDUS:
            r.append("ligne %d : « rendu » doit valoir multi, mono ou être absent — reçu %r"
                     % (n, l.get('rendu')))
        segs = l.get('segments', [])
        if not isinstance(segs, list):
            r.append("ligne %d : « segments » doit être une liste" % n)
            continue
        for k, s in enumerate(segs, 1):
            if not (isinstance(s, (list, tuple)) and len(s) == 2):
                r.append("ligne %d, segment %d : un segment est une paire "
                         "[translittération, français] — reçu %r" % (n, k, s))
            elif not all(x is None or isinstance(x, str) for x in s):
                r.append("ligne %d, segment %d : les deux éléments sont du texte — reçu %r"
                         % (n, k, s))
    if corpus == 'liturgie' and lignes and not d.get('quarantaine') and not apres:
        r.append("pièce de liturgie sans rang : ajouter \"apres\": \"<slug de la pièce qui "
                 "la précède>\" — sans lui la chaîne refuse le lot entier")
    return r


def signalements(d):
    """Ce qu'un humain doit regarder. Ne s'applique qu'à un extrait sans refus."""
    s = []
    for k in ATTENDUES:
        if not _texte(d.get(k)).strip():
            s.append("clé « %s » absente ou vide : la pièce se nomme mal à l'import" % k)
    lignes = d.get('lignes', [])
    if not lignes:
        s.append("aucune ligne : l'import ne chargera rien")
    for n, l in enumerate(lignes, 1):
        he = _texte(l.get('hebreu'))
        segs = [(_texte(a), _texte(b)) for a, b in l.get('segments', [])]
        tr = ' '.join(a for a, _ in segs)

        if l.get('genre') == 'liturgie':
            if he.strip() and not HEBREU.search(he):
                s.append("ligne %d : le champ hébreu ne porte aucune lettre hébraïque (%r)"
                         % (n, he.strip()[:40]))
            if HEBREU.search(he) and not NIQQUD.search(he):
                s.append("ligne %d : hébreu sans voyelles — la translittération ne se "
                         "décide pas sans elles" % n)
            if any(not a.strip() and not b.strip() for a, b in segs):
                s.append("ligne %d : segment mort, ses deux côtés sont vides" % n)

        # Invariant d'alignement (§10 de la norme).
        if HEBREU.search(he) and tr.strip():
            a, m = atomes(he), mots(tr)
            if len(a) != len(m):
                s.append("ligne %d : §10 rompu — %d atomes hébreux, %d mots translittérés"
                         % (n, len(a), len(m)))

        # Recollage : les segments recollés par une espace rendent la ligne.
        for k, (a, b) in enumerate(segs, 1):
            for nom, v in (('translittération', a), ('français', b)):
                if '  ' in v:
                    s.append("ligne %d, segment %d : espace double dans la %s — le "
                             "recollage ne rendra pas le texte" % (n, k, nom))
                elif v.strip() and v != v.strip():
                    s.append("ligne %d, segment %d : %s bordée d'espaces — le "
                             "recollage ne rendra pas le texte" % (n, k, nom))

        # Rapport de longueur français / translittération.
        for k, (a, b) in enumerate(segs, 1):
            if a.strip() and b.strip():
                q = len(b.strip()) / len(a.strip())
                if q > RAPPORT_HAUT or q < RAPPORT_BAS:
                    s.append("ligne %d, segment %d : le français fait %.1f fois la "
                             "translittération — frontière à vérifier (signal, pas verdict)"
                             % (n, k, q))

        # Invariants absolus de la norme (§1, §4) — sur la translittération seule.
        if re.search(r'c', tr, re.I):
            s.append("ligne %d : lettre « c » dans la translittération (§1.1)" % n)
        if re.search(r'è', tr, re.I):
            s.append("ligne %d : « è » dans la translittération — le segol s'écrit e (§1.4)" % n)
        if re.search(r'[‘’ʼʻ“”]', tr):
            s.append("ligne %d : apostrophe ou guillemet typographique — aleph = ' et "
                     "ayin = \" en ASCII (§4)" % n)
    return s


def verdict(data, corpus=None):
    """(refus, signalements) pour un extrait ou un lot `{"chants": [...]}`."""
    if corpus is not None and corpus not in CORPUS:
        return ["corpus inconnu : %r (attendu : %s)" % (corpus, ', '.join(CORPUS))], []
    if isinstance(data, dict) and 'chants' in data:
        lot = data['chants']
        if not isinstance(lot, list):
            return ["« chants » doit être une liste d'extraits"], []
    else:
        lot = [data]
    refus, sig = [], []
    for i, d in enumerate(lot, 1):
        pre = 'pièce %d : ' % i if len(lot) > 1 else ''
        r = refus_extrait(d, corpus)
        refus += [pre + x for x in r]
        if not r:
            sig += [pre + x for x in signalements(d)]
    rangs = [d.get('apres') for d in lot if isinstance(d, dict) and d.get('apres')]
    if len(rangs) != len(set(rangs)):
        refus.append("deux pièces du lot déclarent le même rang : leur ordre ne se lit pas")
    return refus, sig


def main(argv):
    args = list(argv)
    corpus = None
    if '--corpus' in args:
        i = args.index('--corpus')
        corpus = args[i + 1] if i + 1 < len(args) else ''
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__.strip().splitlines()[2].strip())
        return 1
    try:
        with open(args[0], encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print('REFUS  le fichier ne se lit pas comme du JSON : %s' % e)
        print('verdict : REFUSÉ (1 refus)')
        return 1
    refus, sig = verdict(data, corpus)
    for x in refus:
        print('REFUS  ' + x)
    for x in sig:
        print('SIGNAL ' + x)
    if refus:
        print('verdict : REFUSÉ (%d refus) — la chaîne d\'import ne le chargera pas' % len(refus))
        return 1
    if sig:
        print('verdict : IMPORTABLE, %d signalement(s) à relire' % len(sig))
        return 2
    print('verdict : IMPORTABLE, aucun signalement')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
