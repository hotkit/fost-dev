# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['fost-postgres'] = dict(
    source='git@github.com:KayEss/fost-postgres-dev.git',
    libs=['fost-postgres'])

if is_windows():
    PROJECTS['fost-postgres']['post-clone'] = ['PostgreSQL\\configure']
else:
    PROJECTS['fost-postgres']['post-clone'] = ['PostgreSQL/configure']

