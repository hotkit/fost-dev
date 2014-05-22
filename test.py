from configuration import *


def dotests():
    def install_boost(directory, version):
        """
            Installs the right version of Boost for the platform.
        """
        if not is_windows() and not version in ['lucid', 'precise', 'quantal', 'raring', 'saucy', 'trusty']:
            if not os.path.isdir('Boost/1_%s_0' % version):
                execute('Boost/build', version, '0')
            path = '%s/Boost/1_%s_0' % (directory, version)
            if not os.path.isdir(path):
                print "Soft-linking to", path
                os.symlink('../../Boost/1_%s_0' % version, path)
            boost_folder = '%s/Boost/boost' % directory
            if not os.path.isdir(boost_folder):
                os.symlink('../../Boost/boost', boost_folder)
            if not os.path.isdir('%s/Boost/boost/include/boost-1_%s' % (directory, version)):
                execute('%s/Boost/build' % directory, version, 0)
        if is_windows():
            if not os.path.isdir('Boost/1_%s_0' % version):
                execute('Boost\\build', version, '0')
            return execute('%s/Boost/install' % directory, version, 0, '../../Boost')
        else:
            return execute('%s/Boost/install' % directory, version, 0)

    built, success, failure = 0, [], []
    for project, configuration in PROJECTS.items():
        if configuration.get('test', True) == False:
            continue
        directory = configuration.get('folder', project)
        for boost in configuration.get('boost', BOOST_VERSIONS):
            if not install_boost(directory, boost):
                raise "Boost install failed"
            else:
                for variant in configuration.get('variants', VARIANTS):
                    for target in configuration.get('targets', TARGETS):
                        built += 1
                        if not execute('./compile', directory, project, boost,  variant, target):
                            failure.append([project, boost, variant, target])
                        else:
                            success.append([project, boost, variant, target])
                            break

    def status(k, l):
        for project, boost, variant, target in l:
            print k, project, "Boost", boost, \
                "Variant:", variant, "Target:", target
    status("Success", success)
    status("Failure", failure)
    print "Total built", built, "Total success", len(success)

    assert len(failure) == 0, "At least one build failed"


ACTIONS.append(dotests)

