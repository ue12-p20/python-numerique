---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="../media/ensmp-25-alpha.png" /></span>
</div>


# Python et le numérique avec `numpy`


## contextualisons un peu Python et le numérique


Alors maintenant vous avez des rudiments du langage de programmation Python, que ce soit grâce à vos années de prépa ou à l'introduction (rapide) que nous venons de faire ou pour toute autre raison.

Ce langage est plutôt élégant, simple à utiliser, il comporte tout un tas de structures de base pour ranger des données: dictionnaires, ensembles, listes, tuples ... et les fonctions afférantes pour les manipuler.

```python
l = [124, 1, 45, 67, 23, -17, 90, 45, -65]
l.sort()
print(l)
```

La liste ressort triée, c'est beau ! Tout ceci est top: vous allez pouvoir réaliser les super TP de math1 et de data science en math2.


Qui dit data science dit données, jusque là vous nous suivez. Toutes ces données il va donc falloir les stocker dans des programmes écrits en Python, pour les manipuler.

Si vous avez une grande, voire une très grande, quantité de données, il serait judicieux:
   1. que leur stockage soit bien optimisé en espace mémoire et en temps d'accès à cet espace mémoire
   1. que les calculs soient simples à appliquer et s'exécutent le plus rapide possible.

Nous sommes tous d'accord.


Alors ces données quelle forme vont-elles prendre ? Vous allez avoir des matrices, des tables décrivant des individus, des séries de mesurse temporelles, des images ... on regarde des exemples ?


### un exemple de matrice


Vous avez là une très jolie matrice (4 x 5) et sa transposée (5 x 4).

<img src='media/matrice.png'></img>


Comment pourrions nous représenter cette matrice en Python ? Une idée ? Essayez ? 

```python
# votre code ici (ne regardez pas dessous)
```

En voici une solution sous la forme d'un tuple de tuples:

```python
matrice = (
    (1, 2, 3, 4, 5), 
    (6, 7, 8, 9, 10),
    (11, 12, 13, 14, 15),
    (16, 17, 18, 19, 20)
)
```

ou une autre sous la forme d'une liste de listes

```python
matrice = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
```

Si nous avions besoin de transposer cette matrice. Naturellement nous serions capable de coder la fonction, mais franchement quand une fonction est à ce point utile, il doit bien exister une version déjà codée par d'autres qui sera de plus sera débuggée, testée par de nombreuses personnes ...  donc sûrement plus fiable que vôtre version.

Premier principe de programmation: être le plus paresseux possible et toujours chercher avant de la coder si la fonction dont vous avez besoin n'existe pas déjà !


### un exemple de table de données


Maintenant un autre exemple de données. Voici ci-dessous la table de passagers du (pourtant *unsinkable*) titanic. Oui oui cette table est disponible en domaine public (comme des tas de données), par exemple, là https://public.opendatasoft.com/explore/dataset/titanic-passengers/table).

Vous voyez en ligne les passages et en colonnes les quelques informations que nous avons sur eux: numéro, survie à l'accident, classe (première, seconde, troisième), nom, genre, age, *SibSp*, *Parch*, ...

heu ... *SibSp* et *Parch* ? Vous ne comprennez pas ce que c'est ? Oui nous sommes bien d'accord, ils auraient quand même pu choisir des noms un peu plus parlants (comme vous le faites sûrement toujours dans vos codes). Des indices ? SiblingsSpouse et ParentChildren. Et pour plus de details regardez là https://www.kaggle.com/c/titanic/data (mais pas pendant le cours).

<img src='media/titanic.png' width="1000"></img>


### un exemple de série temporelle


Cédons là à l'actualité. Voici la courbe des valeurs cumulées du nombre d'infections* au covid en France entre janvier et août. Où trouve-t-on ce genre d'information ? Nous avons pris nos données là https://www.data.gouv.fr/fr/datasets/coronavirus-covid19-evolution-par-pays-et-dans-le-monde-maj-quotidienne/

Vous remarquez dans cette figure les abcisses qui sont des dates.

<img src='media/corona-france.jpg' width="500"></img>


### un exemple d'image


Encore un exemple de données ? Voici une belle photo, d'un endroit que vous allez apprendre à connaître (si on ne confine pas trop souvent ...)

<img src='media/les-mines.jpg' width="500">


### que sont ces données ?


Notre premier problème est de stocker ces données en mémoire afin de leur appliquer des fonctions. Ces données semblent (à première vue) très différentes, mais nous allons souvent vouloir leur appliquer le même genre de fonctions (comme rechercher le passager le plus agé du titanic, les pixels de la couleur la plus foncée, les maxima des lignes de la matrice).

Ces données vous font-elles penser à quelque chose ? oui bien sûr à des tableaux :
   - la matrice est un tableau de taille 5 x 4 (ligne x colonne);
   - la table des passagers du Titanic est un tableau de taille 891 x 8 (ligne x colonne);
   - la série temporelle sera une suite de valeurs indexées par une date;
   - l'image couleur, en codage RGB rouge-vert-bleu, est constituée de trois tables de couleurs primaires de taille 533 x 800 (ligne x colonne) grâce auxquelles votre écran va reconstituer une image en couleur.


Les structures de données de Python sont très bien mais elles ne sont pas du tout adaptées à stocker et manipuler les tableaux de ce genre.

Pour pallier à ce problème, depuis 2006 une librairie numérique appelée `numpy` est développée.

Il a même été proposé au concepteur de Python de l'intégrer dans son langage, comme la structure de données de tableau Python, mais celui-ci a refusé pour des soucis de maintenance de code.


`numpy` est une très bonne librarie numérique de manipulation de tableaux multi-dimensionnels qui, elle, comporte *toutes* les fonctionnalités numériques dont vous avez besoin.  
`numpy` n'est (définitivement) pas très facile à utiliser contrairement à Python, et si elle s'est imposée comme LA librarie numérique incontournable de Python, c'est parce qu'il n'en existe pas (encore) de meilleure, donc c'est naturellement celle-ci que les mines ont choisi de vous apprendre.

`numpy` est donc considérée comme **LA** bibliothèque qui permet d'étendre le langage de programmation Python avec la manipulation de tableaux multidimensionnels.  
C'est une bibliothèque logicielle libre et open source. Elle va vous fournir des tas de fonctions de création et manipulation de tableaux.

`numpy` est la base de SciPy (ScientificPython) qui est un regroupement de bibliothèques Python pour le calcul scientifique.


## apprenons à faire des tableaux `numpy`


Puisque nous allons parler ici de la librarie `numpy`, importons là. Et donnons lui, par convention, son petit-nom `np` qui est son petit-nom standard pour `numpy`: c'est sous ce nom que l'utiliseront la plupart des codes existants.

```python
import numpy as np
```

Maintenant tout ce qui est défini dans `numpy` sera accessible par `np.` - par exemple le type `int64`.

<!-- #region tags=["level_intermediate"] -->
Et ne jamais jamais jamais jamais jamais jamais jamais jamais jamais faire ceci :
```python
from numpy import *
```

Pourquoi ? parce que si vous faites cela, tout ce qui est défini dans `numpy` devient accessible sans préciser `np.` ce qui est le meilleur moyen d'écrire un code:
   1. super difficile à maintenir : puisque vous ne saurez plus dans quelques temps (disons demain matin) d'où proviennent les fonctions que vous utilisez, sachant qu'un code en vraie grandeur va importer des tas de libraries (mais d'où donc vient la fonction `machin_chose` que j'utilise là ?)
   1. comportant des bugs : puisque des fonctions homononymes pouvant exister dans plusieurs libraries, la dernière librarie importée imposera sa version de la fonction...   
<!-- #endregion -->

Maintenant nous allons créer un tableau et regarder les informations qu'il contient.


### le type de donnée `numpy.ndarray`


`numpy` possède donc **un type** de tableau appelé `numpy.ndarray`. Alors effectivement ici `np.ndarray` serait plus juste mais nous allons écrire `numpy.` (et non `np.`) dans nos explications pour plus de clarté.


Voilà le type `numpy.ndarray`:

```python
np.ndarray
```

Ce type est une structure de donnée, qui va comporter toutes les fonctions nous permettant de construire et de manipuler des tableaux multi-dimentionnels. Super, on essaie ça.


### création de notre premier `np.ndarray`


Pour construire un tableau on va avoir besoin naturellement de plusieurs informations:
   - déjà sa forme, disons par exemple que le tableau est une matrice 4 x 5
   - ensuite le type des éléments, disons que cette matrice contient des entiers
   - ensuite des valeurs, disons que cette matrice est celle que nous avons vu en début du notebook


Pour construire un tableau on n'utilise pas directement la fonction de bas niveau (le constructeur) `numpy.ndarray`. D'autres fonctions sont définies pour cela, comme `numpy.array`, `numpy.zeros` et `numpy.empty`.

La première fonction va initialiser ses éléments à partir de tout objet décrivant un tableau, par exemple la liste de listes décrivant la matrice 4 x 5 que nous avons vue auparavant. Comment savons nous tout cela ? Grâce au help sur `numpy.ndarray` ! 

```python
# pour avoir de l'aide dans un notebook,
# le plus simple c'est avec le ? comme ceci
np.array?

# l'évaluation de cette cellule déclenche l'affichage de l'aide
# cliquez sur la croix en haut à droite pour effacer le pop-up
```

Disons que cette fonction peut être vue comme la manière de convertir un tableau Python en une structure de donnée de type `numpy.ndarray`.

```python
mat = np.array(matrice)
```

et voilà à quoi ressemble le résultat

```python
mat
```

Il est super ! Et nous n'avons même pas eu à indiquer ni la forme du tableau, `numpy` l'a déduite de la forme de la liste de listes passée en argument) ni le type des éléments, `numpy` l'a déterminé à partir des valeurs initiales.


Maintenant à vous de jouer. Créer la matrice $\begin{pmatrix} 5.2 & 9 & 2 \\ 6 & 8 & 1 \\ 0 & 3 & -7 \\ -5 & -8 & 7 \end{pmatrix}$. Appelez la `ma_mat`

```python
# votre code ici
```

On peut bien sûr aussi créer un tableau unidimensionnel.

```python
vec = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### le type des éléments d'un tableau `numpy.ndarray`


Alors notre belle matrice `mat` est dans la variable Python `mat` de type `numpy.ndarray`. On va lui demander quel est le type de ses éléments.

```python
mat.dtype
```

Maintenant à vous de jouer. Regardez le type des éléments de votre matrice `ma_mat`.

```python
# votre code ici
```

Bon dans les deux cas `numpy` a vu large ! Il a choisi d'encoder pour `mat` les entiers chacun sur 64 bits et leur permettre d'être négatifs. Et cela pour stocker des nombres tous positifs entre 1 et 20.

Bon alors au cas où, un petit rappel: le plus petit élément de mémoire est le bit (où vous ne pouvez mettre que deux valeurs 1 et 0), la mémoire est exprimée en nombre de bits (vous savez la plus petite mémoire qui ne peut stocker que les deux valeurs 0 et 1) ou en multiples d'octets (un octet ou bytes en anglais c'est 8 bits).


Si nous comptons bien notre tableau occupe en mémoire 4\*5\*8 soit 160 octets. 
Si nous sommes sûrs que nos entiers seront toujours positifs et prendront toujours leurs valeurs entre 0 et 255 compris (vous nous voyez venir ?), de combien d'octets aurons-nous besoin ?

et bien oui il suffira d'avoir des entiers non signés sur 8 bits ! puisque les valeurs iront de `00000000` soit 0 à `11111111` soit 255 ($2^8-1$). Alors ce type s'écrit `numpy.uint8` (*u* pour *u*nsigned).


Alors indiquons donc à `numpy.array` que nous voulons ce type très précis pour nos éléments. Nous faisons cela, grâce au paramètre `dtype` de la fonction `numpy.array`

```python
mat8 = np.array(matrice, dtype=np.uint8) # vous pouvez aussi dire dtype='uint8' mais c'est moins joli 
```

```python
mat8.dtype
```

Combien notre tableau occupe-t-il en mémoire maintenant ?

Alors oui on peut le calculer ... mais en informatique, nous rappelons la première règle de la programmation *être le plus paresseux possible* donc ne pas calculer quelque chose qui existe déjà !

Nous allons donc demander directement à `mat` de nous dire sa taille en octets (1 octet = 8 bits) parce que i) on est sûr qu'il la connait parfaitement et ii) il ne fera pas d'erreur en nous la donnant (comme nous pourrions faire en la calculant).

On utilise pour cela le *champ* de l'objet `mat` (ce n'est pas une fonction, juste un champ à consulter) `numpy.ndarray.nbytes` (bytes=octets)

```python
mat8.nbytes
```

Oui 20 octets 1 par élément !


Maintenant à vous de jouer: Essayer donc de re-construire votre matrice `ma_mat8` en lui imposant le type `uint8` pour ses éléments. Affichez-là.

```python
# votre code ici
```

Vous voyez un problème ? Oui bien sûr ! Ben c'est normal: vous avez demandé que vos éléments soient entre 0 et 255, il vous obéit au doigt et à l'oeil et convertit vos valeurs ! Nous reviendrons là dessus plus tard, mais `numpy` fait en sorte que tous les éléments du tableau aient la même taille quitte à modifier la valeur des éléments pour obéir à cette règle.


A partir de l'objet `numpy.ndarray` on peut accéder à de nombreuses autres informations sur le tableau.


### la taille du tableau et de ses éléments en mémoire


Si on veut connaître le nombre d'éléments du tableau, on utilise le champ `size`

```python
mat.size
```

Si on veut connaître la taille qu'occupe en mémoire (en octets) chaque élément, on utilise `itemsize` 

```python
mat.itemsize
```

Si on veut connaître le nombre d'octets total qu'occupe notre tableau en mémoire (non on ne le calcule pas !), on utilise `nbytes`. C'est redondant ? Peut être mais alors autant utiliser ces accesseurs.

```python
mat.nbytes
```

Maintenant à vous de jouer: consultez la taille, la taille des éléments et le nombre total d'octets de votre matrice `ma_mat` 

```python
# votre code ici
```

### la forme et la dimension du tableau


Si on veut connaître la forme d'un tableau, on utilise ? Oui `shape` !

```python
mat.shape
```

Et enfin, si on veut connaître la dimension du tableau (non on ne la calcule pas avec la longueur de la liste indiquant la forme) ! On utilise `dim`

```python
mat.ndim
```

Maintenant à vous de jouer: Demandez la forme et la dimension de votre `ma_mat`

```python
# votre code ici
```

### on récapitule les méthodes des ndarrays


Un petit tableau pour récapituler les méthodes des `numpy.ndarray`

| les méthodes             | ce qu'elles font                                 |
|--------------------------|--------------------------------------------------|
| `numpy.ndarray.size`     | le nombre d'éléments du tableau                  |
| `numpy.ndarray.itemsize` | la taille en octet d'un élément                  |
| `numpy.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octet |
| `numpy.ndarray.shape`    | la forme du tableau (tuple)                            |
| `numpy.ndarray.ndim`     | le nombre de dimensions du tableau               |
| `numpy.ndarray.dtype`    | le type des éléments                             |


### création d'un tableau de zéros


Il existe une deuxième fonction pour créer des tableaux dont les éléments sont initialisés à 0. Qui s'appelle `numpy.zeros`. Alors là vous allez devoir donner la forme de votre tableau, la fonction ne peut pas la deviner ... comme elle le faisait dans l'exemple précécent.

```python
zorro = np.zeros(shape=(4, 5))
```

```python
zorro
```

Quel est le type choisit par défaut par `numpy` ?

```python
# votre code ici
```

Encore à vous de jouer ! Demandez à la variable `zorro`: le nombre de ses éléments, sa forme, sa dimension, sa taille totale ... 


### création d'un tableau de *rien*


La dernière fonction ne perd pas de temps à initialiser les éléments.

Pourquoi ? Et bien par exemple vous savez que vous allez initialiser ces éléments par la suite. Alors quand votre tableau est très très très grand, mettre inutilement une valeur dans chaque case est une (très) grande perte de temps. Et oui dans le cas du traitement de données, surtout quand on a beaucoup de données, on veut optimiser le temps d'exećution de nos programmes. Vous allez revoir souvent cela par la suite.


Allons-y. Faisons un tableau non-initialisé de taille 3 x 6 et demandons lui comme type des éléments des entiers 64 8 bits signés (par exemple).

```python
rien = np.empty(shape=(3, 6), dtype=np.int8)
```

C'est le moment où vous vous dites, à juste titre, que pourtant ces cases vont exister en mémoire. Oui bien sûr. Donc vous allez pouvoir regarder ce qu'elles contiennent ! Oui tout à fait ! Mais alors que pensez-vous trouver comme valeur dans une case non initialisée ? Ben non pas 0 (sauf si c'est la valeur qui se trouvait dans cette case par hasard). Affichez votre tableau `rien`

```python
rien
```

Et oui vous aurez n'importe quoi comme valeurs, c'est ce qui était déjà en mémoire avant la création du tableau (puisque toute case mémoire - bit - contient soit un 0 soit un 1) , simplement le contenu a été mis dans le type des éléments de votre tableau.


Maintenant que vous avez un appercu des `numpy.ndarray` parlons de la manière dont la mémoire est stockée dans votre ordi.


### on récapitule les fonctions pour créer un ndarray


| les méthodes | ce qu'elles font |
| --------------------------- | --------------------- ---------------------- |
| `numpy.array` | renvoie la version ndarray d'un tableau existant |
| `numpy.empty` | renvoie un ndarray vide i.e. sans initialiser ses éléments |
| `numpy.zeros` | renvoie un ndarray rempli de *0.* (float) |
| `numpy.ones` | renvoie un ndarray rempli de *1.* (float) |
| `numpy.arange` | renvoie un ndarray avec des valeurs régulièrement espacées (step) |
| `numpy.linspace` | renvoie un ndarray avec des valeurs régulièrement espacées (nb points) |
||
| `numpy.random` | renvoie un ndarray initialisé de manière aléatoire |
| `numpy.logspace` | renvoyer des nombres espacés uniformément sur une échelle logarithmique |


## quiz


considérons le tableau `np.array([[1, 2, 3], [ 4, 5, 6]])`
   - quelle est sa forme `(2, 3)` ou `(3, 2)`
   - quelle est la taille de ce tableau `2` ou `6`
   


Qu'obtient-on si on fait:
   - `np.array([256, 257, 258]).astype('uint8')` ? `[256, 257, 258]` ou `[0, 1, 2]`


Que donne la méthode `size` d'un `numpy.ndarray` ?
   - `le nombre d'éléments` ou `la taille du tableau` ou `la taille d'un élément`


## quelques petits exercices


### comparaison des temps de constructions de tableaux initialisés et non


Pour comparer des temps de calcul, nous allons utiliser une fonction (un peu magique) des notebooks qui s'appelle `timeit` et qui va appeler de nombreuses fois le calcul et faire la moyenne des temps d'exécution.

En voici un exemple l'exécution de la cellule suivante vous donnera la moyenne des temps d'exécution d'un certain nombre d'exécution du code *1 + 1* 


Temps calculé sur l'exécution de la ligne:

```python
%timeit 1 + 1
```

Temps calculé sur l'exécution de la cellule:

```python
%%timeit
1 + 1
```

Mon ordi met 6.12 nano-secondes.


Maintenant utiliser ce calcul des temps d'exécution pour comparer:
   1. la création d'un `numpy.ndarray` à partir d'une liste Python comportant 10.000 floats initialisés à 0.
   1. la création d'un `numpy.ndarray` de 10.000 éléments initialisés à 0.
   1. la création d'un `numpy.ndarray` de 10.000 éléments non-initialisés.
   
Pour la version Python créez la liste Python avant de calculer le temps de calcul.   

```python
# vote code ici
```

```python
# votre code ici
```

```python
# votre code ici
```

```python
# votre code ici
```

Qu'en concluez-vous ?


### génération aléatoire avec affichage couleur


La fonction `numpy.random.randint(min, max, size, dtype)` construit un tableau de forme `size` (et non `shape` mais ca s'utilise de la même manière) rempli avec des nombres aléatoires entre min et max compris de type `dtype`. Mais regardez plutôt le help ! ca sera mieux expliqué !

```python
np.random.randint?
```

Construisez une toute petite image RBG de taille 10 x 10 que vous initialisez avec des entiers générés aléatoirement entre 0 et 255 (indiquer le plus petit type entier qui contienne ces nombres). 

Avec la fonction `plt.imshow`  afficher l'image !

Que c'est joli !

```python hide_input=true
# hidden code
import matplotlib.pyplot as plt
import numpy as np
random_image = np.random.randint(0, 255, (10, 10))
plt.imshow(random_image);
```

```python
# à vous de jouer
```

<!-- #region tags=["level_intermediate"] -->
## informations annexes
<!-- #endregion -->

<!-- #region tags=["level_intermediate"] -->
### les entiers sur 8, 16, 32, ... n bits
<!-- #endregion -->

<!-- #region tags=["level_intermediate"] -->
**avec *8* bits**
   - on représente $2^{8}$ valeurs entières
      - si les entiers ne sont pas signés on va de $0$ à $255$
      - si les entiers sont signés on va de $-128$ à $127$
      
      
**avec n bits**
   - on représente $2^n$ valeurs entières
      - entiers signés $\in [ -2^{n-1}$, $2^{n-1}-1]$
      - entiers non signés $\in [0, 2^n-1]$
<!-- #endregion -->

```python

```
