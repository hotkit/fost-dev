# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['animray'] = dict(
    source='git@github.com:KayEss/AnimRay.git',
    gitflow=False,
    folder='AnimRay',
    libs=[],
    make=['', 'check', 'install'],
)
