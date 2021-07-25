---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  cell_metadata_json: true
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: "alg\xE8bre lin\xE9aire"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
</div>

<img src="media/ensmp-25-alpha.png" />

```{code-cell} ipython3
import numpy as np
```

# algèbre linéaire

+++

Un des premières utilisations de la librarie `numpy` sera faite dans le cadre des cours de mathématiques et de la manipulation de matrices.

Aussi allons-nous voir dans ce notebook les quelques fonctions d'algèbre linéaire qui vont vous être utiles, naturellement il vous faudra vous référer au site de Python-scientifique pour chercher des fonctions plus avancées.

+++ {"tags": ["level_intermediate"]}

Il faut savoir que les fonctions d'algèbre linéaire des libraries `np.linalg` sont tout particulièrement efficaces et ce pour plusieurs raisons:
   1. déjà ces fontions s'appuient sur les algorithmes efficaces 
   1. ensuite ces fonctions sont codées dans des langages de *bas niveau* très proches de la mémoire donc rapides
   1. enfin les implémentations tirent parti du multithreading (où un programme est découpé en sous-programmes s'exécutant *en même temps*) qui permet de grandement améliorer les temps de calculs.

Il existe des différences entre les fonctions de `numpy` et de `scipy` mais nous n'en dirons pas plus référez vous aux explications des concepteurs de ces librairies comme là  https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

```{code-cell} ipython3
import numpy as np
```

La première chose à savoir c'est que naturellement les fonctions `numpy` vont s'appliquer sur des tableaux de dimensions supérieures à 2 mais, nous n'allons voir ici, que les vecteurs et matrices donc rester en dimension < à 3.

+++

Nous n'avons vu pour l'instant que des opérations élément par élément. Comme par exemple le `np.mult` ou encore `*`, qui est le *produit matriciel de Hadamard*. Voyons maintenant les fonctions dédiées à l'algèbre linéaire.

+++

## application linéaire

+++

On va se mettre d'accord sur matrice, vecteur et produit en `numpy`.

Attention, comme les matrices et les vecteurs seront des `np.ndarray`, il faudra naturellement faire attention au type des éléments, lors d'éventuelles modifications. Si on tente de modifier un élément d'une matrice de type entier avec un nombre flottant, celui-ci sera tronqué et transformé en entier: vous perdrez de l'information.

+++

### la matrice

+++

Une matrice $A$ de dimension $m$ lignes et $n$ colonnes, qui représente une application linéaire $f$ d'un espace de dimension $n$ vers un espace de dimension $m$, est un `np.ndarray` de forme $(m, n)$.

+++

Voila un exemple d'une matrice $A$ de dimension $(2 \times 3)$

```{code-cell} ipython3
A = np.array([[2, 3, -7], [6, -4, 5]])
A
```

### le vecteur

+++

Un vecteur $V$ de taille $n$, qui représente un vecteur d'un espace vectoriel de dimension $n$, est un `np.ndarray` de forme $(n,)$.

+++

Voila un exemple de vecteur $V$ de dimension $(3,)$

```{code-cell} ipython3
V = np.array([1, -3, 8])
V
```

Attention les `numpy.ndarray` suivant ne sont pas des vecteurs mais des matrices. Il y a bien deux dimensions.

```{code-cell} ipython3
np.array([[100, 200, 300]]).shape
```

```{code-cell} ipython3
np.array([[100], [200], [300]]).shape
```

Celui là est un vecteur au sens de l'UE11.

```{code-cell} ipython3
np.array([100, 200, 300]).shape
```

### le produit d'une matrice et d'un vecteur

+++

Le produit $A \cdot V$ représente $f(V)$.

+++

Quel est en `numpy` le produit qu'on appelle ici $\times$ ? C'est la fonction `np.dot` (ou encore la méthode `np.ndarray.dot`).

+++

Calculons $A \cdot V$

```{code-cell} ipython3
:cell_style: split

# la fonction
np.dot(A, V)
```

```{code-cell} ipython3
:cell_style: split

# la méthode
A.dot(V)
```

### le produit de deux matrices

+++

Maintenant prenons $A$ et $B$, deux matrices représentant respectivement les applications linéaires $f$ et $g$, le produit de matrices $A \cdot B$ est la composition des applications $ƒ ￮ g$.

+++

$A$ on l'a déjà, prenons $B$

```{code-cell} ipython3
B = np.array([[-5, 4], [3, 9], [-4, 2]])
B
```

```{code-cell} ipython3
:cell_style: split

np.dot(A, B)
```

```{code-cell} ipython3
:cell_style: split

A.dot(B)
```

### raccourci  *@* pour le produit matriciel

Il s'avère que `numpy` possède un fonction `np.matmul` (qui en dimension 2 est à peu près équivalente à `np.dot`) et qui s'écrit aussi sous la forme *@*

```{code-cell} ipython3
np.matmul(A, B)
```

```{code-cell} ipython3
:cell_style: center

A @ B
```

Il existe des différences entre `np.matmul` et `np.dot`  tout d'abord , la multiplication par un scalaire n'est possible qu'avec `np.dot` mais surtout en dimensions supérieure à 2 leur comportement diffère complètement.

Préférer utiliser `np.dot` (ou demandez à votre professeur de math).

+++

## le produit scalaire

+++

Si on applique le produit `np.dot` à deux vecteurs on en obtient le produit scalaire.

```{code-cell} ipython3
V1 = np.array([1, -3, 8])
V1
```

```{code-cell} ipython3
V2 = np.array([-6, 4, -7])
V2
```

```{code-cell} ipython3
:cell_style: split

np.dot(V1, V2)
```

## la norme de vecteur

+++

Pour un vecteur $V1 =[v_1, ..., v_n]$, , la norme `np.linalg.norm` sera la racine carré du produit scalaire par lui-même $\displaystyle \left\|{ {V}}\right\|_{2}={\sqrt {v_{1}^{2}+\cdots +v_{n}^{2}}}$

```{code-cell} ipython3
:cell_style: split

# la fonction idoine
np.linalg.norm(V1)
```

```{code-cell} ipython3
:cell_style: split

# qu'on peut naturellement paraphraser en
np.sqrt(V1.dot(V1))
```

Pour les autres normes de matrices et vecteurs regardez là https://np.org/doc/stable/reference/generated/np.linalg.norm.html#np.linalg.norm

+++

## la transposée d'une matrice

+++

C'est la fonction `np.transpose`. Elle a une version courte `.T` pour écrire des codes plus lisibles.

```{code-cell} ipython3
A = np.arange(1, 13).reshape(4, 3)
A
```

```{code-cell} ipython3
:cell_style: split

np.transpose(A)
```

```{code-cell} ipython3
:cell_style: split

A.T
```

## les matrices identité

+++

En `numpy` la fonction porte le très joli nom de `eye` (parce que *eye* et *I* se prononcent pareil), elle renvoie des matrices de type flottant.

```{code-cell} ipython3
A = np.eye(5)
A
```

## le déterminant d'une matrice

Il est donné par la fonction `np.linalg.det`

```{code-cell} ipython3
A = 2*np.eye(3)
A
```

```{code-cell} ipython3
np.linalg.det(A)
```

Essayez de l'appliquer à une matrice qui n'est pas carrée ? Vous allez recevoir une `np.linalg.LinAlgError` !

```{code-cell} ipython3
B = np.random.random(size=(3, 4))*10
try:
    np.linalg.det(B)
except np.linalg.LinAlgError as e:
    print(f'Oups pas bon ! ou en mieux dit "{e}"')
```

+++ {"tags": ["level_basic"]}

A vous de jouer. Faites une isométrie (une transformation qui conserve les longueurs) et calculez son déterminant.

```{code-cell} ipython3
# votre code ici (une solution dessous)
```

```{code-cell} ipython3
M = np.array([[0, -1], [1, 0]])
print(M)
np.linalg.det(M)
```

```{code-cell} ipython3
# une isométrie
M = np.array([[0, -1], [1, 0]])
print(M)
np.linalg.det(M)
```

## les matrices diagonales

On peut créer une matrice diagonale à partir de la liste des éléments de sa diagonale

```{code-cell} ipython3
np.diag([1., 2, 3])
```

On peut aussi extraire la matrice diagonale d'une matrice.

```{code-cell} ipython3
A = np.random.randint(-100, +100, size=(3, 3))
A
```

```{code-cell} ipython3
:cell_style: center

# returns the diagonal of b
np.diag(A) 
```

```{code-cell} ipython3
:cell_style: split

# creates a diagonal matrix
np.diag([1, 2, 3])
```

## la trace d'une matrice

C'est la somme des éléments de sa diagonale.

```{code-cell} ipython3
A = np.arange(16).reshape(4, 4)
A
```

```{code-cell} ipython3
:cell_style: split

np.trace(A)
```

```{code-cell} ipython3
:cell_style: split

np.sum(np.diag(A))
```

## l'inversion d'une matrice

c'est le calcul de $A^{-1}$

```{code-cell} ipython3
:cell_style: center

# prenons une rotation
R = np.array([0, 1, 0, 0, 0, 1, 1, 0, 0]).reshape(3, 3)
R
```

```{code-cell} ipython3
# pour calculer son inverse
np.linalg.inv(R)
```

pour nous convaincre que ça fonctionne comme attendu :  
lorsqu'en maths on écrit $A^{-1}A = I$, en informatique c'est $A^{-1}A \approx I$ (presque égal à cause des approximations)  

c'est l'intérêt de `np.close` que de comparer si deux tableaux sont presque identiques

```{code-cell} ipython3
:cell_style: center

# on prend maintenant une matrice quelconque
n = 3
A = np.random.random(size=(n, n))
A
```

```{code-cell} ipython3
# son inverse
Ainv = np.linalg.inv(A)
```

Vérifions que leur produit fait bien l'identité

```{code-cell} ipython3
np.dot(Ainv, A) == np.eye(n)
```

Et bien oui on a des valeurs approchées.

```{code-cell} ipython3
np.isclose(  Ainv @ A,  np.eye(n))
```

## les valeurs propres d'une matrice (eigen values)

On va calculer les $v$ tels que:
   - $f(v) = \lambda v$ 
   - $M \cdot v = \lambda v$

```{code-cell} ipython3
:cell_style: center

M = np.random.random(size=(3, 3))
M
```

```{code-cell} ipython3
:cell_style: center

ls, vs = np.linalg.eig(M)  # eigen_values, eigen_vectors
ls, vs
```

Vérifions qu'on a bien $M \cdot v = \lambda v$

Attention les vecteurs propres sont dans une matrice (3, 3) et chacun d'eux est une des 3 colonnes de la matrice.

```{code-cell} ipython3
:cell_style: center

# le premier vecteur propre
v0 = vs[:, 0] # toutes les lignes et la colonne 0
# la première valeur propre
l0 = ls[0]
np.all(np.isclose(np.dot(M, v0),  l0*v0))
```

À vous de jouer, à l'aide d'une boucle for-Python, parcourez les valeurs et les vecteurs propres de $M$ et vérifiez $M \cdot v = \lambda v$.

```{code-cell} ipython3
# votre code ici
```

Prenons la symétrie x↔︎y et calculons ses valeurs et vecteurs propres.

```{code-cell} ipython3
S = np.array([[0, 1], [1, 0]])
values, vectors = np.linalg.eig(S)

print(values)

# les vecteurs sont normés, naturellement
print(vectors)
```

## résolution d'un système linéaire

On va trouver les racines du système linéaire $A \cdot x = b$

Prenons une matrice $A$.

```{code-cell} ipython3
A = np.random.random(size=(3, 3))
A
```

Prenons un vecteur $b$.

```{code-cell} ipython3
b = np.array([1, 2, 3])
```

Calculons la racine de l'équation $A \cdot x = b$

```{code-cell} ipython3
np.linalg.solve?
```

```{code-cell} ipython3
x = np.linalg.solve(A, b)
x
```

```{code-cell} ipython3
np.all( np.isclose( np.dot(A, x), b) )
```

Si la matrice n'est pas inversible ou si elle n'est pas carrée, une erreur `np.linalg.LinAlgError` sera levée

## les fonctions dont nous avons parlé (rapidement)

| fonctions           |   comportement |
|-----------------|--------|
| `np.dot` | produit de matrice |
| `np.linalg.norm` | normes de matrice |
| `np.transpose` | transposition de matrice |
| `np.linalg.det` | déterminant |
| `np.linalg.inv` | inversion |
| `np.linalg.eig` | valeurs propres |
| `np.linalg.solve` | résolution de système linéaire |
| `np.eye`       |matrice identité  |
| `np.diag`      | matrice diagonale|

+++

Les exercices intéressants seront faits dans l'UE11.

+++ {"tags": ["level_advanced"]}

## exercices

+++ {"tags": ["level_advanced"]}

### construire une matrice diagonale à-la-main (peu d'intérêt)

+++ {"tags": ["level_advanced"]}

On vous demande d'écrire une fonction `matdiag` qui 

1. accepte un paramètre qui est une liste de flottants [$x_1$, $x_2$, …, $x_n$] 
1. retourne une matrice carrée diagonale dont les éléments valent

$$
m_{ii} = x_i 
$$
$$
m_{ij} = 0 \ pour\  i ≠ j
$$
* Retournez toujours un tableau de type `float64`
* Programmez une approche naïve et une approche à base de slicing.

https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x5-matdiag

+++ {"tags": ["level_advanced"]}

### remplir une matrice : m(i, j) = xi * xj

+++ {"tags": ["level_advanced"]}

On vous demande d'écrire une fonction qui 

1. accepte un nombre quelconque de paramètres, $x_1$, $x_2$, ..., $x_n$, tous des flottants
1. retourne une matrice carrée symétrique $M$ dont les termes valent

$$
m_{ij} = x_i . x_j
$$

Indices. Vous pouvez utiliser l'opérateur `@`, la méthode `array.dot()`, le broadcasting, la transposée d'une matrice `.T`.

https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x6-xixj
