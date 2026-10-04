# tefillat-tools

Outils [Claude Code](https://code.claude.com) pour préparer des pièces
liturgiques hébraïques destinées à la projection en synagogue.

## Ce que ça contient

**`preparer-une-piece`** — de l'hébreu vocalisé au fichier d'import :
translittération séfarade selon des règles jointes, proposition de traduction
française, découpage de l'alignement hébreu / translittération / français,
contrôle, et fichier `.json` prêt à charger. Le skill ne touche jamais au
texte sacré : il signale, un humain tranche.

## Installer

Dans une session Claude Code :

```
/plugin marketplace add ahegdal/tefillat-tools
/plugin install tefillat-tools@tefillat-tools
```

Le skill se déclenche de lui-même (« translittère ce psaume », « prépare ce
chant ») ou s'appelle par `/tefillat-tools:preparer-une-piece`.

## Mettre à jour

```
/plugin marketplace update tefillat-tools
```

ou, une fois pour toutes : `/plugin` → *Marketplaces* → `tefillat-tools` →
*Enable auto-update*. Voir [CHANGELOG.md](CHANGELOG.md).

## Ne pas modifier ici

Ce dépôt est une **publication**. La source des règles et du skill vit
ailleurs, et chaque version est fabriquée et vérifiée depuis elle : une
correction faite ici serait écrasée à la version suivante. Pour signaler une
erreur, ouvrez une *issue*.
