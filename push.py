from configuration import *


git('.', 'push')
for project, configuration in PROJECTS.items():
    git(project, 'push')
    git(project, 'push', '--tags')
    for lib in configuration['libs']:
        folder = os.path.join(project, lib)
        git(folder, 'push')
        git(folder, 'push', '--tags')

