# -*- coding: utf-8 -*-
import os
import shutil
import sys
import tempfile


ARGS = []
ACTIONS = []

## This is the old version of the BOOST configuration
BOOST_VERSIONS = [62]
## This is now used by the cmake build version
BOOST = [(1, 62, 0)]

OPTIONS = {'platform': None}
PROJECTS = {}
TARGETS = ['all', '']
MAKE = ['', 'check', 'stress', 'install']
VARIANTS = ['debug', 'release']
TOOLSETS = ['clang', 'gcc']


def is_windows():
    """
        Returns True if the system is Windows.
    """
    return sys.platform == 'win32'


def execute(program, *args):
    """
        Execute a program and return True if it worked.
    """
    if is_windows():
        program = program.replace('/', '\\')
    command = '%s %s' % (program, ' '.join([str(a) for a in args]))
    print "++", command
    return os.system(command) == 0


def worked(program, *args):
    """
        Execute and make sure the command worked.
    """
    assert execute(program, *args)


def git(directory, *args):
    """
        Executed git in the requested directory relative to here.
    """
    worked('cd', directory, '&&', 'git', *args)


def git_capture(directory, *args):
    """
        Execute the git command and return it's output.
    """
    args = list(args)
    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, 'c.git.txt')
    args.append("> %s" % (filename,))
    git(directory, *args)
    with open(filename) as f:
        output = f.read()
    shutil.rmtree(tmpdir)
    print output
    return output


def projects():
    """
        A generator that iterates through the projects giving up the name, folder and configuration.
    """
    for project, configuration in PROJECTS.items():
        folder = configuration.get('folder', project)
        yield (project, folder, configuration)


def platform(name):
    """
        Set the platform name.
    """
    OPTIONS['platform'] = name

