from configuration import *


PROJECTS['fost-meta'] = dict(
        source='git@github.com:KayEss/fost-meta.git',
        libs=['cord', 'fost-aws', 'fost-base', 'fostgres',
              'fost-internet', 'fost-postgres', 'fost-web', 'odin', 'threading'],
    )


if is_windows():
    PROJECTS['fost-meta']['post-clone'] = ['PostgreSQL\\configure']
else:
    PROJECTS['fost-meta']['post-clone'] = ['PostgreSQL/configure']

