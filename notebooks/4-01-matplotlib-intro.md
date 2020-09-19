---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  cell_metadata_json: true
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: intro à matplotlib
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
<span><img src="media/ensmp-25-alpha.png" /></span>
</div>

+++

# dataviz avec `matplotlib`

+++

Pour vous familiariser avec des données, rien ne remplace naturellement la visualisation !

Nous allons voir rapidement quelques fonctions de visualisation de la librairie `matplotlib.pyplot` (qui s'appelle de manière standard `plt`).

+++

Pour expliquer rapidement la génèse de `matplotlib`, il s'agissait pour ses développeurs (en 2003) de donner une alternative à la visualisation de donnée sous *matlab*, mais dans l'écosystème Python.

Cette librairie reste encore actuellement **la** librairie la plus populaire pour le dataviz en Python, il existe une communauté de développeurs et d'utilisateurs très active. Les autres librairies sont, le plus souvent, dérivées de `matplotlib` c'est donc celle dont nous allons illustrer quelques fonctions de base très utiles.

+++

Pour commencer nous allons dessiner des courbes en 2D.

+++

On l'importe sous son nom standard.

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

On demande aux dessins de s'insérer en ligne dans le notebook et non pas d'être dessinés sur une fenêtre à part.

```{code-cell} ipython3
%matplotlib inline
```

Nous importons aussi les librairies numériques et de dataframe afin de voir leur relation avec `matplotlib`.

```{code-cell} ipython3
import pandas as pd
import numpy as np
```

https://matplotlib.org/api/pyplot_summary.html

+++

La syntaxe se veut simple. La librairie est très complète et très optimisée. Elle peut traiter de grandes quantités de données (ce qui en fait une bonne librairie pour les sciences de données). Enfin les fonctions ont été *emballées* afin d'être utilisées facilement en `pandas`.

+++

Vous allez y trouver les fonctions classiques: courbes, histogrammes, boîtes à moustache, nuages de points ... que vous allez pouvoir personnaliser avec des textes, des grilles, des étiquettes, des légendes ... et dont vous allez pouvoir contrôler les couleurs, les styles de ligne, les propriétés de police, les propriétés des axes ...

+++

Nous savons faire des tableaux de nombres linéairement espacés avec la fonction `linspace`. Nous savons appliquer une fonction à tout un tableau `numpy` ... apprenons maintenant à dessiner les résultats obtenus.

+++

Voilà vos données pour les abcisses: 50 nombres réels entre 0 et $2\pi$

```{code-cell} ipython3
x = np.linspace(0, 2*np.pi, 50)
```

Et pour les ordonnées : les sinus de ces points. J'applique simplement la fonction (vectorielle) `np.sin` à `x` qui est ... on se rappelle, un `np.ndarray`

```{code-cell} ipython3
y = np.sin(x)
```

## tracer une courbe (`plt.plot`)

+++

En utilisant la fonction `plot` de `matplotlib.pyplot` donc `plt.plot`, nous allons tracer les 50 couples de points (abscisse, ordonnée) entre 0 et $2\pi$.

```{code-cell} ipython3
plt.plot(x, y);
```

C'est très joli et très succinct. Tous les *réglages* ont pris leurs valeurs par défaut: taille de la figure, tailles et polices des caractères, couleurs du fond et de la courbe, titre ...

Améliorons un peu notre figure.

+++

## mettre un titre à la figure (`plt.title`)

```{code-cell} ipython3
plt.title('un beau sinus')
plt.plot(x, y);        
```

## changer la taille des caractères (*fontsize=*)

+++

Et si j'y vois mal et que je préfère un titre plus gros:

```{code-cell} ipython3
:cell_style: center

plt.title('un beau sinus', fontsize=30)
plt.plot(x, y);
```

on vous laisse leur mettre une taille de fonte

+++

## mettre des légendes aux axes (`plt.xlabel` et `plt.ylabel`)

```{code-cell} ipython3
plt.xlabel('abscisses')
plt.ylabel('ordonnées', fontsize=25)
plt.plot(x, y);
```

## afficher les points (`plt.scatter`)

+++

On affiche les points, plutôt que de les relier pour former une courbe continue.

```{code-cell} ipython3
z = np.cos(x)
plt.scatter(x, z);
```

## mettre une légende à plusieurs plots sur la même figure (*label=*)

+++

Il faut leur donner un label et ajouter une légende qui utilisera ces labels:

```{code-cell} ipython3
plt.plot(x, y, label='sinus');
plt.scatter(x, z, label='cosinus')
plt.legend()
```

## fixer la limite des axes (`plt.xlim` et `plt.ylim`)

+++

$y=sin(x)$ est calculé entre $0$ et $2\pi$ mais on l'affiche entre 0 et $\pi$ en abscisse et entre 0 et 1 en ordonnées:

```{code-cell} ipython3
plt.xlim(0, np.pi)
plt.ylim(0,1)

plt.plot(x, np.sin(x));
```

## préciser les *ticks* des axes (`plt.xticks` et `plt.yticks`)

```{code-cell} ipython3
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

plt.yticks([0, 0.5, 1])
plt.plot(x, np.sin(x));
```

On peut même donner des noms aux ticks:

```{code-cell} ipython3
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
            [0, 'pi/2', 'pi', '3pi/2', '2pi'])

plt.plot(x, np.sin(x), label='sinus');
```

On peut utiliser les formules latex - souvenez-vous c'est un trait de markdown, entre deux `$` :

```{code-cell} ipython3
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [0, '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])

plt.title("$x^2$ heu non c'est pas ca du tout ! ")
plt.plot(x, np.sin(x), label='sinus');
```

À vous de jouer. Construisez un tableau d'entiers entre 1 et 10 (non compris) et afficher la courbe $x^3$. Indice utilisez `np.arange` et `np.power`.

```{code-cell} ipython3
# votre code ici
```

## modifier la couleur, le style et l'épaisseur

+++

On va le faire sur la courbe de la fonction $x^2$ entre 1 et 10.

```{code-cell} ipython3
:cell_style: center

x = np.arange(1, 10)
y = np.power(x, 2)

plt.plot(x, y, color='orange', linestyle='-.', linewidth=13);
```

Essayez: '-', '--', '-.', ':', ou encore `solid`, `dashed`, `dashdot`, `dotted`

+++

### style de ligne et couleur en même temps

+++

On précise aussi la taille des marqueurs de points.

```{code-cell} ipython3
plt.plot(x, y, 'g--',) # pointillés verts green --

plt.plot(x, y, 'rs', markersize=10) # rectangles r(red) et s(quare)

plt.plot(x, y, 'y^', markersize=4); # ^triangles y(yellow)

plt.plot(x+0.5, y+0.5, 'mv', markersize=6); # triangles tête en bas majenta ...
```

## écrire du texte à une position

```{code-cell} ipython3
plt.text(1, 1, 'you are here !', fontsize=20)
plt.plot(1, 1, 'rx')
```

## sauver une figure dans un fichier (sans clic-droit)

+++

On dessine la fonction $f(x)=x^2$. Mettez au fichier l'extension du format que vous préférez: *jpeg*, *jpg*, *pdf*, *png*, *svg*...

```{code-cell} ipython3
x = np.linspace(-10, 10, 50)
y = np.power(x, 2)

plt.title('$f(x) = x^2$', fontsize=20)

plt.xlabel('x', fontsize=15)
plt.ylabel('$x^2$', fontsize=15)

plt.plot(x, y, label='$x^2$')

plt.legend(fontsize=12)

plt.savefig('my_figure.jpg')
#plt.savefig('my_figure.png')
```

Et pour voir le résultat..

<img src='my_figure.jpg'>
