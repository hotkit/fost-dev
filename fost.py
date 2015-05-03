# -*- coding: utf-8 -*-
from configuration import *
import beanbag
import mengmom
for lib in ['fost-android', 'fost-aws', 'fost-hello', 'fost-internet',
        'fost-meta', 'fost-postgres', 'fost-py']:
    __import__(lib)


for lib in ['fost-base', 'fost-orm', 'fost-windows']:
    PROJECTS[lib] = dict(
        source='git@github.com:KayEss/%s-dev.git' % lib,
        libs=[lib])

PROJECTS['fost-windows']['test'] = False

