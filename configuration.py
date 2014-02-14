# -*- coding: utf-8 -*-
import os
import sys


ARGS = []
ACTIONS = []
BOOST_VERSIONS = [40, 47, 52]
OPTIONS = {}
PROJECTS = {}
TARGETS = ['all', '']
VARIANTS = ['debug', 'release']


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
    print "Starting", command
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


def projects():
    """
        A generator that iterates through the projects giving up the name, folder and configuration.
    """
    for project, configuration in PROJECTS.items():
        folder = configuration.get('folder', project)
        yield (project, folder, configuration)

