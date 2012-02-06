# -*- coding: utf-8 -*-
from configuration import *

BOOST_VERSIONS.append('oneiric')
for v in xrange(40, 47):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)
