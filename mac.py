# -*- coding: utf-8 -*-
from configuration import *


platform('mac')


TOOLSETS.remove('clang')
TOOLSETS.remove('gcc')
TOOLSETS.append('darwin')
TOOLSETS.append('darwin-clang')
