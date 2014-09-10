from configuration import *


def stable():
    for project, folder, configuration in projects():
        if configuration.get('gitflow', True):
            for location in [folder] + [os.path.join(folder, lib) for lib in configuration['libs']]:
                git(location, 'fetch', 'origin')
                for branch in ['develop', 'master']:
                    git(location, 'checkout', branch)
                    git(location, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
                    git(location, 'submodule', 'update')
                git(location, 'merge', '--no-ff', 'develop', '-m',
                    '"Merge from develop\n$(git diff develop --stat)"')
                git(location, 'push')
                git(location, 'checkout', 'develop')


ACTIONS.append(stable)

