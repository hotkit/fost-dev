# -*- coding: utf-8 -*-
from configuration import *


metachatr_versions = [v for v in BOOST_VERSIONS if v in [41, 42]]
if len(metachatr_versions):
    PROJECTS['metachatr'] = dict(
        suffixes = [''],
        boost = metachatr_versions
    )
