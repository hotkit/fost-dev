# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['fost-meta'] = dict(
    source='git@github.com:KayEss/fost-meta.git',
    libs=[])


if is_windows():
    PROJECTS['fost-meta']['post-clone'] = ['PostgreSQL\\configure']
else:
    PROJECTS['fost-meta']['post-clone'] = ['PostgreSQL/configure']

