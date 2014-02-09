from configuration import *


for project, folder, configuration in projects():
    if configuration.get('gitflow', True):
        git(folder, 'fetch', 'origin')
        for branch in ['develop', 'master']:
            git(folder, 'checkout', branch)
            git(folder, 'merge', '--ff-only', 'remotes/origin/%s' % branch)
        git(folder, 'merge', '--no-ff', 'develop')
        git(folder, 'push')
        git(folder, 'checkout', 'develop')

