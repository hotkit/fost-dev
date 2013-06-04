# -*- coding: utf-8 -*-
import os


def execute(program, *args):
    """
        Execute a program and return True if it worked.
    """
    command = '%s %s' % (program, ' '.join([str(a) for a in args]))
    print "Starting", command
    return os.system(command) == 0


if __name__ == "__main__":
    description = dict(
        package = 'fost-base',
        target = ('lucid', 32),
        release = "trunk",
        variant='release',
        control=dict(
            Package='fost-base',
            Version='4.13.06.1',
            Architecture='i386',
            Description='Core Fost libraries',
            Maintainer=u'Kirit Sælensminde <kirit@felspar.com>'))

    print "Packaging", description['package']

    chroot = "build-%s%s" % description['target']
    def schroot(program, *args):
        return execute('schroot', '--chroot', chroot,
                '--directory', '/tmp/', '--',
            program, *args)
    def schroot_sudo(program, *args):
        return execute('schroot', '--chroot', chroot, "-u", "root",
                '--directory', '/tmp/', '--',
            program, *args)
    def chroot_path(path):
        return os.path.join('/mnt/files4/chroot/%s/' % chroot, path)

    schroot_sudo("bash", "-c", '"rm -rf *"')
    schroot("mkdir", "-p", "/tmp/dest/DEBIAN")
    control = file(chroot_path('tmp/dest/DEBIAN/control'), 'w')
    for key, value in description['control'].items():
        if key != "Description":
            control.write((u"%s: %s\n" % (key, value)).encode('utf-8'))
    control.write('Description: %s\n' % description['control']['Description'])
    control.write('  The core of the Fost libraries together with the self-test program.\n');
    control.close()
    execute("cp", "debian/postinst", chroot_path('tmp/dest/DEBIAN/'))
    schroot_sudo("chmod", "g-w", 'dest/DEBIAN/control', 'dest/DEBIAN/postinst')
    schroot_sudo("chown", "root:root", 'dest/DEBIAN/control', 'dest/DEBIAN/postinst')
    # Get code and do build
    schroot("svn", "export", "--trust-server-cert", "--non-interactive",
        'https://svn.felspar.com/public/%s/%s'
            % (description['package'], description['release']),
        'source')
    schroot("source/Boost/install", description['target'][0])
    schroot_sudo("bash", "-c",
        "'PREFIX=/tmp/dest/usr/local/ source/%s/compile %s'" %
            (description['package'], description['variant']))
    # Fix up the structure
    schroot_sudo("bash", "-c",
        '"chrpath -d /tmp/dest/usr/local/bin/* /tmp/dest/usr/local/lib/*.so"')
    schroot_sudo("bash", "-c",
        '"chmod a-x /tmp/dest/usr/local/lib/*.so"')
    # Build and test package
    schroot("dpkg-deb", "--build", "dest")
    execute("lintian", chroot_path("tmp/dest.deb"))
