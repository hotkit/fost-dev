# -*- coding: utf-8 -*-
from configuration import *


platform('precise')


BOOST_VERSIONS.append('precise')
for v in xrange(35, 47):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

