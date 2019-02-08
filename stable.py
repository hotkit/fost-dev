from configuration import *


def stable():
    for project, folder, configuration in projects():
        if configuration.get('gitflow', True):
            git(folder, 'fetch', 'origin')
            for branch in ['develop', 'master']:
                git(folder, 'checkout', branch)
                git(folder, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
                git(folder, 'submodule', 'update', '--init', '--recursive')
            git(folder, 'merge', '--ff-only', 'develop')
            git(folder, 'push')
            git(folder, 'checkout', 'develop')
            git(folder, 'merge', 'master', '--ff-only')
            git(folder, 'push')


ACTIONS.append(stable)

