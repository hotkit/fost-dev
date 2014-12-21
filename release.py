import os
from configuration import *


VERSION = ARGS.pop(0)
def release():
    for project, folder, configuration in projects():
        libfolders = [os.path.join(folder, lib) for lib in configuration.get('libs', [])]
        for location in [folder] + libfolders:
            tags = git_capture(location, 'tag')
            if not VERSION in tags:
                git(location, 'fetch', 'origin')
                if configuration.get('gitflow', True):
                    for branch in ['develop', 'master']:
                        git(location, 'checkout', branch)
                        git(location, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
                else:
                    git(location, 'checkout', 'master')
                    git(location, 'merge', '--ff-only', 'remotes/origin/master')
                git(location, "tag", '-a', '-m', VERSION, VERSION)
                if configuration.get('gitflow', True):
                    git(location, 'checkout', 'develop')
                    git(location, 'merge', 'master', '--no-ff', '-m', VERSION)
            git(location, "push", "--tags")
        tagged = "../%s/%s" % (VERSION, folder)
        if not os.path.exists(tagged):
            worked('git', 'clone', '--recursive', '--branch', VERSION, folder, tagged)
        if configuration.get('test', True):
            if configuration.has_key('post-clone'):
                worked('cd', tagged, '&&', *configuration['post-clone'])
            worked('%s/Boost/install %s' % (tagged, OPTIONS['platform']))
            worked('./compile', tagged, project)

ACTIONS.append(release)

