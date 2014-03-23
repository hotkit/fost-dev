from configuration import *


def push():
    git('.', 'push')
    for project, folder, configuration in projects():
        git(folder, 'push', '--all')
        git(folder, 'push', '--tags')
        for lib in configuration['libs']:
            subfolder = os.path.join(folder, lib)
            git(subfolder, 'push', '--all')
            git(subfolder, 'push', '--tags')


ACTIONS.append(push)

