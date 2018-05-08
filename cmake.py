from configuration import *
import os
from distutils.dir_util import mkpath


def dotests():
    built, success, failure = 0, [], []
    for project, configuration in PROJECTS.items():
        runtests = configuration.get('cmake', True)
        directory = configuration.get('folder', project)
        if runtests == False:
            continue
        elif runtests == True:
            for toolset in ['gcc', 'clang']:
                for variant in ["Release", "Debug"]:
                    built += 1
                    buildpath = '/'.join([project, 'build.tmp', toolset, variant])
                    mkpath(buildpath)
                    cmd1 = ([] if toolset == 'gcc' else ['CC=clang', 'CXX=clang++']) + ['cmake', '../../..', '-G', 'Ninja']
                    worked(*['cd', buildpath, '&&'] + cmd1)
                    cmd2 = ['ninja', 'check']
                    worked(*['cd', buildpath, '&&'] + cmd2)
        else:
            assert execute('cd', project, '&&', runtests)

    def status(k, l):
        for project, boost, variant, target, toolset in l:
            print k, project, "Boost", boost, \
                "Toolset:", toolset, "Variant:", variant, "Target:", target
    status("Success", success)
    status("Failure", failure)
    print "Total built", built, "Total success", len(success)

    assert len(failure) == 0, "At least one build failed"


ACTIONS.append(dotests)
