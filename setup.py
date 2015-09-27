#!/usr/bin/env python

from setuptools import setup

Description = """/
ExImview
"""

# setup parameters
setup(name='PKView',
      cmdclass={'build_ext': build_ext},
      version='0.1',
      description='Example viewer',
      long_description=Description,
      author='Benjamin',
      author_email='stuff@birving.com',
      classifiers=["Programming Language :: Python :: 2.7",
                   "Development Status:: 3 - Alpha",
                   'Programming Language :: Python',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   "Intended Audience :: Education",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: End Users/Desktop",
                   "Topic :: Scientific/Engineering :: Bio-Informatics",
                   ],
      scripts=["image_app.py"])
