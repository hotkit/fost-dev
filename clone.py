from configuration import *


for project, folder, configuration in projects():
    if not os.path.exists(folder):
        worked('git', 'clone', configuration['source'], folder)
        if configuration.get('gitflow', True):
            git(folder, 'flow', 'init', '-d')
    git(folder, 'submodule', 'init')
    git(folder, 'submodule', 'sync')
    git(folder, 'submodule', 'update')

