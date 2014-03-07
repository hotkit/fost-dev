# -*- coding: utf-8 -*-
from configuration import *

for e in ['%s-mfc' % s for s in list(VARIANTS)]:
    VARIANTS.append(e)

if PROJECTS.has_key('fost-windows'):
    PROJECTS['fost-windows']['test'] = True
    PROJECTS['fost-windows']['variants'] = ['debug-mfc', 'release-mfc']
