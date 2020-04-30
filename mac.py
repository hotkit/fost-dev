# -*- coding: utf-8 -*-
from configuration import *

platform('mac')


del TOOLSET['gcc']

CMAKE.append('CXXFLAGS="-I/usr/local/opt/openssl/include '
    '-L/usr/local/opt/openssl/lib '
    '-Wno-unused-command-line-argument '
    '-Wno-macro-redefined"')

def remove_project(pname):
    if pname in PROJECTS and pname not in sys.argv:
        print("Removing implicitly included project '{}'".format(pname))
        print('To include it specify it directory on the command line.')
        del PROJECTS[pname]

i = len(BOOST) - 1
while i >= 0:
    if BOOST[i][0] and BOOST[i] < (1, 65, 0) or BOOST[i][1] in (66, 67):
        del BOOST[i]
    i -= 1
