from configuration import *


for project, configuration in PROJECTS.items():
    if not os.path.exists(project):
        worked('git', 'clone', configuration['source'], project)
        if configuration.get('gitflow', True):
            git(project, 'flow', 'init', '-d')

