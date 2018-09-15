from configuration import *


def stable():
    for project, folder, configuration in projects():
        if configuration.get('gitflow', True):
            git(folder, 'fetch', 'origin')
            for branch in ['develop', 'master']:
                git(folder, 'checkout', branch)
                git(folder, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
                git(folder, 'submodule', 'update', '--init', '--recursive')
            git(folder, 'merge', '--no-ff', 'develop', '-m',
                '"Merge from develop\n\n$(git diff develop --stat)"')
            git(folder, 'push')
            git(folder, 'checkout', 'develop')


ACTIONS.append(stable)

