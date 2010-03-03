# -*- coding: utf-8 -*-
from configuration import *


spruce_versions = [v for v in BOOST_VERSIONS if v in [41, 42]]
if len(spruce_versions):
    PROJECTS['spruce'] = dict(
        suffixes = [''],
        boost = spruce_versions
    )
