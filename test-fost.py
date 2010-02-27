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
BOOST_VERSIONS = list(range(38, 43))
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
    print "Starting", command
    return os.system(command) == 0


def install_boost(directory, version):
    """
        Installs the right version of Boost for the platform.
    """
    if not is_windows() and version != 'karmic':
        if not os.path.isdir('%s/Boost/1_%s_0' % (directory, version)):
            os.symlink('Boost/1_%s_0' % v, '%s/Boost/1_%s_0' % (directory, version))
        if not os.path.isdir('%s/Boost/boost/include/boost-1_%s' % (directory, version)):
            execute('%s/Boost/build' % directory, version, 0)
    if is_windows():
        return execute('%s/Boost/install' % directory, version, 0, '../../Boost')
    else:
        return execute('%s/Boost/install' % directory, version, 0)


built, success, failure = 0, [], []
if execute('svn', 'up', '--ignore-externals'):
    for project, configuration in PROJECTS.items():
        for suffix in configuration.get('suffixes', SUFFIXES):
            directory = '%s%s' % (project, suffix)
            if execute('svn', 'up', directory):
                for boost in configuration.get('boost', BOOST_VERSIONS):
                    if not install_boost(directory, boost):
                        raise "Boost install failed"
                    else:
                        built += 1
                        if not execute('%s/%s/compile' % (directory, project)):
                            raise "Project failed"
                        else:
                            success.append([project, suffix, boost])
            else:
                raise "svn up failed"

for project, suffix, boost in success:
    print "Success", project + suffix, "Boost", boost
print "Total built", built, "Total success", len(success)
