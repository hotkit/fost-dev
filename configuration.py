# -*- coding: utf-8 -*-
import os
import shutil
import sys
import tempfile

ARGS = []
ACTIONS = []

## This is now used by the cmake build version
BOOST = [(None, None, None)]

OPTIONS = {'platform': None}
PROJECTS = {}
TARGETS = ['all', '']
MAKE = ['', 'install']
CMAKE = []
CMAKE_POST = []
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
    print('++ {}'.format(command))
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
    print(output)
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
