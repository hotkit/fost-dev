# -*- coding: utf-8 -*-
import os


def execute(program, *args):
    """
        Execute a program and return True if it worked.
    """
    command = '%s %s' % (program, ' '.join([str(a) for a in args]))
    print "Starting", command
    return os.system(command) == 0

ARCH = {32: 'i386', 64: 'amd64'}

if __name__ == "__main__":
    description = dict(
        package = 'fost-base',
        target = ('lucid', 32),
        release = "trunk",
        variant='release',
        control=dict(
            Package='fost-base',
            Version='4.13.06.1',
            Section='fost-unstable',
            Architecture='i386',
            Priority='extra',
            Depends='libc6, libboost-date-time1.40.0, libboost-filesystem1.40.0, '
                'libboost-regex1.40.0, libboost-system1.40.0, libboost-thread1.40.0',
            Description='Core Fost libraries',
            Maintainer=u'Kirit Saelensminde <kirit@felspar.com>'))

    print "Packaging", description['package']

    chroot = "build-%s%s" % description['target']
    def schroot(program, *args):
        return execute('schroot', '--chroot', chroot,
                '--directory', '/tmp/', '--',
            program, *args)
    def schroot_bash(program, *args):
        return schroot('bash', '-c', '"%s %s"' % (program, ' '.join(args)))
    def schroot_sudo(program, *args):
        return execute('schroot', '--chroot', chroot, "-u", "root",
                '--directory', '/tmp/', '--',
            program, *args)
    def schroot_sudo_bash(program, *args):
        return schroot_sudo('bash', '-c', '"%s %s"' % (program, ' '.join(args)))
    def chroot_path(path):
        return os.path.join('/mnt/files4/chroot/%s/' % chroot, path)

    schroot_sudo_bash('rm', '-rf', '*')
    schroot("svn", "export", "--trust-server-cert", "--non-interactive",
        'https://svn.felspar.com/public/%s/%s'
            % (description['package'], description['release']),
        'source')
    schroot("mkdir", "-p", "/tmp/dest/DEBIAN")
    control = file(chroot_path('tmp/dest/DEBIAN/control'), 'w')
    for key, value in description['control'].items():
        if key != "Description":
            control.write((u"%s:%s\n" % (key, value)).encode('utf-8'))
    control.write('Description:%s\n' % description['control']['Description'])
    control.write(' The core of the Fost libraries together with the self-test program.\n');
    control.close()
    execute('cp', "debian/postinst", chroot_path('tmp/dest/DEBIAN/'))
    schroot('cp', "source/%s/ChangeLog" % description['package'], "dest/DEBIAN/changelog")
    schroot('gzip', '--best', 'dest/DEBIAN/changelog')
    copyright = file(chroot_path('tmp/dest/DEBIAN/copyright'), 'w')
    copyright.write('Copyright 1995-2013 Felspar Co. Ltd.\n\n')
    copyright.write(file(chroot_path('tmp/source/%s/LICENSE_1_0.txt' % description['package']), 'r').read())
    copyright.close()
    schroot_sudo_bash("chmod", "g-w", 'dest/DEBIAN/*')
    schroot_sudo_bash("chown", "root:root", 'dest/DEBIAN/*')
    schroot_sudo('mkdir', '-p', 'dest/usr/share/doc/%s' % description['package'])
    schroot_sudo('mv', 'dest/DEBIAN/copyright', 'dest/DEBIAN/changelog.gz', 'dest/usr/share/doc/%s/' % description['package'])
    # Do build
    schroot("source/Boost/install", description['target'][0])
    schroot_sudo_bash('PREFIX=/tmp/dest/usr/', 'source/%s/compile %s' %
            (description['package'], description['variant']))
    # Fix up the structure
    schroot_sudo_bash('chrpath', '-d', '/tmp/dest/usr/bin/*', '/tmp/dest/usr/lib/*.so')
    schroot_sudo_bash('chmod', 'a-x', '/tmp/dest/usr/lib/*.so')
    # Build and test package
    schroot("dpkg-deb", "--build", "dest")
    target = '/home/kirit/tmp/apt-inbox/%s_%s-%s1_%s.deb' % \
        (description['package'], description['control']['Version'],
            description['target'][0], ARCH[description['target'][1]])
    execute('cp', chroot_path('tmp/dest.deb'), target)
    execute("lintian", target)

