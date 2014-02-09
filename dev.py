# -*- coding: utf-8 -*-
import os
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
        print "Importing", arg
        __import__(arg)

