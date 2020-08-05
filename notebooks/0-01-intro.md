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
notebookname: cours d'intro
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

https://nbhosting.inria.fr/auditor/notebook/ue12-intro

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
# /Users/tparment/git/ue12-intro/notebooks
pwd
```

```{code-cell}
# je pourrais faire aussi
# (à modifier éventuellement selon votre environnement)

cat /Users/tparment/git/ue12-intro/notebooks/foo.txt
```

et donc pour moi, parce que je suis dans le répertoire
`/Users/tparment/git/ue12-intro/notebooks/`

c'est pareil de faire

```console
cat /Users/tparment/git/ue12-intro/notebooks/foo.txt
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

~~`/User/dupont/mines/première-année/info/ue12/intro`~~

au contraire :

* si vous créez un dossier par sujet avec un nom explicite
  * par exemple ce cours pourrait s'appeler `ue12-intro`
* et que vous regroupez tous ces dossiers dans un répertoire,
* ça peut largement suffire

du coup créez plutôt un dossier  
`/User/dupont/git/ue12-intro`  

ou éventuellement pour une navigation plus facile  
`/User/dupont/Desktop/git/ue12-intro`

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

+++ {"tags": ["level_basic"]}

## éditeur de code

+++

pour pouvoir facilement modifier le contenu de nos fichiers texte, comme tout à l'heure le fichier `foo.txt`, on va utiliser un programme qui s'appelle un **éditeur de code**

+++

### micro-démo vs-code

+++ {"tags": []}

> micro démo de Visual Code sur le fichier `foo.txt`

* depuis le terminal, aller dans le bon répertoire et lancer 
  ```
  code .
  ```

***

* manipulations simples
  * afficher/cacher l'explorateur de fichiers
  * modifier `foo.txt`, sauver la version modifiée
  * créer un nouveau fichier `bar.txt`, le sauver
  * observer le contenu des fichiers depuis le terminal avec `cat` 
  * montrer comment se manifeste la fin de ligne

***

* montrer des manipulations élémentaires de fenêtres
  * afficher les deux fichiers côte à côte
  * puis l'un au dessus de l'autre

***

* montrer comment :
  * chercher une extension  (prétexte : l'extension Python)
  * installer/désinstaller
  * activer/désactiver une nouvelle extension 
 
***

* montrer comment :
  * passer d'une application à une autre avec `⌥ ⇥` (Alt-Tab)
  * typiquement pour basculer entre vscode et terminal
 
***

* de retour dans vs-code, montrer la palette :
  * `⇧ ⌘ P` (mac)
  * `⇧ ` (windows)

+++

voir aussi  
https://code.visualstudio.com/docs/getstarted/userinterface

+++

### installation éditeur de code

+++

* on n'impose pas l'utilisation de vs-code mais c'est **fortement recommandé** si vous êtes débutant

**ATTENTION**

* ne pas utiliser (évidemment) un outil comme Word pour ce type de travail (si vous vous demandez pourquoi : créez sous Word l'équivalent de notre `foo.txt`, puis faites `cat foo.docx`…)
* beaucoup de soucis l'an passé avec les éditeurs de type *pyzo*, on recommande de **ne pas utiliser** cet environnement

+++

**conseil**

en cochant ces cases lors de l'installation, vous pourrez lancer vs-code avec un clic droit depuis un dossier ou un fichier

![](media/fig-explorer-vs-code.png)

+++

exercice :

* refaire les manipulations vous-mêmes après avoir installé un éditeur de code

+++

## markdown

+++

le couteau suisse pour écrire des documents

* avec un minimum de présentation 
  * sections
  * listes
  * gras, italique, code
  * liens
  * maths
* toujours dans un **fichier texte** (à nouveau, ≠ Word)

+++

format **très populaire** en ce moment, supporté e.g. :

* dans les notebooks, justement,
* dans discourse
* dans github
* sur whatsapp (en partie), …

et plus généralement dans tous les sites web de forums/blogs, où on peut entrer du texte directement depuis le navigateur

+++

### micro-démo sous vs-code

> sous vs-code

* créer un fichier `foo.md`
* remarquer la petite icône ![](media/fig-vscode-markdown.png)
  * afficher côte à côte le markdown brut et rendu
* rapide survol
  * sections
  * listes avec et sans numérotation
  * gras, italique
* insister sur les plusieurs façons de mettre du code,
  * soit `inline` sans saut de ligne, ou alors 
  * avec des "triple ticks" <code>```</code>
  * avec 4 espaces de marge
* images et liens
  * montrer le code markdown de cette cellule notebook 
  
cheatsheet <https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf>

+++

### mathjax

+++

on peut aussi écrire des maths en markdown  
ça se fait en utilisant le langage $\LaTeX$  
c'est un peu abscons au début mais on s'y habitue vite

***

$$
\forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+,
\forall x, |x-x_0| < \alpha\implies |f(x)-f(x_0)| < \epsilon
$$

***

$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$

+++

#### *inline*

à la base markdown utilise pour ça le signe `$`

si vous voulez mettre des maths dans un paragraphe (on dit *inline*), vous utilisez un seul `$` au début et à la fin de l'équation; c-a-d si vous écrivez

```latex
voici une petite équation $y = x^2 +2x +1$ au milieu de la ligne
```

vous obtenez 

voici une petite équation $y = x^2 +2x +1$ au milieu de la ligne

+++

#### paragraphe séparé

pour mettre une équation dans un paragraphe séparé on double le dollar de début et de fin

du coup

```latex
$$
\forall x \in \mathbb{R}, \forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+ \\
 |x'-x| < \alpha\implies |f(x')-f(x)| < \epsilon
$$
```

se présentera comme ceci :

$$
\forall x \in \mathbb{R}, \forall \epsilon \in \mathbb{R}^+, \exists\alpha\in\mathbb{R}^+ \\
 |x'-x| < \alpha\implies |f(x')-f(x)| < \epsilon
$$

+++

#### les mots du jargon $\LaTeX$

+++

ça dépasse complètement notre périmètre que d'essayer de faire le tour de $\LaTeX$; je préfère commencer par quelques exemples qui devraient vous permettre de démarrer

+++ {"cell_style": "split"}

$$
\forall x\in \mathbb{R},
\; \exists y \leq \epsilon
$$

+++ {"cell_style": "split"}

```
\forall x \in \mathbb{R},
\; \exists y \leq \epsilon
```

+++ {"cell_style": "split"}

$$x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}$$

+++ {"cell_style": "split"}

```
x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}
```

+++ {"cell_style": "split"}

$$
A_{m,n} = 
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
 \end{pmatrix}
$$

+++ {"cell_style": "split"}

```
$$
A_{m,n} = 
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
 \end{pmatrix}
$$
```

+++ {"cell_style": "split"}

$$
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
$$

+++ {"cell_style": "split", "slideshow": {"slide_type": ""}}

```
\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}
```

+++ {"tags": ["level_intermediate"]}

ceux qui veulent creuser peuvent 

* commencer par cet article https://www.physicsoverflow.org/15329/mathjax-basic-tutorial-and-quick-reference

* approfondir avec celui-ci https://en.wikibooks.org/wiki/LaTeX/Mathematics

+++

## Python

+++ {"tags": []}

### installation de base

* il y a de très nombreuses distributions disponibles
* notre recommandation : miniconda
  * relativement léger
  * permet d'installer en mode "user" i.e. sans droits administrateur
* démo installation miniconda sur Windows
* on écrit un ou deux programmes bidon
* faire tourner dans le terminal

+++

![](media/fig-miniconda-download.png)

+++

![](media/fig-miniconda-install.png)

+++

### première utilisation / vérification

+++

*** 
**Attention**  

* les signes `$ ` ou `>>> ` ne font pas partie de ce que vous devez taper
* c'est juste une indication pour dire 
  * avec `$ ` :  que la commande s'adresse au terminal  
  c-à-d à nouveau : GitBash sur Windows, Terminal sur MacOS,  
  et n'importe quel terminal bash sur linux
  * avec `>>> ` : que la commande s'adresse à l'interpréteur Python
***

ça signifie que ce que vous voyez ici correspond à ce qui sera affiché dans le terminal, mais si vous suivez bien les indications vous n'avez pas à taper le `$` ou les `>>>`, ce sera déjà affiché lorsque vous taperez vos commandes

+++

#### vérifier que Python est bien installé

```console
$ type python
python is /c/Users/Thierry Parmentelat/miniconda3/python
```

si à ce stade vous avez un *python: not found* c'est que vous n'avez pas bien coché la case  
*Add Miniconda3 to my PATH environment variable*

+++

#### lancer python en mode interactif

on va calculer $2^{100}$, afficher un texte, et quitter l'interpréteur

```console
$ python
>>> 2 ** 100
1267650600228229401496703205376
>>> print("hello world")
hello world
>>> exit()
```

+++

#### créer et lancer un premier script

+++

dans le répertoire de votre choix, ouvrez *vs-code* et créez un fichier qui s'appelle `fact.py` contenant ce texte (n'hésitez pas à copier-coller) :

```{code-cell}
cat fact.py
```

et dans le même répertoire lancez python pour calculer le factoriel d'un nombre

```{code-cell}
python fact.py 10
```

#### afficher le numéro de version de Python

+++

c'est toujours utile d'être bien sûr de la version qu'on a sous la main (surtout avec les environnments virtuels)

```{code-cell}
python --version
```

### installation de IPython avec `pip`

+++

lorsqu'on installe Python on installe un ensemble minimal de **librairies**  
par exemple dans `fact.py` on a fait `import sys`  
pour pouvoir utiliser la librairie `sys`

+++

c'est très facile d'installer d'autres librairies au delà de cet ensemble minimal  
pour cela python vient avec une commande qui s'appelle `pip`  
qui s'utilise directement **depuis le terminal**

```{code-cell}
# pour avoir la liste des librairies installées on peut faire 
pip list
```

#### installer d'autres librairies avec `pip install`

nous allons utliser `pip install` pour installer IPython, et pour ça vous allez taper (dans un terminal)

```{code-cell}
# la première fois qu'on installe une librairie, ça peut prendre 
# un petit moment pour aller chercher les packages 
# sur Internet et les installer

pip install ipython
```

### micro-démo `ipython`

+++

si vous devez taper du code Python directement dans le terminal, je vous recommande d'utiliser la commande `ipython` plutôt que l'interpréteur standard `python`

voilà à quoi ça ressemblerait si on devait refaire le calcul de $2^{100}$ comme on l'a fait plus haut


```console
$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 2 ** 100
Out[1]: 1267650600228229401496703205376

In [2]: print("hello world")
hello world

In [3]: exit()
```

comme vous le voyez c'est presque pareil; simplement avec ipython c'est beaucoup plus pratique dès qu'on va au delà de ce genre de session de démo, notamment pour

* remonter et modifier l'historique
* obtenir de l'aide en ligne
* utiliser la complétion

+++

### installation de numpy / pandas / matplotlib

+++

le calcul scientifique en Python se fait avec 3 librairies très très communes, sur lesquelles on reviendra très prochainement

pour l'instant nous allons les installer avec la commande

```console
pip install numpy pandas matplotlib
```

+++

#### vérification

pour vérifier, vous pouvez d'abord, depuis le terminal, faire

    pip show numpy
    
qui vous montrera en plus le numéro de version de `numpy`

+++

vous pouvez aussi importer la librairie depuis `ipython`, ça donne une session qui ressemble à ceci (vous ne devez pas avoir d'erreur du type `ModuleNotFound`)

```
$ ipython
Python 3.8.3 (default, Jul  2 2020, 11:26:31)
<blabla>

In [1]: import numpy

In [2]: numpy.__version__
Out[2]: '1.19.1'
```

+++

### la complétion

+++

ce qu'on appelle complétion, c'est la capacité d'un outil à vous aider à taper votre code; exemple :

* on lance `ipython`
* on tape le début d'une commande, par exemple `import frac` 
* à ce point, on appuie sur la touche `Tabulation`
* ipython se rend compte que le seul mot qui fait du sens dans ce contexte et qui commence par `frac` est `fractions`, du coup il remplit la commande

+++

la complétion est un outil **indispensable** pour ne pas perdre un temps précieux; apprenez à la maitriser

notez d'ailleurs que **ça existe aussi dans le terminal**, typiquement très utile avec les noms de fichiers, entre autres

+++

### *RTFEM*

+++

il est normal de faire des erreurs quand on code, tout le monde en fait  

on verra un peu plus loin comment les détecter le plus tôt possible (grâce à des extensions dans un éditeur de code)  
mais les cas où ça se produit quand même, la première chose à faire est bien entendu de **lire le message d'erreur**

le langage Python s'efforce de vous donner des indications plutôt claires dans ces cas-là

+++

voici par exemple un fichier très proche de `fact.py` qu'on vient de faire tourner  
mais j'y ai intentionnellement glissé une petite erreur de syntaxe  
voici le code, et ce qui se produit si on essaie de le faire tourner

```{code-cell}
:cell_style: split

cat fact-broken.py
```

```{code-cell}
:cell_style: split

python fact-broken.py
```

je vous demande en exercice de trouver l'erreur en question

+++

en pratique il arrive qu'on se trouve face à des erreurs plus difficiles à diagnostiquer, mais dans tous les cas **commencez par *RTFEM***  
ça va de soi mais ça va mieux en le disant, je suis certain qu'on aura l'occasion de le rappeler pendant les cours de langage :)

+++

## git

+++

### survol

+++

git fait partie des outils dits de "SCM" *source code management*

son rôle est d'aider les développeurs à s'y retrouver dans la gestion des versions

+++

d'ailleurs ça n'est pas limité aux logiciels :

* jeux de données
* documentation
* lois (très utile pour gérer les modifications)
* …

+++

### à quoi ça sert - quand on travaille seul

+++

en première approximation, on peut se servir de `git` pour :

* travailler "avec un filet"  
  pour facilement **revenir en arrière** à une version qui marche  
  ça sert donc en particulier de **sauvegarde de luxe**
* lorsqu'on travaille sur plusieurs améliorations en même temps  
  on peut facilement créer **des branches**  
  pour traiter les améliorations séparément  
  avant de tout mettre ensemble

+++

### à quoi ça sert - en équipe

+++

on peut aussi :

* **synchroniser** le travail entre groupes / personnes
* dans un sens ou dans l'autre  
  c-a-d: chacun travaille de son coté, et on réconcilie le tout ensuite

git ne fait pas de supposition sur le workflow ou l'organisation,  
on peut l'adapter à tous les cas d'usage (un seule personne, un petit groupe, plusieurs groupes, open-source, …)

+++

### les notions de base

+++ {"tags": []}

* un dépôt (en anglais *repo*) :
  * ça ressemble à **un répertoire** avec **tout son contenu**
  * mais ça contient aussi **toutes les versions** successives
* un *commit* :
  * ça correspond à une version particulière du dépôt
  
et donc un dépôt contient autant de commits que de versions successives

+++

### alice et bob

+++

un exemple de workflow [sous forme de présentation pdf](../filmedia/git-workflow-animations.pdf)

(le pdf fait partie du dépôt git,  
dans `media/git-workflow-animations.pdf`)

+++

### installation

+++

* Windows : normalement à ce stade vous avez déjà installé *git for windows*
* MacOS: voyez ce lien <https://www.atlassian.com/git/tutorials/install-git#mac-os-x>
* linux : voyez ce lien <https://www.atlassian.com/git/tutorials/install-git#linux>

+++

**vérification**

+++

pour vérifier votre installation, vous devez pouvoir taper dans le terminal

```{code-cell}
git --version
```

### digression : URL

+++

lorsque bob copie le travail qu'alice a publié sur github, il va utiliser `git clone` (on va le faire dans un tout petit moment)

mais il faut évidemment qu'il puisse dire à `git clone` exactement **quoi copier**, parce que l'Internet, c'est grand…

pour ça il a besoin [d'une URL (Uniform Resource Locator)](https://en.wikipedia.org/wiki/URL), pour désigner le dépôt d'Alice

c'est quoi une URL ? vous en connaissez déjà plein d'exemples, comme  
http://google.com/  
https:/google.com/  
https://en.wikipedia.org/wiki/URL

* le premier terme (`http` ou `https`) désigne **le protocole** à utiliser pour joindre la ressource
* le second morceau (`google.com` ou `en..wikipedia.org`) désigne le *hostname* qu'il faut joindre; en fait on utilise un service réseau [qui s'appelle le DNS (Domain Name Server](https://en.wikipedia.org/wiki/Domain_Name_System) pour traduire le nom `www.google.com` en une adresse réseau (et c'est comme ça qu'en fait deux requêtes n'aboutissent pas forcément sur le même serveur, heureusement d'ailleurs)
* la suite est optionnellea permet de désigner un item particulier à l'intérieur de ce serveur; c'est comme ça qu'on peut ranger des milliers de page à l'intérieur du serveur wikipedia

+++

#### les URLs sur `github`

+++

à l'intérieur du serveur github, les URLs des dépôts ressemblent toutes à celles-ci

https://github.com/python/cpython  
https://github.com/gvanrossum/cpython

* le premier étage (`python` ou `gvanrossum`) désigne une organisation ou un individu 
* le second étage (`cpython`) désigne un dépôt  
  (ici par exemple `cpython` pour l'implémetation classique du langage Python)

+++

### cloner le dépôt du cours

+++

vous avez maintenant tout le bagage pour pouvoir copier le dépôt du cours

il vous suffit pour ça de faire 

    git clone https://github.com/ue12/intro
    
**Attention toutefois**

* cette commande va créer sur votre disque tout un répertoire, dont le nom est `intro`
* notez qu'il sera créé **dans votre répertoire de travail** (`pwd`)
* donc commencez par **vous mettre au bon endroit** 
* le nom `intro` est déduit de la dernière partie de l'URL  
  et si cela ne vous convient pas comme nom vous pouvez en choisir un autre :
  
      git clone https://github.com/ue12/intro ue12-intro

+++

pour vérifier que tout s'est bien passé :

    # si vous avez utilisé la deuxième forme
    # votre répertoire local s'appelle ue12-intro et pas juste intro
    cd ue12-intro 
    
    # le répertoire est rempli avec la dernière version du cours
    cat README.md

+++

### suivre les évolutions

+++

pour terminer cette micro-introduction : imaginez que demain je publie des modifications dans ce dépôt

alors pour mettre à jour votre dépôt local, il vous suffira de faire 

    # toujours dans le même répertoire bien sûr
    git pull

+++

bon en pratique il arrive que ce soit un peu plus compliqué que ça, mais c'est l'idée générale

on creusera tout ceci dans le cours dédié à git dans quelques semaines

+++

## notebooks Jupyter

+++

### installation

+++

le socle s'installe comme ceci (ça peut prendre un moment) :

```console
pip install jupyter
```

+++

je vous invite à installer également ceci; c'est optionnel pour débuter avec Jupyter, mais ça sera nécessaire très vite pour lire les notebooks du cours

```console
pip install jupytext[myst]
```

+++ {"tags": []}

#### vérification

+++

si tout s'est bien passé vous devez pouvoir voir les versions des différents morceaux de Jupyter comme ceci :

```{code-cell}
jupyter --version
```

### utilisation de base

+++

pour lancer un serveur jupyter vous tapez dans le terminal la commande

```
jupyter notebook
```

![](media/notebooks-001-run.png)

+++

ce qui va avoir pour effet d'ouvrir une fenêtre ou un onglet dans votre navigateur Web

![](media/notebooks-002-welcome.png)

+++

### le processus serveur

en fait là on fait deux choses complémentaires

* on lance un programme (le serveur Jupyter) qui tourne dans le terminal
* on demande au browser de créer une page qui interagit avec ce serveur

du coup ça signifie que **le serveur Jupyter doit tourner en permanence**

* si vous le tuez depuis le terminal, le notebook dans le browser va cesser de fonctionner
* ça signifie aussi que cette session du terminal n'est plus utilisable pour autre chose…

+++

### micro-démo Jupyter classic

+++

* un notebook est associé à **un langage**
* nos supports de cours :
  * le plus souvent le langage est **Python**
  * le présent notebook est une exception, son langage est **bash** 
* chaque cellule est *typée* comme **markdown** ou **code*
* et bien sûr celles typées **code** sont exécutées par … le langage du notebook

+++ {"tags": ["level_intermediate"]}

(il est possible aussi de mélanger plusieurs langages dans un notebook, mais c'est d'un usage plus complexe)

+++

pour créer un nouveau notebook

![](media/notebooks-003-creating-py3.png)

+++

pour renommer le notebook

![](media/notebooks-004-renaming.png)

![](media/notebooks-005-named.png)

+++

comme toujours il faut sauver son travail régulièrement;  
remarquez dans le terminal où vous avez lancé le serveur, un message de confirmation

![](media/notebooks-006-saved.png)

+++

choisir le type de la cellule; on peut aussi faire 

* `Control-M M` pour markdown
* `Control-M Y` pour code (y comme pYthon)

![](media/notebooks-007-markdown.png)

il y a aussi des raccourcis pratiques pour créer directement des sections

* `Control-M 1` met la cellule en markdown, et insère si nécessaire un `#` au début de la cellule; on crée ainsi une cellule de titre de rang 1
* `Control-M 2` : de rang 2, etc…

+++

insérer une cellule; souvent on fait aussi/plutôt

* `⌥-Enter` pour évaluer la cellule et en insérer une dessous

![](media/notebooks-008-insert-cell.png)

+++

une cellule de code

![](media/notebooks-009-code-cell.png)

+++

on est toujours dans un des deux modes :

* édition : pour changer le contenu d'une cellule
* commande : pour voir le résultat
* la couleur du bandeau vous dit dans quel mode vous êtes
* pour sortir du mode édition : tapez `Escape` ou encore `Control-M`

![](media/notebooks-010-edit-mode.png)

![](media/notebooks-011-cmd-mode.png)

+++

à partir du menu, faites *Help* → *Keyboard Shortcuts*

![](media/notebooks-020-keyboard-shortcuts.png)

+++

sélection multiple

* en général on a exactement **une** cellule courante
* mais avec `Shift-⬆` ou `Shift-⬇` on peut sélectionner plusieurs cellules contigües

![](media/notebooks-030-sel-mult.png)

+++

du coup on peut par exemple les déplacer toutes ensemble

![](media/notebooks-031-sel-moved-down.png)

+++

## lire le cours localement

+++

### prérequis

+++

#### indispensable 

pour pouvoir ouvrir un notebook du cours - n'importe lequel - il faut avoir fait ceci

```console
pip install jupytext[myst]
```

autrement, vous allez avoir un affichage bizarre…

+++

#### utile pour ce notebook

pour pouvoir exécuter les notebooks en bash (dont celui-ci, donc), il vous faut également faire

    pip install calysto_bash

+++

### épilogue

+++

à ce stade vous avez tout ce qu'il faut pour tout mettre ensemble, c'est-à-dire :

* cloner le repo du cours
* lancer jupyter à la racine

+++

puis vous pouvez

* ouvrir le notebook de démonstration  
  (je ne recommande pas forcément de commencer avec le présent notebook, car il utilise un kernel `bash` qui n'est pas standard…)
* l'exécuter localement
* et vous amuser à le modifier

+++

je vous demande surtout de

* ouvrir le notebook de checklist, qui résume les compétences attendues
* et vérifier que vous avez bien tout installé 
* et si vous êtes en avance, attaquez-vous à l'exercice qui figure à la fin de la checklist

+++ {"tags": ["level_advanced"]}

### jupyter lab

+++ {"tags": ["level_advanced"]}

pour les curieux, sachez qu'il existe une nouvelle interface Jupyter qui s'appelle JupyterLab

c'est un plus moderne que Jupyter classic que nous utilisons, mais c'est beaucoup plus compliqué à intégrer… quoi qu'il en soit, si vous voulez jeter un coup d'oeil à cet outil, il faut savoir que 

* on le lance en tapant `jupyter lab` au lieu de `jupyter notebook`
* et pour ouvrir un notebook en `.md` - comme ceux du cours donc - on ne peut pas double-cliquer dans le .md, il faut utiliser `Open with` comme ceci

![](media/fig-jupyter-lab-open-md.png)

+++

***
***
***

+++

**Partie optionnelle**

+++ {"tags": ["level_intermediate"]}

## Python et vs-code

+++

si vous avez le temps (section intermédiaire)

+++

maintenant qu'on a installé Python, on peut retourner dans vs-code pour voir à quoi ressemble l'extension Python
(vérifiez que vous l'avez bien installée)

il y a quelques réglages à faire la toute première fois qu'on s'en sert, voyons cela :

+++

### `pylint`

* `pylint` est un outil pour trouver les erreurs dans le code Python  
* il détecte beaucoup d'erreurs (erreurs de syntaxe, variables mal orthographiées, etc..)

vs-code vous montre les erreurs :

* l'extension Python de vs-code permet d'afficher **en permanence**  (à chaque sauvegarde) les soucis détectés par `pylint` 
* c'est pourquoi si `pylint` n'est pas installé, vs-code va automatiquement vous proposer de le faire (choisissez alors de préférence l'option *install with pip*)

+++ {"tags": []}

pour information, le terme `lint` ou `linter` désigne, de manière générique, un outil qui fait des vérifications statiques (i.e. sans faire tourner le code); ça existe pour beaucoup de langages

+++

### l'interpréteur Python

+++

vs-code a besoin de savoir où est installé Python, pour pouvoir le lancer 

ne serait-ce que pour lancer `pylint`,   
mais il peut aussi, dans un usage plus avancé, vous aider à exécuter votre code;   
bref il a besoin de savoir où se trouve l'interpréteur Python  

en fait il est malin et il sait trouver **tous** les interpréteurs qui sont installés  
et donc ce dont il a besoin c'est que vous lui disiez **lequel** vous voulez utiliser

+++ {"tags": ["level_advanced"]}

lorsqu'on fait du développement professionnel, on a habituellement une installation Python par projet; une partie optionnelle avancée sera consacrée à ce sujet un peu plus loin

+++

![](media/fig-vscode-select-python.png)

+++

### voir les erreurs

+++

votre premier objectif est de pouvoir trouver les erreurs visuellement au fur et à mesure que vous écrivez votre code Python

dans l'illustration suivante j'ai fait exprès d'importer le module `mathematic` qui est fantaisiste (on verra que la librarie mathématique s'appelle en fait simplement `math`)

si votre installation est correcte vous devez pouvoir sauver un fichier qui se termine en `.py`, et si vous y insérez la même erreur (et que vous sauvez le fichier) vous devez voir apparaître un *zigouigoui* comme ceci ![](media/fig-vscode-zigouigoui.png)

lorsque le texte est souligné de cette manière, cela indique une erreur; apprenez à les lire et à les corriger **avant même** d'essayer de faire tourner votre code, cela vous fera gagner du temps

+++

![](media/fig-vscode-show-errors.png)

+++ {"tags": []}

**Avertissement**

Il faut toutefois toujours garder à l'esprit que cette phase de détection préliminaire des erreurs de programmation n'a **qu'une valeur indicative**

`pylint` fait tous ses efforts pour vous faire gagner du temps en trouvant le maximum d'erreurs le plus tôt possible, **mais** : 

* ce n'est pas parce qu'un programme n'a pas de zigouigoui qu'il va tourner à coup sûr 
* et réciproquement, il y a des programmes qui tournent alors qu'ils ont exhibé des erreurs

donc il faut garder votre cerveau en marche, et ne pas se fier aveuglément à cette information

+++ {"tags": ["level_intermediate"]}

## extensions Jupyter

+++

si vous avez le temps (section intermédiaire)

+++

vous remarquerez que certaines *features*, disponibles sur nbhosting, ne le sont pas sur votre ordinateur à ce stade; par exemple, les codes de couleur des cellules par niveau, ou la table des matières navigable sur le coté

Jupyter est un système extensible; sur nbhosting on a activé quelques-unes de ces extensions, et voici comment vous pouvez les activer également de votre côté

```{code-cell}
:tags: []

# d'abord on installe les extensions standard

pip install -U ipywidgets
jupyter nbextension enable --py widgetsnbextension

pip install -U jupyter_contrib_nbextensions 
jupyter contrib nbextension install
```

```{code-cell}
:tags: []

# puis on active celles qui nous intéressent

# la table des matières navigable
jupyter nbextension enable toc2/main
# les cellules qui ne prennent que la moitié de la largeur
jupyter nbextension enable splitcell/splitcell

# les codes de couleur 
pip install nb-courselevels
jupyter nbextension enable courselevels/index
```

+++ {"tags": ["level_advanced"]}

## multiples environnements Python

+++

pour ceux qui sont très en avance (section niveau avancée)

+++

on l'a mentionné un peu plus haut, cela peut être utile de créer plusieurs environnements Python différents; c'est utile notamment :

* si vous travaillez sur plusieurs projets différents, qui ont chacun leur ensemble de dépendances, pas forcément compatibles entre elles; par exemple, l'un utilise Django-2.x et l'autre Django-3.x
* et aussi, lors de la sortie d'une nouvelle release de Python, que vous voulez essayer sans tout casser

+++

il existe plusieurs solutions pour gérer cela, notamment la solution `virtualenv`, mais nous allons pour notre part nous concentrer sur miniconda, puisque c'est ce qu'on a installé

+++

### miniconda

+++

c'est un des points forts de miniconda, que de permettre de facilement créer/activer/détruire des environnements multiples; on entend par environnement :

* un socle `Python` accessible par les commandes `python` et `pip`
* installé au départ sans aucune librairie tierce (enfin si, disons pliutôt le strict minimum, comme `pip`), pour que vous puissiez construire votre environnement de scratch

+++

les commandes utiles sont

* `conda env list`
* `conda create -n mon_environnement python=3.8`  
* `conda env remove -n mon_environnement`

+++

et pour gérer tout cela, on dispose de commandes pour changer d'environnement; le modèle mental est simple : 

* lorsque vous créez un terminal, vous êtes dans l'environnement qui s'appelle `base`, c'est celui que vous avez utilisé jusqu'ici
* vous pouvez passer dans un autre environnement avec  
  `conda activate mon_environnement`  
  qui a pour effet, entre autres, de modifier votre `PATH` pour que la commande `python` soit cherchée ailleurs
* pour en sortir, et revenir dans `base`, vous faites  
  `conda deactivate`

+++

### exemple de session

+++

voici à titre indicatif une session sous macos pour illustrer tout ceci

vous remarquerez comme le *prompt* bash reflète **l'environnement dans lequel on se trouve**, ça semble **relativement impératif** si on ne veut pas s'emmêler les pinceaux; surtout n'utilisez pas cette technologie si votre prompt ne montre pas l'environnement courant, c'est beaucoup trop facile de se tirer une balle dans le pied si on n'a pas cet aide-mémoire

+++

#### la liste de mes environnements
```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/tparment/miniconda3
<snip ...>
```

+++

#### j'en crée un nouveau avec Python-3.8

```
[base] ~ $ conda create -n demo-py38 python=3.8
Collecting package metadata (current_repodata.json): done
Solving environment: done
<snip ...>
```

+++

#### on le voit
```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/tparment/miniconda3
demo-py38                /Users/tparment/miniconda3/envs/demo-py38
<snip...>
```

+++

##### pour entrer dans le nouvel environnement

```
[base] ~ $ conda activate demo-py38
[demo-py38] ~ $
```

+++

#### les packages installés

très peu de choses

```
[demo-py38] ~ $ pip list
Package    Version
---------- -------------------
certifi    2020.4.5.1
pip        20.0.2
setuptools 46.2.0.post20200511
wheel      0.34.2
```

+++

#### on y installe ce qu'on veut
```
[demo-py38] ~ $ pip install numpy==1.15.3
```

+++

#### la version de python
```
[demo-py38] ~ $ python --version
Python 3.8.2
```

+++

#### sortir 
```
[demo-py38] ~ $ conda deactivate
[base] ~ $
```

+++

#### la version de python
```
[base] ~ $ python --version
Python 3.7.6
```

+++

#### on n'a pas perturbé l'environnement de départ
```
[base] ~ $ pip show numpy
Name: numpy
Version: 1.18.1
```

+++

#### pour détruire l'environnement en question
```
[base] ~ $ conda env remove -n demo-py38

Remove all packages in environment /Users/tparment/miniconda3/envs/demo-py38:
```

+++

### retour dans vs-code

+++

* créez un nouvel environnement miniconda avec Python-3.8
* de retour dans vs-code, sélectionnez cet environnement

notez que ce réglage est associé au *workspace* vs-code

c'est quoi un *workspace* ? ça correspond en gros à la sauvegarde de l'état de l'éditeur lui-même : la liste des fichiers en cours d'édition, les onglets ouverts, etc…  

pour expérimenter, créez une session vs-code dans un directory, choisissez votre environnement Python, sortez de la session; ré-ouvrez vs-code sur le même répertoire, vous devez retrouver ce réglage
