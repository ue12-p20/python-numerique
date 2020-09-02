---
celltoolbar: Slideshow
ipub:
  sphinx:
    toggle_input: false
    toggle_input_all: false
    toggle_output: false
    toggle_output_all: false
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: primer programmation Python
rise:
  autolaunch: true
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
version: '1.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat</span>
<span><img src="media/inria-25-alpha.png" /></span>
</div>

+++ {"slideshow": {"slide_type": ""}}

# UE12 - Python : généralités

comment utiliser le langage

+++ {"slideshow": {"slide_type": "slide"}}

## notion de programme

+++

dans un ordinateur coexistent plusieurs programmes 

* qui partagent les ressources matérielles
* c'est le rôle de l'OS que de garantir leur cloisonnement

parmi ces programmes

* explorateur de fichiers
* navigateur Internet
* éditeur de code : Visual Studio code (vscode), atom, emacs, vim, pycharm, ...
* et plein d'autres naturellement (mail, pdf, spotify, vlc, ...)
* terminal
* interpréteur Python

+++ {"slideshow": {"slide_type": "notes"}}

Dans ce qui suit, nous envisageons surtout deux programmes, le terminal et l'interpréteur Python.

+++ {"cell_style": "split", "slideshow": {"slide_type": "slide"}}

## démos d'utilisation de Python

1. lancer un programme tout fait  
  `$ python monprogramme.py`
1. lancer un interpréteur interactif  
  `$ python`  
  ou encore mieux  
  `$ ipython`
1. mode 'mixte' comme ce notebook  
  `$ jupyter notebook`

+++ {"cell_style": "split"}

**illustration**

ces usages sont explicités dans cette
[vidéo introductive](https://youtu.be/ULzWaZQa1Dc)

+++ {"slideshow": {"slide_type": "slide"}}

## nos cas d'usage

+++ {"slideshow": {"slide_type": ""}}

les programmes impliqués dans les différents scénarios

* terminal : la façon la plus simple/rustique de lancer d'autres programmes
* interpréteur Python : le programme qui exécute le code Python
  * (différence avec les langages compilés)
* interpréteur IPython : une surcouche qui ajoute de la souplesse
  * complétion
  * aide en ligne
  * déplacement et édition dans l'historique

+++ {"slideshow": {"slide_type": "slide"}}

### nos cas d'usage (2)

+++ {"slideshow": {"slide_type": ""}}

dans les cas hybrides comme les notebooks, plusieurs programmes collaborent ensemble

  * on écrit du code dans un éditeur / navigateur
  * qui dialogue avec un serveur Jupyter
  * qui lui-même dialogue avec un interpréteur Python (ou autre)
  * le code et les résultats sont échangés de l'un à l'autre

+++ {"slideshow": {"slide_type": "slide"}}

## sachez à qui vous parlez

+++

**convention**

lorsque c'est ambigu, on notera :

* commande à taper dans un terminal, préfixée avec un `$`  

```bash
    $ python
```
    
* commande à taper dans un interpréteur Python

```python
>>> a = 100
```

+++ {"slideshow": {"slide_type": "slide"}}

### note à propos de Windows

+++

* la notation avec un `$` pour se référer au terminal vient historiquement de Unix
  * i.e. aujourd'hui Linux et MacOS

* le programme en question s'appelle un *shell* 
  * on l'apparente à l'application `Terminal`
  * en pratique souvent `bash` - il en existe des variantes
  
* sur Windows cette sorte de terminal n'est pas native
  * mais elle est présente dans les versions récentes de Windows
  * dans un composant `WSL` - Windows Susbsytem Linux
  * envisagez de l'installer (quelques exemples du cours risquent peut-être de ne pas fonctionner à l'identique)

* autre option: Git Bash semble être un bon `bash` pour Windows

+++ {"slideshow": {"slide_type": "slide"}}

## savoir si Python est installé

+++

vous avez peut-être déjà python installé; tapez dans un terminal

```bash
$ python --version
```

ou encore

```bash
$ python3 --version
```

si vous lisez:

* `Python 3.6.n` ou `Python 3.7.n` : vous avez un Python installé
* `Python 3.x` avec $x <= 5$ : votre Python a besoin d'une mise à jour
* `Python 2.x` : ne pas utiliser Python 2 !
* `command not found` : Python n'est pas installé

+++ {"slideshow": {"slide_type": "slide"}}

## guide pour l'installation

+++

il existe des programmes d'installation de Python pour toutes les plateformes, MAIS

* si vous êtes débutant et n'avez pas d'idée préconçue 
* on recommande d'utiliser conda - <https://docs.conda.io>
  * anaconda pour les utilisateurs débutants  
    (grosse installation très complète)

  * miniconda pour les plus aguerris
  
anaconda vient avec un ensemble très complet : 

* Python, IPython
* notebooks Jupyter
* énorme pile de data science / machine learning
  * dont bien sûr `numpy`, `pandas` `matplotlib`

+++ {"slideshow": {"slide_type": "slide"}}

## note historique

Python2 est une version plus ancienne du langage

* elle **n'est pas compatible** et il ne **faut surtout pas** l'utiliser
* sa fin de vie est prévue en Janvier 2020 (plus du tout de support)
* ce qui achève une période de transition de 10 ans

+++ {"cell_style": "center", "slideshow": {"slide_type": ""}}

c'est pourquoi 

* pendant la période transitoire les deux ont coexisté
* d'où les commandes `python2` et `python3` 
* pour lancer Python3
  * sur certains systèmes `python3`
  * de plus en plus `python` tout court suffit

+++ {"slideshow": {"slide_type": "slide"}}

## testez votre installation

+++ {"cell_style": "center"}

* avec votre navigateur allez visiter [le cours sur github](https://github.com/ue12/python-numerique/tree/master/demo)
* si ce n'est pas déjà fait, utilisez `git clone` pour dupliquer le repo sur votre oridinateur  
  `$ git clone https://github.com/ue12/python-numerique`  
  ou encore si vous voulez choisir le nom du dossier créé par le clone 
  `$ git clone https://github.com/ue12/python-numerique ue12-python-numerique`  
* déplacez-vous dans le sous-dossier `demo`  
  `$ cd ue12-python-numerique/demo`

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}

### lancez les deux programmes

```bash
$ python3 fact.py
fact(4) = 24
fact(25) = 15511210043330985984000000
```

*** 

```bash
$ python3 users.py
Emilie (Lambert), 25 ans
Julien (Masson), 30 ans
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

## options : Jupyter et VScode

* une introduction rapide à   
  [l'installation et à l'usage des notebooks](https://nbhosting.inria.fr/auditor/notebook/python-slides:extras/slides-extras/03-1-notebooks-basic)  
  est disponible sur nbhosting

* idem en ce qui concerne [Visual Studio Code](https://nbhosting.inria.fr/auditor/notebook/python-slides:extras/slides-extras/07-vscode)
