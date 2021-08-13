# UE12

Cours d'introduction à Python et à l'écosystème Python scientifique

## cours 1

installer et découvrir l'environnement Python / IPython / Jupyter; où on gratte le vernis en ce qui concerne

* le terminal
* les fichiers et répertoires, le répertoire courant
* l'éditeur de code (vs-code recommandé)
* markdown
* Python
* git
* Jupyter

on installe tout ce qu'il faut pour pouvoir localement : 
cloner le cours, exécuter les notebooks, et *a fortiori* écrire et exécuter un programme Python

## cours 2
* les rudiments du langage Python

## cours 3
* Python numérique (numpy)

## cours 4 
* pandas
* dataviz (matplotlib)

# Utilisation

## Notebooks du cours

Les notebooks se trouvent dans le répertoire `notebooks` situé à la racine du projet.
Ainsi pour y accéder, le plus simple est dans doute de lancer Jupyter directement dans ce répertoire:

```bash
# en supposant qu'on est dans notre env pip/conda
(PyNum) $ cd notebooks
(PyNum) $ jupyter notebook
```

Puis on peut ouvrir les notesbooks un par un depuis l'insterface de Jupyter.

## Création de la documentation HTML avec `jupyter book`

Le projet dispose d'une `Makefile` dédié rendant très simple la génération de la documentation HTML.

Pour se faire:

```bash
# On se rend dans le répertoire notebooks
(PyNum) $ cd notebooks

# et on lance le Makefile
(PyNum) $ make
```

Le résultat du build sera alors diposbile dans le sous-répertoire
[`notebooks/_build/html`](notebooks/_build/html/) et le point d'entrée est le fichier
[`index.htmlz](notebooks/_build/html/index.html) qu'il contient.

