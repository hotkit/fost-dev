from configuration import *


for project, configuration in PROJECTS.items():
    def git(directory, *args):
        worked('cd', directory, '&&', 'git', *args)
    git(project, 'push')
    git(project, 'push', '--tags')
    for lib in configuration['libs']:
        folder = os.path.join(project, lib)
        git(folder, 'push')
        git(folder, 'push', '--tags')

