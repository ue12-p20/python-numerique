# UE12

Cours d'introduction à Python et à l'écosystème Python scientifique

# Installation

Afin de pouvoir visualiser et exécuter localement les éléments du cours, il est nécessaire d'installer les dépendances associées, via `pip` ou `conda`.

## Installation via `pip`

```bash
$ pip install -r requirements.txt
```

## Installation via `conda`

Nous allons créer un environnement virtuel `conda` à partir du fichier `environment.yml` fourni:

```bash
$ conda env create -f environment.yml
```

Cette commande a généré un nouvel environnement nommé "python-numérique" comme on peut le voir via la sous-commande `env list` (les différents Paths peuvent changer...):

```bash
❯ conda env list
# conda environments:
#
base                  *  /Volumes/Tools/miniconda
python-numerique         /Volumes/Tools/miniconda/envs/python-numerique
```

Pour utiliser cet environnement et à chaque fois que l'on voudra de ré-activer, on lancera la commande suivante:

```bash
$ conda activate python-numerique
```

# Objectif des cours

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
