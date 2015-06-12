# -*- coding: utf-8 -*-
from configuration import *


platform('trusty')


for v in xrange(35, 55):
    if v in BOOST_VERSIONS:
        BOOST_VERSIONS.remove(v)

