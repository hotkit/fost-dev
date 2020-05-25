from configuration import *


PROJECTS['fost-meta'] = dict(
        source='git@github.com:hotkit/fost-meta.git',
        libs=['cord', 'fost-aws', 'fost-base', 'fostgres', 'fost-beanbag',
              'fost-internet', 'fost-postgres', 'fost-web', 'json-schema',
              'odin', 'makham', 'threading'],
        make=['', 'check', 'pgtest', 'stress', 'install'],
    )
