from configuration import *
from distutils.dir_util import mkpath
import os
import re
import sys


def dotests():
    def platform_boost(version):
        return re.compile(r'[a-z]+').match(unicode(version))
    def install_boost(directory, version):
        """
            Installs the right version of Boost for the platform.
        """
        if not os.path.exists(os.path.join(directory, 'Boost')): return
        if not is_windows() and not platform_boost(version):
            if not os.path.isdir('Boost/1_%s_0' % version):
                execute('Boost/build', version, '0')
            path = '%s/Boost/1_%s_0' % (directory, version)
            if not os.path.isdir(path):
                print "Soft-linking to", path
                os.symlink('../../Boost/1_%s_0' % version, path)
            boost_folder = '%s/Boost/boost' % directory
            if not os.path.isdir(boost_folder):
                print "Soft-linking to", boost_folder
                os.symlink('../../Boost/boost', boost_folder)
            if not os.path.isdir('%s/Boost/boost/1_%s_0' % (directory, version)):
                execute('%s/Boost/build' % directory, version, 0)
        if is_windows():
            if not os.path.isdir('Boost/1_%s_0' % version):
                execute('Boost\\build', version, '0')

    built, success, failure = 0, [], []
    for project, configuration in PROJECTS.items():
        runtests = configuration.get('cmake', True)
        directory = configuration.get('folder', project)
        if runtests == False:
            continue
        elif runtests == True:
            for toolset in TOOLSETS:
                for bmajor, bminor, bpatch in BOOST:
                    if platform_boost(bminor) and toolset != 'gcc':
                        break
                    install_boost(directory, bminor)
                    bver = "%d.%d.%d" % (bmajor, bminor, bpatch)
                    for variant in VARIANTS:
                        failed = False
                        targets = configuration.get('make', MAKE)
                        for target in targets:
                            built += 1
                            tname = toolset + '-' + bver + '-'+ variant
                            buildpath = '/'.join([directory, 'build.tmp', tname])
                            mkpath(buildpath)
                            cmd1 = ([] if toolset == 'gcc' else ['CC=clang', 'CXX=clang++']) + ['cmake', '../..', '-G', 'Ninja']
                            conf = lambda n, v: cmd1 + ['-D' + n + '=' + v]
                            cmd1 = conf('CMAKE_BUILD_TYPE', variant.title())
                            cmd1 = conf('BOOST_VMAJOR', str(bmajor))
                            cmd1 = conf('BOOST_VMINOR', str(bminor))
                            cmd1 = conf('BOOST_VPATCH', str(bpatch))
                            cmd1 = conf('CMAKE_INSTALL_PREFIX', '../../dist-test/' + tname)
                            worked(*['cd', buildpath, '&&'] + cmd1)
                            if not execute('cd', buildpath, '&&', 'ninja', target):
                                failure.append([project, (bmajor, bminor, bpatch), variant, [target], toolset])
                                failed = True
                                break
                        if not failed:
                            success.append([project, (bmajor, bminor, bpatch), variant, targets, toolset])
        else:
            assert execute('cd', project, '&&', runtests)

    def status(k, l):
        print
        for project, boost, variant, targets, toolset in l:
            tmsg = ', '.join([t or "''" for t in targets]) if k == "Failure" else ''
            print k, project, "Boost", boost, toolset, variant, tmsg
    status("Success", success)
    status("Failure", failure)
    print "\nTotal built", built, "Total success", len(success)
    if len(failure):
        print("At least one build failed")
        sys.exit(2)


ACTIONS.append(dotests)
