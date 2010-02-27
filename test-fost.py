#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


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
BOOST_VERSIONS.append(['karmic'])


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
