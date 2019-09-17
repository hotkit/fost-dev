# -*- coding: utf-8 -*-
from configuration import *


PROJECTS['test-android'] = dict(
    source='git@github.com:hotkit/test-android.git',
    gitflow=False,
    libs=['fost-android-ndk', 'fost-android-java'],
    targets=[],
    test=False)

