# pylint: disable=c0111

from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    result is a list of Track instances
    """

    # tentative numbering
    # 00-19 for course
    # 50-69 for exos
    # 80-[89]9 for quiz and the like

    track_specs = [
        ('cours #1: intro & install' , 'survol & mise en place des outils', 'intro',
         [ 
           ('introduction', 'notebooks/0-[0-8]*.md'),
           ('checklist', 'notebooks/0-[89]*.md'),
         ]),
        ('cours #2: Python' , 'survol du langage Python', 'python',
         [ 
           ('Python primer', 'notebooks/1-[01]*.md'),
           ('exos', 'notebooks/1-[56]*.md'),
         ]),
        ('cours #3: numpy' , 'programmation vectorielle', 'numpy',
         [ 
           ('quiz & annonces', 'notebooks/1-[89]*.md'),
           ('numpy', 'notebooks/2-[01]*.md'), 
           ('exos', 'notebooks/2-[56]*.md'), 
#           ('quiz', 'notebooks/2-[89]*.md'), 
        ]),
        ('cours #4: pandas & dataviz' , 'outils pour la data science', 'datascience',
         [ 
           ('pandas & dataviz', 'notebooks/[34]-[01]*.md'),
           ('exos', 'notebooks/[34]-[56]*.md'),
#           ('quiz', 'notebooks/[34]-[89]*.md'),
         ]),
        ]

    return [Track(coursedir, 
                  [Section(coursedir=coursedir,
                           name=section_name, 
                           notebooks=notebooks_by_pattern(
                               coursedir, pattern))
                   for section_name, pattern in section_specs],
                  name=track_name,
                  description=track_description,
                  id=track_id)
            for (track_name, track_description, track_id, section_specs) in track_specs]
