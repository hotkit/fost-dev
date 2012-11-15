# -*- coding: utf-8 -*-
from configuration import *

for v in range(40, 53):
    if v not in BOOST_VERSIONS and (v < 43 or v > 44):
        BOOST_VERSIONS.append(v)
