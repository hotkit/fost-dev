from configuration import *


PROJECTS['mengmom'] = dict(
    source='git@github.com:KayEss/mengmom.git')
if is_windows():
    PROJECTS['mengmom']['post-clone'] = ['PostgreSQL\\configure']
else:
    PROJECTS['mengmom']['post-clone'] = ['PostgreSQL/configure']
