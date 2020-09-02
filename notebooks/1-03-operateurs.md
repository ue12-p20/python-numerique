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
rise:
  autolaunch: true
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
notebookname: opérateurs
---

+++ {"slideshow": {"slide_type": "slide"}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat</span>
<span><img src="media/inria-25-alpha.png" /></span>
</div>

+++ {"slideshow": {"slide_type": ""}}

# opérateurs

+++ {"slideshow": {"slide_type": "slide"}}

## arithmétiques

```{code-cell}
# sans surprise, les 4 opérations arithmétiques
a = 10
b = 25

(a + b) * (b - a)
```

```{code-cell}
:cell_style: split

# une petite subtilité 
# toutefois avec la division
# ceci retourne TOUJOURS 
# un flottant

25 / 10
```

```{code-cell}
:cell_style: split

# la division entière 
# quant a elle 
# se note //

25 // 10
```

+++ {"slideshow": {"slide_type": "slide"}}

## typage

en Python tous les objets sont typés  
le comportement des opérateurs dépend du type

```{code-cell}
:cell_style: split

# ajouter deux chaines permet
# de les concatener
'abc' + 'def' 
```

```{code-cell}
:cell_style: split

# on peut même multiplier 
# par un entier
3 * 'abc'
```

+++ {"slideshow": {"slide_type": "slide"}}

## arithmétiques - suite

```{code-cell}
:cell_style: split

# division euclidienne
c = 64
d = 5
```

```{code-cell}
:cell_style: split

# le reste 
c % d
```

```{code-cell}
:cell_style: split

# le quotient

c // d
```

```{code-cell}
:cell_style: split

# puissance

d ** c
```

```{code-cell}
:cell_style: split

# remarque: pas de limite 
# de précision avec les entiers

d ** c > 2 ** 64
```

+++ {"slideshow": {"slide_type": "slide"}}

## comparaisons

```{code-cell}
a = 10
b = 25
```

```{code-cell}
:cell_style: split

a == b
```

```{code-cell}
:cell_style: split

a != b
```

```{code-cell}
:cell_style: split

a <= b
```

```{code-cell}
:cell_style: split

a < b
```

```{code-cell}
:cell_style: split

# une curiosité
6 <= a <= 20
```

```{code-cell}
:cell_style: split

6 <= a <= 25 <= b <= 30
```

+++ {"slideshow": {"slide_type": "slide"}}

## logiques

```{code-cell}
:cell_style: split

6 <= a and b <= 10
```

```{code-cell}
:cell_style: split

6 <= a or b <= 10
```

+++ {"slideshow": {"slide_type": "slide"}}

## indexation avec `[]`

+++

sur tous les objets de type 'séquence'  
c'est-à-dire pour nous à ce stade les chaines  
mais on verra que ça s'applique à d'autres, comme les listes (un peu de patience..)

```{code-cell}
chaine = 'abcdefghij'
len(chaine)
```

```{code-cell}
:cell_style: split

# en python les index commencent à 0
chaine[0]
```

```{code-cell}
:cell_style: split

# les index négatifs commencent à la fin
chaine[-1]
```

+++ {"slideshow": {"slide_type": "slide"}}

## slices

```{code-cell}
:cell_style: split

# une 'slice' permet de découper un morceau
chaine[1:4]
```

```{code-cell}
:cell_style: split

# et même de choisir un pas
chaine[1:8:2]
```

```{code-cell}
:cell_style: split

# dans un slice on peut omettre
# n'importe lequel des 3 termes
chaine[3::]
```

```{code-cell}
:cell_style: split

# ce qui serait ici 
# identique à juste
chaine[3:]
```

```{code-cell}
:cell_style: split

# dans un slice on peut omettre
# n'importe lequel des 3 termes
chaine[:4:]
```

```{code-cell}
:cell_style: split

# ce qui serait ici 
# identique à juste
chaine[:4]
```

+++ {"slideshow": {"slide_type": "slide"}}

## slices et bornes

la forme générale est donc `debut:fin:pas`  
**ATTENTION** que l'index `fin` **n'est pas inclus**

```{code-cell}
# la convention permet de facilement emboiter les résultats
chaine[0:3] + chaine [3:6] + chaine[6:] == chaine
```

```{code-cell}
# notez enfin que le pas peut être négatif aussi
# ce qui donne cette forme idiomatique
# pour renverser une séquence
chaine[::-1]
```
