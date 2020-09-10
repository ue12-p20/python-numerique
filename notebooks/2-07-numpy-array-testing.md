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
  notebookname: masques pour tester les tableaux
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>


# masques et tableaux booléens

ou comment tester tous les éléments d'un tableau


Nous avons vu les fonctions vectorisées (qui s'appliquent à tout un tableau sans recours à une boucle for-Python). Nous avons aussi vu les fonctions qui aggrègent les valeurs suivant les axes des `np.ndarray` et permettent par exemple de sommer les lignes ou les colonnes d'une matrice ou encore trouver le plus petit élément ou son index dans la `np.ndarray`.

Nous allons voir une dernière chose qui consiste à tester tous les éléments d'un `np.ndarray` (ou bien sûr une slice d'un `np.ndarray`).

Il y a deux manières de tester: soit vous voulez tester tous les éléments et combiner les résultats des tests unitaires en un seul résultat global, soit vous voulez obtenir un `np.ndarray` de booléens qui vous donne chaque tests individuellement.

Nous allons voir rapidement ces deux manières de tester.

```python
import numpy as np
```

## appliquons une condition à un `np.ndarray`

Les conditions s'appliquent à tous les éléments d'un tableau en une seule fois, ce qui signifie que vous ne devez pas écrire de boucle en Python mais laisser les fonctions vectorisées le faire pour vous.

Les opérateurs de comparaison sont donc des fonctions vectorisées (encore appelées *UFuncs*). Elles vont retourner un tableau contenant les résultats des comparaisons éléments-par-élément.
   
Vous allez obtenir une sorte de masque que vous pouvez ensuite utiliser pour filtrer les éléments de votre tableau pour, par exemple, ne garder que ceux pour lesquels la condition est vraie..

On va faire tout de suite un exemple. Construisons une matrice de forme *(3 x 4)* qui contient des entiers générés aléatoirement entre *-10* et *10*.

Vous rappelez-vous comment faire une telle matrice ? Essayer avec `np.random.randint` et `reshape`:

```python
# votre code ici
```

```python cell_style="center"
a = np.random.randint(-10, 10, 12).reshape(3, 4)
a
```

Testons les si les élements sont pairs c'est à dire si le reste de leur modulo 2(*%2*) est 0.

Déjà il faut calculer le module:

```python
a%2
```

Et ensuite tester les valeurs de ces résultats qui sont nulles:

```python
a%2 == 0
```

Nous avons un tableau qui s'appelle aussi un masque de booléens.

Maintenant vous avez deux manières d'utiliser ce masque

* soit de manière globale pour savoir, par exemple, le nombre d'éléments pairs de votre tableau 
* soit pour filtrer votre matrice initiale, en ne gardant par exemple que les éléments pairs.


## prendre le résultat global d'une condition


Vous pouvez faire des manipulations sur la matrice des résultats d'une condition de manière globale avec `np.all` et `np.any` - qu'on a déjà rencontrés, rappelez-vous, dans la section sur les agrégations

La permière fonction vous dit si tous les éléments de votre matrice répondent à la condition et la seconde si au moins un élément de votre matrice répond à la condition.


Tous les éléments de la matrice sont-ils pairs ?

```python
np.all(a%2==0)
```

Non (ou alors vous avez une chance incroyable, une chance sur 4096 que ça se produise).

Y-a-t-il au moins un élément pair ?

```python
# sans doute vrai 
np.any(a%2==0)
```

Pour information, il existe aussi une fonction qui permet de compter les éléments qui ne sont pas nuls:

```python
np.count_nonzero(a%2==0)
```

## filtrer les éléments d'un tableau par une condition

Reprenons notre matrice des 12 entiers générés aléatoirement entre *-10* et *10*. Nous ne voulons garder que les éléments pairs de notre matrice.

Nous générons le masque booléen des nombres pairs:

```python
pairs = (a%2==0)
pairs
```

Ce masque a naturellement la même forme que votre matrice. Pour **ne garder que** les éléments pairs, (on dit qu'on filtre les éléments de la matrice par ce masque booléens), nous allons **indexer** la matrice par ce masque:

```python
# cette construction n'est pas anodine
# l'expression dans les [] est **elle-même un tableau** !
a[a%2==0] # ou a[pairs]
```

```python cell_style="split"
# comme on peut le voir ici
type(pairs)
```

```python cell_style="split"
type(a[pairs])
```

Vous avez obtenu un nouveau tableau de type `np.ndarray` qui contient les éléments pairs. Maintenant essayons de composer les conditions sous forme d'une expression logique (e.g. pour faire des *et* ou des *ou* entre expressions)


## composer les conditions

Pour composer les conditions

* vous **devez** utiliser les opérateurs logiques *bit-à-bit* (ou ***bitwise***) `&` (pour et), `|` (pour ou), `~` (pour non) 
* ou leur contrepartie `numpy` qui sont respectivement `np.logical_and`, `np.logical_or`, `np.logical_not`.

SI nous voulons les éléments qui ne sont pas pairs et qui sont strictement inférieurs à 6, calculons le masque et indexons notre matrice avec ce masque:

```python
(a < 6) & ~(a%2==0)
```

```python
a[(a < 6) & ~(a%2==0)]
```

Ou en version *loooongue*

```python
a[np.logical_and(a < 6, np.logical_not(a%2==0))]
```

### mise en garde


Cette façon de faire à base d'opérateurs *bitwise* n'est pas forcément très intuitive… 
en Python on aurait eu envie d'utiliser par exemple les opérateurs `and` et `not`, au lieu de `&` et `~`

Il ne faut pas le faire, et **ça ne fonctionne pas** de toutes façons (les opérateurs logiques Python `and`, `or` et `not` qui ne sont pas vectorisés)

```python tags=["raises-exception"]
# au lieu de (a < 6) & ~(a%2==0)
# on pourrait avoir envie d'écrire
(a < 6) and not (a%2==0)

# mais ça ne marche pas...
```

## compter les éléments répondant à une condition


Nous allons compter les éléments répondant à une condition:

```python
# on pourrait à la rigueur utiliser sum() aussi
np.count_nonzero((a < 6) & ~(a%2==0))
```

Et naturellement vous pouvez compter ces éléments le long des axes de votre `np.ndarray`. Par exemple si on veut le nombre d'éléments impairs inférieurs à 6 dans les colonnes, je vais compter dans l'axe des lignes et recevoir un tableau de la taille des colonnes donc 4:

```python
np.count_nonzero((a < 6) & ~(a%2==0), axis=0)
```

Si on veut le nombre d'éléments impairs inférieurs à 6 dans les lignes, je vais compter dans l'axe des colonnes et recevoir un tableau de la taille des lignes donc 3:

```python
np.count_nonzero((a < 6) & ~(a%2==0), axis=1)
```

Et maintenant que nous avons extrait les éléments d'un `np.ndarray` avec une condition, donnons-lui un nom et essayons de modifier un de ses éléments. Faisons simple, prenons le tableau des éléments négatifs et modifions (si il existe) le premier.

```python
nouveau_tableau = a[a<0]
nouveau_tableau
```

```python
nouveau_tableau[0] = -999
nouveau_tableau
```

Notre `nouveau_tableau` est bien modifié. Pensez-vous qu'il en soit de même dans la matrice d'origine ? Non, ce `np.ndarray` est un tableau complètement différent où les éléments de la matrice d'origine ont été recopiés ! Ce n'est pas une vue sur le tableau d'origine. Pour le voir affichons-le:

```python
a
```

Si nous voulions modifier les éléments de la matrice d'origine et pas une copie ? Il va falloir passer par les indices: prendre les indices de ces éléments dans la matrice d'origine est accéder à ces eléments pour les modifier.


## calculer les indices des éléments dans le tableau d'origine

Nous venons de voir que quand nous "isolons" les éléments, d'une matrice, qui obéissent à une condition, ils sont recopiés dans un nouvel `np.ndarray` et nous ne pouvons pas les modifier à partir de ce nouveau tableau. Si nous voulons accéder aux éléments, qui obéissent à la condition, dans la matrice d'origine: il faut passer par leurs indices.

Ainsi il va nous falloir des fonctions qui nous retournent les indices de ces éléments. Non, il n'est toujours pas question de le faire à-la-main en parcourant le `np.ndarray` avec des boucles for-Python: ca serait beaucoup trop long.

Nous allons voir plusieurs manière de faire.


### la fonction `np.nonzero`


La fonction `np.nonzero` renvoie les indices des éléments, qui ne sont pas `False` ou `0`, sous la forme d'un tuple de liste d'indices, la tuple ayant la dimension du tableau.

Par exemple si notre tableau `num.ndarray` est de dimension 2: la fonction renvoie deux listes d'indices, la première liste contient les indices des lignes et la secondes des colonnes.


À vous de jouer. Créez une matrice *b* de taille *(3, 4)* qui contient les entiers entre 1 et 12. Créez le masque des éléments qui sont divisibles par *3* et appliquez la fonction `np.nonzero` à ce masque.

Que devez-vous obtenir ? Les éléments 3, 6, 9, 12 étant respectivement aux indices *(0, 2), (1, 1), (2, 0)* et *(2, 3)*, si on sépare les indices de lignes et les indices de colonne, on obtient un tuple contenant les deux ndarray *(0, 1, 2, 2)* et *(2, 1, 0, 3)*.

Essayez de le faire:

```python
# votre code ici (la correction ci-dessous)
```

```python cell_style="split"
# la correction
b = np.arange(1, 13).reshape(3, 4)
b
```

```python cell_style="split"
view_index = np.nonzero(b%3==0)

# comme b est de dimension 2,
# view_index est un tuple de 2 listes
view_index
```

C'est là que ça devient un peu magique  
car si je prends la matrice `b`, je peux **l'indicer avec ce tuple** et créer ainsi **une vue** qui ne contient **que les éléments** qui nous intéressent :

```python cell_style="split"
type(view_index)
```

```python cell_style="split"
b[view_index]
```

Que je peux alors modifier:

```python
b[view_index] = b[view_index] * 10
b
```

Voila qui est bien utile pour créer une vue sur un ensemble d'arbitraire d'éléments donnés par leurs indices.


### la fonction `np.argwhere`

La fonction `np.argwhere` renvoie les indices des éléments pour lesquels un masque est vrai, pour chaque élément il renvoit ses indices dans chacune des dimensions. Pour un tableau de dimension *n* de forme *(d1, d2, ..., dn)*, il renverra les indices des éléments sous la forme de *m* n-uplets *(i1, i2, ..., in)*.

Le type du tableau retourné par la fonction est un `np.ndarray`. Quelle en est la taille ? On y trouve *m* lignes (une par élément qui satisfait la condition) de *n* colonnes (une par dimension) donc *(m,n)*.

<!-- #region {"tags": ["level_intermediate"]} -->
En fait donc les deux utilitaires `np.nonzero` et `np.argwhere` font à peu près le même travail, simplement les coordonnées des points qui *matchent* sont retournés dans des formats qui sont différents
<!-- #endregion -->

```python tags=["level_intermediate"]
# si on reprend l'exemple précédent
b = np.arange(1, 13).reshape(3, 4)
b
```

```python cell_style="split" tags=["level_intermediate"]
# le résultat de nonzero
# est un tuple conçu 
# pour pouvoir créer une vue

np.nonzero(b%3==0)
```

```python cell_style="split" tags=["level_intermediate"]
# le résultat de argwhere est
# disons plus *human-friendly*
np.argwhere(b%3==0)
```

```python tags=["level_intermediate"]
# remarquez que pour reconstruire le résultat de argwhere
# à partir de celui de nonzero 
# on pourrait faire par exemple
list(zip(*view_index))
```

À vous de jouer. Faites un tableau sde dimension 3 de taille *(2, 3, 4)* initialisé avec les entiers de 1*1* à *25* et demandez les indices des nombres divisibles par *5*.

Imprimer le masque et sa forme:

```python
# votre code ici (la correction dessous)
```

```python cell_style="split"
# la correction
a = np.arange(1, 25).reshape(2, 3, 4)
a%5 == 0
```

```python cell_style="split"
indices = np.argwhere(a%5==0)
indices
```

```python
# il y a 4 points qui matchent
# et pour chacun 3 dimensions, c'est pourquoi
indices.shape
```

Maintenant que vous avez calculé les indices des éléments divisibles par 5 de votre tableau `a`, comment atteindre ces éléments dans la matrice `a` ?

À vous de jouer. Essayez, à partir du tableau `indices` de modifier les éléments de votre tableau `a` (par exemple pour les remplacer par *999*).

```python
# votre code ici (une correction ci-dessous)
```

```python
# une correction
a[tuple(indices[:, i] for i in range(indices.shape[1]))]
```

```python
# une autre correction qui utilise la transposition de matrice (que nous verrons un peu après)
a[tuple(indices.T)]
```

## modifier les éléments d'un `np.ndarray` avec `putmask`

La fonction `np.putmask` modifie, dans un tableau, les éléments obéissant à un masque avec une valeur donnée en argument (on ne verra que l'exemple avec une valeur unique); le masque étant obtenu par une condition sur le tableau d'origine. La modification est effectuée dans le tableau (en place).

On va voir l'exemple avec une seule valeur. Construisons un tableau de forme *(2, 5)* de *10* nombre aléatoires de loi normale $N(0, 1)$ (avec `np.random.randn`) et remplacons tous les éléments entre *-0.5* et *0.5* par 1. 

```python
a = np.random.randn(10).reshape(2, 5)
a
```

```python
np.putmask(a, (-0.5 < a) & (a < 0.5), 0)
```

```python
a
```

## exercices


### modifier la gaussienne


À vous de jouer. Faites un `np.ndarray` que vous initialisez-le avec des nombres aléatoirement tirés d'une distribution de loi normale de moyenne *3* et de variance *6.25* ($N(3, 6.25)$ avec `np.random.randn`. Comptez les éléments qui sont inférieurs à *-5* ainsi que ceux qui sont supérieurs à *10* et remplacez les tous par la moyenne. Faites le de plusieurs manières différentes.


Avant de commencer, dans la cellule suivante je vous montre comment afficher un histogramme d'un vecteur de points. Afin que nous voyez graphiquement ce qui se passe:

```python
import matplotlib.pyplot as plt
%matplotlib inline
b = np.random.randn(10000)
# vous avez une gaussienne de moyenne 0 et d'écart-type 1
plt.hist(b, bins=30)
```

## correction


### modifier la gaussienne


Une solution avec `putmask`

```python
b = np.random.randn(10000)*np.sqrt(6.25)+3
plt.hist(b, bins=30);
```

```python
np.putmask(b, (b < -5) | (b > 10), 3)
```

```python
plt.hist(b, bins=30);
```
