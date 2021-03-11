les trucs à faire pour l'an prochain; trop tard pour faire cette année car ça va créer
plein de conflits...


# deux formats de notebook différents

**DONE**

les fichiers problématiques étaient en fait du markdown standard et pas du myst

pour convertir, simplement

jupytext --to md:myst ...


# install miniconda

**DONE**

la recette exposée dans `0-02-outils.md` est buggée pour les gens qui ont un accent dans leur nom

on a corrigé ça dans un addendum `0-03-install-miniconda-revised.md` qu'il convient maintenant de merger


# jupyter book

**MOSTLY OK**

reste à vérifier que ça marche vraiment bien, y compris les recherches

images: elles marchent pour l'essentiel, mais pas dans les cellules de licence

dans ce cas, problème identifié: les images qui sont incluses dans du html ne sont pas bien traitées par jupyter-book
voir sample-course et notamment le 3eme notebook pour voir comment on peut faire autrement si on veut vraiment


# espaces en fin de ligne

ATTENTION: ne pas enlever TOUS les espaces dans le markdown (à cause des double espace)

**ONGOING**

OK:
0-01 0-02 0-10 0-98 0-99
1-01 1-02 1-03 1-04 1-05 1-06 1-07 1-08 1-09 1-10 1-98 1-99
