# -*- coding: utf-8 -*-
import os
import subprocess
import sys


if __name__ == "__main__":
    from configuration import *
    for arg in sys.argv[1:]:
        ARGS.append(arg)
    while len(ARGS):
        arg = ARGS.pop(0)
        print "Importing", arg
        __import__(arg)

    if not OPTIONS['platform']:
        if sys.platform == 'linux2':
            name = subprocess.check_output(['lsb_release', '-cs']).strip()
            print "Guessing linux platform", name
            __import__(name)
        elif sys.platform == 'win32':
            print "Guessing Windows platform"
            __import__('windows')
        else:
            print "Don't know which platform this is"
            print "sys.platform reports", sys.platform
            sys.exit(1)

    if len(ACTIONS):
        while len(ACTIONS):
            action = ACTIONS.pop(0)
            action()
    else:
        print "No actions specified"
        print "Loaded projects are", ', '.join(PROJECTS.keys())
