# -*- coding: utf-8 -*-
from configuration import *


for p in ['fost-aws', 'fost-base', 'fost-internet',
        'fost-meta', 'fost-orm', 'fost-postgres',
        'fost-py', 'fost-web']:
    PROJECTS[p] = dict(
        suffixes = ['', '-stable']
    )

# Example project
PROJECTS['hello'] = dict(
    suffixes = [''],
    folder = 'fost-hello',
    targets = [''],
)

