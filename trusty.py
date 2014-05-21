# -*- coding: utf-8 -*-
from configuration import *


platform('trusty')


BOOST_VERSIONS.append('trusty')
for v in xrange(35, 54):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

