---
jupyter:
  jupytext:
    cell_metadata_filter: all,-hidden,-heading_collapsed
    cell_metadata_json: true
    notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
    text_representation:
      extension: .md
      format_name: markdown
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  notebookname: broadcasting
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>


Vous y êtes habitués, on importe notre librarie `numpy`

```python
import numpy as np
```



<!-- #region {"tags": []} -->
# broadcasting

ou comment faire des opérations sur des tableaux qui ont des formes différentes
<!-- #endregion -->

## opération sur des tableaux de même forme


Vous savez désormais construire des tableaux `np.ndarray` en leur donnant des formes (vecteurs, matrices, images...) et vous savez faires des opérations vectorielles (vectorisées) sur ces tableaux `np.ndarray`.


Construisons deux matrices donnons leur la même forme et des types différents:
   - `m1`* de forme (3, 4) et de type entier contenant les valeurs de 1 à 12
   - `m2` de forme (3, 4) et de type float contenant des valeurs entre 0 et 1

```python
m1 = np.arange(1, 13).reshape(3, 4)
m1
```

```python
m2 = np.linspace(0, 1, 12).reshape(3, 4)
m2
```

Pour que ce soit plus lisible, on va arrondir les valeurs de la matrice `m2` à 2 chiffres après la virgule avec la fonction `np.round`, et pour éviter une duplication inutile, on lui indique que sa sortie `out` est elle même:

```python
# on arrondit sans copier le tableau
np.round(m2, 2, out=m2)
```

Maintenant ajoutons `m1` et `m2`, On obtient bien ce qu'on attendait:

```python
m1 + m2
```

Donc jusqu'ici nous avons fait une addition sous une forme vectorisée, rien de nouveau.


## opération sur tableaux de formes différentes (*broadcasting*)


Mais supposons maintenant que nous voulions ajouter **le même scalaire** à tous les éléments d'une matrice. Par exemple on a une matrice d'entiers de taille (3000, 3000) et on veut ajouter 1 à tous les éléments.

Pour le faire, on peut créer une nouvelle matrice de `1` de la même taille et les ajouter...

Franchement, cela demande des manipulations mémoire qui prennent une place inutile et ne sont pas informatives (on a une matrice  de 9 millions de `1`), ensuite elles n'améliorent pas le code voire elles nuisent à sa lisibilité.

Bref c'est complètement sous-optimal. `numpy` propose une manière abrégée d'écrire afin de ne pas avoir à créer de tableaux inutiles, `numpy` se chargera de faire les *bonnes* opérations.

On appelle cela le broadcasting


### comment ça marche ?


Souvenez-vous, en `numpy` les tableaux peuvent être de différentes dimensions:
   - en dimension 1 ce sont de simples tables de taille *n* avec *shape=(n,)*
   - en dimension 2 ce sont des  matrices avec *shape=(l, c)* où *l* est le nombre de lignes et *c* de colonnes (qui peuvent être 1)
   - en dimension supérieures avec shape=$(n_1, ..., n_m, l, c)$ les deux dernières dimensions vont être une matrice

<!-- #region {"tags": []} -->
Une matrice (1, 1) est aussi de dimension 2...
<!-- #endregion -->

```python tags=[]
mat = np.array([1]).reshape(1, 1)
# utilisation d'un f-string (c'est super pratique)
print(f'mat={mat} est de dimension {mat.ndim} !')
```

<!-- #region {"tags": ["level_advanced"]} -->
et, parlant de *f-string* d'ailleurs, je vous signale en passant que lorsqu'on a Python-3.8, on peut même raccourcir et transformer

    print(f'mat={mat}')

par tout simplement

    print(f'{mat=}')

mais reprenons...
<!-- #endregion -->

Revenons à notre problème d'opérations sur des tableaux de formes différentes. Les opérations dont nous parlons ici sont les opérations qui agissent élément par élément, comme des opérations arithmétiques.

`numpy` relâche donc la contrainte et permet aux tableaux impliqués dans des opérations d'avoir des formes différentes et des tailles différentes.

Cela permet des codes plus condensés, plus lisibles et (souvent mais pas toujours) plus rapides que leur version explicite (où tous les tableaux auraient la même forme lors des opérations)

Naturellement ces formes doivent obéir à certaines conditions ! On ne va pas pouvoir faire n'importe quoi !

On va d'abord voir des exemples puis ensuite donner la règle:


Le plus simple: j'ajoute un tableau de dimension 1 ou même un simple scalaire à un tableau de dimension supérieure.

```python
tab = np.array([0, 1, 2, 3, 4, 5]) # voila le tableau de taille (6,)
tab + 10 
```

Ou bien, ce qui est sémantiquement pareil:

```python
tab = np.array([0, 1, 2, 3, 4, 5])
tab + [ 10 ]
```

Que s'est-il passé ?

Oui là, le scalaire `10` a été considéré comme un tableau, de la même forme que `tab`
, i.e. de 6 éléments (avec la valeur 10). Nous disons "*considéré*" parce que l'intérêt est bien que ce tableau n'ait pas été créé du tout, mais géré dans le code `numpy` sous-jacent.


En Python qu'est ce que cela donnerait sur une liste ? Essayons :

```python
[1, 2, 3, 4, 5, 6] + [10]
```

Ah oui c'est très différent ! (c'est bien que Python ait appelé cela des listes et non des tableaux ...)


Passons en dimension 2 et ajoutons 10 à une matrice (2, 3):

```python
tab1 = np.arange(6).reshape(2, 3)
tab1 + 10
```

Alors comment 10 a-t-il été considéré ? Oui là 10 a été considéré comme une matrice de forme 2 x 3 d'éléments de valeur 10.


On peut continuer à l'infini. A vous de jouer faites une matrice de 3 x 2 x 3 et ajoutez lui 10 le tout en une seule ligne de code.

```python
# votre code ici
```

Maintenant passons à des ajouts de tableaux à la place d'un scalaire.  
Prenons une matrice, par exemple, de 3 x 5.

```python
mat = np.arange(15).reshape(3, 5)
mat
```

Qu'est ce que `numpy` peut faire si nous ajoutons, à la matrice `mat` de 3 lignes et 5 colonnes, un tableau de la forme d'une ligne de `mat` ?

C'est à dire de forme `(5,)` ou encore de forme `(1, 5)` ? Voici la première:

```python
line = np.array([100, 200, 300, 400, 500])
line.shape
```

```python
# et oui, on peut ajouter (3, 5) avec (5,)
mat + line
```

Donc ici, `numpy` décide de répéter 3 fois cette ligne pour obtenir une matrice de la même forme que `mat` i.e. (3, 5).  
On fait de même avec une matrice de dimension (1, 5) donc 1 ligne et 5 colonnes.

```python
line1 = line.reshape(1, 5)
line1.shape
```

```python
# et oui, on peut ajouter (3, 5) avec (1, 5)
mat + line1
```

Et donc il accepte aussi: il répéte 3 fois cette matrice-ligne pour obtenir une matrice de la même forme que `mat`


Vous essayez avec les colonnes ? Il va donc falloir ajouter, à notre matrice de 3 lignes et 5 colonnes, une matrice composée d'une seule colonne et de 3 lignes, qui sera un tableau de taille (3, 1).

```python
col = np.array([1000, 2000, 3000]).reshape(3, 1)
col.shape
```

```python
# et oui, on peut ajouter (3, 5) avec (3, 1)
mat + col
```

Mais ca fait exactement ce à quoi on s'attend !


Et si on essayait d'ajouter une matrice comportant une seule ligne (par exemple de taille (1, 5)) avec une matrice comportant une seule colonne (par exemple de taille (3, 1)) ?


Donc on va ajouter ces deux objets

```python cell_style="split"
line
```

```python cell_style="split"
col
```

```python
# et ça nous donne 
line + col
```

Oui il déduit bien ce que nous attendions !


Alors maintenant, on commence à saisir sa manière de faire !

Pour les avancés on peut regarder la règle.

<!-- #region {"tags": ["level_intermediate"]} -->
## règles de broadcasting (pour les avancés)
<!-- #endregion -->

Les dimensions des deux tableaux (sur lesquels une opération élément-par-élément est appliquée), sont comparées de droite à gauche.

Dans cet ordre, les dimensions sont prises par paire, le broadcasting sera possible:
   1. soit si les deux dimensions sont identiques
   1. soit si l'une des 2 dimensions vaut 1 et auquel cas elle est élargie à la dimension compatible


Explicitons sur un exemple. 


on se donne $A=\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix}$ et $b$ un tableau à un scalaire, donc de forme `(1,)`

on calcule `A + b`

la forme de *A* est $(2_A, 3_A)$ et la forme de *b* est ($1_b$,) , on compare les dimensions de droite

$3_A$ est associé à $1_b$, et du coup $b$ est élargi à $\begin{pmatrix} b & b & b  \end{pmatrix}$ de dimension $(1_b, 3_b)$

on ajoute maintenant un tableau $(2_A, 3_A)$ à une ligne $(1_b, 3_b)$  
   
   $\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix} + \begin{pmatrix} b & b & b  \end{pmatrix}$   
   
on compare les dimensions suivantes, $2_a$ est comparé à $1_b$, et de nouveau $b$ est élargi à la dimension $(2_b, 3_b)$

  $\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\  \end{pmatrix} + \begin{pmatrix} b & b & b \\ b & b & b \end{pmatrix} = \begin{pmatrix} a_{11} + b & a_{12} + b & a_{13} + b \\ a_{21} + b & a_{22} + b & a_{23} + b \\  \end{pmatrix}$   
   
les formes sont désormais compatibles, les deux tableaux peuvent être ajoutés !


Et naturellement quand les formes ne sont pas consistantes, `numpy` va rejeter le programme en vous envoyant une erreur de type `ValueError`.

```python cell_style="center" hide_input=false tags=["raises-exception"]
m1 = np.arange(6).reshape(2, 3)
m2 = np.arange(8).reshape(2, 4)

m1 + m2
```

On la rattrape ?

```python cell_style="center"
try:
    m1 + m2
except ValueError as exc:
    print(f'{m1}\n+\n{m2}\n ➡ {exc}')
```

Encore un exemple où on ajoute une matrice comportant une seule ligne à une matrice comportant une seule colonne pour avoir une nouvelle matrice.

<!-- #region -->
on veut faire l'opération $\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{pmatrix}$

la forme de la matrice *a* est $(1_a, 3_a)$, la forme de la matrice *b* est $(4_b, 1_b)$

`numpy` compare $3_a$ à $1_b$ et il élargit *b* à $\begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix}$

on ajoute maintenant un tableau $(1_a, 3_a)$ à une matrice $(4_b, 3_b)$

$\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix}$
 
   
`numpy` compare les dimensions $1_a$ et $4_b$, et il élargit $a$ à $\begin{pmatrix} a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \end{pmatrix}$
   
 
$\begin{pmatrix} a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \\ a_{1} & a_{2} & a_{3} \end{pmatrix} + \begin{pmatrix} b_1 & b_1 & b_1 \\ b_2 & b_2 & b_2 \\ b_3 & b_3 & b_3 \\ b_4 & b_a & b_4 \end{pmatrix} = \begin{pmatrix} a_{1} + b_1 & a_{2} + b_1 & a_{3} + b_1 \\ a_{1} + b_2 & a_{2} + b_2 & a_{3} + b_2 \\ a_{1} + b_3 & a_{2} + b_3 & a_{3}  + b_3\\ a_{1} + b_4 & a_{2} + b_4 & a_{3} + b_4 \end{pmatrix}$
 
     
   
   
les formes sont désormais compatibles, les deux tableaux ont pu être ajoutés !
<!-- #endregion -->

## le broadcasting en dimension > 2


Naturellement le broadcasting se généralise à des dimensions supérieures à 2.

```python
m = np.arange(24).reshape(2, 3, 4)
m
```

ajout d'un scalaire

```python
m + 10
```

ajout d'une matrice comportant une seule ligne

```python
m + np.array([100, 200, 300, 400])
```

ajout d'une matrice comportant une seule colonne

```python
m + np.array([[1000], [2000], [3000]])
```

ajout de 2 matrices comportant 1 seule ligne dont la forme est (2, 1, 4)

```python
vecl = np.array([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]).reshape(2, 1, 4)
vecl
```

```python
m + vecl
```

ajout de 2 matrices comportant une seule colonne donc de forme (2, 3, 1)

```python
vecc = np.array([100000, 200000, 300000, 400000, 500000, 600000]).reshape(2, 3, 1)
vecc
```

```python
m + vecc
```

A vous de jouer. Essayer d'ajouter un tableau (généré par `np.arange` qui contient les entiers de 0 à 11) de la forme: 4 fois 1 matrice de 3 lignes sur 1 colonne ... heu bon je pense que vous avez compris.

```python
# votre code ici
```

<!-- #region {"tags": ["level_advanced"]} -->
Si vous êtes fort en Python, et que vous avez du temps, sauriez-vous coder en Python, la fonction qui détermine si deux formes (données par des tuples) sont compatibles pour le broadcasting ? à vous de jouer…
<!-- #endregion -->

```python tags=["level_advanced"]
# votre code ici

def are_broadcast_compatible(shape1, shape2):
    ...
```

## conclusion


Le broadcasting est très efficace. Les éléments broadcastés ne sont naturellement pas réellement créés en mémoire, mais le broadcasting est basé sur du code C optimisé qui va avoir le même genre d'efficacité que les opérations vectorisées. Donc à utiliser (intelligemment) !


## exercices


### ajouter un scalaire à une matrice


Construisez une matrice de forme *(3000, 3000)* contenant les entiers à partir de 1.
   1. Calculer le temps pour ajouter le scalaire *10* à cette matrice
   1. Calculer le temps pour ajouter une matrice de taille de *(3000, 3000)* remplie de `1` à cette matrice.

Pour la deuxième option, envisagez deux variantes dans lesquelles vous comptez ou non le temps nécessaire à la construction de la matrice temporaire

Expliquez pourquoi on fait ça…

```python
# votre code
```

#### correction

```python
N = 3000

m = np.arange(1, N**2 + 1).reshape(N, N)
```

```python
%timeit m + 10
```

```python
uns = np.ones(shape=(N, N))
```

```python
%timeit m + uns
```

<!-- #region {"tags": ["level_intermediate"]} -->
### les dès (intermédiaire)
<!-- #endregion -->

On étudie les probabilités d'obtenir une certaine somme avec plusieurs dés. 

Tout le monde connaît le cas classique avec deux dés à 6 faces, ou l'on construit mentalement la grille suivante:

|  +  | &#124; | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:------:|:-:|:-:|:-:|:-:|:-:|:-:|
| *1* | &#124; | 2 | 3 | 4 | 5 | 6 | 7 | 
| *2* | &#124; | 3 | 4 | 5 | 6 | 7 | 8 | 
| *3* | &#124; | 4 | 5 | 6 | 7 | 8 | 9 | 
| *4* | &#124; | 5 | 6 | 7 | 8 | 9 |10 | 
| *5* | &#124; | 6 | 7 | 8 | 9 |10 |11 | 
| *6* | &#124; | 7 | 8 | 9 |10 |11 |12 | 

Imaginons que vous êtes un étudiant, vous venez de faire un exercice de maths qui vous a mené à une formule qui permet de calculer, pour un jeu à `nb_dice` dés, chacun à `sides` faces, le nombre de tirages qui donnent une certaine somme `target`.

Vous voulez **vérifier votre formule**, en appliquant une **méthode de force brute**. C'est-à-dire constuire un hypercube avec toutes les possibilités de tirage, puis calculer pour chaque point dans l'hypercube la somme correspondante; de cette façon on pourra compter les occurrences de `target`.

C'est l'objet de cet exercice. Vous devez écrire une fonction `dice` qui prend en paramètres:

* `target` : la somme cible à atteindre,
* `nb_dice` : le nombre de dés,
* `sides`: le nombre de faces sur chaque dé.

On convient que par défaut `nb_dice`=2 et `sides`=6, qui correspond au cas habituel.

Dans ce cas-là par exemple, on voit, en comptant la longueur des diagonales sur la figure, que `dice(7)` doit valoir 6, puisque le tableau comporte 6 cases contenant 7 sur la diagonale.

À nouveau, on demande explicitement ici un parcours de type force brute; c'est-à-dire de créer sous la forme d'un tableau `numpy`, un hypercube qui énumère toutes les combinaisons possibles; et sans faire de `for` sur les éléments d'un tableau.


https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x4-dice


**Indice**

Il existe en `numpy` une astuce pour augmenter la dimension d'un tableau, ça s'appelle `np.newaxis`, et ça s'utilise comme ceci

```python cell_style="center"
dice_1 = np.arange(1, 7)
dice_2 = dice_1[:, np.newaxis]
```

```python cell_style="split"
dice_1
```

```python cell_style="split"
dice_2
```

et remarquez que pour créer le tableau ci-dessus il suffit de faire

```python
dice_1 + dice_2
```
