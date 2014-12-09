# -*- coding: utf-8 -*-
from configuration import *


platform('utopic')


BOOST_VERSIONS.append('utopic')
for v in xrange(35, 54):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

