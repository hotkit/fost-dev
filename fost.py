# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['fost-base'] = dict(
    source='git@github.com:KayEss/fost-base-dev.git')
PROJECTS['fost-internet'] = dict(
    source='git@github.com:KayEss/fost-internet-dev.git')


PROJECTS['hello'] = dict(
    source='git@github.com:KayEss/fost-hello.git',
    folder='fost-hello',
    gitflow=False, libs=[],
    targets = [''])


for project, configuration in PROJECTS.items():
    if not configuration.has_key('libs'):
        PROJECTS[project]['libs'] = [project]

