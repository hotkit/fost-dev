from configuration import *


def master():
    for project, folder, configuration in projects():
        if not os.path.exists(folder):
            worked('git', 'clone', configuration['source'], folder)
        else:
            git(folder, 'checkout', 'master')
            git(folder, 'pull')
            git(folder, 'remote', 'prune', 'origin')
        git(folder, 'submodule', 'init')
        if not is_windows():
        git(folder, 'submodule', 'sync', '--recursive')
        git(folder, 'submodule', 'update', '--init', '--recursive')
        if configuration.has_key('post-clone'):
            worked('cd', folder, '&&', *configuration['post-clone'])


ACTIONS.append(master)

