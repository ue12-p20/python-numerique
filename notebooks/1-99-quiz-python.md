---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: quiz sur Python
version: 1
---

# quiz

pour vous évaluer sur 

* la séance d'installation et introduction aux outilds
* le cours de survol du langage Python

+++

## mode d'emploi

+++

* le quiz est contenu dans **une cellule de code**, le plus souvent celle-ci est **vide au départ**, vous devez **l'évaluer** pour faire **apparaitre les questions**

* toutes les questions ont au moins une réponse valable, si vous ne cochez aucune réponse on considère que vous préférez ne pas répondre
* le barême est indiqué pour chaque question; par exemple `4 pts / -1 pt / 0 pt` signifie
  * 4 points pour une **bonne réponse**
  * -1 point en cas de **réponse fausse**
  * 0 point si vous ne répondez **pas du tout** (à nouveau : si vous ne cochez aucune option)
* le signe ♧  indique que plusieurs réponses sont possibles
* vous avez plusieurs essais pour y répondre; le résultat final correspond exactement à votre meilleur essai;  
  les essais sont notés indépendamment les uns des autres, il n'y a pas d'effet cumulatif : si par exemple vous obtenez 10/20 au premier essai en ayant juste à la question 1, et 12/20 au deuxième essai en ayant faux à la question 1, on retient le 12/20, la bonne réponse à l'essai #1 n'affecte pas l'essai #2
  
* **horaires :** vous avez un temps limité pour répondre, qui vous est indiqué pendant la séance  
  **attention :** le relevé des réponses **ignore** les réponses données **après l'heure limite**, même si, pour des raisons techniques, vous pouvez toujours soumettre après ce délai.

+++

Pour ce premier quiz <span style="background-color:red; padding: 5px; margin-top: 5px;">l'heure limite est fixée à 09:10</span>

+++

## le quiz

+++

la cellule suivante semble vide au départ, mais **évaluez-la** pour faire apparaitre le quiz

```{code-cell} ipython3
:hide_input: true
:tags: [raises-exception]

from nbautoeval import run_yaml_quiz
run_yaml_quiz("python", "quiz")
```

```{code-cell} ipython3

```
