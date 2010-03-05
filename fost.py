# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['fost-aws'] = {}
PROJECTS['fost-base'] = dict(
    suffixes = ['', '-rc', '-stable']
)
PROJECTS['fost-internet'] = dict(
    suffixes = ['', '-rc', '-stable']
)
PROJECTS['fost-meta'] = {}
PROJECTS['fost-orm'] = {}
PROJECTS['fost-postgres'] = {}
PROJECTS['fost-py'] = {}

# Example project
PROJECTS['hello'] = dict(
    suffixes = [''],
    folder = 'fost-hello',
    targets = [''],
)
