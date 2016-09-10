# -*- coding: utf-8 -*-
from configuration import *


for v in range(55, 62):
    if v not in BOOST_VERSIONS:
        BOOST_VERSIONS.append(v)
