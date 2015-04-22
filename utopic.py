# -*- coding: utf-8 -*-
from configuration import *


platform('utopic')


BOOST_VERSIONS.append('utopic')
for v in xrange(35, 55):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

