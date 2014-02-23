from configuration import *


def latest():
    for project, folder, configuration in projects():
        if configuration.get('gitflow', True):
            git(folder, 'checkout', 'develop')
        else:
            git(folder, 'checkout', 'master')
        git(folder, 'pull')
        git(folder, 'submodule', 'foreach',
            "\"(git branch -a | grep '. develop$' > /dev/null 2>&1)"
                " && git checkout develop || git checkout master\"")
        git(folder, 'submodule', 'foreach', "\"git pull\"")
        submods = git_capture(folder, 'submodule').split('\n')
        for submod in submods:
            if len(submod) and submod[0] == "+":
                name = submod.split(' ')[1]
                git(folder, 'add', name)
                git(folder, 'commit', '-m', '"$(git submodule summary %s)"' % name)


ACTIONS.append(latest)

