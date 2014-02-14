# -*- coding: utf-8 -*-
from configuration import *


platform('raring')


BOOST_VERSIONS.append('raring')
for v in xrange(35, 50):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

