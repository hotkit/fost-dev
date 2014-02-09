from configuration import *


for project, configuration in PROJECTS.items():
    folder = configuration.get('folder', project)
    if not os.path.exists(folder):
        worked('git', 'clone', configuration['source'], folder)
        if configuration.get('gitflow', True):
            git(folder, 'flow', 'init', '-d')
    git(folder, 'submodule', 'init')
    git(folder, 'submodule', 'sync')
    git(folder, 'submodule', 'update')

