---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: quiz sur Python
version: '1.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat</span>
</div>

<img src="media/inria-25-alpha.png" />

+++

# quiz

pour vous évaluer sur

* la séance d'installation et introduction aux outils
* le cours de survol du langage Python

+++

## mode d'emploi

```{code-cell} ipython3
from nbautoeval import quiz_help
quiz_help("fr")
```

Pour ce premier quiz <span style="background-color:red; padding: 5px; margin-top: 5px;">l'heure limite est fixée à 09:10</span>

+++

## le quiz

+++

**évaluez la cellule suivante** pour faire apparaitre le quiz

```{code-cell} ipython3
:hide_input: false
:tags: [raises-exception]

from nbautoeval import run_yaml_quiz
run_yaml_quiz("python", "quiz")
```

le quiz se trouve dans la cellule précédente, que vous devez évaluer
****
