from configuration import *


def clone():
    for project, folder, configuration in projects():
        if not os.path.exists(folder):
            worked('git', 'clone', configuration['source'], folder)
            if configuration.get('gitflow', True):
                if is_windows():
                    git(folder, "checkout", "-b", "develop", "origin/develop")
                else:
                    git(folder, 'flow', 'init', '-d')
        else:
            git(folder, 'pull')
        git(folder, 'submodule', 'init')
        git(folder, 'submodule', 'sync')
        git(folder, 'submodule', 'update')
        if configuration.has_key('post-clone'):
            worked('cd', folder, '&&', *configuration['post-clone'])


ACTIONS.append(clone)

