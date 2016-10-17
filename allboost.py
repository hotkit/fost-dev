# -*- coding: utf-8 -*-
from configuration import *


for v in range(55, 62):
    if v not in BOOST_VERSIONS and v != 60:
        BOOST_VERSIONS.append(v)
