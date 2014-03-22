from configuration import *


VERSION = ARGS.pop(0)
def release():
    for project, folder, configuration in projects():
        for location in [folder] + [os.path.join(folder, lib) for lib in configuration['libs']]:
            git(location, 'fetch', 'origin')
            if configuration.get('gitflow', True):
                for branch in ['develop', 'master']:
                    git(location, 'checkout', branch)
                    git(location, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
            else:
                git(location, 'merge', '--ff-only', 'remotes/origin/master')
            git(location, "tag", VERSION)
            if configuration.get('gitflow', True):
                git(location, 'checkout', 'develop')
        worked('git', 'clone', '--recursive', configuration['source'],
            "../%s/%s" % (VERSION, folder))
        worked('../%s/%s/build' % (VERSION, folder))

ACTIONS.append(release)

