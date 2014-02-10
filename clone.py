from configuration import *


for project, folder, configuration in projects():
    if not os.path.exists(folder):
        worked('git', 'clone', configuration['source'], folder)
        if configuration.get('gitflow', True):
            git(folder, 'flow', 'init', '-d')
    else:
        git(folder, 'pull')
    git(folder, 'submodule', 'init')
    git(folder, 'submodule', 'sync')
    git(folder, 'submodule', 'update')
    if configuration.has_key('post-clone'):
        worked('cd', folder, '&&', *configuration['post-clone'])

