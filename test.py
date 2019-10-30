import os
import re
import sys
from distutils.dir_util import mkpath

from configuration import *


def dotests():
    def uses_boost(directory):
        """Returns `True` if there is a Boost folder inside the project
        which is taken to indicating that the project requires the Boost
        infrastructure to be set up."""
        return os.path.exists(os.path.join(directory, 'Boost'))
    def platform_boost(version):
        return re.compile(r'[a-z]+').match(str(version))
    def install_boost(directory, version, patch):
        """
            Installs the right version of Boost for the platform.
        """
        if not uses_boost(directory) or not version: return
        if not is_windows() and not platform_boost(version):
            if not os.path.isdir('Boost/1_%s_%s' % (version, patch)):
                execute('Boost/build', version, patch)
            path = '%s/Boost/1_%s_%s' % (directory, version, patch)
            if not os.path.isdir(path):
                print("Soft-linking to {}".format(path))
                os.symlink('../../Boost/1_%s_%s' % (version, patch), path)
            boost_folder = '%s/Boost/boost' % directory
            if not os.path.isdir(boost_folder):
                print("Soft-linking to {}".format(boost_folder))
                os.symlink('../../Boost/boost', boost_folder)
            if not os.path.isdir('%s/Boost/boost/1_%s_%s' % (directory, version, patch)):
                execute('%s/Boost/build' % directory, version, patch)
        if is_windows():
            if not os.path.isdir('Boost/1_%s_%s' % (version, patch)):
                execute('Boost\\build', version, patch)

    built, success, failure = 0, [], []
    for project, configuration in PROJECTS.items():
        runtests = configuration.get('cmake', True)
        directory = configuration.get('folder', project)
        if runtests == False:
            continue
        elif runtests == True:
            for toolset in TOOLSETS:
                for mode_name, mode_opts in MODES[toolset].items():
                    for bmajor, bminor, bpatch in BOOST:
                        if platform_boost(bminor) and toolset != 'gcc':
                            break
                        install_boost(directory, bminor, bpatch)
                        if bmajor and bminor:
                            bver = "%d.%d.%d" % (bmajor, bminor, bpatch)
                        else:
                            bver = ''
                        for variant in VARIANTS:
                            failed = False
                            targets = configuration.get('make', MAKE)
                            tname = toolset + '-' + bver + '-' + variant
                            if mode_name: tname += '-' + mode_name
                            buildpath = '/'.join([directory, 'build.tmp', tname])
                            mkpath(buildpath)
                            cmd1 = ([] if toolset == 'gcc' else ['CC=clang', 'CXX=clang++'])
                            cmd1 += mode_opts.env
                            cmd1 += CMAKE
                            cmd1 += ['cmake', '../..', '-G', 'Ninja']
                            cmd1 += CMAKE_POST
                            cmd1 += mode_opts.cmake
                            conf = lambda n, v: cmd1 + ['-D' + n + '=' + v]
                            cmd1 = conf('CMAKE_BUILD_TYPE', variant.title())
                            if uses_boost(directory):
                                if bmajor or bminor or bpatch: cmd1 = conf('BOOST_SEARCH', 'NO')
                                if bmajor: cmd1 = conf('BOOST_VMAJOR', str(bmajor))
                                if bminor: cmd1 = conf('BOOST_VMINOR', str(bminor))
                                if bpatch: cmd1 = conf('BOOST_VPATCH', str(bpatch))
                            cmd1 = conf('CMAKE_INSTALL_PREFIX', '../../dist-test/' + tname)
                            worked(*['cd', buildpath, '&&'] + cmd1)
                            for target in targets:
                                built += 1
                                if not execute('cd', buildpath, '&&', 'ninja', target):
                                    failure.append([project, (bmajor, bminor, bpatch), variant, [target], toolset, mode_name])
                                    failed = True
                                    break
                            if not failed:
                                success.append([project, (bmajor, bminor, bpatch), variant, targets, toolset, mode_name])
        else:
            assert execute('cd', project, '&&', runtests)

    def status(k, l):
        print('')
        for project, boost, variant, targets, toolset, mode in l:
            tmsg = ', '.join([t or "''" for t in targets]) if k == "Failure" else ''
            print('{} {} Boost {} {} {} {} {}'.format(k, project, boost, toolset, variant, tmsg, mode))
    status("Success", success)
    status("Failure", failure)
    print('\nTotal build {} Total success {}'.format(built, len(success)))
    if len(failure):
        print("At least one build failed")
        sys.exit(2)


ACTIONS.append(dotests)
