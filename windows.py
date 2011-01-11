# -*- coding: utf-8 -*-
from configuration import *

if 37 in BOOST_VERSIONS:
    BOOST_VERSIONS.remove(37)

PROJECTS['fost-windows'] = dict(
    suffixes = ['', '-stable'],
    variants = ['debug-mfc', 'release-mfc'],
)
