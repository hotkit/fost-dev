# -*- coding: utf-8 -*-
import os
import subprocess
import sys


def update(directory):
    """
        Update the code to the latest version.
    """
    updater = os.path.join(directory, 'update' if not is_windows() else 'update.cmd')
    if os.path.exists(updater):
        return execute(updater)
    else:
        return execute('svn', 'up', directory)


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
        else:
            print "Don't know which platform this is"
            print "sys.platform reports", sys.platform
            sys.exit(1)

    while len(ACTIONS):
        action = ACTIONS.pop(0)
        action()
