from configuration import *

PROJECTS['cord'] = {
        'source': 'git@github.com:KayEss/f5-cord.git',
        'make': ['check'],
        'test': "./runtests",
    }
