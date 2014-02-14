# -*- coding: utf-8 -*-
from configuration import *

if 37 in BOOST_VERSIONS:
    BOOST_VERSIONS.remove(37)

if PROJECTS.has_attr('fost-windows'):
    PROJECTS['fost-windows']['test'] = True
