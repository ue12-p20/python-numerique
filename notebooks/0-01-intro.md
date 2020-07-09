---
celltoolbar: Slideshow
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: Intro
rise:
  autolaunch: true
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
version: '1.0'
---

+++ {"slideshow": {"slide_type": "slide"}}

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

+++ {"slideshow": {"slide_type": ""}}

# introduction

**survol Python / numérique / dataviz**

+++ {"slideshow": {"slide_type": "slide"}}

## programme

* pré-requis pour autres cours  
 (notamment mathématiques)
* 3 parties
  * le langage Python 
  * tableaux et programmation vectorielle (`numpy`)
  * préparation (`pandas`) et  
    visualisation (`matplotlib`) des données

+++ {"slideshow": {"slide_type": "slide"}}

## objectifs

* vernis sur les concepts du langage
* et sur les outils de base  de calcul scientifique

pour être capable de :

* lire du code simple
* écrire du code simple
* mettre en oeuvre dans un notebook
* et progressivement dans des programmes autonomes  
  (pas forcément pendant cette première série de 3 cours)

+++ {"slideshow": {"slide_type": "slide"}}

## outils (infrastructure)

* `nbhosting.inria.fr` : notebooks prêt à l'emploi  
  * aucune installation nécessaire
  * navigation dans les slides : *Espace* et *Shift-Espace*
  * évaluer une cellule de code : *Shift-Entrée*
* *"handout"* au format html (non interactif)
  * https://ue12-python-numerique.readthedocs.io
* forum de discussion (tous les cours de maths & info)
  * <https://discourse.mines-paristech.fr>

+++ {"slideshow": {"slide_type": "slide"}}

## outils (installés localement)

pas indispensable au début (grâce à `nbhosting`), mais requis à terme :

* terminal (*bash*)
* un éditeur de texte (si vous n'en avez pas : VScode)
* Python 
* IPython / Jupyter  
  `pip install jupyter`
