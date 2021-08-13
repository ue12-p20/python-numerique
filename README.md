# UE12

Cours d'introduction à Python et à l'écosystème Python scientifique

# Installation

Afin de pouvoir visualiser et exécuter localement les éléments du cours, il est nécessaire d'installer les dépendances associées, via `pip` ou `conda`.

## Installation via `pip`

Un bonne première étape, optionnelle mais recommandée, consiste à créer un environnement virtuel:

```bash
# on se place dans le répertoire des fichiers clônés de Github
$ cd python-numerique

# puis on crée notre venv
# ⚠️ ici je suite sur Mac et je vais utiliser Python 3.9 comme base
$ python3.9 -m venv ./venv pip wheel --prompt "PyNum"
$ . ./venv/bin/activate

# Enfin je peux installer mes dépendances À L'INTÉRIEUR DE MON VENV
(PyNum)$ pip install -r requirements.txt
```

En détail:
- je crée un venv qui utilisera mon Python 3.9 installé
- il est créé dans un sous-répertoire `venv` du répertoire courant
- j'installe immédiatement les paquets `pip` et `wheel` dans leur dernière version
- et je définir un prompt custom `PyNum` qui me premettra de savoir quand mon venv est actif

## Installation via `conda`

```bash
$ conda env create -f environment.yml
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
