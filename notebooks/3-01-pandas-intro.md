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

# UE12 - pandas et matplotlib

+++

Où on découvre les deux dernière bibliothèques socles de l'écosystème Python :

* `pandas` pour la data-science (importation et mise en forme de données)
* `matplotlib` pour la visualisation de données, en abrégé *dataviz*

+++

Et nous commençons par étudier les bases de `pandas`

+++

## contextualisons Python et les tables de données

+++

Nous venons de voir quelques fonctions de base de la librairie numérique de Python `numpy`. Nous savons désormais faires des manipulations simples de tableaux `np.ndarray` qui sont des tableaux multidimensionnels, homogènes, d'éléments de taille fixe.

Revenons à notre introduction à `numpy` où nous avons vu différents styles de tableaux, la matrice que nous avons déjà bien manipulée dans les notebooks précédents, l'image que nous ne traiterons pas plus en avant dans ces cours introductifs, la série temporelle que nous verrons plus loin ... attardons-nous sur les tables d'informations comme celle de 891 naufragés du Titanic, nous la montrons à nouveau:

<img src='media/titanic.png' width="1000"></img>

+++

En ligne vous avez toute une série d'observations, une par ligne (ici les passagers du Titanic), et en colonne vous avez les 12 informations que nous savons d'eux, comme leur nom, leur âge, leur genre, leur classe de cabine, si ils ont survécu ... quand on regarde la table chaque information forme une colonne.

Ce genre de tables sera très fréquent en data-science.

Pour les stocker en mémoire, vous pensez à un type particulièrement utile que nous venons de voir dans une librairie numérique ... mais oui bien sûr un `np.ndarray` de dimension 2 et de forme (891, 12) !

+++

Voilà nous savons quel va être le type de ces tables. Mais bien sûr, vous n'allez pas entrer ces tables *à-la-main* dans votre code (comme on l'a fait parfois pour nos matrices !) ces tables seront déjà décrites dans un fichier que vous allez simplement lire afin que son contenu soit transformé en une structure de données Python.

Quel est le format le plus simple pour ces tables dans un fichier ? Il suffit de mettre chaque observation sur une ligne et, dans les lignes, de séparer chaque information par un caractère choisi, toujours le même.

C'est ce qui a été fait: ces tables sont décrites dans des fichiers de type *csv* pour *comma-separated-values*, littéralement des *valeurs séparées par des virgules*. Ces fichiers porteront l'extension *.csv* ainsi la description de notre fichier de données du titanic a pour nom `titanic.csv` ! Gardons-le !

```{code-cell} ipython3
file = 'titanic.csv'
```

Regardons le début de la table du Titanic:

```
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S
.../...
```

+++

Vous remarquez que les champs sont bien séparés par des `,` et que la première ligne contient le nom des colonnes. Deux questions se posent:

   - *Les champs peuvent-ils être séparés par un autre caractère que la virgule dans un fichier csv ?*

   Oui vous pouvez mettre le caractère que vous voulez pour séparer les champs dans un *csv*: le tout est de bien l'indiquer lors de la lecture de la table (la fonction de lecture ne pourra pas le deviner). Par exemple le `;` qui apparaîtra souvent. Quel que soit le caractère qui sépare ses champs, un fichier portera toujours l'extension *.csv* qui est l'extension standard pour ce genre de table.
   
   
   - *Trouve-t-on toujours les noms des colonnes en première ligne des fichiers *.csv* ?*
   
   Non ce n'est pas obligatoire ! Certains fichiers ne comporteront pas d'entête, certains fichiers auront des lignes de commentaires en début de fichier  ... oui vous commencez à vous dire qu'il va falloir bien indiquer tout cela lors de la lecture du fichier (la fonction de lecture ne pourra pas le deviner).

+++ {"tags": ["level_intermediate"]}

Uniquement pour les avancés, deux autres remarques:

Certains champs - comme `"Braund, Mr. Owen Harris"` - sont mis dans des chaînes entre `""` et les autres champs non. Pourquoi ? Est-ce parce qu'il y a des espaces ? Non, une fonction sait prendre tous les caractères entre deux `,` ... heu ... tous ? non ! pas le séparateur lui-même (ici la `,`), bien sûr ! Les champs qui contiennent le séparateur doivent du coup être protégés, c'est le propos de ces `""`.
   
   
Une dernière chose ? oui il n'y a PAS d'espace autour des virgules ... pourquoi ? et bien parce que ce n'est pas un caractère séparateur mais un vrai caractère, et il sera pris dans le champ ! Et si on avait mis des espace après les séparateurs (comme on le fait quand on écrit) ?
   
```
1 ,0 ,3 ,"Braund, Mr. Owen Harris",male ,22 ,1 ,0 ,A/5 21171 ,7.25 , ,S\
```
   
Là monsieur "Braund, Mr. Owen Harris" aura pour `PassengerId` le nombre 1 suivi d'un espace ("1 ") quel drôle de nombre, la fonction qui va le traiter pourra-t-elle y voir un nombre ? sûrement pas, elle verra une chaîne de caractères contenant un 1 et un espace. 

Bien sûr il va exister des (tas de) paramètres pour régler ce genre de petits problèmes, là ce sera `skipinitialspace` qui est à `False` par défaut et que donc vous passerez avec la valeur `True` pour *Skip spaces after delimiter*.

+++

Un constat: `numpy` ne comporte pas de fonction pour lire ces tables !

Ce rôle est pris depuis 2008 par une autre librairie qui s'appelle `pandas` et qui repose entièrement sur `numpy`: toutes les données que vous allez manipuler en `pandas` sont des tableaux `np.ndarray`.

`pandas` va vous en faciliter l'utilisation en leur donnant un type évolué de table de données `pandas.DataFrame`. Un autre type permettra de gérer les séries le `pandas.Series`.

+++

Une dernière chose à préciser, si le langage Python favorise la simplicité, l'uniformité et la lisibilité du code sur son efficacité ... et bien disons que `pandas` comme `numpy` ... non, ils ne font pas exactement le contraire ... mais disons qu'ils favorisent très clairement l'efficacité au détriment du reste. Ou dit plus simplement: "*Ne vous attendez pas au même niveau de maturité et de cohérence dans `numpy` et `pandas` que celui que vous avez dans Python*"

Ils n'ont pas trouvé leur *BDFL* comme Python avec Guido van Rossum.

+++

## lisons une table de données (`pandas.read_csv`)

+++

Sans plus attendre on importe la librairie `pandas` (son petit nom standard est `pd`) et on lit notre table du titanic dans une variable `df` (pour dataframe, c'est un nom très couramment utilisé)! Avec quelle fonction lisons-nous le fichier ? Avec la fonction `pandas.read_csv` !

+++

Vous n'avez pas `pandas` ? Qu'à cela ne tienne ! Importez-le à partir d'un terminal (ou du notebook si vous savez le faire).
```
pip install pandas
```

```{code-cell} ipython3
import pandas as pd
```

+++ {"tags": ["level_intermediate"]}

Pour les avancés, les nouveautés des différentes versions sorties (releases) sont ici https://pandas.pydata.org/docs/whatsnew/index.html. Si nous voulons savoir le numéro de version d'une librairie, il faut regarder l'attribut `__version__` de la librairie, donc ici `pandas.__version__` (enfin `pd.__version__`, mais on a choisi de toujours mettre le nom complet de la librairie dans les notebooks).

```{code-cell} ipython3
:tags: [level_intermediate]

pd.__version__
```

Au passage importons donc `numpy` puisque les deux librairies sont très liées ...

```{code-cell} ipython3
import numpy as np
```

Plutôt que de détailler les fonctionnalités de `pandas`, partons d'un exemple existant et lisons la table des passagers du titanic:

```{code-cell} ipython3
df0 = pd.read_csv(file)
```

Regardons les quelques premières lignes (le header) de la table avec la méthode `pandas.DataFrame.head` qui par défaut en affiche 5.

```{code-cell} ipython3
df0.head()
```

Nous remarquons là une chose importante qui va être la clé pour comprendre l'intérêt de `pandas`: les lignes et les colonnes sont **indexées**.

+++

## la notion d'index dans les bases de données

+++

En guise de digression, et pour bien comprendre cette histoire d'index, on va parler d'une notion qui est bien plus ancienne que `pandas`, et qu'on a inventée au départ dans le contexte des bases de données relationnelles.

L'idée tourne toujours autour de cette affaire de recherche dans les listes, qui est très inefficace. C'est comme dans les bibliothèques (à l'époque où elles existaient encore sous une forme physique) : lorsque vous cherchez un livre vous n'allez **pas reparcourir tous les rayons** jusqu'à trouver le livre qui vous intéresse; non, vous allez demander au guichet, où l'on dispose d'un **index** qui vous indique où se trouve le livre; c'est quand même beaucoup plus rapide !

C'est un peu pareil avec les données; imaginez que vous avez des données à propos de 10 millions de personnes; si vous vous **contentez de modéliser ça sous la forme d'une liste** de personnes, il vous faut en moyenne 5 millions d'essais pour localiser quelqu'un. La technique de l'index consiste simplement à trouver une caractéristique qui identifie la personne de manière unique (disons le numéro de sécurité sociale), et à **calculer un index** qui permette un accès rapide - pour ça on utilise une table de hachage, exactement comme avec les dictionnaires Python.

De cette façon, l'opération qui consiste à localiser (les informations concernant) une personne, à partir de son numéro de sécu, peut être en grossière approximation considérée comme en temps constant.

+++

## les tables `pandas` sont indexées

+++

Fort de cette expérience avec les bases de données, `pandas` a choisi d'indexer ses tables, dans les deux directions : ligne et colonne; le travail de `pandas` va consister à rendre les opérations sur ces index les plus efficaces possible
(on pourrait discuter de l'intérêt d'indexer les colonnes qui sont généralement moins nombreuses, disons que ça rend le design plus homogène, et aussi, *qui peut le plus peut le moins*, ça ne nuit pas du tout d'indexer les colonnes)

```{code-cell} ipython3
# revenons à nos moutons
df0.head()
```

Les index apparaissent **en gras** dans la sortie de `head()`, si bien que sur notre exemple, on voit que :

* les **colonnes** ont été **indexées par leur nom**, naturellement,
* et que, comme nous n'avons **rien** précisé **de particulier**, les **lignes** ont, elles, été **indexées par leur indice** i.e. une simple numérotation à partir de 0.

+++

Mais si vous regardez bien le contenu de notre dataframe, il y a là une colonne `PassengerId`; rien qu'avec le nom, on devine que cette colonne contient effectivement un identifiant unique pour chaque passager; (c'est d'ailleurs presque toujours le cas dans les bases de données aussi, vous allez trouver des noms de colonne en `PersonId`, `BookId`, etc...); du coup, ça devient un réflexe que d'utiliser cette colonne-là comme clé pour l'index des lignes; et pour faire ça il suffit de l'indiquer à pandas, comme ceci :

```{code-cell} ipython3
# on charge le même fichier
# on choisit la colonne qui sert d'index

df = pd.read_csv(file, index_col='PassengerId')
```

```{code-cell} ipython3
df.head()
```

On a vu que ce n'était pas indispensable, mais c'est une **bonne pratique** que de choisir comme index une colonne qui puisse jouer ce rôle d'identifiant unique.

+++

## le type d'une table (`pandas.DataFrame`)

+++

Maintenant regardons d'un peu plus près les attributs de cette table.

+++

Nous allons comprendre à travers cette table du Titanic comment sont composées les tables, et quels sont leurs attributs utiles (à notre niveau) et comment les utiliser pour exploiter nos données.

+++ {"tags": ["level_intermediate"]}

Si vous êtes familier de Python, le premier réflexe est d'afficher le type de la table; 
c'est utile de connaitre le type des objets, car c'est le type qui détermine les opérations qu'on a le droit de faire sur ces objets;

```{code-cell} ipython3
:tags: [level_intermediate]

type(df)
```

+++ {"tags": ["level_intermediate"]}

Le type de `df` est `pandas.core.frame.DataFrame`, un nom plus court pour ce type est `pandas.DataFrame`.

+++

## la dimension et la forme de la table (`ndim`, `shape`)

+++

Quelle est la dimension et la forme de cette table ?  
on va retrouver les attributs classiques que nous avions en `numpy` soit `ndim`, `shape`... qui seront là des noms de méthode des dataframes.

```{code-cell} ipython3
# une dataframe est toujours de dimension 2 
df.ndim
```

Notre table est une `pandas.DataFrame` de dimension 2, on s'y attendait.

```{code-cell} ipython3
print(df.shape)
```

Sa forme est 891 lignes et 11 colonnes.

+++

Nous avons dit que `pandas` est fondé sur `numpy`. Donc où `numpy` intervient-il ? Vous l'avez compris bien sûr : il va s'occuper du stockage et de la gestion du tableau de dimension 2 sous-jacent.

Et `pandas` ? il va nous *décorer* ce tableau avec des fonctions très pratiques, et de plus haut-niveau que `numpy`, pour manipuler plus facilement qu'en `numpy` notre table de lignes et de colonnes, de manière à faire du data-science.

+++

## les colonnes de la table

+++

Quels sont les noms des colonnes ?

Ils sont accessibles par la *property* `pandas.DataFrame.columns` qui va vous renvoyer un objet de type ... de type ? oui `Index` ! puisque les noms des colonnes sont les index des colonnes !

```{code-cell} ipython3
df.columns
```

Oui je sais, on voit le type des éléments mais nous parlerons des types après, on ne peut pas tout faire en même temps ! et il va falloir comprendre de petites choses avant.

+++

Qui dit index dit accés, donc nous allons bien pouvoir accéder aux colonnes de la table.

+++

Les colonnes ont un traitement un peu priviligié en `pandas`. En fait une table `pandas` est un peu comme un dictionnaire où les clés sont les noms des colonnes, et où les valeurs sont les colonnes.

Un peu comme un dictionnaire ? la dataframe ? Donc nous pouvons accéder à une colonne par sa clé, par exemple, `Age` ou encore `Name` !

```{code-cell} ipython3
df['Age']
```

C'est bien la colonne des 891 âges. Et là on peut regarder le type des éléments, ce sont des `float64`, pas de problème, les âges ne sont pas toujours des nombres entiers.

Nous allons regarder quel est le type de la structure de donnée de colonnes.

+++

### le type d'une colonne (`pandas.Series`)

+++

Reprenons notre dataframe favorite, des malheureux passagers du Titanic, et regardons le type utilisé par `pandas` pour la structure de donnée de colonne.

```{code-cell} ipython3
type(df['Age'])
```

Voilà, qu'apparaît le second type de `pandas`, celui des `Series` ... Une colonne est une série de données ! Le nom de la colonne est la clé dans un pseudo-dictionnaire pour accéder à cette série de données ! On commence à y voir un peu plus clair !

Je dis pseudo parce que `pandas` accepte que plusieurs colonnes portent le même nom. Et si vous demandez d'aller chercher les colonnes correspondant à cette clé ... il vous les donne toutes.

+++

Que peut-on faire comme calculs sur nos colonnes ? Des tas de choses dont nous allons voir quelques exemples.

+++

### les petites fonctions statistiques sur les colonnes

+++

Que peut-on faire sur une série de valeurs ?

Si les valeurs sont quantitatives (comme l'âge) on peut essayer de mieux décrire cette colonne en calculant des fonctions comme le minimum, la maximun, la moyenne, l'écart-type, les quartiles ...

Appliquons le à la colonne des âges :

```{code-cell} ipython3
df['Age'].describe()
```

Ces calculs sont regroupées dans une méthode appelée `pandas.Series.describe`. On y voit que le plus jeune avait dans les 5 mois et le plus vieux 80, que la moyenne d'âge est de presque 30 ans, que 75% des passagers avaient en dessous de 38 ans.

+++

Si la valeur est qualitatives, ou catégorielle (comme le genre), on peut calculer le nombre des valeurs différentes et les fréquences de chacune de ces valeurs.

```{code-cell} ipython3
df['Sex'].value_counts()
```

Vous remarquez que les fonctions appliquées sont naturellement des fonctions vectorisées.

+++

### programmation vectorielle - conditions sur les éléments d'une colonne

+++

Revenons à l'âge des passagers. Et si je voulais savoir, combien de passager avaient moins de 12 ans ? ou combien avaient plus de 65 ?

+++

Rappelez-vous qu'en `numpy` on fait de la **programmation vectorielle**, i.e. on applique les fonctions à tout un tableau ou à tout un sous-tableau, et non en itérant sur les valeurs avec un for-Python ! et cela par souci d'efficacité !

Il faut faire **pareil en `pandas`**: éviter les itérations sur les données, utiliser les fonctions vectorisées; ainsi l'itération sur les éléments sera faite dans le langage dans lequel sont écrits `numpy` et `pandas`, rapide et proche de la mémoire.

+++

Voici un premier exemple, avec les opérateurs de comparaison: ils s'appliquent à toute la colonne. Ainsi pour les moins de 12 ans je vais écrire simplement

    df['Age'] < 12
    
et avec cette expression, je récupère un tableau de booléens qui me disent pour chaque valeur de la colonne comment elle répond à cette condition; en fait cet expressions va me retourner un objet `Series` (comme une colonne)

Ce tableau contient des `False` et des `True`. Et comment puis-je compter le nombre de résultats `True` qui me donnera le nombre d'enfants ?

+++

On le fait. Alors il va y avoir plusieurs manières. Je peux faire la somme de toutes les réponses (les `True` seront des 1 et les `False` des 0, c'est très pratique les booléens); je peux aussi utiliser la fonction `value_counts`, et il y a sûrement d'autres manières de faire ... On va montrer les deux (essayez de faire *\%timeit* sur les deux lignes de code):

```{code-cell} ipython3
# value_counts marche avec toutes les Series
# pour compter le nombre d'occurrence des
# différentes valeurs trouvées dans la colonne

(df['Age']<12).value_counts()
```

Donc on a 68 passagers de moins de 12 ans dans cette table.

```{code-cell} ipython3
# on peut faire la somme lorsqu'on 
# sait qu'on n'a que des booléens

(df['Age'] < 12).sum()
```

Oui, voilà la même chose calculée différemment.

+++

Est-ce qu'on peut dire qu'il y a *823* passagers de plus de 12 ans (attention piège ...). En fait on ne peut pas le dire en regardant les âges. Pourquoi ? Affichez la table des âges.

```{code-cell} ipython3
df['Age']
```

Effectivement on remarque que le passager 889 à un âge un peu particulier qui est *NaN* ! Allons-y voir de plus prés ! Quel est donc cet étrange `Age` et son type ?

+++

## les valeurs manquantes, NA (non-available) ou NaN (not-a-number)

+++

Donc nous venons de nous rendre compte que dans la colonne `Age` le passager d'index *889* a un *NaN* et pas un nombre flottant ! Élucidons vite ce mystère !

Affichons cet élément.

```{code-cell} ipython3
df['Age'][889]
```

C'est bien toujours un `nan` (en fait `np.nan`)

+++

Regardons le type de l'élément `nan` ... heu ... `pandas` a dit `float64`, on pourrait peut-être le croire ! oui mais vérifions quand même:

```{code-cell} ipython3
type(df['Age'][889])
```

Oh c'est bien un flottant ! Mais quel est donc de drôle de flottant ? Une idée ?

Et bien c'est le flottant qui signifie *Not A Number* parce que là, tout simplement, cette table ne connait pas l'âge de cette personne et elle l'indique avec cette valeur `nan` de type flottant.

Regardons dans le fichier *csv* comment est indiquée cette absence de valeur ... une idée ?

```
889,0,3,"Johnston, Miss. Catherine Helen ""Carrie""",female,,1,2,W./C. 6607,23.45,,S
```

Alors cette absence de valeur ? ahhh ce sont tout simplement  `,,`  deux virgules qui se suivent avec rien entre elles, pas bête ! Cette valeur est aussi appelée *NA* pour *Not Available*.

+++

Ainsi nous ne connaissons pas l'âge de certains passagers. Pouvons-nous dire combien il nous manque d'informations dans la colonne des âges ?

Pour cela, on peut utiliser (par exemple) la fonction `pandas.Series.notna` qui va nous rendre une colonne de `True` et de `False` et tout simplement - comme pour le test de l'âge inférieur à 12 ans ci-dessus - on va compter les `True` (qui sont donc les passagers pour lesquels la valeur de l'âge est `notna` !).

```{code-cell} ipython3
np.sum(df['Age'].notna())
```

On connait l'âge de 714 passagers.

+++ {"tags": []}

Pour combien de passagers nous manque-t-il l'information d'âge ? On a l'embarras du choix ... 
   - Soit on utilise *714* qu'on retranche au nombre total de passagers (qui est le nombre de lignes ou encore la longueur `len` de la table).
   - Soit on prend la négation de la colonne de booléen (`np.logical_not`) et on compte les `True`.
   - Soit on utilise la fonction `pandas.Series.isna` qui nous renvoie une colonne de `True` et `False` et on compte le nombre de `True`.
   - Soit on utilise `pandas.value_counts` sur le tableau de booléens...
   
je vous montre l'une des plus rapides: compter le nombre de `True` dans la colonne résultant du test.

```{code-cell} ipython3
(df['Age'].isna()).sum()
```

Donc 177 informations sur l'âge sont manquantes.

+++

Si vous voulions faires des opérations booléennes entre les colonnes, il faut utiliser les fonctions dédiées `np.logical_not`, `np.logical_and`, `np.logical_or`...

```{code-cell} ipython3
np.sum(np.logical_not(df['Age'].isna()))
```

Reprenons dans le fichier *csv* la passagère *889*.

```
889,0,3,"Johnston, Miss. Catherine Helen ""Carrie""",female,,1,2,W./C. 6607,23.45,,S
```

+++

On remarque que la valeur de son avant-dernière colonne n'est pas non plus indiquée. Regardons alors quelle est l'avant dernière colonne et accédons à sa série de valeurs. Les colonnes sont données par le champ `columns` et l'indice de l'avant-dernier sera *-2*.

```{code-cell} ipython3
df.columns[-2]
```

Regardons la colonne des `Cabin`.

```{code-cell} ipython3
df['Cabin']
```

Vous remarquez que dans ce cas là aussi, la valeur manquante est undiquée par un *NaN*, avec un type des éléments `object` (on y reviendra plus tard sur les types).

À vous de jouer. Calculez le nombre de valeurs manquantes dans la colonne des numéros des cabines.

```{code-cell} ipython3
# votre code ici
```

Une `pandas.DataFrame` a aussi des lignes, nous allons les voir dans la section suivante...

+++

## les lignes de la table

+++

### index et indice

+++

On a vu que `pandas` tend à favoriser l'utilisation des index.

Il est important avec `pandas` de bien faire la différence entre ***index*** et ***indice*** :

* les **index** peuvent être un peu ce qu'on veut, ici on a des entiers, ça pourrait être aussi bien des **chaines**
* les **indices** sont toujours des **entiers** qui **commencent à 0** (comme les indices de listes et de tableau)

Une autre différence importante, c'est que l'index "appartient" à la ligne, et sera préservé par exemple lors d'un tri ou d'une insertion; alors qu'au contraire bien sûr, les indices eux se retrouvent tout chamboulés

+++

Dans l'état actuel de la dataframe, l'index (qui coincide avec `PassengerId`, et qui commence à 1), est très voisin de l'indice (qui commence toujours à 0). 

Du coup les deux sont très proches, et on risque de s'emmêler; pour rendre les choses plus claires, nous allons trier la table - disons selon les âges des passager.

```{code-cell} ipython3
# on recharge
df = pd.read_csv("titanic.csv").set_index('PassengerId')

# avant de trier: la première ligne a
# son indice = 0 (c'est la premiere)
# son index = 1 (PassengerId)

df.head()
```

```{code-cell} ipython3
# je trie la dataframe (sans faire de copie)
# on reparlera plus longuement des méthodes de tri plus tard

df.sort_values(by='Age', inplace=True)

df.head()
```

Dans cette version triée, la ligne correspondant à Miss Eugenie Baclini a  pour index `645`, et pour indice `2`.

+++

### contenu de l'index

+++

Comment connaître les index des lignes ?

Ils sont accessibles grâce à la méthode `pandas.DataFrame.index`.

```{code-cell} ipython3
# comme pour df.columns, le résultat est un Index

df.index
```

```{code-cell} ipython3
:cell_style: split

# par exemple pour savoir s'il existe 
# dans la table un PassengerId qui vaut 645

645 in df.index
```

```{code-cell} ipython3
:cell_style: split

1000 in df.index
```

+++ {"tags": ["level_advanced"]}

pour les curieux, qui s'interrogeraient sur la relation entre `Index` et `Int64Index` :  

* il se trouve que dans cette dataframe, l'index a des valeurs entières,  
  c'est pourquoi `pandas` a choisi pour lui le type `Int64Index`  
* on peut vérifier que cet objet est bien aussi un `Index` :

```{code-cell} ipython3
:tags: [level_advanced]

# Int64Index est bien une sous-classe de Index

issubclass(pd.Int64Index, pd.Index)
```

```{code-cell} ipython3
:tags: [level_advanced]

# on peut le vérifer aussi comme ceci,
# de manière équivalente

isinstance(df.index, pd.Index)
```

### accéder aux lignes et cellules : utilisez `loc`

+++

La **méthode recommandée** pour accéder à une ligne, (ou à une cellule d'ailleurs, on en reparlera), consiste à **utiliser les index**. 
La philosophie de `pandas`, de façon générale, consiste à **favoriser** les accès par **index** - par opposition aux accès par indices.

+++

Les accès par **index** se font au travers de `loc`; voici comment ça se présente :

```{code-cell} ipython3
# pour accéder à la personne dont le PassengerId est 889

df.loc[889]
```

```{code-cell} ipython3
# remarquez que le résultat est, à nouveau, de type `Series`

type(df.loc[889])
```

La property `loc` permet aussi d'accéder aux cellules :

```{code-cell} ipython3
:cell_style: center

df.loc[889, 'Pclass']
```

***RÉSUMÉ*** pour les accès en lecture

* la forme `df['Age']` fonctionne bien pour **accéder aux colonnes** 
* la forme `df.loc[889]` permet **d'accéder aux lignes**
* pour accéder à une cellule, on utilise
  * `df.loc[889, 'Age']` ou
  * `df['Age'][889]`
* sauf que les deux formes ont **leurs indices renversés**; et de plus l'un utilise une virgule et l'autre des crochets !
  * `df[colonne][ligne]` et   
  * `df.loc[ligne, colonne]`  
  c'est parmi les choses assez confusantes au sujet de pandas

+++

**RÉSUMÉ*** à propos des types

* les tables pandas sont représentées par le type `DataFrame`
* une dataframe a un index pour accéder aux colonnes (`df.columns`)  
  et un index pour accéder aux lignes (`df.index`)  
  ces deux objets sont de type `Index` 
* une colonne, ou une ligne, sont de type `Series` - qui correspond si on veut à des données en 1 seule dimension

+++

### modifier une cellule

+++

***MISE EN GARDE*** 

Pour modifier (écrire dans) une cellule, on pourrait penser écrire du code de ce genre

* ~~`df.loc[889]['Age'] = 10`~~  
  ou encore
* ~~`df['Age'][889] = 10`~~

**il ne faut pas le faire**; 
si vous essayez l'une ou l'autre de ces formes, vous obtenez un gros avertissement (parfois miraculeusement ça marche tout de même, mais c'est accidentel !)

+++

La bonne méthode, je vous engage à en prendre l'habitude, consiste à utiliser cet idiome :

* `df.loc[889, 'Age'] = 10`

+++ {"tags": ["level_intermediate"]}

vous remarquez qu'ici 

* on a indexé l'objet `df.loc` **au travers d'un tuple**  
  (souvenez-vous qu'en Python `889, 'Age'` est un tuple), 
* et **non pas en indexant deux fois**  
  (quand on utilise une des deux formes à éviter  
  on indexe une première fois par `889`  
  puis on indexe le résultat par `'Age'`  
  en anglais on parle de *chained indexing*)

```{code-cell} ipython3
df.loc[889, 'Age'] = 10

# pour vérifier 
df.loc[889]
```

## accès par indices : `iloc` et `iat`

+++

Bien que la plupart du temps on utilise les index pour accéder aux contenus, il se trouve parfois des situations où l'accès par indices peut être ponctuellement intéressant.

Et en fait c'est **très** simple : pour **utiliser des indices** plutôt que des index, il sufit de **remplacer `loc` par `iloc`**

Pour s'en souvenir, on peut se rappeler que le *i* veut dire *integer*, donc indices et non pas index

```{code-cell} ipython3
# le contexte 

df.head()
```

```{code-cell} ipython3
# on va upgrader un passager qui est en 3-ème classe

# ligne d'indice 2 = PassengerId 645
# colonne d'indice 1 = PClass
df.iloc[2, 1]
```

```{code-cell} ipython3
# si vous voulez coder par indices, utilisez iloc 

# regardez la nouvelle valeur de Pclass sur le passager 645
df.iloc[2, 1] = 2
df.head()
```

## exercice

+++

### lecture d'un mini-titanic

+++

Le fichier `petit-titanic.csv` contient les 10 premières lignes de passagers. Saurez-vous déjouer les deux pièges et lire le fichier ? En cas de problème ? Lisez le help ! Sauriez-vous changer l'index des colonnes ?

```{code-cell} ipython3
# rappelez-vous, pour lire le help de read_csv:
pd.read_csv?
```

```{code-cell} ipython3
file = 'petit-titanic.csv'
```

```{code-cell} ipython3
# votre code ici
```

+++ {"tags": []}

some text
* a wrong bullet
