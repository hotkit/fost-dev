# -*- coding: utf-8 -*-
from configuration import *

if not 49 in BOOST_VERSIONS:
    BOOST_VERSIONS.append(49)
BOOST_VERSIONS.append('quantal')
for v in xrange(35, 49):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)
