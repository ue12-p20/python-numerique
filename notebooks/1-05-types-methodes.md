---
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
notebookname: "objets, types et m\xE9thodes"
version: '1.0'
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
<span>Thierry Parmentelat</span>
<span><img src="media/inria-25-alpha.png" /></span>
</div>

+++ {"slideshow": {"slide_type": ""}}

# objets, types et méthodes

+++ {"slideshow": {"slide_type": "slide"}}

## Python est un paradigme orienté objet  

cela signifie que toutes vos données sont des objets  
entre autres choses chaque objet a un type

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: slide
---
# en Python absolument toutes les données
# en mémoire sont des objets
# chaque objet possède (entre autres)
# un type

# un module
import math

# un nombre
x = 4 * math.pi

# une chaine
texte = "une chaine"

# une fonction
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)
```

```{code-cell} ipython3
:cell_style: split

type(x)
```

```{code-cell} ipython3
:cell_style: split

type(texte)
```

```{code-cell} ipython3
:cell_style: split

type(fact)
```

```{code-cell} ipython3
:cell_style: split

type(math)
```

+++ {"slideshow": {"slide_type": "slide"}}

## méthode = fonction attachée à un type

+++

lorsqu'on appelle un méthode sur un objet,  
la syntaxe est donc  

```python
objet.methode(parametre)
```
    
ce qui se passe c'est que

* on cherche la méthode **à partir du type** de `objet`  
* on trouve une **fonction**, et on l'appelle 
* avec en premier argument l'objet

+++ {"slideshow": {"slide_type": "slide"}}

## appel de méthode illustré

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: ''
---
chaine = "bonjour"
chaine
```

```{code-cell} ipython3
:cell_style: split

# la recherche de 'capitalize' 
# à partir de `chaine`
# trouve une fonction rangée
# dans le type `str`

la_methode = str.capitalize
la_methode
```

```{code-cell} ipython3
:cell_style: split

# lorsqu'on écrit ceci
chaine.capitalize()
```

```{code-cell} ipython3
:cell_style: split

# c'est comme si on avait
# écrit 
la_methode(chaine)
```

```{code-cell} ipython3
:cell_style: split

# si on passe des arguments
chaine.center(13, '-')
```

```{code-cell} ipython3
:cell_style: split

# ils sont ajoutés après l'objet
str.center(chaine, 13, '-')
```

+++ {"slideshow": {"slide_type": "slide"}}

## à quoi ça sert ?

par rapport à un appel de fonction, 2 avantages

* la résolution du nom de la méthode se fait à l'exécution
  * le même code se comporte différemment
  * sur des entrées de type différents
  * permet d'écrire du code plus générique

* espaces de nom plus propres  
  pas besoin d'inventer des noms comme `str_capitalize`
