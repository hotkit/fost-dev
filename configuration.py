# -*- coding: utf-8 -*-


PROJECTS = {
    'animray': dict(
        suffixes = [''],
        variants = ['release'],
    ),
    'appservices': dict(
        suffixes = ['']
    ),
    'appservicesdk': {},
    'fost-aws': {},
    'fost-base': dict(
        suffixes = ['', '-rc', '-stable']
    ),
    'fost-internet': {},
    'fost-meta': {},
    'fost-orm': {},
    'fost-postgres': {},
    'fost-py': {},
    'metachatr': dict(
        suffixes = [''],
        boost = [41, 42],
    ),
    'spruce': dict(
        suffixes = [''],
        boost = [41, 42],
    ),
}
SUFFIXES = ['', '-rc']
BOOST_VERSIONS = [38]
VARIANTS = ['debug', 'release']
TARGETS = ['', 'all']
