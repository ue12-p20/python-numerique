---
jupyter:
  jupytext:
    cell_metadata_filter: all,-hidden,-heading_collapsed
    notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
    text_representation:
      extension: .md
      format_name: markdown
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  notebookname: les types en numpy
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="../media/ensmp-25-alpha.png" /></span>
</div>


# numpy et la mémoire


| les méthodes             | ce qu'elles font                                 |
|--------------------------|--------------------------------------------------|
| `np.ndarray.size`     | le nombre d'éléments du tableau                  |
| `np.ndarray.itemsize` | la taille en octet d'un élément                  |
| `np.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octet |
| `np.ndarray.shape`    | la forme du tableau (tuple)                            |
| `np.ndarray.ndim`     | le nombre de dimensions du tableau               |
| `np.ndarray.dtype`    | le type des éléments                             |


Reprenons notre matrice du notebook précédent:

```python
import numpy as np
```

```python
matrice = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
mat = np.array(matrice)
mat
```

Nous voyons que la matrice contient 20 éléments:

```python
mat.size
```

Que chaque élément est codé sur 8 octets (64 bits puisque ce sont des `int64`)

```python
mat.itemsize
```

```python
mat.dtype
```

Et que la mémoire qu'occupe la matrice en nombre d'octets est $20 \times 8$

```python
mat.nbytes # byte = otet
```

Nous allons maitenant nous intéresser à la manière dont est représentée cette mémoire dans l'ordinateur lorsque la matrice est créée.


## organisation de la mémoire des tableaux


Si vous lisez le help (en faisant ```help(np.ndarray)```  ou directement  ```np.ndarray?``` dans un notebook), on vous dit que votre `np.ndarray`  est un tableau:
   1. **homogène**
   1. **multidimensionnel**
   1. d'éléments de **taille fixe**
   1. et que les tableaux doivent être construits en utilisant les méthodes `np.array`,`np.zeros` ou `np.empty`


Que les tableaux soient **multidimensionnel**s ça ne nous étonne pas trop: ils sont fait pour cela.

Mais ensuite vous avez là tous les ingrédients qui vont permettre à `numpy` d'être aussi rapide.

Les tableaux sont **homogènes** (vous avez commencé à vous en rendre compte avec les tableaux que nous avons construits)  cela signifie que tous leurs éléments sont du même type de données, donc toutes les cases du tableau occupent la même taille en mémoire. Comme dans nos exemples les éléments avaient tous le même type: `np.int64`, `np.float64`, `np.uint8` ... 


Tous les éléments sont de **taille fixe** c'est à dire que vous n'allez pas pouvoir modifier la taille d'éléments d'un tableau `numpy` existant.


Quel est le secret d'un code rapide sur des tableaux ? C'est un code qui passe très rapidement d'un élément du tableau à un autre élément du même tableau.

Comment fait-on cela ? On y arrive si toute la zone mémoire du tableau est crée comme un unique block mémoire. Les cases du tableaux sont contiguëe (continues) en mémoire ! Passer d'une case à une autre, i.e. d'un élément à un autre se fait alors grâce à un simple décalage (offset) et les ordis font ca super super vite !

Beaucoup beaucoup plus rapidement que si les éléments du tableau étaient dissiminés un peu partout dans la mémoire, comme c'est lecas justement pour les listes Python.

<!-- #region tags=["level_intermediate"] -->
Quelques mots sur les listes Python pour ceux qui sont avancés:

Nous dirons que les listes Python sont en fait codées sous la forme de vecteurs (un peu comme des tableaux sauf qu'ils peuvent changer de taille) mais que, comme les éléments sont de type hétérogène, la seule chose que la liste Python peut stocker dans une case du tableau c'est l'adresse de l'élément dans la mémoire. Ainsi pour y aller lire sa valeur, nous n'avons pas un simple offset à faire mais bien une indirection (aller à une adresse en mémoire) et c'est beaucoup beaucoup plus long... cf. NTFS vs ext4 fragmentation
<!-- #endregion -->

Pour illustrer le fait que la taille des éléments est fixe dans un tableau `numpy`, vous allez faire un petit exercice: créer un tableau `numpy` de chaînes de caractères.

On va prendre les jours de la semaine (que nous vous donnons dans une liste Python de chaînes de caractères `str`).

Regardez le type que `numpy` a choisi comme type pour les éléments. Rappelez-vous tous les éléments vont-être du même type ! Donc toutes les chaînes de caractères vont avoir le même type.

```python
les_jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
type(les_jours[0])
```

```python
# votre code ici (correction ci-dessous, ne pas regarder tout de suite !)
```

```python
semaine = np.array(les_jours)
semaine.dtype
```

Alors le plus petit type de donné que `numpy` a trouvé pour ce tableau est *'<U8'* mais qu'est-ce que va peut bien pouvoir dire ?

Oublions *'<'* pour l'instant. Déjà *U* signifie ...  une idée ? oui *Unicode*. Ouf on en a un.

Et bien pourquoi 8 ? Une idée ? ... une chaîne de caractères contient un certain nombre de caractères ... vous me suivez ? quel est le nombre de caractères minimum qui nous permet d'écrire chacun des jours de la semaine ? Bingo c'est 8.

Et si vous essayiez de remplacer un des jours du tableau par une chaîne de caractères qui comporte plus de 8 caractères ? Que va-t-il se passer ? Oui `numpy` ne va bien sûr retenir (stocker) que les 8 premiers caractères du nouveau nom ... (taille fixe on vous a dit !)

```python
semaine[0] = 'lundi en plus long'
```

```python
semaine
```

Au passage vous venez de voir comment on accède à un élément d'un `np.ndarray` oui là c'est de dimension 1 donc on n'a qu'un seul index à donner !


Pour les super curieux rapides et les avancés (les autres peuvent passer ou y revenir par la suite). Que signifie *<*  ?

Ca veut dire *little endian* ! Pour expliquer rapidement: ca indique dans quel ordre sont pris (lus) les octets dans lesquels sont stockés nos objets informatique. Par exemple, un entier 64 bits est codé sur 8 octets, et on se demande dans quel ordre l'ordi va considérer ces octets: ceux de poids fort avant ou ceux de poids faible avant.

Poids fort et poids faible ?  expliquons par analogie avec notre numérotation classique: quand vous écrivez 42, 4 est le poids fort (les dizaines) et 2 le poids faible.

Bref *'<8'* dit: poids faible en premier (donc 24 pour notre 42 habituel).

```python
2**8
```

Maintenant essayez de créer un tableau `np.ndarray` à partir d'une liste Python avec des éléments numériques de différents types. Mettez les entiers 127 et 128, le flottant `np.pi` (oui pour vous `np.pi` puisque vous avez importé `numpy` avec son petit nom et les booléens python True et False.

```python
l = 127, 128, np.pi, True, False, 127 # quel est le type de l ? 
```

```python
# votre code ici
```

Nous commencions à nous y attendre tout a été mis sous la forme de flottants 64 bits ! les entiers sont *127.* et *128.*, `False` est *0.* et `True` est *1.*


Essayez maintenant de créer un tableau `np.ndarray` à partir de la même liste en inposant lors de la création que le type soit un `np.int8`


Combien vaut 128 en entier signé sur 8 bits ? Bizarre n'est-il pas ! mais tout à fait normal ...


Maintenant rajouter une chaîne de caractère dans la liste et créer un tableau sans donner de type puis en donnant le type `np.int16`

```python
l = [127, 128, np.pi, True, False, 127, 'bonjour'] # trouvez l'intru...
```

```python
# votre code ici (sans type)
```

Qu'avez vous obtenu ? Oui tous les éléments ont été transformés en chaînes de caractères ... seul type commun

```python
# votre code ici avec le type
```

Qu'avez-vous eu ? Oui une erreur `ValueError` lorsque `numpy` a essayé de convertir 'bonjour' en un entier ... bon il arrive à faire les conversions évidentes et là il n'en trouve pas !


Il existe des types prédéfinis, regardez là: https://docs.scipy.org/doc/numpy/user/basics.types.html).

Ce qu'il faut en retenir :

* vous pouvez choisir entre `bool`, `int`, `uint` (entier non signé), `float` et `complex` ;
* ces types ont diverses tailles pour vous permettre d'optimiser la mémoire réellement utilisée ;
* ces types existent en tant que tels (hors de tableaux).


### organisation de la forme des tableaux


Vous savez désormais que la mémoire qui stocke le tableau est un segment unidimensionnel continu de cases du même type.

Mais vous avez aussi vu que cette mémoire va être organisée (on dit qu'on va l'indexer) pour lui donner la forme d'un tableau numti-dimensionnel représenté par une liste de dimensions (..., m, n, l, c), donc votre segment unidimensionnel continu fera $... \times m \times n \times l \times c$ cases de long. Chaque case étant de la taille mémoire suffisante pour stocker le type demandé pour les éléments, par exemple 64 bits.

Dans cette multi-indexation, les deux dernières dimensions sont les *lignes* et les *colonnes* d'un tableau en dimension 2 (comme une matrice). Par exemple notre matrice (4, 5) ou notre table du titanic (891, 8).

Ensuite on augmente ls dimension, $n$ serait un nombre de *matrices* comme prendre 2 matrices de 3 lignes et 4 colonnes serait une dimension (2, 3, 4) et ainsi de suite...


Pour les avancés ou les curieux, dans l'exemple de l'image en couleur (avec l'encodage RGB), on voit que la dimension de l'image est (530, 800, 3). C'est à dire que l'image et présentée comme 530 matrices de 800 lignes et 3 colonnes et non pas 3 matrices de 533 lignes et 800 colonnes ! Comme on s'y attendait (peut être)

Pourquoi ? Parce qu'en fait une image est plutôt vue comme une unique matrice où chaque élément (donc chaque pixel de l'image) a trois valeurs une pour chacune des couleurs primaires. Donc on va plutôt la voir comme 530 fois 800 fois 3, puisqu'il est préférable de rapprocher les 3 valeurs RGB de chaque pixel pour les calculs.


Maintenant créons un segment de, par exemple, 30 éléments. Et ne donnons pas de forme, juste la taille. On en profite pour montrer une nouvelle fonction qui fait des tableaux de 1, la bien-nommée `np.ones`. Heu non y'a pas `np.twos` ... `np.threes` ? non plus

Pourquoi avoir une fonction dédiée aux tableaux de 1 ? Parce que cela vous permet de créer très rapidement un tableau où tous les éléments ont la même valeur, il suffit de multiplier un tableau de 1 de la bonne forme par votre valeur, on y reviendra ... mais vous pouvez déjà essayer `np.ones(shape=30)*np.pi`, oh les 30 beaux $\pi$ !

```python
seg = np.ones(shape=30)
```

Quel est le type des éléments ? Une idée ? En bien si vous n'indiquez pas le type des éléments à ce genre de fonctions (comme `np.zeros`, `np.empty`, `np.ones`), elles prennent par défaut le type flottants sur 64 bits. Nous le vérifions:

```python
seg.dtype
```

Donc nous voici avec un tableau dont la taille initiale est la suivante:

```python
seg.shape
```

Et dont la dimension est la suivante:

```python
seg.ndim
```

Disons que cette forme est celle d'un vecteur *ligne*. Dans ce cas on n'a donc besoin que d'un seul index pour parcourir ce tableau (si on voulait le parcourir).

Et si nous voulions que ce tableau de 30 cases prenne une nouvelle forme: on ne veut plus le considérer comme un vecteur ligne mais comme, par exemple, une matrice avec 3 lignes et 10 colonnes ?

On a bien le même nombre d'éléments (30) dans les deux formes, simplement dans la seconde forme, on est en dimension 2. C'est à dire qu'on aura besoin de deux index (un pour les lignes et un pour les colonnes) pour parcourir notre matrice (si on voulait la parcourir). 


Et bien `np.ndarray` comporte deux fonctions pour ré-indexer notre mémoire unidimensionnelle sous-jacente. Ces fonctions sont `np.ndarray.reshape` et `np.ndarray.resize`.

Elles s'appliquent toutes les deux aux objets de type `np.ndarray` (ce sont des méthodes du type `np.ndarray`).

Quelle est leur différence ? Essayez de regarder leur help. Alors ? La voyez-vous ?

Le help de `np.ndarray.resize` vous dit "*Change shape and size of array in-place*". **in-place** signifie dans l'objet auquel la fonction est appliquée alors que le help de `np.ndarray.reshape` vous dit "*Returns an array containing the same data with a new shape.*" elle renvoie une nouvelle forme de notre tableau tout en gardant (comme resize) les données (c'est à dire la mémoire sous-jacente).

Leur similitude ? Aucune des deux ne crée de nouveau `np.ndarray`, elle en modifient uniquement la forme, c'est à dire la manière dont le segment unidimensionnel est considéré.


Naturellement la taille du tableau initial doit correspondre à la taille du tableau re-structuré.


Pour les curieux et les avancés, nous dirons que les méthodes pour modifier la forme d'un tableau le feront sous la forme d'une vue sans copie du tableau initial, mais qu'il peut exister des cas où ce n'est pas le cas.


On le fait avec resize:

```python
seg.resize((3, 10)) # vous voyez que l'application de la fonction resize à seg ne renvoie rien et modifie seg
```

On vérifie sa forme et sa dimension:

```python
seg.shape
```

```python
seg.ndim
```

Ou plus simplement on l'affiche. On voit bien les 3 lignes de 10 éléments.

```python
seg
```

On le fait avec reshape qui sera plus simple d'utilisation puisqu'il ne nécessitera qu'une ligne de code:

```python
seg = np.ones(shape=30).reshape(3, 10) # vous voyez que reshape renvoie 
                                       # un nouvel objet avec une nouvelle forme
seg
```

Parlons un peu de ce qu'on a appelé précédemment décalages ou offsets pour les relier à notre problème de forme.

Dans le cas de la matrice 3 x 10. Si je suis sur l'élément en début d'une ligne, pour passer directement à l'élément en début de la ligne suivante, combien me faudra-t-il *sauter*  d'éléments ? I.e. de combien me faudra-t-il me décaler sur mon segment unidimensionnel sous-jacent ? Oui il faudra "sauter" 10 éléments et 10, on le connait ce chiffre ! c'est la valeur de la deuxième dimension de notre forme.

DESSIN (il sera fait ultérieurement, si vous en aviez un perso joli, envoyez le nous, nous sommes très intéressés, et naturellement il vous sera *copyrighté*)

Et si je voulais passer de l'élément de début d'une colonne à l'élément en début de la colonne suivante ? De combien je dois *sauter* ?  Oui ok 3 ! qui est la taille de la première dimension.

Ah et si je suis en début de la dernière colonne et que je saute 3 éléments ? Et bien je tombe en dehors de la mémoire qui m'a été attribuée et là c'est pas bon du tout du tout du tout du tout ! Vous allez vous attirer les foudres de l'ordi en essayant d'aller dans un segment (une zone mémoire) qui n'est pas à vous ! mais heureusement avant d'en arriver là `numpy` va vérifier que vous restez dans les bornes et vous indiquera que vous en sortez avec une erreur !

DESSIN


À vous de jouer: transformez votre `seg` en 2 matrices de 5 lignes et 3 colonnes:

```python
# votre code ici
```

### on change le type d'un tableau


Comme vous l'avez compris, `np.ndarray` va toujours faire en sorte que i) tous les éléments d'un tableau aient le même type à la création du tableau et ii) que les éléments restent de ce type quoi qu'on leur fasse subir.

Mais alors comment pouvons-nous "modifier" le type des éléments d'un tableau ? Donc on ne peut pas (on vous a dit) mais on va pouvoir créer un nouveau tableau avec la même forme dont les éléments sont du nouveau type et on recopie les éléments dedans ... rassurez-vous il existe une fonction pour cela ! Elle s'appelle `np.ndarray.astype`. 


Allons y: créons un tableau `np.ndarray`  à partir d'une liste de flottants et faisons-en un tableau d'entiers.

```python
l = [-2.7, 8.45, -0.89, 1.56, -67 ]
```

```python
tab1 = np.array(l)
```

On appelle la fonction `np.ndarray.astype` avec le type `np.int32` sur notre tableau de flottants

```python
tab1.astype(np.int)
```

On remarque que la fonction `astype` retourne un tableau. Regardons `tab1`

```python
tab1
```

On remarque que `tab1`  n'a pas été modifié ! on s'y attendait: la taille des éléments est fixe. Donc `astype` construit bien un nouveau tableau qu'on aurait pu garder dans une variable comme `tab2`


On remarque que les flottants pour devenir des entiers ont été modifiés fortement, on a perdu de l'information cette conversion est appelée *unsafe* i.e. *non sûre*.

C'est peut être ce que vous vouliez mais au cas où vous voulez interdire ce genre de conversions (casting) ... la fonction possède un paramètre qui interdit la création du nouveau tableau si la conversion n'est pas *safe*: 

```python tags=["raises-exception"]
tab1.astype(np.int, casting='safe')
```

Oui cela va se faire par la génération d'une erreur (laquelle ? comme on parle de *type* ca sera une `TypeError`). `numpy` veut prévenir le programmeur de cette tentative de conversion interdite en arrêtant le programme. On doit la rattrapper si on veut continuer ...

```python
try:
    tab1.astype(np.int, casting='safe')
except TypeError as e:
    print("pas content ! ")
```

## valeurs régulièrement espacées


Afin de simplifier les codes, `numpy` fournit des fonctions qui vont générer des points espacés régulièrement sur un intervalle que nous spécifions. On pourra ensuite appliquer des fonctions à ces points.

Il existe pour cela deux fonctions: `np.arange` et `np.linspace`. Pour `arange` vous indiquer l'incrément entre deux valeurs successives (le pas `step`) et pour `linspace` vous donnez le nombre de points.


#### la fonction `np.arange`


La fonction `np.arange(from-included, to-excluded, step)` renvoie des nombres distants de la valeur `step` sur l'intervalle spécifié dans lequel seule la borne inférieure est incluse.

Le help vous dit de ne pas utiliser un incrément non entier, le résultat peut être non consistent, préférez pour cela `np.linspace`.

```python
np.arange(0, 10, 2)
```

Par défaut le permier point sera 0 et l'incrément 1

```python
np.arange(10)
```

On peut bien sûr aller dans l'autre sens.

```python
np.arange(10, 0, -1)
```

Les bornes peuvent être des nombre réels.

```python
np.arange(0.2, 10.3, 2)
```

On peut préciser les arguments positionnels `start`, `stop` et `step`:

```python
np.arange(start=1, stop=10, step=1) # attention stop n'est pas inclus
```

```python
np.arange(start=1, stop=-10, step=-1) # stop n'est toujours pas inclus
```

Et si c'est *absurde*  il va vous donner un tableau vide, ca paraît bien:

```python
np.arange(start=1, stop=-10)
```

Pour les avancés et les très curieux, oui parfois `np.arange` peut vous retourner des tableaux bizarrement initialisés lorsque vous lui préciser des arguments positionnels ... essayez donc de ne lui passer uniquement `start=10` ... ah oui bizarre n'est-il pas ?

la raison ? demandez donc à stackoverflow (actuellement les meilleurs en réponses sur les problèmes de code tout langage - bon ils parlent anglais et oui il va falloir vous y faire de mener vos recherches sur l'informatique sur Internet en anglais)


#### la fonction `np.linspace`


La fonction `np.linspace(from-included, to-included, number)` crée des valeurs flottantes régulièrement espacés dans un intervalle. Vous lui fournissez l'intervalle, dont les deux extrèmes seront inclus dans le tableau, et le nombre de points et `numpy` nous crée un `np.ndarray` avec les bonnes valeurs et le bon type.

Notons la différence avec le `np.arange` dont la valeur supérieure de l'intervalle n'est pas incluse dans le tableau.


Voyons la fonction `np.linspace`. On va créer un tableau qui part de $-\pi$, va jusqu'à $\pi$ et comporte 30 points.

```python
x = np.linspace(-np.pi, np.pi, 30)
```

```python
x
```

```python
x.shape
```

On vérifie l'inclusion des deux bornes.

```python
x[0], x[-1]
```

Quel est le type de ses éléments ?

```python
# votre code ici
```

A quoi cela peut-il bien servir ? Voyons rapidement un exemple, calculons et affichons un beau sinus entre $0$ et $2\pi$.

```python
import matplotlib.pyplot as plt # une librarie graphique (on la verra)
# on demande ensuite à ce que les dessins soient inclus dans le notebook
%matplotlib inline
```
```python
x = np.linspace(0, 2*np.pi, 100)
plt.plot(np.sin(x)); # regardez comment on applique la fonction np.sin à tout x d'un coup ! (on y reviendra bien sûr)
```




## quiz


considérons le tableau `np.array([[1, 2, 3], [ 4, 5, 6]])`
   - quel est le type de ses éléments (sur un ordi récent) ? `int8`, `int32` ou `int64` 


Qu'obtient-on si on fait:
   - `np.arange(1, 3)` ? `[1, 2, 3]` ou `[1, 2]` 
   - `np.arange(1, 5, -1)` ? `[5, 4, 3, 2]` ou `[]` 
   - `np.arange(3, 1, -1)` ? `[3, 2]` ou `[3, 2, 1]` 


Qu'obtient-on si on fait:
   - `np.linspace(1, 3, 3)` ? `[1., 2., 3.]` ou `[1, 2]`)
   - `np.linspace(1, 2, 5)` ? `[1., 1.25, 1.5, 1.75, 2.]` ou `[1., 1.2, 1.4, 1.6, 1.8, 2.]`


Que vaut `d` si on fait:
   - `d = np.array(['un', 'deux', 'trois'])`
   - `d[0] = 'quatre'`
   
Est-ce  `['quatre', 'deux', 'trois']` ? `oui` ou `non`


Qu'est-ce la méthode `itemsize` d'un `np.ndarray` ?
   - `le nombre d'éléments` ou `la taille du tableau` ou `la taille d'un élément`


## Exercices


### comparaison des tailles mémoire d'une liste Python et d'un `ndarray`


Utiliser la fonction `getsizeof` de la librarie `sys` de Python pour afficher la taille d'une liste Python de 1.000 entiers initialisés de 0 à 999 et d'un ndarray de la même série de nombres.

```python
# votre code ici
```

```python
# votre code ici
```

Que constatez-vous ?
