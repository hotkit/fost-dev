# -*- coding: utf-8 -*-
from configuration import *


platform('mac')


TOOLSETS.remove('gcc')

CMAKE.append('CXXFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib -Wno-unused-command-line-argument"')

def remove_project(pname):
    if pname in PROJECTS and pname not in sys.argv:
        print "Removing implicitly included project '%s'." % (pname,)
        print "To include it specify it directoy on the command line."
        del PROJECTS[pname]

i = len(BOOST) - 1
while i >= 0:
    if BOOST[i][0] and BOOST[i] < (1, 65, 0):
        del BOOST[i]
    i -= 1
