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
        ('python' , 'survol langage',
         [ 
           ('intro', 'notebooks/0-[0-9]*.ipynb'),
           ('python', 'notebooks/1-[0-9]*.ipynb'),
         ]),
#        ('numpy' , 'numpy',
#         [ ('numpy', 'notebooks/2-[0-9]*.ipynb'), 
#        ]),
#        ('dataviz & pandas' , 'dataviz & pandas',
#         [ ('dataviz & pandas', 'notebooks/3-[0-9]*.ipynb'),
#         ]),
#        ('évaluation', 'évaluation',
#         [ ('évaluation', 'notebooks/4-[0-9]*.ipynb'),
         ])
        ]

    return [Track(coursedir, 
                  [Section(coursedir=coursedir,
                           name=section_name, 
                           notebooks=notebooks_by_pattern(
                               coursedir, pattern))
                   for section_name, pattern in section_specs],
                  name=track_name,
                  description=track_description)
            for track_name, track_description, section_specs in track_specs]
