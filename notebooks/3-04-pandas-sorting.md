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


Notebook très rapide !

```python
import pandas as pd
import numpy as np
```

# trier une dataframe


il peut être utile de trier une dataframe selon l'ordre d'une colonne (resp. ligne) de la dataframe et le résultat sera une dataframe dont les lignes (resp. colonnes) auront été réordonnées, les index sont conservés (ils bougent avec les lignes qu'ils indexent ...). attention par contre, bien sûr les indices sont modifiés ...

c'est l'axe qui indiquera si on trie dans l'axe des lignes (auquel cas on trie selon une colonne) ou si on trie dans l'axe des colonnes (auquel cas on trie selon une ligne).

la fonction est `pandas.dataframe.sort_values`


Vous pouvez décider de trier en place (`inplace=True`) auquel cas la dataframe sur laquelle vous appliquez la fonction est modifiée sinon la fonction renverra une dataframe ... (si vous voulez une copie, comme toujours précisez le, votre code sera plus clair).


## tri d'une dataframe selon une colonne


Reprenons notre exemple du titanic.

```python
file = 'titanic.csv'
```

```python
df = pd.read_csv(file, index_col=0)
df.head()
```

Nous voulons trier la dataframe suivant l'ordre de la colonne de `Age`. Dans quel axe (`axis`) devons-nous trier? Vous vous rappelez `axis=0` et `axis=1`?
   - si `axis=0` je trie les lignes
   - si `axis=1` je trie les colonnes 

```python
df_sorted1 = df.sort_values(by='Age', ascending=False, axis=0)
```

```python
df_sorted1.head(8)
```

Vous voyez que la colonne des `Age` est triée, les lignes ont été changées de place dans la table et leur indexation conservée.

<!-- #region {"tags": []} -->
Regardons les lignes d'index 673 et 746. Les ages sont identiques, nous aurions pu indiquer une seconde colonne avec `by=[col1, col2]` pour trier les valeurs trouvées identiques par la première colonne.

Par exemple trions par `Age`, et si les âges sont égaux, trions par `Fare`.
<!-- #endregion -->

```python
df_sorted2 = df.sort_values(by=['Age', 'Fare'], ascending=False, axis=0)
```

```python
df_sorted2.head(8)
```

Vous voyez que les lignes d'index 746 et 673, dont les âges sont égaux, ont été triées par `Fare` et ont changé d'ordre par rapport à la première dataframe `df_sorted1`.


Si vous voulez modifier la dataframe initiale faites le tri en place en passant le paramètre `inplace=True`.

<!-- #region {"tags": ["level_intermediate"]} -->
Une dernière question: Où sont les lignes dont les valeurs concernées par le tri ne sont pas connues (i.e. `np.nan`)?

Listons les 5 dernières lignes de la dataframe avec la méthode `pandas.DataFrame.tail` 
<!-- #endregion -->

```python tags=["level_intermediate"]
df.sort_values(by='Age', ascending=False, axis=0).tail() # oui à la fin
```

<!-- #region {"tags": ["level_intermediate"]} -->
Il est possible de les mettre en début de la dataframe:
<!-- #endregion -->

```python tags=["level_intermediate"]
df.sort_values(by='Age', ascending=False, axis=0, na_position='first').head()
```

## tri d'une dataframe selon une ligne


L'exemple du Titanic se prête mal à cet exemple. Créons une dataframe bidon à partir d'un `np.ndarray`. Donnons lui un index de colonnes et un de lignes.

```python
petite_df = pd.DataFrame(np.random.randint(-10, 10, 20).reshape(4, 5),
                         columns=['d', 'e', 'a', 'c', 'b'])
petite_df.index = ['un', 'deux', 'trois', 'quatre']
petite_df
```

Trions la dataframe par la ligne d'index `un` donc `axis=1`

```python
petite_df.sort_values(by='un', axis=1)
```

Vous voyez que la ligne *'un'* a été triée et la dataframe réorganisée autour de cette ligne en conservant les index.


## tri des index


Comme son nom d'indique, nous allons pouvoir trier les index d'une dataframe, et comme toujours, suivant l'axe 0 pour les lignes, et suivant l'axe 1 pour les colonnes.


Par exemple, nous pouvons trier l'index des colonnes (`axis=1`) de `df`. 


Regardons la dataframe.

```python
df.head(6)
```

Trions ses noms de colonnes et affichons le header de la dataframe.

```python
df.sort_index(axis=1).head()
```

Les colonnes ont bien été réordonnées par ordre lexicographique croissant.


Maintenant, trions l'index des lignes (*axis=0*) de `df_sorted1` (parce que celui de `df` est déjà trié). 


Regardons avant le tri:

```python
df_sorted1.head(6)
```

Trions et regardons après le tri.

```python
df_sorted1.sort_index(axis=0).head()
```

Voilà l'index `PassengerId` tout bien réordonné !
