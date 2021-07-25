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
notebookname: indexation & slicing
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
</div>

<img src="media/ensmp-25-alpha.png" />

+++

# indexation et slicing

où on accède aux éléments, et à des sous-tableaux

```{code-cell} ipython3
import numpy as np
```

## accéder aux éléments d'un `ndarray`

+++

Il est naturellement possible d'accéder (*accessing*) aux éléments d'un tableau `np.ndarray`, comme nous le faisons pour les listes Python.

+++

Rappel sur les fonctions vectorisées:

La possibilité d'accéder aux éléments d'un ndarray ne doit pas vous faire oublier que l'appel de **fonctions vectorisées** doit toujours être **priviligié**: c'est LA meilleure manière de coder.

Vous vous rappelez pourquoi ? Parce que l'application d'une fonction vectorisée ne se fait pas en utilisant des fonctions codées en Python mais des fonctions codées dans un langage de programmation beaucoup proche de la mémoire de l'ordinateur et qui va (entre autres) très rapidement d'une case (un élément) à une autre case du tableau.

Il ne faut donc **jamais** utiliser l'accès aux éléments d'un tableau dans des itérations où vous pourriez appliquer directement des fonctions vectorisées.

+++

Ceci dit, accéder aux éléments et aux sous-tableaux d'un tableau `numpy` , va (par exemple) vous servir à appliquer des fonctions vectorisées à des sous-parties de votre tableau donc elles sont **très** utiles

+++

La manière d'accéder aux éléments d'un tableau `numpy` va dépendre tout naturellement ... de quoi ? oui bien sûr de la forme du tableau !

Vous vous rappelez que la forme d'un `np.ndarray` est donnée par une indexation sur le segment mémoire sous-jacent continu de votre tableau.

Par exemple, le segment $\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$$\fbox{}$ peut être indexé avec les formes (12,), (1, 12), (2, 6), (3, 4), (12, 1) ... (2, 3, 2)...

+++

### en dimension 1

+++

Commencons par un petit tableau de dimension 1 qui contient les dix entiers de 10 à 19.

```{code-cell} ipython3
vec = np.arange(10, 20)
vec
```

L'indexation prise sur le tableau ne comporte qu'une dimension i.e. on n'a besoin que d'un index pour accéder à un élément.

```{code-cell} ipython3
vec[0]
```

Quelles sont les bornes de cet index ? dit autrement, on peut aller de 0 à ?

```{code-cell} ipython3
# ceci retourne un tuple, 
# mais à un seul élément (puisqu'en dimension 1)
# d'où la présentation un peu bizarre avec la virgule
vec.shape
```

Et osons modifier cet élément !

```{code-cell} ipython3
vec[0] = np.pi
vec
```

Le tableau a bien été modifié ! ... mais est-ce exactement comme en Python ? Rien de spécial ?

ah heu si (on l'a déjà vu): vous avez un **3** là où vous attendiez **π** !

Gardez bien à l'esprit que, contrairement à Python, les tableaux numpy sont typés et de **taille fixe**. Donc si vous tentez de mettre une valeur flottante à la place d'un entier, la valeur flottante sera silencieusement (et implicitement) coupée ... et ce comportement peut ne pas vous convenir du tout !

Faites bien attention à ce que vous faites.

+++

### en dimension supérieure à 1

+++

En dimension supérieure à 1, naturellement l'accès à un élément du tableau va dépendre de la forme du tableau donc de ses indices dans chacune des dimensions.

Construisons un tableau avec des valeurs de 1 à 12 et donnons lui une forme de matrice 3 lignes et 4 colonnes 

Nous allons pour cela utiliser la fonction `np.ndarray.resize` qui modifie la forme d'un tableau *en place* c'est à dire que la fonction bien sûr ne crée pas un nouveau tableau mais modifie l'indexation de celui auquel elle est appliquée.

Il existe une autre fonction `np.ndarray.reshape` qui fait la même chose en créant un nouvelle indexation (donc vous avez désormais 2 indexations différentes sur la même mémoire sous-jacente, vous vous rappelez des références partagées ?).

+++

Notre tableau en dimension 1:

```{code-cell} ipython3
vec = np.arange(1, 13)
vec
```

Le voila redimensionné en dimension 3 x 4

```{code-cell} ipython3
vec.resize(3, 4)
vec
```

Le voilà indexé par une nouvelle forme:

```{code-cell} ipython3
vec1 = vec.reshape(6, 2)
vec1
```

Pour accéder à un élément on voit bien que nous allons avoir besoin de 2 indices: celui des lignes et celui des colonnes.

```{code-cell} ipython3
:cell_style: split

# le premier élément
vec[0, 0]
```

```{code-cell} ipython3
:cell_style: split

# le dernier élément
vec[2, 3]
```

+++ {"tags": ["level_intermediate"]}

Pour un tableau *vec* en dimension 4 de dimensions $(n, m, l, c)$ et bien vous allez indiquer pour un élément les indices dans chacune de ses dimensions;  
donc $vec[i_n, i_m, i_l, i_c]$, avec  
$0<=i_n<n$,  
$0<=i_m<m$,  
etc…

Notez qu'en grande dimension, les deux derniers indices correspondent toujours à  
..., ligne, colonne  
c'est pourquoi on a utilisé $l$ et $c$ comme noms pour les deux derniers indices

+++

Sauriez-vous dire la dimension de votre tableau ?

```{code-cell} ipython3
vec.ndim # attention au n de ndim
```

Sauriez-vous lister le nombre d'éléments dans chacune des dimensions ?

```{code-cell} ipython3
vec.shape
```

+++ {"tags": ["level_intermediate"]}

Remarquez qu'on pourrait aussi écrire, puisque le tableau a `np.ndarray.ndim` dimensions et que le nombre d'éléments dans chaque dimension est donné par `np.ndarray.shape`:

```{code-cell} ipython3
:tags: [level_intermediate]

[vec.shape[i] for i in range(vec.ndim)]
```

+++ {"tags": ["level_intermediate"]}

ce qui revient à dire qu'en fait

```{code-cell} ipython3
:tags: [level_intermediate]

# c'est toujours vrai pour un tableau numpy
# et ici la valeur commune est 2, la dimension de notre tableau
len(vec.shape) == vec.ndim 
```

On peut modifier l'élément, en faisant attention comme tout à l'heure: ici on attend des entiers ! toute valeur d'un autre type sera convertie (lorsque c'est possible) dans le type entier avec plus ou moins d'effet: `True` deviendra `1`, `False` deviendra `0`, un flottant sera réduit à sa *partie  entière*, etc...

```{code-cell} ipython3
:cell_style: split

vec
```

```{code-cell} ipython3
:cell_style: split

vec[0, 0] = False
vec
```

```{code-cell} ipython3
:cell_style: split

vec
```

```{code-cell} ipython3
:cell_style: split

vec[0, 0] = 150.99
vec
```

ah bien oui ! il a coupé 0.99 !

+++

Vérifions que `vec1` a bien été modifié ?

```{code-cell} ipython3
vec1[0, 0] # oui !
```

Et vous pouvez comme en Python utiliser les indices négatifs qui se traduisent facilement en indices positifs

```{code-cell} ipython3
vec[-1, -1] # dernier élément ou élément d'indice (3-1, 4-2)
```

```{code-cell} ipython3
vec[3-1, 4-1] # oui c'est bien cela
```

```{code-cell} ipython3
vec[-2, -2] # un autre élément donc d'indice (3-2, 4-2) 
```

```{code-cell} ipython3
vec[3-2, 4-2] 
```

À vous de jouer, créez un tableau de 30 valeurs entre 0 et 30 non compris. Donnez lui la dimension de 2 matrices de 5 lignes et 3 colonnes, et accédez à l'élément qui se situe dans la 2ième matrice, 4ième ligne, 3ième colonne ? vous obtenez quelle valeur ? 26 ?

```{code-cell} ipython3
:cell_style: center

# à vous de jouer
```

+++ {"cell_style": "center"}

Souvenez-vous, dans toutes les dimensions $\ge2$, on remarque que les tableaux ont leurs lignes à l'indice -2 (avant-dernière dimension) et leurs colonnes à l'indice -1 (dernière dimension)

A vous de jouer, faites un `np.ndarray` contenant des 1, de dimension 3 x 2 x 5 x 4,  
i) affichez le, vous allez bien voir trois groupes de 2 matrices de 5 lignes sur 4 colonnes,  
ii) afficher le nombre des éléments des dimensions -2 et -1 (un indice la forme c'est `np.ndarray.shape`).

```{code-cell} ipython3
# votre code ici
```

## accéder à un sous-tableau (slicing)

+++

Maintenant nous allons voir comment accéder à un sous-tableau d'un tableau existant.

Là encore vous pourrez obtenir des sous-tableaux de différentes dimensions !

Cette opération de *slicing* sera syntaxiquement équivalent au slicing des listes et autres séquences en Python (toutefois il y aura une différence très importante entre le slicing-python et le slicing-numpy; nous y reviendrons).

+++

### en dimension 1

+++

#### rappel du slicing Python

+++

Prenons un exemple Python d'une liste contenant les 10 premiers entier positifs  
`L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]`

```{code-cell} ipython3
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ] # ou tout autre manière de faire
```

Extrayons de `L` une sous-liste.

On vous rappelle que le *slicing* (découpage) Python de la liste `L` s'écrira syntaxiquement comme  
`L[from_included, to_excluded, step]`  
`from_included` et `to_excluded` étant respectivement les indices de départ et d'arrivée, et `step` le pas; i.e. un pas de 1 veut dire tous les éléments, un pas de 2 signifie un élément sur deux ... 

On peut utiliser des indices négatifs `-1` est le dernier élément, `-2` l'avant dernier ...

Extrayons la liste partant du deuxième élément de la liste (donc d'indice 1), en allant jusqu'au dernier (donc soit 9 soit -1), en considérant un élément tous les 2 éléments.

```{code-cell} ipython3
L[1:-1:2]
```

```{code-cell} ipython3
L[1:9:2]
```

À l'identique le découpage (*slicing*) d'un `np.ndarray` de dimension 1.

+++

#### slicing d'un `np.ndarray`

```{code-cell} ipython3
# oui on réutilise L (on reste très paresseux puisque c'est souvent bien de l'être)
v = np.array(L) 
v[1:-1:2]
```

```{code-cell} ipython3
v[1:9:2]
```

Là aussi on peut utiliser des indices négatifs (donc `-1` est le dernier élément, `-2`
 l'avant dernier ...)

Si le pas est négatif, alors il faut faire attention aux indices du début et de la fin dans l'expression de slicing `vec[debut:fin:pas]`, puisque pour descendre on partira d'un indice supérieur (oui logique):

```{code-cell} ipython3
v[-2:0:-2]
```

On part de l'avant dernier $-2$ on va jusqu'à l'indice 0 et on descend avec un pas de -2. On remarque que l'élément d'indice 0 n'est pas compris ! oui c'est calculé comme cela `to` n'est pas compris).

Si on voulait avoir le dernier élément ? et bien, tout simplement, on n'indique pas la valeur de `to`, il prendra tous les éléments par défaut.

```{code-cell} ipython3
# remarquez le :: qui indique 
# que le to_excluded n'est pas indiqué 
# du coup par défaut la slice
# va jusqu'à la fin du tableau
v[-2::-2] 
```

Et si on n'indique rien ?

```{code-cell} ipython3
v[::]
```

On a tout le tableau, et dans l'autre sens aussi:

```{code-cell} ipython3
v[::-1]
```

Passons en accès pour des dimensions supérieures à 1:

+++

### en dimension supérieure à 1

+++

Si nous reprenons l'exemple du *vec* en dimension 4 de forme $(n, m, l, c)$. Avec $vec[i_n, j_m, k_l, l_c]$ (où les indices sont corrects i.e dans les bornes de leur dimension) on accède a un élément.

Si à la place de mettre des indices uniques, vous utilisez une syntaxe de *slicing* (en `a:b:c` comme on vient de le re-voir), vous allez accéder à un sous-tableau.

Faisons un tableau de $40$ éléments qui vont de $0$ à $39$ (en valeur).  
Redimensionnons-le en une forme $2 \times 5 \times 4$, et affichons-le: on voit bien les deux matrices.

```{code-cell} ipython3
mat = np.arange(0, 40)
mat.resize((2, 5, 4))
print(mat)
```

Disons qu'on cherche à extraire, dans la première matrice, la sous-matrice du milieu  
(obtebnue en enlevant une épaisseur de largeur 1 sur le pourtour), donc ici pour nous  
$\begin{pmatrix} 5 & 6 \\ 9 & 10 \\ 13 & 14 \\ \end{pmatrix}$

Donc on veut la première matrice (0), puis les éléments qui vont du deuxième élément (1) à l'avant dernier compris (-1) pour les lignes et les colonnes:

```{code-cell} ipython3
# vous essayez ? la solution est dessous
```

```{code-cell} ipython3
mat[0, 1:-1, 1:-1]
```

Maintenant si je veux extraire la même zone, mais pour les deux matrices, et bien je dis, pour la dimension du nombre de matrice, que je prends tous les éléments, avec '::'

```{code-cell} ipython3
mat[::, 1:-1, 1:-1]
```

ce qui, comme dans la syntaxe des slicing de listes Python, s'abrège en ':'

```{code-cell} ipython3
mat[:, 1:-1, 1:-1]
```

et ainsi de suite ... si je veux toute la première ligne de la seconde matrice ? Et bien je peux le faire comme ceci

```{code-cell} ipython3
:cell_style: center

# 1 parce que la seconde matrice
# 0 parce la première ligne
# : parce que toutes les colonnes
mat[1, 0, :]
```

```{code-cell} ipython3
# pour vérifier visuellement
mat
```

C'est super tout cela !

Maintenant nous allons voir comment modifier les valeurs de nos sous-tableaux ... mais avant de modifier, il faudrait comprendre ce qu'on va modifier !

En effet, les sous-tableaux (les slices) **Sont-ils des vues sur le tableau existant ou des copies du tableau**  ou encore **Va-t-on modifier le tableau initial ou une copie du tableau initial ?**

Alors votre idée ?

+++

## les slices sont des vues et non des copies

+++

En effet la question qui se pose est la suivante:  
Est-ce que le slicing a créé un nouveau `np.ndarray` avec son propre segment de mémoire ? Ou est-ce qu'il a calculé une nouvelle vue (view) sur le segment mémoire du tableau existant ?

Prenons un exemple:

```{code-cell} ipython3
mat = np.arange(5)
mat1 = mat[2::2]
```

```{code-cell} ipython3
:cell_style: split

mat
```

```{code-cell} ipython3
:cell_style: split

mat1
```

$mat1$ est-il un nouveau `np.ndarray` ou une vue sur le `np.ndarray` de *mat* ?

+++

On se doute bien que `numpy` veut garder sa première place de LA librairie rapide et bien codée de tableaux pour Python.

Si ils avaient choisi de construire un nouveau segment unidimensionnel dans mémoire, pour les données, à chaque fois qu'on accèdait à une sous-partie d'un tableau `np.ndarray` existant ... et bien ça pénaliserait fortement tous les codes !

D'autre part, les utilisateurs de `numpy` savent pertinemment si ils veulent une vue ou une copie pour leur sous-tableau...

Donc ? et bien oui:
   - un nouvel objet `np.ndarray` est bien créé,
   - il est différent de l'objet `np.ndarray` initial
   - mais ils **partagent** la mémoire (le segment unidimensionnel)

+++

Donc `mat` et `mat1` sont bien deux objects de type `np.ndarray` et ils sont différents

```{code-cell} ipython3
type(mat), type(mat1)
```

```{code-cell} ipython3
mat is mat1
```

+++ {"tags": ["level_intermediate"]}

Pour les avancés ou les curieux rapides (les autres pourront y revenir lors de leurs révisions, parce que naturellement vous révisez vos cours d'une fois sur l'autre ? du moins quand ce n'est pas du matin pour l'après-midi ?

Dans un objet `np.ndarray` je peux savoir si cet objet est une vue !  
Oui le champ `base` m'indique si mon `ndarray` est *basé* sur un autre `ndarray`!

```{code-cell} ipython3
:tags: [level_intermediate]

mat.base # None: mat n'a pas de base !
```

```{code-cell} ipython3
:tags: [level_intermediate]

mat1.base # ah et bien voila mat ! qui est la base de mat1
```

```{code-cell} ipython3
:tags: [level_intermediate]

# ceci nous montre que mat1 a été
# construit à partir de mat
mat1.base is mat
```

```{code-cell} ipython3
:tags: [level_intermediate]

# ce sont bien deux objets différents
id(mat), id(mat1)
```

+++ {"tags": ["level_intermediate"]}

a contrario, si je prends une référence vers l'objet `mat` et que je l'appelle `mat2`

```{code-cell} ipython3
:tags: [level_intermediate]

mat2 = mat
```

+++ {"tags": ["level_intermediate"]}

alors là par contre, *mat* et *mat2* sont bien les mêmes objets !

```{code-cell} ipython3
:tags: [level_intermediate]

mat is mat2
```

On arrête les informations pour les avancés et on revient à notre mémoire: Réfléchissez à une manière de voir si *mat* et *mat1* partagent la même mémoire sous-jacente ?

Oui par exemple: si vous modifiez un élément de l'un, cet élément apparaîtra modifié dans l'autre !

```{code-cell} ipython3
:cell_style: split

mat
```

```{code-cell} ipython3
:cell_style: split

mat1
```

```{code-cell} ipython3
# en touchant à mat1 ...
mat1[1] = 4444

# en fait je modifie **aussi** mat
mat
```

et c'est bien cela qui se passe: *mat* a été modifié ! Donc `mat1` est donc une *autre* vue sur le segment mémoire sous-jacent de `mat`.

Et si vous vouliez vraiment construire un nouveau `ndarray` à partir d'un slicing ? Il va falloir indiquer clairement que vous voulez faire une *copy*

Pour ça on peut tout simplement utiliser la méthode `copy()` sur n'importe quel tableau, donc en particulier sur la slice; illustrons-le

```{code-cell} ipython3
:cell_style: split

mat = np.arange(6)
mat
```

```{code-cell} ipython3
:cell_style: split

matc = mat[2::2].copy()
matc
```

cette fois-ci `matc` est un nouveau `ndarray`, qui n'a plus rien à voir avec `mat`. La preuve :

```{code-cell} ipython3
# cette fois-ci je peux toucher 
# à la copie sans affecter l'original
matc[1] = 4444
```

```{code-cell} ipython3
:cell_style: split

# ici, changement
matc
```

```{code-cell} ipython3
:cell_style: split

# mais ici, intact
mat
```

Bien sûr ne faites des copies que lorsque vous avez besoin de copies, par exemple lorsque vous devez garder votre tableau initial intact.

+++ {"tags": ["level_intermediate"]}

Pour les avancés: quelle est la base de `matc` ?

```{code-cell} ipython3
:tags: [level_intermediate]

# votre code ici
```

À vous tous de jouer (exercice sur les deux matrices renversées).  
On veut créer un tableau qui est formé des deux matrices  
$[\begin{pmatrix} 2 & 4 & 6\\ 8 & 10 & 12 \end{pmatrix}, \begin{pmatrix} 14 & 16 & 18 \\ 20 & 22 & 24 \end{pmatrix}]$.  

On veut ensuite le *slicer* pour obtenir  
$[\begin{pmatrix} 24 & 22 & 20 \\ 18 & 16 & 14 \\ \end{pmatrix}, \begin{pmatrix} 12 & 10 & 8 \\ 6 & 4 & 2\end{pmatrix}] $, 

et on veut mettre 999 à la place de 2 et afficher le premier tableau.

```{code-cell} ipython3
# votre code ici
```

Nous l'avons déjà bien dit mais il est important de le rappeler: ces tranches de tableaux (slices) ne sont que des vues sur le tableau initial et non des copies. Si vous les modifiez, c'est bien le tableau initial qui est modifié.

Le seul objet qui est créé est une nouvelle vue sur votre tableau, un nouvel `np.ndarray` qui sait qu'il est une vue !

Et là c'est très différent de Python, où les sous-listes obtenues par slicing sont des copies de la liste initiale !

+++

## modifier les sous-tableaux

+++

Maintenant que vous savez accéder à une slice d'un tableau, naturellement vous allez vouloir la modifier ?

Il va falloir faire attention:  
i) au type des éléments  
ii), mais aussi maintenant à la forme du tableau

+++

Prenons un vecteur `vec`:

```{code-cell} ipython3
vec = np.arange(1, 7)
vec
```

Prenons une vue sur les nombres pairs du vecteur `vec`

```{code-cell} ipython3
vec[1::2]
```

Modifions ces nombres tous en une seule fois:

```{code-cell} ipython3
vec[1::2] = [20, 40, 60]
vec
```

Il l'a fait.

Essayons de le tromper ? si je ne lui donne pas assez d'éléments pour remplir sa slice :

```{code-cell} ipython3
:tags: [raises-exception]

vec[1::2] = [2, 4]
```

Il s'en apercoit: il ne sait donc pas déduire un tableau de taille 3 à partir de \[2, 4\]. Et on le comprend ! Quelle valeur choisir pour l'élément manquant ? Rien de logique ne nous vient à l'esprit.

Essayons d'une autre manière:

```{code-cell} ipython3
vec[1::2] = [ 999 ]
vec
```

Que s'est-il passé ! `numpy` a  parfaitement accepté de faire l'affectation !

Comment a-t-il considéré \[999\] ?

Il a considéré \[ 999 \] comme étant \[ 999, 999, 999 \] !

Et oui là il trouve une manière intelligente de transformer (d'élargir, d'agrandir), un tableau réduit à un seul élément (\[ 999 \]) en tableau à 3 éléments: il met 3 fois le même !

Vous auriez indiqué juste 999 il l'aurait fait aussi !

C'est ce qu'on appelle le *broadcasting*, on y reviendra plus tard. C'est super utile ! Quand c'est possible `numpy` *élargit* vos tableaux de manière à pouvoir faire l'opération.

```{code-cell} ipython3
# la manière classique de faire, mais l'autre est plus jolie et plus rapide
vec[1::2] = [ 999, 999, 999 ] 
```

Et en plus, ça va même plus vite ! En effet quand vous voulez faire une opération du genre "*ajouter 10 à tous les éléments d'un vecteur de taille 800*", `numpy` va éviter de créer un nouveau tableau de taille 800 rempli de 10, avant de l'ajouter, il va donc être plus rapide que vous !

+++

On essaie ?

```{code-cell} ipython3
m = np.ones(800) # des tas de 1
```

Combien de temps pour ajouter 10 à chacune des cases de ce tableau:

```{code-cell} ipython3
%%timeit
m+10
```

Et combien de temps si on doit créer le tableau de 10 ?

```{code-cell} ipython3
%%timeit
m10 = np.ones(800)*10 # l'utilisation classique de la fonction ones (on utilise là aussi le broadcast)
m+m10
```

Et bien oui on met naturellement la création du tableau dans le code dont le temps d'exécution est mesurée, sinon naturellement `numpy` sera plus rapide si il n'a pas de broadcasting à faire !

+++

On y reviendra. Oublions pour le moment le broadcasting,

+++

## exercices

+++

avant d'aborder ces exercices, je vous signale un utilitaire très pratique (parmi les 2347 que nous n'avons pas eu le temps de couvrir ;); il s'agit de `numpy.indices()`

commençons par un exemple :

```{code-cell} ipython3
lignes, colonnes = np.indices((3, 5))
```

```{code-cell} ipython3
:cell_style: split

lignes
```

```{code-cell} ipython3
:cell_style: split

colonnes
```

vous remarquerez que dans le tableau qui s'appelle `lignes`, la valeur dans le tableau correspond au numéro de ligne; dit autrement :

* `lignes[i, j] == i` pour tous les $(i, j)$,
    
et dans l'autre sens bien sûr 

* `colonnes[i, j] == j`

```{code-cell} ipython3
:cell_style: split

lignes[1, 4]
```

```{code-cell} ipython3
:cell_style: split

colonnes[1, 4]
```

Pourquoi est-ce qu'on parle de ça me direz-vous ? 

Eh bien en guise d'indice, je vous renvoie à la notion de programmation vectorielle.

Ainsi par exemple si je veux créer une matrice de taille (3,5) dans laquelle `M[i, j] == i + j`, je **ne vais surtout par écrire une boucle `for`**, et au contraire je vais écrire simplement

```{code-cell} ipython3
I, J = np.indices((3, 5))
M = I + J
M
```

### les rayures

+++

Écrivez une fonction `zebre`, qui prend en argument un entier *n* et qui fabrique un tableau carré de coté $n$, formé d'une alternance de colonnes de 0 et de colonnes de 1.

+++

par exemple pour $n=4$ on s'attend à ceci

```console
0 1 0 1 
0 1 0 1 
0 1 0 1 
0 1 0 1 
```

+++

### le damier

Écrivez une fonction *checkers*, qui prend en argument la taille *n* du damier, et un paramètre optionnel qui indique la valeur de la case (0, 0), et qui crée un tableau `numpy` carré de coté $n$, et le remplit avec des 0 et 1 comme un damier (0 pour les cases noires et 1 pour les cases blanches).


https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x1-checkers

+++ {"tags": ["level_advanced"]}

### le damier (variante)

+++ {"tags": ["level_advanced"]}

Il y a beaucoup de méthodes pour faire cet exercice de damier; elles ne vont pas toutes se généraliser pour la variante :

**Variante** écrivez une fonction `super_checkers` qui crée 

* un damier de coté $k.n \times k.n$ 
* composé de blocs de $k\times k$ homogènes (tous à 0 ou tous à 1)
* eux mêmes en damiers
* on décide que le premier bloc (en 0,0) vaut 0

c'est-à-dire par exemple pour $n=4$ et $k=3$ cela donnerait ceci :

```
0 0 0 1 1 1 0 0 0 1 1 1 
0 0 0 1 1 1 0 0 0 1 1 1 
0 0 0 1 1 1 0 0 0 1 1 1 
1 1 1 0 0 0 1 1 1 0 0 0 
1 1 1 0 0 0 1 1 1 0 0 0 
1 1 1 0 0 0 1 1 1 0 0 0 
0 0 0 1 1 1 0 0 0 1 1 1 
0 0 0 1 1 1 0 0 0 1 1 1 
0 0 0 1 1 1 0 0 0 1 1 1 
1 1 1 0 0 0 1 1 1 0 0 0 
1 1 1 0 0 0 1 1 1 0 0 0 
1 1 1 0 0 0 1 1 1 0 0 0 
```

```{code-cell} ipython3
:tags: [level_advanced]

def super_checkers(n, k):
    ...
```

```{code-cell} ipython3
:tags: [level_advanced]

# doit vous donner la figure ci-dessus
# éventuellement avec des False/True au lieu de 0/1
super_checkers(4, 3)
```

### les escaliers

+++

Écrivez une fonction *escalier*, qui prend en argument un entier *n*, qui crée un tableau de taille *2n+1*, et qui le remplit de manière à ce que:
   - aux quatre coins du tableau on trouve la valeur *0*
   - dans la case centrale on trouve la valeur *2n*
   - et si vous partez de n'importe quelle case  et que vous vous déplacez d'une case (horizontalement ou verticalement), en vous dirigeant vers une case plus proche du centre, la valeur que vous trouvez est *1* de plus que la valeur de la case où vous étiez.

+++

https://nbhosting.inria.fr/auditor/notebook/python-mooc:exos/w7/w7-s05-x3-stairs

+++ {"tags": ["level_advanced"]}

### calculs imbriqués (avancé)

+++ {"tags": ["level_advanced"]}

Regardez le code suivant :

```{code-cell} ipython3
:tags: [level_advanced]

# une fonction vectorisée
def pipeline(array):
    array2a = np.sin(array)
    array2b = np.cos(array)
    array3 = np.exp(array2a + array2b)
    array4 = np.log(array3+1)
    return array4
```

+++ {"tags": ["level_advanced"]}

Les questions : j'ai un tableau `X` typé `float64` et de forme `(1000,)`

* j'appelle `pipeline(X)`, combien de mémoire est-ce que `pipeline` va devoir allouer pour faire son travail ?
* quel serait le minimum de mémoire dont on a besoin pour faire cette opération ?
* voyez-vous un moyen d'optimiser `pipeline` pour atteindre ce minimum ?

+++ {"tags": ["level_advanced"]}

**indice**

* l'exercice vous invite à réfléchir à l'utilisation du paramètre `out=` qui est supporté dans les fonction vectorisées de numpy
* dans ce cadre, sachez qu'on peut presque toujours remplacer l'usage d'un opérateur (comme ici `+`) par une fonction vectorisée (ici `np.add`)
