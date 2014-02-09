# -*- coding: utf-8 -*-
from configuration import *

BOOST_VERSIONS.append('saucy')
for v in xrange(35, 50):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)
