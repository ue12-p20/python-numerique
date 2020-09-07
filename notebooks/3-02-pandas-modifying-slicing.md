---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"tags": []}

# modifications et *slicing* de dataframe

Où on apprend à découper et modifier des parties de dataframe

+++

Nous allons nous intéresser dans ce notebook à la manière de découper (trancher) slicer les objets `pandas` comme des séries ou des dataframes, et à les modifier.

+++

Importons nos bibliothèques et nous allons lire une table des passagers du Titanic pour servir d'exemple.

```{code-cell} ipython3
:tags: []

import pandas as pd
import numpy as np
```

Lisons notre dataframe du Titanic et passons lui comme index des lignes, la colonne `PassengerId`.

```{code-cell} ipython3
file = 'titanic.csv'
df = pd.read_csv(file, index_col='PassengerId')
```

et aussi, comme dans le notebook précédent on va le trier par âge histoire de bien voir la différence entre les index et les indices

```{code-cell} ipython3
df.sort_values(by='Age', inplace=True)
df.head(3)
```

## copier une dataframe

+++

Une chose que nous pouvons apprendre est à copier une dataframe. Pour cela il faut utiliser la méthodes `copy` des `pandas.DataFrame`.

```{code-cell} ipython3
df_copy = df.copy()
df_copy.head(3)      # df_copy est une nouvelle dataframe jumelle de l'originale
```

voilà `df_copy` est une nouvelle dataframe avec les mêmes valeurs que l'originale.

+++

## créer une nouvelle colonne

+++

Il est souvent pratique de créer une nouvelle colonne, en faisant un calcul à partir des colonnes existantes
les opérations sur les colonnes sont, en pratique, les seules opérations qui utilisent la forme `df[nom_de_colonne]`

```{code-cell} ipython3
# pour créer une nouvelle colonne
# par exemple ici je vais ajouter une colonne 'Deceased'
# qui est simplement l'opposé de 'Survived'

df['Deceased'] = 1 - df['Survived']
```

```{code-cell} ipython3
df.head(3)
```

## contextualisons l'accés et la modification de parties d'une dataframe

+++

Pour accéder ou modifier des sous-parties de dataframe, vous pourriez être tenté d'utiliser les syntaxes classiques d'accés aux éléments d'un tableau par leur indice, comme vous le feriez en Python.

Comme par exemple en Python:

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: subslide
---
L = [-12, 56, 34]
L[0] = "Hello !"
L
```

```{code-cell} ipython3
:cell_style: split

L[1:2] = [100, 200, 300]
L
```

Ou encore, d'utiliser l'accés à un tableau par une paires d'indices, comme vous le feriez en `numpy`:

```{code-cell} ipython3
mat = np.arange(25).reshape((5, 5))   # je crée la matrice 5x5
mat[2, 2] = 100                        # je modifie l'élément au milieu
mat[0::4, 0::4] = 10000                 # je modifie les 4 coins
print(mat)                            # j'affiche la matrice
mat[0]                                # j'accède à sa première ligne
```

Mais voilà en `pandas`, c'est très différent: comme on l'a vu déjà, ils ont mis leurs efforts sur la gestion d'une indexation des lignes et des colonnes.

Ils ont priviligié le repérage des éléments d'une dataframe **par des index** (les **noms** de colonnes et les **labels** de lignes), et **pas** les **indices** comme en Python et en `numpy`

Pourquoi ? parce que si vous utilisez `pandas` c'est que vous avez besoin de voir vos données sous la forme d'une table avec des labels pour indexer les lignes et les colonnes. Si vous n'avez pas besoin d'index particuliers, ça veut dire que vous êtes à l'aise pour manipuler vos données uniquement à base d'indices - des entiers - et dans ce cas-là autant utiliser un simple tableau numpy : vous n'allez pas stocker une matrice dans une dataframe ! `numpy` et ses indices ligne, colonne vous suffisent !

+++

Néanmoins, `pandas` offre des techniques assez similaires, et assez puissantes aussi, que nous étudier dans ce notebook.

+++

## rappels : `loc` et `at` pour les accès atomiques

+++

on l'a vu dans le notebook précédent, les accès à un dataframe pandas se font 
* le plus souvent à base d'index et non pas d'indices
* et dans ce cas on utilise `df.loc` pour accéder aux lignes et cellules
* et, toujours avec les index, on utilise `df.at` pour écrire dans la dataframe

```{code-cell} ipython3
df.head(3)
```

```{code-cell} ipython3
:cell_style: split

# avec loc, c'est ligne x colonne
df.loc[756, 'Name']
```

```{code-cell} ipython3
:cell_style: split

# pour upgrader un passager
df.at[645, 'Pclass'] -= 1
```

```{code-cell} ipython3
df.head(3)
```

## slicing

+++

### `df.loc`  et **bornes inclusives**

+++

Du coup, la première chose qu'on peut avoir envie de faire, c'est d'accéder à la dataframe par des *slices*; ça doit commencer à être banal maintenant, puisqu'à chaque fois qu'on voit une structure de données qui s'utilise avec `[]` on finit par étendre le sens de l'opération pour des slices.

Je rappelle qu'en Python une slice c'est de la forme `start:stop:step`, et qu'on peut éluder les morceaux qu'on veut, c'est-à-dire que par exemple `:` désigne une slice qui couvre tout l'espace, `::-1` permet de renverser l'ordre, je vous renvoie aux chapitres idoines si ce n'est plus clair pour vous.

**Par contre**, il faut tout de suite souligner une petite anomalie, qui est que **dans le cas des index** les slices de dataframes **contiennent les bornes**, ce qui, vous vous souvenez, n'a jamais été le cas jusqu'ici avec les slices en Python, où la borne supérieure est toujours exclue; voyons cela

```{code-cell} ipython3
df.head(5)
```

```{code-cell} ipython3
# je sélectionne les lignes entre 
# l'index 756 et l'index 470 INCLUSIVEMENT

df.loc[756:470]
```

Il y a tout de même une certaine logique, c'est que les index sont a priori tout mélangés, mais bon c'est troublant au début.

+++

### `df.loc` avec slicing sur les colonnes

+++

Voyons comment faire du slicing dans l'autre direction

```{code-cell} ipython3
:cell_style: split

# si j'écris ceci, je désigne 
# toutes les lignes de la colonne 
# donc toute la colonne Pclass

df.loc[:, 'Pclass']
```

```{code-cell} ipython3
:cell_style: split
:tags: [level_advanced]

# d'ailleurs effectivement, c'est optimisé
# au point que c'est le même objet en mémoire !

df.loc[:, 'Pclass'] is df['Pclass']
```

Et donc logiquement ici, si je veux sélectionner une plage de colonnes, je vais utiliser deux slices:
* dans la direction des lignes, on prend tout avec une simple slice `:`
* dans la direction des colonnes, le slicing marche aussi **en mode inclusif**

```{code-cell} ipython3
# ici comme pour les lignes, comme on est dans l'espace des index
# et pas celui des indices, les bornes de la slice sont INCLUSIVES

df.loc[:, 'Sex':'Parch'].head(3)
```

### slicing généralisé

+++

Bon bien sûr on peut mélanger toutes les features que nous connaissons déjà, et écrire des sélections arbitrairement compliquées - pas souvent utile, mais simplement pour montrer que toute la logique est préservée

```{code-cell} ipython3
df.head(8)
```

```{code-cell} ipython3
# tous ce qu'on a appris jusqu'ici à propos des slices
# fonctionne comme attendu, à part cette histoire de 
# borne supérieure qui est inclusive avec les index

df.loc[804:828:2, 'Sex':'Ticket':2]
```

### `df.at` pour écrire : **bornes inclusives**

+++

Une autre différence majeure avec les objets Python qu'on a étudiés jusqu'ici, c'est que pour pouvoir écrire dans la dataframe, on ne **peut pas** utiliser `loc`, il **faut utiliser `at`**; ce n'est pas tellement surprenant puisque c'était déjà le cas pour écrire dans une seule cellule, mais ça déroute les débutants, d'autant plus que parfois la forme avec `.loc` fonctionne quand même (mais avec un gros avertissement).

Il faut retenir donc que `df.at` peut tout à fait être utilisé avec des slices aussi, et ici à nouveau les bornes seront bien sûr inclusives; voyons cela

```{code-cell} ipython3
df.head(5)
```

```{code-cell} ipython3
# sans vouloir chercher un "use case" très utile
# multiplions par 1000 une portion de la dataframe

# les lignes entre 756 et 470 inclusivement
# les colonnes entre SibSp et Parch inclusivement

# ici on ne peut pas utiliser *= 1000
# car les deux termes à gauche et à droite
# de l'affectation ne sont pas les mêmes

df.at[756:470, 'SibSp':'Parch'] = df.loc[756:470, 'SibSp':'Parch']*1000

# vérifions
df.head(5)
```

### *copied or not copied, that is the question*

+++

Pour terminer cette section, pour les curieux, il y a une question parfois épineuse qui se pose lorsqu'on fait des sélections de parties de dataframe.

Quand une opération sur une dataframe `pandas` renvoie une sous-partie de la dataframe, savoir si cette sélection est en fait **une référence partagée** vers, ou si **c'est une copie** de la dataframe d'origine, ... dépend du contexte !!

Bon très bien, vous dites-vous mais en quoi cela me concerne-t-il ! il gère bien comme il veut ses sous-tableaux, je ne vais pas m'en soucier ...

alors oui cela est vrai ... jusqu'à ce que vous vous mettiez à modifier des sous-parties de dataframe ...

   - si la sous-partie est une **copie** de la sous-partie de dataframe, votre modification ne sera **pas prise en compte** sur la dataframe d'origine ! évidemment…
   
   - et si c'est une référence partagée vers une partie de la dataframe d'origine, alors vos modifications dans la sélection vont bien se répercuter dans les données d'origine.
   
ahhh ... vous commencez à comprendre: savoir si une opération retourne une copie ou une référence devient important mais dépend du contexte.

Ce qu'il faut retenir c'est que
* **lorsqu'on utilise `df.at`**, dont c'est l'unique propos en fait, vous faites bien les modifications, comme on l'a bien vu déjà
* et c'est pour cela précisément qu'il ne faut pas essayer de changer une cellule en faisant  
  `df[col][line] = new_value`  
  car dans ce cas de figure, dit du *chained indexing*, on n'est pas du tout sûr du résultat !!

+++

## autres mécanismes d'indexation

+++

### accés à une liste explicite de lignes ou colonnes

+++

Nous voulons maintenant prendre une référence sur une sous-partie d'une dataframe qui **ne s'exprime pas sous la forme d'une slice (tranche)**, mais par contre nous possédons la liste des (index des) lignes et des colonnes que nous souhaitons conserver dans ma sous-partie de dataframe.

`pandas` sait parfaitement le faire :
* on utilise `df.loc[]` puisqu'on va désigner des index,
* et on va passer dans les `[]`,  non plus des slices, mais tout simplement des listes (et de plus, vous donnez les index dans l'ordre qui vous intéresse) :

+++

Prenons ainsi par exemple 
* les lignes d'index 450, 3, 67, 800 et 678
* et les colonnes `Age`, `Pclass` et `Survived`

Et comme ce sont des index, nous utilisons `loc`.

```{code-cell} ipython3
# c'est facile de créer une sélection de lignes et de colonnes 
df.loc[[450, 3, 67, 800, 678], ['Age', 'Pclass', 'Survived']]
```

### recherche selon une formule booléenne

+++

Nous avons vu dans le notebook précédent que nous pouvions faire des tests sur toutes les valeurs d'une colonne et que cela nous rendait un tableau de booléens.

```{code-cell} ipython3
:cell_style: center

# rappel: cette expression retourne une dataframe
mask = df['Pclass'] >= 3

# voyons ce qu'elle contient
mask.head(3)
```

Et bien la dernière manière d'accéder à des sous-parties de dataframe, va être d'**indexer par un tableau de booléens**, i.e. on va isoler de la dataframe les lignes où la valeur du booléen est vraie.

Par exemple, pour extraire de la dataframe les lignes correspondant aux voyageurs en 3-ième classe, on va utiliser `mask` - un objet de type `Series` donc, qui contient des booléens - comme moyen pour indexer la dataframe.

```{code-cell} ipython3
# voyez qu'ici dans les crochets on n'a plus 
# une slice, ni une liste, 
# mais une colonne (une Series) de booléens
# qu'on appelle souvent un masque, justement

df.loc[ mask ]
```

Notez que bien souvent on ne prendra pas la pein de décortiquer comme ça, et on écrira directement

```{code-cell} ipython3
# en une seule ligne, c'est un peu moins lisible 
# mais c'est un idiome fréquent

# je rajoute .head(3) pour abrèger un peu

df[df['Pclass'] >= 3].head(3)
```

### combinaison d'expressions booléennes

+++

Un peu plus sophistiqué, nous pouvons mettre **plusieurs conditions**, par exemple personnes qui ne sont pas en première classe et dont l'age est supérieur à 70 ans.

Mais comment écrire ces conditions ...

```{code-cell} ipython3
# on pourrait être tenté d'écrire quelque chose comme ceci

try:
    df['Age'] >= 70 and not(df['Pclass'] == 1)
except ValueError as e:
    print(f"Ce n'est pas bon, il me dit '{e}'")
```

Est-ce que cela vous rappelle quelque chose ?  
Nous avons déjà vu le même comportement lorsqu'il s'était agi d'écrire des conditions sur les tableaux `numpy`; 
alors oui parmi les petites choses que l'on peut trouver parfois contre-intuitives avec `numpy` et `pandas`, il y a les expressions logiques sur les tableaux de booléens.

Vous ne pouvez **pas** utiliser `and`, `or` et `not` ! 

   - soit vous utilisez les `np.logical_and`, `np.logical_or` et `np.logical_not` mais ce n'est pas super lisible ... 
   
   - soit vous utilisez les `&`, `|` et `~` (les opérateurs logiques qu'on appelle *bitwise* i.e. qui travaillent bit à bit) et vous parenthésez bien !

```{code-cell} ipython3
# plus de 70 ans, et pas en première classe
# remarquez que ça se bouscule pas dans cette catégorie...

df.loc [ (df['Age'] >= 70) & (~ (df['Pclass'] == 1)) ] 
```

```{code-cell} ipython3
# pareil avec les opérateurs numpy
# personnellement je préfère la version précédente mais bon

df.loc [ np.logical_and(df['Age'] >= 70, np.logical_not(df['Pclass'] == 1)) ] # bof ...
```

+++ {"tags": []}

### résumé des méthodes d'indexation

+++

Pour résumer cette partie, nous avons vu trois méthodes d'indexation utilisables avec `loc` (et avec `at` donc, par voie de conséquence) :
* on peut utiliser une slice, et parce qu'on manipule des index et pas des indices dans ce cas **les bornes sont inclusives** (on va voir tout de suite qu'avec les indices par contre les bornes sont les bornes habituelles, avec la fin exclue)
* on peut utiliser une liste explicite, pour choisir exactement et dans le bon ordre les index qui nous intéressent
* on peut utiliser un masque, c'est-à-dire une colonne obtenue en appliquant une expression booléenne à la dataframe de départ - cette méthode s'applique sans doute plus volontiers à la sélection de lignes

+++ {"tags": ["level_intermediate"]}

Remarquez d'ailleurs, pour les geeks, que si on veut on peut même mélanger ces trois méthodes d'indexation; c'est-à-dire par exemple utiliser une liste pour les lignes et une slice pour les colonnes :

```{code-cell} ipython3
:tags: [level_intermediate]

# on peut indexer par exemple
# les lignes avec une liste
# les colonnes avec une slice
```

```{code-cell} ipython3
:tags: [level_intermediate]

df.loc[
    # dans la dimension des lignes: une liste
    [450, 3, 67, 800, 678], 
    # dans la dimension des colonnes: une slice
    'Sex'::2]
```

## travailler avec les indices : **bornes habituelles**

+++

Dans les - rares - cas où on veut travailler avec les indices plutôt qu'avec les index, tout fonctionne presque exactement pareil qu'avec les index, sauf que

* on doit utiliser `iloc` et `iat` au lieu de `loc`et `at`, bien entendu
* qui supportent les mêmes mécanismes de *slicing* et d'indexation que l'on vient de voir,
* et dans ce cas comme on est dans l'espace des indices, **les bornes des slices** se comportent comme les **bornes habituelles (début inclus, fin exclue)**

Je vous invite à vérifier ce point par vous même, en remettant à leur valeur originelle la portion de la dataframe que l'on avait un peu arbitrairement multipliée par 1000 tout à l'heure, tout ça en utilisant `iloc` et `iat`

```{code-cell} ipython3
# je vous rappelle où on en est
df.head(5)
```

```{code-cell} ipython3
# votre mission si vous l'acceptez
# rediviser par 1000 les 6 cases, mais à bases d'indices cette fois-ci
# donc en utilisant iloc et iat
...
```

## exercices

+++ {"tags": ["level_advanced"]}

## problème de modification de copies (pour les avancés)

+++

Cette section ne sera, pour une première lecture de ce notebook, que compréhensible par des avancés, les autres pourront y revenir plus tard.

+++

On va voir rapidement le problème de *tentative* de modification d'une copie d'une dataframe.

+++

### modification par chaînage d'indexations

+++

Supposez qu'on accède à une colonne, par exemple celle de la survie qui s'appelle `Survived`, en utilisant la syntaxe classique d'accés à une clé d'un dictionnaire.

```{code-cell} ipython3
df['Survived']
```

On obtient une seule colonne, elle est de type `pandas.Series`, on le savait déjà.

+++

Maintenant que j'ai une colonne, rien ne m'empêche d'accéder à un élément de la colonne, avec la simple notation d'accés à un élément d'un tableau comme dans Python, prenons l'élément d'index 1.

```{code-cell} ipython3
# so far, so good
df['Survived'][1]
```

Maintenant LA question. Je viens d'accéder à un élément de la colonne `Survived`, puis-je utiliser cette manière d'accéder pour modifier l'élément ?

Dit autrement, puis-je ressusciter le pauvre passager d'index 1 en faisant passer son état de survie à 1 par l'affectation `df['Survived'][1] = 1`

La réponse est non ! Pourquoi ? parce que `df['Survived'][1]` est une copie ! pas une référence vers une partie de la dataframe `df` !

On appelle cela une *indexation par chaînage* (on chaîne `['Survived']`et `[1]`) et bien: *toutes les indexations par chaînage  sont des copies* et ne peuvent pas donner lieu à des modifications ...

Vous avez l'obligation d'utiliser `loc` ou `iloc` !

+++

Pour les avancés ce *problème* s'appelle le *chained indexing* et pour plus d'explications regardez là https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy (quand vous en aurez le temps ...)

+++

### indexation par une liste et modification

+++

On va indexer une dataframe par une liste d'index de colonnes sans utiliser `loc` ni `iloc`. Dans cet exemple on isole les trois colonnes `Survived`, `Pclass` et `Sex`

```{code-cell} ipython3
df1 = df[ ['Survived', 'Pclass', 'Sex'] ]
df1.head()
```

On obtient une dataframe que nous appelons `df1`. Donc vous vous rappelez que nous avons deux possibilité pour la sous-partie d'une dataframe, obtenue par découpage de la dataframe d'origine:
   - c'est une copie de la dataframe (vous ne devez pas la modifier)
   - c'est une référence sur la dataframe (vous pouvez la modifier).

+++

LA question est donc de savoir si `df1` est une copie ou une référence sur votre dataframe ?

C'est une copie donc vous ne devez pas tenter de la modifier mais on va le faire.

On tente de ressusciter notre pauvre passager d'index 1 en utilisant `loc` sur la sous-dataframe `df1` (on a oublié que `df1` était une copie).

+++

On regarde ce que vaut l'élément qu'on veut modifier:

```{code-cell} ipython3
df1.loc[1, 'Survived']
```

ok 0. On tente de le modifier:

```{code-cell} ipython3
df1.loc[1, 'Survived'] = 1
```

Je recois un warning de `pandas` me disant que j'ai potentiellement un problème. Comme il n'est pas sûr que pour moi ca en soit un, il me donne un simple avertissment et non une erreur.

En fait, là il m'indique que: si je pensais modifier `df` en passant par `df1` alors je me trompe puisque `df1` est une copie de ma dataframe `df`, donc `df` ne sera pas modifié.

Il se peut que ce soit ce que vous voulez que `df1` soit une copie ! mais alors pourquoi ne l'avez vous pas clairement indiqué en faisant une copie explicite !

+++

Si mon idée était bien de ne modifier que `df1` parce que je veux une copie de `df`: alors je le code **proprement**:

```{code-cell} ipython3
df2 = df[ ['Survived', 'Pclass', 'Sex'] ].copy()
df2.head()
```

```{code-cell} ipython3
df2.loc[1, 'Survived'] = 1
```

Ah voilà qui est mieux !
