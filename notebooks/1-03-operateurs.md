---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: "op\xE9rateurs"
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
</div>

<img src="media/inria-25-alpha.png" />

+++ {"slideshow": {"slide_type": ""}}

# opérateurs

+++ {"slideshow": {"slide_type": "slide"}}

## arithmétiques

```{code-cell} ipython3
# sans surprise, les 4 opérations arithmétiques
a = 10
b = 25

(a + b) * (b - a)
```

```{code-cell} ipython3
:cell_style: split

# une petite subtilité
# toutefois avec la division
# ceci retourne TOUJOURS
# un flottant

25 / 10
```

```{code-cell} ipython3
:cell_style: split

# la division entière
# quant a elle
# se note //

25 // 10
```

```{code-cell} ipython3
:cell_style: split

# et le reste la division entière
# se note %

25 % 10
```

```{code-cell} ipython3
# et on peut combiner les deux précédents
f"{25} = {25 // 10} * 10 + {25 % 10}"
```


+++ {"slideshow": {"slide_type": "slide"}}

## typage

en Python tous les objets sont typés  
le comportement des opérateurs dépend du type

```{code-cell} ipython3
:cell_style: split

# ajouter deux chaines permet
# de les concatener
'abc' + 'def'
```

```{code-cell} ipython3
:cell_style: split

# on peut même multiplier
# par un entier
3 * 'abc'
```

+++ {"slideshow": {"slide_type": "slide"}}

## arithmétiques - suite

```{code-cell} ipython3
:cell_style: split

# division euclidienne
c = 64
d = 5
```

```{code-cell} ipython3
:cell_style: split

# le reste
c % d
```

```{code-cell} ipython3
:cell_style: split

# le quotient

c // d
```

```{code-cell} ipython3
:cell_style: split

# puissance

d ** c # qu'il est grand !
```

```{code-cell} ipython3
:cell_style: split

# remarque: pas de limite
# de précision avec les entiers

d ** c > 2 ** 64
```

+++ {"slideshow": {"slide_type": "slide"}}

## comparaisons

```{code-cell} ipython3
a = 10
b = 25
```

```{code-cell} ipython3
:cell_style: split

a == b
```

```{code-cell} ipython3
:cell_style: split

a != b
```

```{code-cell} ipython3
:cell_style: split

a <= b
```

```{code-cell} ipython3
:cell_style: split

a < b
```

```{code-cell} ipython3
:cell_style: split

# une curiosité
6 <= a <= 20
```

```{code-cell} ipython3
:cell_style: split

6 <= a <= 25 <= b <= 30
```

+++ {"slideshow": {"slide_type": "slide"}}

## logiques

```{code-cell} ipython3
:cell_style: split

6 <= a and b <= 10
```

```{code-cell} ipython3
:cell_style: split

6 <= a or b <= 10
```

+++ {"slideshow": {"slide_type": "slide"}}

## indexation avec `[]`

+++

sur tous les objets de type 'séquence'  
c'est-à-dire pour nous à ce stade les chaines  
mais on verra que ça s'applique à d'autres, comme les listes (un peu de patience..)

```{code-cell} ipython3
chaine = 'abcdefghij'
len(chaine)
```

```{code-cell} ipython3
:cell_style: split

# en python les index commencent à 0
chaine[0]
```

```{code-cell} ipython3
:cell_style: split

# les index négatifs commencent à la fin
chaine[-1]
```

+++ {"slideshow": {"slide_type": "slide"}}

## slices

```{code-cell} ipython3
:cell_style: split

# une 'slice' permet de découper un morceau
# là du caractère d'indice 1 à celui d'indice 4 exclus
chaine[1:4]
```

```{code-cell} ipython3
:cell_style: split

# et même de choisir un pas
chaine[1:8:2]
```

```{code-cell} ipython3
:cell_style: split

# dans un slice on peut omettre
# n'importe lequel des 3 termes
chaine[3::]
```

```{code-cell} ipython3
:cell_style: split

# ce qui serait ici
# identique à juste
chaine[3:]
```

```{code-cell} ipython3
:cell_style: split

# dans un slice on peut omettre
# n'importe lequel des 3 termes
chaine[:4:]
```

```{code-cell} ipython3
:cell_style: split

# ce qui serait ici
# identique à juste
chaine[:4]
```

+++ {"slideshow": {"slide_type": "slide"}}

## slices et bornes

la forme générale est donc `debut:fin:pas`  
**ATTENTION** que l'index `fin` **n'est pas inclus**

```{code-cell} ipython3
# la convention permet de facilement emboiter les résultats
chaine[0:3] + chaine [3:6] + chaine[6:] == chaine
```

```{code-cell} ipython3
# notez enfin que le pas peut être négatif aussi
# ce qui donne cette forme idiomatique
# pour renverser une séquence
chaine[::-1]
```
