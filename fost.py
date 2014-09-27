# -*- coding: utf-8 -*-
from configuration import *
import beanbag
import mengmom
for lib in ['fost-aws', 'fost-meta', 'fost-postgres']:
    __import__(lib)


for lib in ['fost-base', 'fost-internet', 'fost-orm',
        'fost-py', 'fost-windows']:
    PROJECTS[lib] = dict(
        source='git@github.com:KayEss/%s-dev.git' % lib)

PROJECTS['fost-windows']['test'] = False
PROJECTS['hello'] = dict(
    source='git@github.com:KayEss/fost-hello.git',
    folder='fost-hello',
    gitflow=False, libs=[],
    targets = [''])


for project, configuration in PROJECTS.items():
    if not configuration.has_key('libs'):
        PROJECTS[project]['libs'] = [project]

