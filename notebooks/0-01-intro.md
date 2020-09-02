---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Calysto Bash
  language: bash
  name: calysto_bash
notebookname: introduction
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<div style="display:grid">
    <span>Thierry Parmentelat</span>
    <span>Valérie Roy</span>
</div>
<div style="display:grid">
    <span><img src="media/inria-25-alpha.png" /></span>
    <span><img src="media/ensmp-25-alpha.png" /></span>
</div>
</div>

+++

# UE 12 - Introduction

+++

## comment lire ce notebook

+++

### nbhosting

+++

pour que vous puissiez lire ce premier cours, alors que vous n'avez encore rien installé sur votre ordi, vous pouvez le suivre en ligne sur le serveur de notebooks 

https://nbhosting.inria.fr/auditor/notebook/ue12-python-numerique

+++

### *Shift-Enter*

+++

ce document est un *notebook*; il contient des **cellules**, avec soit du texte (comme celle-ci), soit du code (comme la suivante) qu'on peut exécuter au fur et à mesure qu'on lit

le plus simple pour lire un notebook c'est de 

* sélectionner une cellule (avec la souris)
* taper *Maj-Entrée* (ou *Shift-Return* sur un clavier anglais)  
  ça exécute la cellule courante et ça passe à la suivante; essayez...

```{code-cell}
# ma première cellule de code contient
# un commentaire
# et une commande toute simple 
# qui affiche un message

echo "hey there !"
```

vous avez dû provoquer l'affichage de `hey there !` comme résultat de l'exécution de la cellule juste au dessus de celle-ci;  
continuez la lecture en faisant 'Maj-Entrée'

+++

### niveaux de lecture

+++

parfois on verra du contenu un peu technique, qui s'adresse plutôt aux élèves qui ont déjà des connaissances poussées  
on utilisera alors un code de couleur, c'est comme pour les pistes de ski :

+++ {"tags": ["level_basic"]}

* vert : niveau de base

+++ {"tags": ["level_intermediate"]}

* bleu : niveau intermédiaire

+++ {"tags": ["level_advanced"]}

* rouge : niveau avancé

+++

lorsqu'il n'y a pas de couleur, c'est comme si c'était vert, ça s'adresse à tout le monde

si c'est la tête de chapitre ou section qui est en couleur, cette couleur s'applique à toute la section; dans ce cas on met en vert, le cas échéant, la tête de section suivante

+++

### table des matières

+++

vous pouvez en principe activer la tables des matières en cliquant sur ce bouton :  
(sinon, voyez la toute dernière section)

![](media/fig-jupyter-toc2.png)

+++

### *readthedocs*

+++

je vous signale enfin que les supports du cours sont disponibles également sur  
https://ue12-python-numerique.readthedocs.io/

ce site est accessible depuis Internet sans authentification, mais par contre le contenu est *statique*, on ne peut pas modifier le contenu des cellules de code, ni rien exécuter

+++ {"slideshow": {"slide_type": ""}}

## objectifs

+++

l'approche pédagogique vise en premier lieu **à vous mener à l'autonomie** en ce qui concerne l'utilisation des ressources digitales; c'est pourquoi nous ne disposons **pas de salle informatique** comme ça a pu se faire à une époque; l'objectif est que vous sachiez à terme utiliser **uniquement votre ordinateur** pour travailler

+++

ce cours d'introduction vise à présenter, et à vous faire installer, les outils de base pour le cours d'informatique; il ne présente **aucune difficulté** mais vous êtes invité·e malgré tout à le suivre **avec une grande attention** car tous ces éléments sont **cruciaux pour la suite**

+++ {"slideshow": {"slide_type": ""}}

### objectifs globaux

pour le cours d'informatique de 1ère année :

* prise d'**autonomie**  
  * par rapport au numérique et à la programmation
  * focus sur quelques outils
* pour les mathématiques  
  * Python - numpy - pandas - matplotlib  
  * notebooks Jupyter
* workflow
  * git & github
* approfondissement langage
  * Python
  * C++
  * Java
* culture informatique
  * notions sur l'OS   
  * rudiments de programmation Web
  * rudiments sur programmation parallèle
  * rudiments sur l'utilisation du réseau

+++

### objectifs du premier module

+++

s'agissant du premier bloc de 4 x 3h :

* c'est un pré-requis pour autres cours  
 (notamment mathématiques)
* 4 parties
  * installations (ce cours-ci)
  * le langage Python 
  * tableaux et programmation vectorielle (`numpy`)
  * préparation (`pandas`) et  
    visualisation (`matplotlib`) des données

+++

### objectifs aujourd'hui

pour ce premier cours d'introduction/installation

* survol ultra-rapide des concepts de base (simple, basique)
* survol rapide et installation des outils de base  
  * OS, terminal, dossiers et fichiers
  * éditeur de code, markdown
  * git (ultra-light)
  * Python, Jupyter
* être capable de rapatrier le cours sur votre ordi, et d'y exécuter les notebooks

Notez que

* le cours est **coopératif**, et pas compétitif   
  ceux qui savent déjà **aident leurs camarades**
* voyez la checklist des compétences requises
  * à terminer pour la prochaine fois si nécessaire
  * posez vos questions sur [discourse.mines-paristech.fr](https://discourse-mines-paristech.fr)

+++

## outils (infrastructure)

+++

### notebooks : nbhosting

notebooks prêt à l'emploi

* aucune installation nécessaire
* navigation dans les slides : *Espace* et *Shift-Espace*
* évaluer une cellule de code : *Shift-Entrée*
* <https://nbhosting.inria.fr>

+++

### forum de discussion : discourse

forum de discussion pour 

* tous les cours de maths & info
* <https://discourse.mines-paristech.fr>

+++

### *handouts* html : readthedocs
* selon les cours
* celui-ci est disponible sur <https://ue12-python-numerique.readthedocs.io>
* par contre bien sûr, ce n'est pas interactif, on ne peut pas exécuter le code

+++ {"slideshow": {"slide_type": ""}}

## OS

+++ {"slideshow": {"slide_type": ""}}

* Windows, MacOS, linux
* quelques différences (très) visibles
* mais de nombreux concepts communs

+++ {"slideshow": {"slide_type": ""}}

### à quoi ça sert ?

* calculette  
  * un programme a accès à toutes les ressources
  * exemple: je range X dans la case mémoire 1
* ordinateurs
  * plein de programmes **en même temps**
  * accessoirement plein d'utilisateurs

+++ {"slideshow": {"slide_type": ""}}

### rôle de l'OS

* fournir de l'**isolation** entre les programmes
  * si deux programmes différents utilisent la case 1  
    pour ranger une donnée, ça ne va pas le faire !
* permettre la **concurrence**
  * faire tourner plusieurs programmes en même temps  
    sur un nombre fini de processeurs  
  * démo Activity Monitor  
    typiquement **plusieurs dizaines** de programmes
* fournir de l'**isolation** entre les utilisateurs

+++ {"slideshow": {"slide_type": ""}, "tags": ["level_advanced"]}

### notion de **processus** (en anglais *process*) 

* chaque programme qui tourne constitue un *process*
* les process sont isolés les uns des autres  
  * notamment la mémoire
* l'OS fait tourner tous les programmes  
  * dans un mode *chacun son tour*  
  * à relativement haute fréquence 
  * c'est le travail du *scheduler*

+++ {"tags": ["level_advanced"]}

#### soyons précis

le terme *OS* - *Operating System* a plein de significations différentes dans le langage courant

* Windows et MacOS : inclut une interface graphique 
* linux : l'interface graphique est plus clairement séparée, on a le choix

**mais** nous ici lorsqu'on parle d'OS, on désigne **seulement** ce qu'on appelle aussi le **noyau**

c'est-à-dire techniquement :  

* le **seul** programme dans l'ordinateur qui a **accès direct** aux périphériques
* les programmes sont **isolés les uns des autres**
* tous les autres programmes (*user land*) accèdent à ces ressources au travers d'**abstractions**
  * mémoire : **mémoire virtuelle**  
    la case mémoire '1' est redirigée vers un bout de mémoire allouée au programme  
  * **système de fichiers**  
    le disque dur est accessible au travers de dossiers et fichiers
  * etc ...

+++

### multi-utilisateurs, administrateur

+++

#### historiquement

le modèle d'usage des ordinateurs (très chers) était  
1 ordi = plusieurs (dizaines/centaines d') utilisateurs 

ce qui a mis en évidence le rôle de l'**adminstrateur** (*super-user*)  
qui se chargeait des tâches de maintenance et d'installation

+++

les usages ont beaucoup changé, mais cette dualité est restée  
dans beaucoup d'institutions / compagnies c'est la *DSI* (Direction des Systèmes d'Information) qui se charge de l'installation de base et de la sécurité

+++

jusque récemment, le modèle mental était que, pour faire une installation, il faut les droits d'administrateur  
de cette façon on peut faire des économies d'échelle (installation = processus compliqué, autant le faire 1 bonee fois pour tous les utilisateurs)

+++

#### les usages ont changé

+++

* non seulement pour les postes de travail c'est maintenant  
  1 ordi = 1 personne
* mais en plus, la **même personne** peut avoir besoin de **plusieurs environnements**
par exemple, un développeur peut travailler sur plusieurs projets, un en Python-3.6, un autre en Python-3.8, avec des combinaisons de librairies différentes pour chaque projet

+++

si bien que la notion d'installation unique pour 1 ordi n'a **que des inconvénients**

* c'est compliqué d'avoir les droits d'administrateur : la DSI y veille, et même sans DSI ça demande des manipulations en plus
* et ça rend très compliqué la mise à disposition de multiples environnements  
  si tout le monde a le même Python, a fortiori un développeur aura toujours le même Python

+++

#### choisir un mode d'installation dans l'espace utilisateur

+++

c'est pourquoi je vous recommande de choisir, lorsque c'est possible, un mode d'installation **dans l'espace utilisateur** plutôt qu'une installation dans la zone système

ainsi vos installation seront plus simples, et plus extensibles : vous pourrez plus facilement jongler entre les environnements lorsque vous serez plus agiles avex tout ceci

pour anticiper un peu, c'est la raison pour laquelle on vous recommandera d'installer Python avec miniconda, dans la section qui traite de Python

+++ {"slideshow": {"slide_type": ""}, "tags": []}

## le terminal

+++

le premier outil que nous allons voir c'est ce qu'on appelle le terminal; un terminal qu'est-ce que c'est ?

le terminal c'est tout simplement un programme qui permet d'exécuter des commandes

```{code-cell}
:hide_input: false

# la commande la plus basique est `pwd`
# pour afficher le répertoire courant

pwd
```

### `bash`

+++

il y a plein de types de terminal selon les systèmes d'exploitation, mais pour que nous travaillions tous ensemble sur le même objet, nous allons choisir un terminal qui s'appelle ``bash``

* `bash` vient avec l'installation de base sur MacOS et linux
* sur Windows, il faut l'installer séparément : je vous invite à installer une app qui s'appelle ***git for windows***  <https://gitforwindows.org/>,  
 qui fait d'une pierre deux coups (on parlera de git bientôt)
 
mais avant de voir cette installation, on va faire une digression sur la façon dont le terminal recherche ses commandes

+++

### `command not found`

+++

la première difficulté rencontrée par les débutants, c'est ce genre de symptôme  
(rappelez-vous, on exécute les cellules avec *Maj-Entrée*)

```{code-cell}
# j'essaie d'appeler une commande qui n'existe pas 

tutu
```

ce message d'erreur `command not found` - ou `commande introuvable`, vous indique le plus souvent qu'il y a quelque chose de mal installé

+++ {"tags": ["level_intermediate"]}

### le `PATH`

+++ {"tags": ["level_intermediate"]}

le `PATH` c'est le mécanisme qui permet au terminal de trouver les commandes

du coup quand on installe un nouveau logiciel, comme on va le faire tout de suite avec 'git for windows', il est parfois nécessaire de modifier le `PATH` pour que les nouvelles commandes deviennent accessibles depuis le terminal

+++ {"tags": ["level_intermediate"]}

ce n'est pas crucial de le savoir, mais si vous êtes curieux, sachez que

* `PATH` c'est ce qu'on appelle une variable d'environnement (ça veut dire qu'elle se propage d'un processus à l'autre), 
* et que c'est une liste de répertoires où sont cherchées les commandes

```{code-cell}
:tags: [level_intermediate]

# ici le ':' est un séparateur
echo $PATH
```

+++ {"tags": []}

### installation de *git for windows*

+++

> installation en live de gitforwindows sur une virtualbox 

à la question ***Adjusting your PATH environment*** :  
choisissez au moins l'option recommandée (#2), idéalement l'option #3

+++

![](media/fig-set-path-git-for-windows.png)

+++

### lancez un terminal

+++

![](media/fig-git-for-windows.png)

+++

### exercice

* installer *git for windows* si vous êtes sur windows
* lancez un terminal
* le cas échéant créez un raccourci pour pouvoir lancer un terminal rapidement
* tapez les commandes suivantes :

![](media/fig-terminal.png)

+++

## dossiers et fichiers

+++

le contenu du disque dur est organisé en **dossiers** et **fichiers** 

le **dossier** est juste un cas particulier de fichier  

* qui **contient d'autres fichiers** (ou dossiers, donc)  
* au lieu de contenir des données

termes synonymes :

* dossier, répertoire, *folder*, *directory*
* fichier, *file*

+++

### répertoire courant

+++

tous les programmes (processus) ont ce qu'on appelle un répertoire courant

dans le terminal on peut le voir avec la commande `pwd`  
(*print working directory*)

```{code-cell}
# petite digression, ici je suis dans un notebook 'bash'
# et je peux exécuter des commandes comme dans un terminal
pwd
```

#### à quoi ça sert

c'est uniquement une **commodité** pour ne pas avoir à retaper le chemin complet depuis la racine des dossiers

je m'explique :

```{code-cell}
# on crée un fichier bidon 

echo "Hello world" > foo.txt
```

```{code-cell}
# avec la commande `ls`
# on peut voir la liste des fichiers 
# et donc ici on va voir entre autres 
# le fichier 'foo.txt' qu'on vient de créer

ls 
```

```{code-cell}
# on peut vérifier que le fichier 'foo.txt' existe bien

ls foo.txt
```

```{code-cell}
# ou avoir plus de détails sur ce fichier: sa taille, sa date

ls -l foo.txt
```

```{code-cell}
:tags: [level_intermediate]

# pourquoi sa taille est de 12 ? 
# on a écrit dedans
# 
# hello (5 caractères)
# espace (1 caractère)
# world (5 caractères)
# newline (1 caractère)
```

une autre commande utile c'est `cat`; ça permet tout simplement de voir le contenu d'un fichier

```{code-cell}
# le point important c'est que je peux faire référence
# à ce fichier sous le nom simplement 'foo.txt'

cat foo.txt
```

```{code-cell}
# comme je suis dans le répertoire
# /Users/tparment/git/ue12-python-numerique/notebooks
pwd
```

```{code-cell}
# je pourrais faire aussi
# (à modifier éventuellement selon votre environnement)

cat /Users/tparment/git/ue12-python-numerique/notebooks/foo.txt
```

et donc pour moi, parce que je suis dans le répertoire
`/Users/tparment/git/ue12-python-numerique/notebooks/`

c'est pareil de faire

```console
cat /Users/tparment/git/ue12-python-numerique/notebooks/foo.txt
```

ou tout simplement 

```
cat foo.txt
```

+++ {"tags": []}

### chemins relatifs

+++ {"tags": ["level_intermediate"]}

ce serait aussi équivalent de faire 

```console
cat ./foo.txt
```

car le répertoire `.` désigne justement le répertoire courant

+++ {"tags": []}

par convention, `..` désigne le répertoire "au dessus" du répertoire courant  
on l'utilise pour fabriquer des chemins du genre de 

    cat ../frere/neveu

+++ {"tags": []}

pour "remonter" dans l'arborescence des dossiers, je peux donc utiliser un chemin relatif

```{code-cell}
:tags: []

pwd
```

```{code-cell}
# `cd` ça veut dire *change directory* 

cd ..
```

```{code-cell}
pwd
```

enfin, une astuce utile c'est pour **revenir en arrière** avec `cd -`

```{code-cell}
# du coup là je me retrouve à mon point de départ
cd -
```

### répertoire utilisateur (*home directory*)

+++

chaque utilisateur possède un répertoire,  
qui est la racine de l'arbre dans lequel il peut ranger ses affaires  
indépendamment du système d'exploitation

pour y aller le plus simple est de faire simplement `cd` sans paramètre

```{code-cell}
# sans paramètre je retourne tout en haut de mon espace
cd
```

```{code-cell}
# c'est mon home-directory
pwd
```

```{code-cell}
# et je peux redescendre là d'où je venais
cd -
pwd
```

+++ {"tags": ["level_intermediate"]}

pour information, le répertoire utilisateur peut être représenté par le signe `~` dans le terminal

```{code-cell}
:tags: [level_intermediate]

echo ~/git
```

## organisation en dossiers

+++

quelques conseils pour organiser votre travail en dossiers

+++

### ne pas abuser sur la profondeur des arbres  

évitez de couper les cheveux en 4 en créant plein de sous-répertoires, genre :

~~`/User/dupont/mines/première-année/info/ue12/python-numerique`~~

au contraire :

* si vous créez un dossier par sujet avec un nom explicite
  * par exemple ce cours pourrait s'appeler `ue12-python-numerique`
* et que vous regroupez tous ces dossiers dans un répertoire,
* ça peut largement suffire

du coup créez plutôt un dossier  
`/User/dupont/git/ue12-python-numerique`  

ou éventuellement pour une navigation plus facile  
`/User/dupont/Desktop/git/ue12-python-numerique`

+++

### noms de fichiers 

c'est assez facile (avec l'explorateur de fichiers notamment) de créer des fichiers dont le nom contient des caractères biscornus, comme des espaces ou des accents

mais après ça devient rapidement compliqué de les utiliser, dans le terminal notamment

c'est pourquoi on recommande d'**éviter les espaces et les accents** dans les noms de fichiers

+++

### créez des raccourcis

pour pouvoir facilement accéder à vos fichiers, investissez un peu de temps pour trouver comment on peut créer des raccourcis depuis l'explorateur de fichiers

+++

sur le screenshot suivant, on a choisi

* de créer un dossier `git` directement dans le Desktop
* pour l'instant il est vide, mais c'est là qu'on va ranger tous les dossiers de premier niveau
* comme il est créé dans le dossier `Desktop`, on voit ce dossier `git` directement sur le bureau
* et pour faire bon poids on a même créé un raccourci dans l'explorateur de fichiers 
* tout ça pour pouvoir y accéder rapidement en toute circonstance
* remarquez aussi le menu contextuel; on peut facilement créer un `git bash` qui démarrera directement dans ce dossier (`git` sera son répertoire courant)

![](media/fig-dossier-git.png)

+++ {"tags": ["level_intermediate"]}

### affichez les extensions dans les noms de fichier

dans l'explorateur Windows par défaut, si vous créez un fichier `foo.txt` on va vous montrer dans l'explorateur de fichiers une entrée qui s'affiche avec simplement `foo`

par défaut, on a jugé que c'était "plus simple" de ne pas montrer l'extension, ici `.txt`  
personnellement je ne trouve pas ça très pratique…

voici comment on peut changer ce comportement, pour voir les noms de fichier en entier, i.e. comme avec le terminal


![](media/fig-show-extensions-1.png)
![](media/fig-show-extensions-2.png)
