from configuration import *


for project, configuration in PROJECTS.items():
    if not os.exists(project):
        worked('git', 'clone', configuration['source'], project)
        worked('cd', project, '&&', 'git', 'flow', 'init', '-d')

