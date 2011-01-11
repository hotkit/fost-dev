# -*- coding: utf-8 -*-
from configuration import *


spruce_versions = [v for v in BOOST_VERSIONS if v >= 41] or [41]
if len(spruce_versions):
    PROJECTS['spruce'] = dict(
        suffixes = [''],
        boost = spruce_versions
    )
