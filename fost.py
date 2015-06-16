# -*- coding: utf-8 -*-
from configuration import *
import beanbag
import mengmom
for lib in ['fost-android', 'fost-aws', 'fost-base', 'fost-hello',
        'fost-internet', 'fost-orm', 'fost-meta', 'fost-postgres', 'fost-py']:
    __import__(lib)

#PROJECTS['fost-windows']['test'] = False

