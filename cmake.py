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
            for toolset in TOOLSETS:
                for bmajor, bminor, bpatch in [(1, 65, 0), (1, 66, 0)]:
                    bver = "%d.%d.%d" % (bmajor, bminor, bpatch)
                    for variant in ["Release", "Debug"]:
                        built += 1
                        tname = toolset + '-' + bver + '-'+ variant
                        buildpath = '/'.join([project, 'build.tmp', tname])
                        mkpath(buildpath)
                        cmd1 = ([] if toolset == 'gcc' else ['CC=clang', 'CXX=clang++']) + ['cmake', '../..', '-G', 'Ninja']
                        conf = lambda n, v: cmd1 + ['-D' + n + '=' + v]
                        cmd1 = conf('CMAKE_BUILD_TYPE', variant)
                        cmd1 = conf('BOOST_VMAJOR', str(bmajor))
                        cmd1 = conf('BOOST_VMINOR', str(bminor))
                        cmd1 = conf('BOOST_VPATCH', str(bpatch))
                        cmd1 = conf('CMAKE_INSTALL_PREFIX', '../../dist-' + tname)
                        worked(*['cd', buildpath, '&&'] + cmd1)
                        worked('cd', buildpath, '&&', 'ninja', 'check')
                        worked('cd', buildpath, '&&', 'ninja', 'install')
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
