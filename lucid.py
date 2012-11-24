# -*- coding: utf-8 -*-
from configuration import *

# Boost 1.40 is the version that ships with Lucid
if 40 in BOOST_VERSIONS:
    BOOST_VERSIONS.remove(40)

BOOST_VERSIONS.append('lucid')
