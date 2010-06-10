# -*- coding: utf-8 -*-
from configuration import *


metachatr_versions = [v for v in BOOST_VERSIONS if v >= 41] or [41]
if len(metachatr_versions):
    PROJECTS['metachatr'] = dict(
        suffixes = [''],
        boost = metachatr_versions
    )
