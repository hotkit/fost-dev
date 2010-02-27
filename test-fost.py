#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys


PROJECTS = {
    'fost-aws': {},
    'fost-base': dict(
        suffixes = ['', '-rc', '-stable']
    ),
    'fost-internet': {},
    'fost-meta': {},
    'fost-orm': {},
    'fost-postgres': {},
    'fost-py': {},
}
SUFFIXES = ['', '-rc']
BOOST_VERSIONS = [[b, 0] for b in range(38, 43)]
if sys.platform == 'linux2':
    BOOST_VERSIONS.append(['karmic'])


def is_windows():
    """
        Returns True if the system is Windows.
    """
    return sys.platform == 'win32'

def execute(program, *args):
    """
        Execute a program and return True if it worked.
    """
    command = '%s %s' % (program, ' '.join([str(a) for a in args]))
    print program, args, command
    return os.system(command) == 0

def install_boost(directory, version):
    """
        Installs the right version of Boost for the platform.
    """
    if not is_windows() and version != ['karmic']:
        version = version[0]
        if not os.path.isdir('%s/Boost/1_%s_0' % (directory, version)):
            sys.symlink('Boost/1_%s_0' % version, '%s/Boost/1_%s_0' % (directory, version))
        if not os.path.isdir('%s/Boost/boost/include/boost-1_%s' % (directory, version)):
            execute('%s/Boost/build', *version)
    return execute('%s/Boost/install' % directory, *boost)


built, success, failure = 0, [], []
if execute('svn', 'up', '--ignore-externals'):
    for project, configuration in PROJECTS.items():
        for suffix in configuration.get('suffixes', SUFFIXES):
            for boost in configuration.get('boost', BOOST_VERSIONS):
                directory = '%s%s' % (project, suffix)
                if not install_boost(directory, boost):
                    raise "Boost install failed"
                else:
                    built += 1
                    if not execute('%s/%s/compile' % (directory, project)):
                        raise "Project failed"
                    else:
                        success.append([project, suffix, boost])

for project, suffix, boost in success:
    print "Success", project + suffix, "Boost", boost
print "Total built", built, "Total success", len(success)
