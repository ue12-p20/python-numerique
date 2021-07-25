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
notebookname: quiz sur pandas
version: '1.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Valérie Roy</span>
</div>

<img src="media/ensmp-25-alpha.png" />

+++

# quiz

pour vous évaluer sur l'introduction à pandas

+++

## mode d'emploi

```{code-cell}
from nbautoeval import quiz_help
quiz_help("fr")
```

<span style="background-color:red; padding: 5px; margin-top: 5px;">L'heure limite est fixée à 14:10</span>

+++

## le quiz

+++

**évaluez la cellule suivante** pour faire apparaitre le quiz

```{code-cell}
:hide_input: false
:tags: [raises-exception]

from nbautoeval import run_yaml_quiz
run_yaml_quiz("pandas", "quiz")
```

le quiz se trouve dans la cellule précédente, que vous devez évaluer
****
