#!/usr/bin/env python

import os
from setuptools import setup

LICENSE = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')).read().strip()

DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.md')).read().strip()

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development",
]

setup(
    name='colorpp',
    version='0.1.0',
    description='pretty print json, yaml, and python object.',
    author='aminamid',
    author_email='pekorinko@gmail.com',
    url='https://github.com/aminamid/colorpp',
    py_modules=['colorpp'],
    keywords=['json', 'yaml','pretty', ],
    classifiers=classifiers,
    install_requires=[''],
    license=LICENSE,
    long_description=DESCRIPTION,
    test_suite='')
