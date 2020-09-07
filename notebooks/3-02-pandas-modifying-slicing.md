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

# la dataframe

Où on apprend à découper et modifier des parties de dataframe

+++

Nous allons nous intéresser dans ce ntebook à la manière de découper (trancher) slicer les objets `pandas` comme des séries ou des dataframes, et à les modifier.

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
df = pd.read_csv(file)

df.index = df['PassengerId']
df.head(3)
```

## copier une dataframe

+++

Une chose que nous pouvons apprendre est à copier une dataframe. Pour cela il faut utiliser la méthodes `copy` des `pandas.DataFrame`.

```{code-cell} ipython3
df_copy = df.copy()
df_copy.head()      # df_copy est une nouvelle dataframe jumelle de l'originale
```

voilà `df_copy` est une nouvelle dataframe avec les mêmes valeurs que l'originale.

+++

## contextualisons l'accés et la modification de sous-parties d'une dataframe

+++

Pour accéder ou modifier des sous-parties de dataframe, vous pourriez être tenté d'utiliser les syntaxes classiques d'accés aux éléments d'un tableau par leur indice, comme vous le feriez en Python.

Comme par exemple en Python:

```{code-cell} ipython3
l = [-12, 56, 34]
l[0] = "Hello !"
l
```

Ou encore, d'utiliser l'accés à un tableau par une paires d'indices, comme vous le feriez en `numpy`:

```{code-cell} ipython3
nl = np.array([[-12, 56], [34, 18]]) # je crée la matrice nl
nl[0, 0] = 999                       # je modifie son premier élément
print(nl)                            # j'affiche la matrice
nl[0]                                # j'accède à sa première ligne
```

Mais voilà en `pandas`, c'est très différent: ils ont mis leurs efforts sur la gestion d'une indexation des lignes et des colonnes.

Ils ont priviligié le repérage des éléments d'une dataframe par des **noms** de colonnes et des **labels** de lignes, des **index**, et pas les *indices* comme en Python et en `numpy`

Pourquoi ? parce que si vous utilisez `pandas` c'est que vous avez besoin de voir vos données sous la forme d'une table avec des labels pour indexer les lignes et les colonnes. Si vous n'avez pas besoin d'index particuliers, ça veut dire que vous êtes à l'aise pour manipuler vos données uniquement à base d'indices - des entiers - et dans ce cas-là autant utiliser les `np.ndarray`: vous n'allez pas stocker une matrice dans une dataframe ! `numpy` et ses indices ligne, colonne vous suffisent !

Ainsi si nous voulons accéder à la première colonne de notre dataframe, on fera:

```{code-cell} ipython3
# quand on utilise l'opérateur [] sur une data frame pandas
# on utilise les index car c'est ce qui est le plus souvent pratique
```

```{code-cell} ipython3
df.columns
#df[0]
```

```{code-cell} ipython3
:cell_style: split

# on peut accéder à la colonne par son nom 
# (qui est sa clé dans l'index des colonnes)
df['Survived']
```

```{code-cell} ipython3
:cell_style: split

# mais pas par son indice
try:
    df[0]
except Exception as exc:
    print(f"OOPS {type(exc)}")
```

On obtient une série `pandas` qui est indexée par `PassengerId` (on le voit écrit en haut de la colonne).

On accède aux éléments (cellules) par leur index dans la ligne. Et attention, nous avons donné comme index aux lignes les identificateurs des passagers - le fameux `PassengerId` qui commence à 1 et pas à 0.

```{code-cell} ipython3
# le passager dont le PassengerId vaut 1 a-t-il survécu ?
df['Survived'][1]
```

Si vous ne donnez pas de noms de colonnes ni de noms de lignes à une dataframe, alors les index existeront, simplement ils seront confondus avec les indices des lignes et des colonnes (i.e. leurs numéros dans leur liste sont devenus leurs index).

Mais les règles d'indexage demeurent. Si la dataframe `data` contient au moins un élément et si les lignes et les colonnes n'ont pas été explicitement indexées:
   - `data[0]` accédera bien à la première colonne de votre dataframe
   - `data[0][0]` au premier élément de la première colonne.
   
Vous voulez essayer ? Il existe un fichier de nom `titanic-sans-header.csv` avec les passagers du Titanic, sans noms de colonnes. Lisez-le avec `pandas.read_csv`, donnez le paramètre `header=None` à `read_csv` pour lui dire qu'il n'existe pas de noms de colonnes (pas de header) et ne mettez pas les `PassengerId` en index des lignes.

Accédez alors à `df_no_header[1][0]`. Que trouvez-vous ?

```{code-cell} ipython3
# votre code ici (correction ci-dessous)
```

```{code-cell} ipython3
df_no_header = pd.read_csv('titanic-sans-header.csv', header=None)
df_no_header[1][0]
```

```{code-cell} ipython3
df_no_header.head()
```

`pandas` a priviligié la manière de voir les dataframe comme des tables indexées et de considérer les noms de ses colonnes un peu comme des clés de dictionnaires. Voilà qui est très très différent de `numpy` .

+++

Mais cela a un prix. Quand une opération sur une dataframe `pandas` renvoie une sous-partie de la dataframe, savoir si cette sous-partie est une copie de la dataframe d'origine ou savoir si c'est une référence vers la dataframe d'origine ... dépend du contexte !!

Bon très bien, vous dites-vous mais en quoi cela me concerne-t-il ! il gère bien comme il veut ses sous-tableaux, je ne vais pas m'en soucier ...


alors oui cela est vrai ... jusqu'à ce que vous vous mettiez à modifier des sous-parties de dataframe ...

   - si la sous-partie est une **copie** de la sous-partie de dataframe, votre modification ne va pas donc être prise en compte sur la dataframe d'origine
   
   - et si c'est une référence vers une partie de la dataframe d'origine (la sous-partie référence bien la dataframe d'origine) alors `pandas` vous permettra de la modifier.
   
ahhh ... vous commencez à comprendre: savoir si une opération retourne une copie ou une référence devient important mais dépend du contexte.

heu ... nous n'allons quand même pas apprendre tous les contextes ou abandonner `pandas` ... non `pandas` a prévu quelque chose de très bien ...

+++

`pandas` fournit une méthode dont l'indexation se base uniquement sur les indices (le *0-based indexing* en anglais) et obéit donc au découpage classique de Python et `numpy` ... vous l'avez reconnue ... nous en avons déjà parlé rapidement ...

Oui il s'agit de `pandas.DataFrame.iloc` ! Seule cette fonction est assurée par `pandas` de retourner une référence sur la dataframe d'origine. La seconde fonction `pandas.DataFrame.loc` dérive simplement de cette première fonction.

+++

Donc règle numéro un: quand je veux modifier une sous-parte d'une dataframe, je dois accéder à cette sous-partie avec `iloc` et `loc`. Rien d'autre ...

Sinon quoi ? Et bien sinon la modification ne sera pas faite sur la dataframe d'origine comme vous le pensiez.

+++

Allons-y ! Utilisons `iloc` pour accéder et modifier un élément.

+++

## accés et modification d'un élément

+++

Allons-y ! Utilisons `iloc` pour accéder à l'état de survie du passager `PassengerId` 1

```{code-cell} ipython3
df.head(2)
```

son indice de ligne est 0 (première ligne) et son indice de colonne est 1 (deuxième colonne)

```{code-cell} ipython3
df.iloc[0, 1]
```

Vous remarquez que `iloc` s'utilise comme `numpy`: les lignes sont indiquées en premier !

+++

Si au lieu de ça on utilisait `loc`, on pourrait utiliser des éléments visibles pour identifier la ligne et la colonne, au lieu de devoir compter; autrement dit on pourrait lui donner des index et pas des indices ...

```{code-cell} ipython3
df.loc[1, 'Survived']
```

Passons son état à survivant avec `iloc` ou `loc`

```{code-cell} ipython3
df.loc[1, 'Survived'] = 1
```

On vérifie !

```{code-cell} ipython3
df.head(1)
```

À vous de jouer, utiliser `pandas.DataFrame.iloc` pour remettre l'état de survie de ce même passager à 0.  
Comme c'est `iloc` (rappelez-vous, *i* est pour *integer*), vous devez lui passer les **indices** de ligne et de colonne, et pas les index.

```{code-cell} ipython3
# votre code ici (solution ci-dessous)
```

```{code-cell} ipython3
df.iloc[0, 1] = 0
```

```{code-cell} ipython3
df.head(1)
```

(pauvre Mr. Braund)

+++

En quelle classe était ce monsieur ? Utilisez `loc` pour le savoir:

```{code-cell} ipython3
# votre code ici (correction ci-dessous)
```

```{code-cell} ipython3
df.loc[1, 'Pclass']
```

Oui en troisième classe. Ce sont les hommes de cette classe qui ont le moins survécu au naufrage ... D'après-vous, quelle catégorie de personne a le mieux survécu au naufrage ? On regardera cela bientôt.

+++

## accés et modification de parties de dataframes

+++

Prendre une référence sur une sous-partie d'une dataframe va vous rendre naturellement un objet de type `pandas.DataFrame`.

+++

Rappelez-vous vous d'utiliser en priorité: `pandas.DataFrame.iloc` ou `pandas.DataFrame.loc`.

+++

### accés et modifications par slicing à-la-Python

+++

Vous allez utiliser `pandas.DataFrame.iloc` avec donc les indices des lignes et des colonnes.

+++

Avec `pandas.DataFrame.iloc` c'est le slicing archi-classique Python ou `numpy`  
c'est à dire la forme `df.iloc(from : to-excluded : step)`

+++

Faisons un slicing `[from:to:step]` classique, on ne précise pas `step` qui par défaut vaut 1, et on prend les lignes de l'indice 32 à l'indice 37 et les colonnes de l'indice 3 à l'indice 5.

Attention, comme c'est `iloc`, à nouveau ce sont des **indices** donc à partir de 0. Pour les lignes, la première ligne est de numéro 0 donc d'indice 0 mais elle est d'index 1 puisque les lignes sont indexées (labellisées) par les valeurs de la colonne `PassengerId` qui commencent à 1.

Ainsi on nous donne les entrées d'index 33 à 37 et les colonnes `Name` et `Sex`. On voit que les bornes supérieures du slicing sont exclues comme dans le slicing classique Python.

```{code-cell} ipython3
df.iloc[32:37, 3:5]
```

Et vous remarquez que `iloc` s'utilise vraiment comme le slicing en `numpy`: les lignes sont indiquées en premier !

+++

Aucun problème pour modifier ! Un exemple stupide, je mets toutes ces valeurs à "Hello !".

```{code-cell} ipython3
df_copy.iloc[32:37, 3:5] = "Hello !"
```

On le vérifie.

```{code-cell} ipython3
df_copy.iloc[32:37, 3:5]
```

Supposons que je veuille utiliser `iloc` pour prendre une référence sur (toutes les colonnes de) la ligne d'indice 4.

```{code-cell} ipython3
df.iloc[4]
```

Maintenant, si dans l'autre sens nous voulons prendre (toutes les lignes de) la première colonne, il va falloir préciser les lignes, et comme on les prend toutes on va utiliser le '::' ou son raccourci le simple ':'

```{code-cell} ipython3
:cell_style: split

# pour désigner toutes les lignes
df.iloc[::, 0]
```

```{code-cell} ipython3
:cell_style: split

# ou encore + simple
df.iloc[:, 0]
```

### accés et modifications par localisation d'index

+++

Vous allez accéder à une sous-partie d'une dataframe en utilisant `pandas.DataFrame.loc`, au travers cette fois des index.

+++

Alors voilà, il va y avoir une surprise ! Vous n'êtes plus dans le slicing à-la-Python ! On va voir si vous vous en apercevez.

+++

Prenons, comme dans l'exemple précédent  
* les lignes de l'index 33 (indice 32) à l'index 38 (indice 37)
* et les colonnes de l'index 'Name' (indice 3) à l'index 'Age' (indice 5).

```{code-cell} ipython3
df.loc[33:38, 'Name':'Age']
```

Voyez vous, la grande différence entre `loc` et `iloc` quand on leur passe une slice de la forme `from:to` ... oui c'est que l'index supérieur (le `to`) est **inclus**, on se retrouve avec une ligne et une colonne en plus que dans la version avec `iloc`.

Bon ce n'est peut être pas la meilleure idée que `pandas` ait eue mais il faut s'y habituer ... ou utiliser `iloc` !

+++

De même que pour `iloc` on peut modifier.

```{code-cell} ipython3
df_copy.loc[33:38, 'Name':'Age'] = "Hello !"
```

On le vérifie.

```{code-cell} ipython3
df_copy.loc[33:38, 'Name':'Age'] 
```

### accés et modifications par liste d'indices

+++

Nous voulons prendre une référence sur une sous-partie d'une dataframe qui ne s'exprime pas sous la forme d'une slice (tranche) mais nous possédons la liste des (indices des) lignes et des colonnes que nous souhaitons conserver dans ma sous-partie de dataframe.

`pandas` sait parfaitement le faire, il suffit de remplacer les slices par les listes (et de plus, vous donnez les indices dans l'ordre qui vous intéresse):

Prenons ainsi par exemple 
* les lignes d'indice 450, 3, 67, 800 et 678
* et les colonnes d'indice 3, 2, 9 et 1.  

Et comme ce sont des indices, nous utilisons `iloc`.

```{code-cell} ipython3
# c'est facile de créer une sélection de lignes et de colonnes 
df.iloc[[450, 3, 67, 800, 678], [3, 2, 9, 1]]
```

On peut faire exactement la même chose avec `loc`, mais bien sûr en lui passant des index et non des indices, à ce stade vous devez avoir compris l'idée générale…

```{code-cell} ipython3
# la même sélction mais en utilisant les index
df_copy.loc[[451, 4, 68, 801, 679], ['Name', 'Pclass', 'Fare', 'Survived']]
```

### accés et modification par tableaux de booléens

+++

Nous avons vu dans le notebook précédent que nous pouvions faire des tests sur toutes les valeurs d'une colonne et que cela nous rendait un tableau de booléens.

Et bien la dernière manière d'accéder à des sous-parties de dataframe, va être l'accés par tableau de booléens i.e. on va isoler de la dataframe les lignes où la valeur du booléen est vraie.

Par exemple, prenons la colonne `Age`, localisons les personnes dont l'âge est supérieur ou égal à 70 ans, et isolons ces personnes dans une dataframe.

```{code-cell} ipython3
df.loc[ df['Age'] >= 70 ]
```

Nous pouvons mettre plusieurs conditions, nous voulons les personnes qui ne sont pas en première classe et dont l'age est supérieur à 70 ans.

Mais comment écrire ces conditions ...

```{code-cell} ipython3
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
df.loc [ np.logical_and(df['Age'] >= 70, np.logical_not(df['Pclass'] == 1)) ] # bof ...
```

```{code-cell} ipython3
df.loc [ (df['Age'] >= 70) & (~ (df['Pclass'] == 1)) ] # ahhh
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
df['Survived'][1]
```

Maintenant LA question. Je viens d'accéder à un élément de la colonne `Survived`, puis-je utiliser cette manière d'accéder pour modifier l'élément ?

Donc *Puis-je ressusciter le pauvre passager d'index 1 en faisant passer son état de survie à 1 par l'affectation `df['Survived'][1] = 1`

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
