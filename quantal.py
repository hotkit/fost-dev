# -*- coding: utf-8 -*-
from configuration import *

BOOST_VERSIONS.append('quantal')
for v in xrange(35, 47):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)
