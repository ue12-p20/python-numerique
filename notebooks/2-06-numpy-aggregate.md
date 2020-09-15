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
  notebookname: "agr\xE9gation selon les axes"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>

<!-- #region {"tags": []} -->
# agrégation

ou comment combiner les données dans un tableau, selon certains axes
<!-- #endregion -->

```python tags=[]
import numpy as np
```

Nous venons de voir des opérations `numpy` qui s'appliquent élément par élément. Nous avons ausi abordé la vectorisation et le broadcasting.

Il existe en `numpy` des fonctions qui travaillent sur tous les éléments le long d'un axe. Par exemple: la somme des lignes, le maximum des colonnes, le maximum global du tableau...


On va appeler cela l'agrégation de valeurs d'un tableau


## agrégation en dimension 1


En dimension 1, il n'y a qu'un axe, tous les éléments du tableau sont sur le même axe. 
Donc cela va rester très simple: il suffira d'appliquer la fonction d'agrégation désirée au tableau, en laissant `numpy` déduire l'axe sur lequel l'appliquer ... y'en a qu'un ! 

```python
vec = np.array([10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120, 130, 140])
vec
```

### sommons tous les éléments


Deux manières identiques de faire : on appelle la **fonction** globale `np.sum` ou on appelle la **méthode** des tableaux `np.ndarray.sum`.

```python cell_style="split"
# qu'on utilise une fonction ...
np.sum(vec)
```

```python cell_style="split"
# ... ou une méthode
# le résultat est le même
vec.sum()
```

La seule chose à remarquer ici est que `sum` renvoie la valeur calculée. Rien que de très normal.


Et aucun "*piège*". Afin de ne pas retourner une somme fausse, le type de la variable retournée sera:
   - celui des éléments votre tableau sauf si ...
   - sauf si la *version* demandée pour ce type (`int8`) le rend *plus petit* que le type qu'utilise votre ordinateur (`int64`).

Essayons:

```python
vec = np.array([10,  20,  30, ], dtype=np.uint8)
s = np.sum(vec)
(type(s))
```

Bingo. Il passe en `np.int64` ! Et ce quelle que soit la valeur du résultat. Même si la somme est tout à fait stockable sur 8 bits puisqu'elle vaut .. combien ? oui, 60.


C'est bien normal une somme d'éléments d'un type *peut* ne pas pouvoir tenir sur une variable de ce même type. Dans le premier exemple, la somme vaut *1050* qui ne peut pas être stocké sur un entier non signé de 8 bits ... (oui parce que le maximum est ? et bien calculons: $11111111 = 2^8 -1$ en décimal soit 255).


### calculons le minimum d'un vecteur


Prenons un tableau de dimension 1, de 15 entiers sur 8 bits, aléatoirement générés entre 1 et 100.

```python
ran = np.random.randint(0, 100, 15,  dtype=np.int8)
ran
```

Deux manières identiques de faire: on appelle la fonction globale `np.min` on appelle la méthode des tableaux `np.ndarray.min`. Vous avez compris l'idée générale...

```python cell_style="split"
np.min(ran)
```

```python cell_style="split"
ran.min()
```

```python
type(ran.min()) # notez qu'il conserve le type des éléments
```

Oui là le type que vous avez demandé pour vos éléments suffit ! puisque votre minimum appartient à votre tableau, c'est bien que `numpy` est arrivé à la stocker dans une variable du type que vous avez indiqué.


De même que vous allez pouvoir calculer le minimum ou le maximum vous allez pouvoir aussi accéder à l'indice du minimum (ou du maximum) dans votre tableau.

```python
np.argmin(ran)
```

Et on accède à l'élément

```python
# on retrouve bien le minimum
ran[ np.argmin(ran) ]
```

Oui bien sûr c'est identique à aller directement chercher le min, mais parfois c'est utile de connaitre à quel indice se situe ce minimum...


### testons les valeurs sur tout un vecteur (`all` et `any`)


Travaillons maintenant sur un tableau de booléens.

Comment savoir si tous les éléments de votre tableau sont vrais (sont à True) ? Ou si l'un au moins, d'entre eux, est à vrai ?

Première idée ... on peut en faire la somme (True sera pris comme 1) et regarder si la somme est égale au nombre d'éléments de votre tableau (dans le permier cas) et strictement supérieure à 0 dans le second cas ... vous vous voyez faire cela à chaque fois que vous allez vouloir appliquer ce genre de tests ? heu non pas trop.

`numpy` vous donne des fonctions pour cela, la première s'appelle `all`  et la seconde `any`; et comme tout à l'heure vous avez les deux versions (la fonction globale de `numpy` et la méthode des `ndarray`).


Pour créer un tableau de 10 booléens (par exemple)

* je génère 10 entiers aléatoirement entre 0 et 2 (non compris)
* et je type ce tableau comme étant de type `np.bool` avec la méthode `np.ndarray.astype` 

vous vous souvenez de `astype` ? nous l'avons vu rapidement dans le tout premier notebook d'introduction à `numpy`

```python
boo = np.random.randint(0, 2, 10).astype(np.bool)
boo
```

Voici le tableau, en dimension 1, `boo` de 10 booléens. Regardons si ils tous vrais ? 

```python cell_style="split"
# la fonction ..
np.all(boo)
```

```python cell_style="split"
# .. ou la méthode
# les deux font la même chose
boo.all()
```

Y-en-a-t-il au moins un à `True` ?

```python cell_style="split"
np.any(boo)
```

```python cell_style="split"
boo.any()
```

Bien sûr `any` ne s'applique pas qu'à des tableaux booléens ! Il va indiquer les valeurs non nulles d'un tableau.

```python
# ici comme on a changé l'intervalle,
# toutes les valeurs sont non-nulles
np.all(np.random.randint(1, 3, 10))
```

## exemples de fonctions d'agrégation

| fonction | comportement|
|------|-----|
| `np.sum` | somme les éléments sur un axe|
| `np.min` | retourne le plus petit élément|
| `np.max` | retourne le plus grand|
| `np.argmin` | retourne l'indice du plus petit élément|
| `np.argmax` | retourne l'indice du plus grand élément|
| `np.mean`| calcule la moyenne des éléments|
| `np.std`  | calcule l'écart type des éléments |
| `np.var`  | calcule la variance des éléments |
| `np.all`  | vrai si aucun élément n'est nul |
| `np.any`  | vrai si au moins un élément n'est pas nul |
| `np.where`  | une condition ternaire |
| .../...| .../... |


## agrégation en dimension 2

Effectivement en `numpy` les tableaux peuvent avoir des dimensions supérieures à 1 comme des matrices avec une seule ligne, des matrices avec une seule colonne, des matrices, des paquets de matrices, des groupes de paquets de matrices...


### sommons en dimension 2


Voici une petite matrice de 3 lignes et 5 colonnes contenant les entiers de 0 à 15.

```python
mat = np.arange(15).reshape(3, 5)
mat
```

Nous sommes en dimension 2, nous avons 2 axes, celui des lignes et celui des colonnes qui auront respectivement l'indice 0 et l'indice 1 (comme les dimensions apparaissent dans `shape`).

Pour spécifier l'axe sur lequel on veut faire une opération, il faut passer l'argument `axis=0` ou `axis=1` à `np.sum` ou `np.ndarray.sum`.

Allons-y ! Demondons à `mat` de sommer ses valeurs sur l'axe `0` des lignes.

```python
mat.sum(axis=0)
```

Il somme bien suivant l'axe des lignes (vous avez 3 lignes, il les somme entre elles) donc vous obtenez la somme de chacune des colonnes ... oui peut être un peu contre-intuitif mais c'est bien cela qui se passe.

Si je demande de sommer sur l'axe des colonnes, il va créer un tableau avec la somme de chaque ligne.

```python
mat.sum(axis=1)
```

Et si vous n'indiquer pas d'axe ? Et bien il va sommer tous les éléments entre eux !

```python
mat.sum()
```

Comme nous l'avons dit dans la section sur la dimension 1. Le type du résultat des sommes d'entier sera le type des entiers de votre ordi. (pour le mien 64 bits) ou celui qui a été indiqué pour votre tableau si il est plus grand donc a plus de précision). Mais les entiers sur 64 bits sont le plus grand type entier proposé par `numpy`.

Pour les flottants pareil avec des flottants sur 64 bits.


### calculons les min et max


Maintenant regardons le minimum et le maximum globaux d'une matrice, ceux de l'axe des lignes et ceux de l'axe des colonnes et l'indice de ces valeurs dans la matrice.

Prenons une matrice de taille 3 x 5 d'entiers de 1 à 15.

```python
al = np.arange(1, 16).reshape(3, 5) # 15 éléments
al
```

Le maximum global.

```python
al.max() # oui bien sûr 15
```

Son indice:

```python
al.argmax()
```

Ah mince 14 ? il me donne bien l'indice mais de manière *absolue* pas l'indice relatif aux lignes et aux colonnes de la matrice ! 

Si vous lisez le *help*, on vous dit que la fonction *retourne les indices des valeurs maximales le long d'un axe*. Là il n'y a pas d'axe indiqué, le maximum est donc retourné de manière absolue puisque c'est bien le maximum absolu que vous demandez. 

Comment faire pour accéder à l'élément à cette position ?

Il faut surtout éviter les opérations qui prendraient du temps et de l'espace, comme celles qui recopieraient le tableau (comme le fait la fonction `np.ndarray.flatten`, lisez son help).

Vous allez utiliser la fonction **dédiée** `np.unravel_index` qui re-calcule les index dans chacune des dimensions à partir de l'indice absolu et de la forme du tableau.

On le fait:

```python
#np.unravel_index?
```

```python
indices = np.unravel_index(al.argmax(), al.shape)
print(indices)
```

Notre max est bien à l'indice (2, 4) soit la case de la matrice à la troisième ligne cinquième colonne. On accède à l'élément.

```python
al[indices]
```

<!-- #region {"tags": ["level_advanced"]} -->
Pour les avancés, sauriez-vous reprogrammer la fonction `np.unravel_index` à partir d'un indice *absolu* et de la forme d'un tableau ?
<!-- #endregion -->

```python tags=["level_advanced"]
# votre code ici
```

Passons aux calculs sur les axes. Calculons les minimums sur l'axe des lignes.

```python
np.min(al, axis=0)
```

Là vous demandez les minimums dans l'axe des lignes donc vous calculez le minimum de chacune des colonnes.


Regardons les indices des minimums sur l'axe des lignes ?


Il vous donne, pour chaque colonne, l'indice de la ligne où vous allez trouver le minimum.

```python
al
```

```python
al.argmin(axis=0)
```

 Pour accéder aux éléments ? Comme on peut indicer une matrice par un tuple, vous avez la première partie du tuple (les indices des lignes), il vous reste à donner la liste des indices des colonnes (toutes les colonnes auront un min). 

```python
al[al.argmin(axis=0), np.arange(0, 5)]
```

Pour prendre le minimum dans l'axe des colonnes:

```python
np.min(al, axis=1)
```

```python
np.argmin(al, axis=1)
```

La suite de ce notebok sort des bases utiles et n'est que l'extension de l'agrégation en dimension > à 2 qui est immédiate. Elle n'est là que pour dire que ca existe.

<!-- #region {"tags": ["level_advanced"]} -->
Pour les avancés, sauriez vous faire sur un ndarray en 2 dimensions, la fonction qui, étant donné une forme du tableau, l'axe et une liste d'indices dans cet axe, calcule la paire d'index ? Sauriez-vous généraliser cette fonction ?
<!-- #endregion -->

```python tags=["level_advanced"]
# votre code ici
```

<!-- #region {"tags": ["level_advanced"]} -->
## agrégation en dimension > 2
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
Ce n'est sûrement pas très utile d'appliquer des fonctions d'agrégation sur des tableaux autres que des matrices ou des vecteurs, regardons très rapidement ce qui se passe dans certains cas.
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
### sommons en dimension 3
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
Générons 2 matrices de 3 lignes et 4 colonnes. Oui à partir de `np.random.randint` et son argument *size* par exemple. Cela vous permet de ne pas compter...
<!-- #endregion -->

```python tags=["level_advanced"]
mats = np.random.randint(-100, 100, size=(2, 3, 4))
mats
```

<!-- #region {"tags": ["level_advanced"]} -->
Combien cette matrice a-t-elle de dimensions ? Oui 3. Combien d'axes ? Et bien oui 3 ?

Quels sont les indices de ces axes ? 0, 1 et 2. A quoi correspondent-ils ? respectivement: aux matrices, aux lignes et aux colonnes.
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
Si nous sommons sans mention d'axe nous sommons tous les éléments du `ndarray`, dans ses 2 versions
<!-- #endregion -->

```python tags=["level_advanced"]
np.sum(mats), mats.sum()
```

<!-- #region {"tags": ["level_advanced"]} -->
Si nous sommons sur l'axe des matrices, nous sommons les deux matrices ensemble:
<!-- #endregion -->

```python tags=["level_advanced"]
np.sum(mats, axis=0)
```

<!-- #region {"tags": ["level_advanced"]} -->
Si nous sommons sur l'axe des lignes nous sommons les lignes ensembles donc obtenons un tableau de la taille des lignes qui donne la somme des colonnes.
<!-- #endregion -->

```python tags=["level_advanced"]
np.sum(mats, axis=1)
```

<!-- #region {"tags": ["level_advanced"]} -->
Si nous sommons sur l'axe des colonnes, nous sommons les colonnes ensembles donc obtenons un tableau de la taille des colonnes qui donne la somme des lignes.
<!-- #endregion -->

```python tags=["level_advanced"]
np.sum(mats, axis=2)
```

<!-- #region {"tags": ["level_advanced"]} -->
### calculons les min et max en dimension 4
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
De la même manière nous pouvons calculer les min et les max ainsi que les arguments des min et des max en dimensions supérieures, par exemple là en dimension 4.
<!-- #endregion -->

<!-- #region {"tags": ["level_advanced"]} -->
Supposons que nous prenions un tableau en dimension (2, 3, 4, 5). Dé-commentez les lignes suivantes si vous voulez en voir un.
<!-- #endregion -->

```python tags=["level_advanced"]
tab = np.arange(1, 121).reshape(4, 3, 2, 5)
```

<!-- #region {"tags": ["level_advanced"]} -->
Appelons ce tableau: 4 paquets de 3 matrices de 2 lignes et de 2 colonnes.

On va pouvoir demander le maximum, le minimum et leurs indices suivant tous les axes. Pour la signification de ces calculs ... il faut réfléchir.

Par exemple, si on demande le maximum sur l'axe 0 où nous avons les 4 paquets. Regardons suivant cet axe, nous voyons (4 fois) 3 matrices avec 2 lignes et 5 colonnes, on aura donc cette forme pour la réponse (3, 2, 5). La dimension qui *disparaît* est celle de l'axe où on demande le calcul, les autres restent en agrégeant les calculs donc il nous reste (3, 2, 5), la dimension 4 a été agrégée lors du calcul.
<!-- #endregion -->

```python tags=["level_advanced"]
tab.max(axis=0).shape
```

<!-- #region {"tags": ["level_advanced"]} -->
### testons en dimension 4

Nous avons vu que `np.all` returns `True` si toutes les valeurs du tableau testé sont `True` (aucune n'est nulle) et `np.any` si au moins une n'est pas nulle. Ces fonctions, si-besoin, s'appellent bien sûr suivant les différents axes. Avec les interprétations dont nous avons déjà parlé.

Prenons un tableau en dimension (2, 3, 4, 5) et demandons sur l'axe des colonnes (3 ou -1) si toutes les valeurs sont non-nulles. On va se retrouver avec une valeur par ligne donc la dimension qui *disparaît* est celle de l'axe où on demande le calcul, les autres restent en agrégeant les calculs donc il nous reste (2, 3, 4).
<!-- #endregion -->

```python cell_style="center" tags=["level_advanced"]
tab = np.random.randint(-10, 10, size=(2, 3, 4, 5))
```

```python tags=["level_advanced"]
tab.max(axis=-1).shape
```

<!-- #region {"tags": ["level_advanced"]} -->
On ne va pas aller plus loin. Attendez d'en avoir besoin.
<!-- #endregion -->
