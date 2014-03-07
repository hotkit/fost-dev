# -*- coding: utf-8 -*-
from configuration import *


platform('windows')


if 37 in BOOST_VERSIONS:
    BOOST_VERSIONS.remove(37)

for project, configuration in PROJECTS.items():
    if configuration.has_key('post-clone'):
        configuration['post-clone'].append('&&')
        configuration['post-clone'].append('OpenSSL\\configure')
    else:
        configuration['post-clone'] = ['OpenSSL\\configure']

