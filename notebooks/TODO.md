# deux formats de notebook différents

les fichiers suivants

```
1-99-annonces.md:jupyter:
2-01-numpy-intro.md:jupyter:
2-02-numpy-type-memory.md:jupyter:
2-03-numpy-vectorization.md:jupyter:
2-04-numpy-indexing-slicing.md:jupyter:
2-05-numpy-broadcast.md:jupyter:
2-06-numpy-aggregate.md:jupyter:
2-07-numpy-array-testing.md:jupyter:
2-08-numpy-linalg.md:jupyter:
3-04-pandas-sorting.md:jupyter:
3-05-pandas-group-by.md:jupyter:
4-03-matplotlib-figure-and-sub-figures.md:jupyter:
4-04-matplotlib-pandas-dataframe.md:jupyter:
4-05-matplotlib-plots-3D.md:jupyter:
```

sont différents des autres;
leur metadata contient un niveau d'imbrication supplémentaire, en 'jupyter:'
si on enlève à la main ce niveau de plus, le notebook est abimé

une autre différence est que

* le format usuel (sans jupyter:) vient avec des cellules de code taggées

    ```{code-cell} ipython3
    def foo():
        pass
    ```

* alors que les numpy ont simplement

    ```{code-cell} python
    def foo():
        pass
    ```

ce sont des différences que je vois parfois apparaitre spontanément
je ne sais pas lequel de ces deux formats est le plus recommandé mais il faut arriver
à unifier d'une manière ou d'une autre

c'est très confusant pour l'édition manuelle des metadata (notebookname notamment)
et surtout j'aimerais bien comprendre

trop tard pour faire cette année car ça va créer plein de conflits


# espaces en fin de ligne

à enlever; pareil, trop de conflits