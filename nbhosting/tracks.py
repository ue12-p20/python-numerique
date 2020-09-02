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

    track_specs = [
        ('cours #1: intro & install' , 'survol & mise en place des outils', 'intro',
         [ 
           ('introduction', 'notebooks/0-[0-8]*.md'),
           ('checklist', 'notebooks/0-9*.md'),
         ]),
        ('cours #2: python' , 'survol du langage Python', 'python',
         [ 
           ('les bases', 'notebooks/1-[0-8]*.md'),
           ('quiz', 'notebooks/1-9*.md'),
         ]),
        ('cours #3: numpy' , 'programmation vectorielle', 'numpy',
         [ 
           ('numpy', 'notebooks/2-[0-8]*.md'), 
           ('quiz', 'notebooks/2-9*.md'), 
        ]),
        ('dataviz & pandas' , 'outils pour la data science', 'dataviz',
         [ 
           ('dataviz & pandas', 'notebooks/3-[0-8]*.md'),
           ('quiz', 'notebooks/3-9*.md'),
         ]),
#        ('évaluation', 'évaluation', 'eval',
#         [ ('évaluation', 'notebooks/4-[0-9]*.md'),
#         ])
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
