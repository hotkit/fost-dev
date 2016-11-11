from configuration import *


def stable():
    for project, folder, configuration in projects():
        if configuration.get('gitflow', True):
            libfolders = [os.path.join(folder, lib) for lib in configuration.get('libs', [])]
            for location in [folder] + libfolders:
                git(location, 'fetch', 'origin')
                for branch in ['develop', 'master']:
                    git(location, 'checkout', branch)
                    git(location, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
                    git(location, 'submodule', 'update', '--init', '--recursive')
                git(location, 'merge', '--no-ff', 'develop', '-m',
                    '"Merge from develop\n\n$(git diff develop --stat)"')
                git(location, 'push')
                git(location, 'checkout', 'develop')


ACTIONS.append(stable)

