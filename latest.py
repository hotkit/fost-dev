from configuration import *


def latest():
    def submodules(folder):
        submods = git_capture(folder, 'submodule').split('\n')
        for submod in submods:
            if len(submod) and submod[0] == "+":
                name = submod.split(' ')[1]
                git(folder, 'add', name)
                with open('/tmp/m.txt', 'w') as t:
                    t.write("Latest %s\n\n" % name)
                git(folder, 'submodule', 'summary', name, '>> /tmp/m.txt')
                git(folder, 'commit', '-F', '/tmp/m.txt')
    def get_latest(gitflow, folder, libs):
        if gitflow:
            git(folder, 'checkout', 'develop')
        else:
            git(folder, 'checkout', 'master')
        git(folder, 'pull')
        git(folder, 'submodule', 'foreach', '--recursive',
            "\"(git branch -a | grep '. develop$' > /dev/null 2>&1)"
                " && git checkout develop || git checkout master\"")
        git(folder, 'submodule', 'foreach', "\"git pull\"")
        git(folder, 'submodule', 'foreach', "\"git submodule init\"")
        git(folder, 'submodule', 'foreach', "\"git submodule sync --recursive\"")
        git(folder, 'submodule', 'foreach', "\"git submodule update --init --recursive\"")
        submodules(folder)
        for lib in libs:
            submodules(os.path.join(folder, lib))
    get_latest(False, ".", [])
    for project, folder, configuration in projects():
        get_latest(configuration.get('gitflow', True), folder, configuration.get('libs', []))


ACTIONS.append(latest)

