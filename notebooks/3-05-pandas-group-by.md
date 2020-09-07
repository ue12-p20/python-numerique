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
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>


# regroupement de données

Une table de données `pandas` est en 2 dimensions mais elle peut indiquer des sous-divisions de vos données. Par exemple, les passagers du Titanic sont divisés en femmes et hommes, en passagers de première, deuxième et troisiéme classe. On pourrait même les diviser en classe d'âge, enfants, jeunes, adultes...

Des analyses mettant en exergue ces différents groupes de personnes peuvent être intéressantes. Lors du naufrage du Titanic, valait-il mieux être une femme en première classe ou un enfant en troisième ?


On reprend nos données

```python
import numpy as np
import pandas as pd
```

```python
file = 'titanic.csv'
df = pd.read_csv(file, index_col=0)
df.head(3)
```

On va calculer des regroupements en utilisant la fonction `pandas.DataFrame.groupby`, à laquelle on indique un ou plusieurs critères. 


## groupement par critère unique


Par exemple, prenons le seul critère de genre des passagers (`Sex`). Cette colonne a deux valeurs: `female` et `male`, nous allons donc obtenir une partition de notre dataframe en deux dataframes : celle des hommes et celle des femmes, sur lesquelles nous allons pouvoir faire des analyses (moyenne...) différencées par genre.

Allons-y:

```python
df_by_sex = df.groupby('Sex')
```

`pandas` calcule les différentes valeurs de la colonne en question (ici `Sex`), et partitionne la dataframe en autant de dataframes que de valeurs différentes, et les met dans un objet de type `DataFrameGroupBy` sur lequel vous pouvez, par exemple, itérer pour voir les différentes dataframes.

```python
for name, subdf in df_by_sex:
    print(f"La dataframe de clé '{name}' a {subdf.shape[0]} éléments sur les {df.shape[0]}")
```

Voilà, la fonction a bien partitionné votre dataframe en autant de dataframes que de genre des personnes.


L'objet `DataFrameGroupBy` (ici de nom `df_by_sex`) vous donne accés à de nombreuses fonctionnalités (regardez le help pour plus de détails), nous allons voir ici très peu de choses ici.


Vous pouvez accéder, au travers du champ `groups`, à un dictionnaire vous donnant les deux groupes d'`Index` (deux parce `male` et `female`). Chaque clé est une des valeurs possibles (donc à nouveau `male` et `female`), et sa valeur est la liste des index des lignes ayant cette valeur: 

```python
# df_by_sex.groups est un dictionnaire
# et voici ses clés et valeurs 
for k, v in df_by_sex.groups.items():
    print(f"{k}\t→ {v}")
```

Une fonction pratique pour récapituler les groupes est `size`.

```python
df_by_sex.size()
```

## groupement multi-critères


Si maintenant on s'intéresse à plusieurs colonnes ? Comment est-ce que ça pourrait se présenter à votre avis ?

La solution adoptée, c'est de passer à `groupby`, non plus une seule colonne mais .. une liste de colonnes. 

Le fonctionnement de `groupby` dans ce cas consiste à 
* calculer pour chaque colonne les valeurs distinctes (comme dans le cas simple)
* et en faire le **produit cartésien** pour obtenir les clés du groupement (et incidemment, sous la forme de tuples)

Ainsi dans notre exemple si nous prenons les critères :  `Pclass` et `Sex`:
* le premier critère donne trois valeurs `1`, `2` et `3` pour les trois classes de navigation
* le second donne 2 valeurs `female` et `male`

et donc on va avoir 6 tuples qui serviront de clés pour le groupement : (1, 'female'), (1, 'male'), (2, 'female')...

```python
df_by_sex_class = df.groupby(['Pclass', 'Sex'])
```

```python
# pour itérer sur les 6 catégories
for name, dataframe in df_by_sex_class:
    print(f"{len(dataframe)} passagers en classe '{name[0]}' de genre '{name[1]}'")
```

<!-- #region {"tags": ["level_intermediate"]} -->
Pour les curieux, une petite astuce, utile à ce stade; on pourrait avoir envie d'utiliser la méthode `.head()` pour afficher chacune des sous-dataframes, en écrivant ceci
<!-- #endregion -->

```python tags=["level_intermediate"]
# malheureusement ceci ne marche pas !!
for name, dataframe in df_by_sex_class:
    dataframe.head(1)
```

<!-- #region {"tags": ["level_intermediate"]} -->
En fait ce qui se passe ici, c'est que la méthode `.head()` renvoie un objet que le notebook sait afficher; donc quand on écrit une cellule qui ne contient que (ou dont la dernière instruction est) `df.head()`, cet objet se fait afficher parce que c'est le résultat de la cellule (comme quand `40` se fait affichez quand vous évaluez une cellule avec juste `10+30`)

Mais dans le cas du `for` qu'on est en train de vouloir écrire, le résultat du for est `None`, et rien ne se fait afficher; il nous faut donc provoquer l'affichage (un peu comme quand on est obligé d'insérer un `print()` au milieu d'une cellule); voici l'astuce pour arriver à provoquer l'affichage souhaité :
<!-- #endregion -->

```python tags=["level_intermediate"]
# pour que ça fonctionne il faut forcer l'affichage 
# en utilisant display() qui se trouve dans le module IPython
import IPython 
for name, dataframe in df_by_sex_class:
    IPython.display.display(dataframe.head(1))
```

Reprenons... pour faire une synthèse on peut utiliser `size()` pour récapituler les groupes; la présentation nous montre bien le produit cartésien qui a été fait

```python
# ou en une seule ligne:
# df.groupby(['Pclass', 'Sex']).size()

df_by_sex_class.size()
```

À vous de jouer : calculer le `groupby` avec le genre, la classe et si la personne a survécu ou non. Dans quel groupe de personnes reste-il le plus de survivants ? Et le moins ?

```python
# votre code ici (une petite idée de correction ci-dessous)
```

```python
df_by_sex_class_survived = df.groupby(['Pclass', 'Sex', 'Survived'])
df_by_sex_class_survived.size()
```

Les clés sont des tuples de valeurs.

```python
df_by_sex_class_survived.groups.keys()
```

Les valeurs sont des listes d'index, ça me permet de retrouver les entrées dans la dataframe d'origine.

```python
# voici les trois survivantes de première classe
# cette fois en allant les rechercher dans la grande dataframe
# remarquez que bien sûr ici on utilise loc
# puisque nous sommes uniquement dans l'espace des index
df.loc[df_by_sex_class_survived.groups[(1, 'female', 0)]]
```

## découper des intervalles de valeurs dans une colonne


Parfois, nous sommes intéressés, non pas par les différentes valeurs d'une colonne (qui seraient trop nombreuses) mais par des intervalles de ces valeurs.

Prenons par exemple la colonne des âges. Si nous faisons un groupement brutalement sur la colonne `Age`, nous obtenons 88 âges différents, ce qui ne nous apporte pas une information intéressante.

Par contre ça devient plus intéressant si on raisonne par **classes** d'âges, par exemple les enfants, jeunes, adultes et les plus de 55 ans.
   - *'enfant'* disons entre 0 et 12 ans
   - *'jeune'* disons entre 13 et 19 ans
   - *'adulte'* disons entre 20 et 55 ans
   - *'+55'*  et les personnes de plus de *55 ans
   
Nous aimerions donc avoir une colonne dans notre dataframe avec ces informations à la place des âges.
   
La fonction `pandas.cut`, appliquée à une colonne de votre dataframe, va vous générer une telle colonne, vous pouvez même donner des noms aux intervalles:


Nous allons rajouter la colonne à la dataframe. Sachant que les colonnes d'une dataframe sont les clés d'un dictionnaire, pour ajouter une colonne à votre dataframe, il faut faire comme pour les `dict` en Python. 

```python
# 'bin' en anglais signifie corbeille ou panier
# c'est comme si on mettait les gens dans 4 paniers

df['age-periode'] = pd.cut(df['Age'], bins=[0, 12, 19, 55, 100])
```

Je montre les 6 premières lignes des 3 dernières colonnes de la dataframe:

```python
# on a rajouté une colonne 
df[df.columns[-3:]].head(6)
```

Je donne des noms aux périodes d'âge (ici on va rajouter encore une colonne)

```python
df['name-age-periode'] = pd.cut(df['Age'], bins=[0, 15, 25, 55, 100], 
                                labels=['children', ' young', 'adult', 'old'])
```

```python
df[df.columns[-3:]].head(6)
```

Et maintenant nous pouvons utiliser cette colonne avec un `groupby` sur cette nouvelle colonne

```python
df.groupby(['name-age-periode']).size()
```

```python
# etc...
df.groupby(['name-age-periode', 'Survived']).size()
```

```python
# etc..
df.groupby(['Sex', 'name-age-periode', 'Survived']).size()
```

Vous avez désormais une petite idée de l'utilisation de la fonction `groupby` pour des recherches multi-critères sur une table de données.
