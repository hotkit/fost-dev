# -*- coding: utf-8 -*-
from configuration import *
import aws


for lib in ['fost-base', 'fost-internet', 'fost-orm',
        'fost-postgres', 'fost-py', 'fost-windows']:
    PROJECTS[lib] = dict(
        source='git@github.com:KayEss/%s-dev.git' % lib)

PROJECTS['fost-meta'] = dict(
    source='git@github.com:KayEss/fost-meta.git',
    libs=[])
if is_windows():
    PROJECTS['fost-postgres']['post-clone'] = ['PostgreSQL\\configure']
else:
    PROJECTS['fost-postgres']['post-clone'] = ['PostgreSQL/configure']
PROJECTS['fost-windows']['test'] = False
PROJECTS['hello'] = dict(
    source='git@github.com:KayEss/fost-hello.git',
    folder='fost-hello',
    gitflow=False, libs=[],
    targets = [''])


for project, configuration in PROJECTS.items():
    if not configuration.has_key('libs'):
        PROJECTS[project]['libs'] = [project]

