# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['fost-beanbag'] = {
    'source': 'git@github.com:KayEss/beanbag.git',
    'folder': 'beanbag',
    'libs': ['fost-beanbag'],
}

PROJECTS['fost-beanbag-seed'] = {
    'source': 'git@github.com:KayEss/beanbag-seed.git',
    'folder': 'beanbag-seed',
    'gitflow': False, 'test': False,
    'libs': [], 'targets': [],
}
