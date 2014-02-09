from configuration import *


git('.', 'push')
for project, folder, configuration in projects():
    git(folder, 'push')
    git(folder, 'push', '--tags')
    for lib in configuration['libs']:
        subfolder = os.path.join(project, lib)
        git(subfolder, 'push')
        git(subfolder, 'push', '--tags')

