from configuration import *


PROJECTS['fost-meta'] = dict(
        source='git@github.com:KayEss/fost-meta.git',
        libs=['cord', 'fost-aws', 'fost-base', 'fostgres',
              'fost-internet', 'fost-postgres', 'fost-web', 'json-schema',
              'odin', 'threading'],
        make=['', 'check', 'stress', 'install'],
    )

