from configuration import *


def latest():
    def get_latest(gitflow, folder):
        if gitflow:
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
    get_latest(False, ".")
    for project, folder, configuration in projects():
        get_latest(configuration.get('gitflow', True), folder)


ACTIONS.append(latest)

