# -*- coding: utf-8 -*-
from configuration import *


for p in [
        'fost-aws', 'fost-base', 'fost-internet',
        'fost-meta', 'fost-orm', 'fost-postgres',
        'fost-py']:
    PROJECTS[p] = dict(
        suffixes = ['', '-rc', '-stable']
    )

# Example project
PROJECTS['hello'] = dict(
    suffixes = [''],
    folder = 'fost-hello',
    targets = [''],
)
