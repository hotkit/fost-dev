from configuration import *


def push():
    git('.', 'push')
    git('Boost', 'push')
    for project, folder, configuration in projects():
        git(folder, 'push')
        for lib in configuration.get('libs', []):
            subfolder = os.path.join(folder, lib)
            git(subfolder, 'push')


ACTIONS.append(push)

