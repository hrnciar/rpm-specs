# The canonical copy of this spec file is upstream at:
# https://github.com/projectatomic/rpm-ostree/blob/master/packaging/rpm-ostree.spec.in

Summary: Hybrid image/package system
Name: rpm-ostree
Version: 2020.3
Release: 1%{?dist}
#VCS: https://github.com/cgwalters/rpm-ostree
# This tarball is generated via "cd packaging && make -f Makefile.dist-packaging dist-snapshot"
# in the upstream git.  If rust is enabled, it contains vendored sources.
Source0: rpm-ostree-%{version}.tar.xz
License: LGPLv2+
URL: https://github.com/projectatomic/rpm-ostree

ExclusiveArch: %{rust_arches}

%if 0%{?rhel} && !0%{?eln}
BuildRequires: rust-toolset
%else
BuildRequires: cargo
BuildRequires: rust
%endif

# RHEL8 doesn't ship zchunk today.  See also the comments
# in configure.ac around this as libdnf/librepo need to be in
# sync, and today we bundle libdnf but not librepo.
%if 0%{?rhel} && 0%{?rhel} <= 8
%bcond_with zchunk
%else
%bcond_without zchunk
%endif

# For the autofiles bits below
BuildRequires: /usr/bin/python3
# We always run autogen.sh
BuildRequires: autoconf automake libtool git
# For docs
BuildRequires: chrpath
BuildRequires: gtk-doc
BuildRequires: gperf
BuildRequires: gnome-common
BuildRequires: /usr/bin/g-ir-scanner
# Core requirements
# One way to check this: `objdump -p /path/to/rpm-ostree | grep LIBOSTREE` and pick the highest (though that might miss e.g. new struct members)
BuildRequires: pkgconfig(ostree-1) >= 2019.2
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(rpm)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: libcap-devel
BuildRequires: libattr-devel

# We currently interact directly with librepo
BuildRequires: pkgconfig(librepo)

# Needed by curl-rust
BuildRequires: pkgconfig(libcurl)

# libdnf bundling
# We're using RPATH to pick up our bundled version
%global __requires_exclude ^libdnf[.]so[.].*$

# Our bundled libdnf.so.2 is for us only
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$

BuildRequires: cmake
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(libsolv)

# We need g++ for libdnf
BuildRequires: gcc-c++


# more libdnf build deps (see libdnf's spec for versions)
%global swig_version 3.0.12
%global libmodulemd_version 2.5.0
BuildRequires:  swig >= %{swig_version}
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(smartcols)
%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= 0.9.11
%endif
BuildRequires:  gpgme-devel

Requires:       libmodulemd%{?_isa} >= %{libmodulemd_version}

# For now...see https://github.com/projectatomic/rpm-ostree/pull/637
# and https://github.com/fedora-infra/fedmsg-atomic-composer/pull/17
# etc.  We'll drop this dependency at some point in the future when
# rpm-ostree wraps more of ostree (such as `ostree admin unlock` etc.)
Requires: ostree
Requires: bubblewrap
Requires: fuse

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
rpm-ostree is a hybrid image/package system.  It supports
"composing" packages on a build server into an OSTree repository,
which can then be replicated by client systems with atomic upgrades.
Additionally, unlike many "pure" image systems, with rpm-ostree
each client system can layer on additional packages, providing
a "best of both worlds" approach.

%package libs
Summary: Shared library for rpm-ostree

%description libs
The %{name}-libs package includes the shared library for %{name}.

%package devel
Summary: Development headers for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files for %{name}-libs.

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules --enable-gtk-doc
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p -c"
find $RPM_BUILD_ROOT -name '*.la' -delete

# I try to do continuous delivery via rpmdistro-gitoverlay while
# reusing the existing spec files.  Currently RPM only supports
# mandatory file entries.  What this is doing is making each file
# entry optional - if it exists it will be picked up.  That
# way the same spec file works more easily across multiple versions where e.g. an
# older version might not have a systemd unit file.
cat > autofiles.py <<EOF
import os,sys,glob
os.chdir(os.environ['RPM_BUILD_ROOT'])
for line in sys.argv[1:]:
    if line == '':
        break
    if line[0] != '/':
        sys.stdout.write(line + '\n')
    else:
        files = glob.glob(line[1:])
        if len(files) > 0:
            sys.stderr.write('{0} matched {1} files\n'.format(line, len(files)))
            sys.stdout.write(line + '\n')
        else:
            sys.stderr.write('{0} did not match any files\n'.format(line))
EOF
PYTHON=python3
if ! test -x /usr/bin/python3; then
    PYTHON=python2
fi
$PYTHON autofiles.py > files \
  '%{_bindir}/*' \
  '%{_libdir}/%{name}' \
  '%{_mandir}/man*/*' \
  '%{_datadir}/dbus-1/system.d/*' \
  '%{_sysconfdir}/rpm-ostreed.conf' \
  '%{_prefix}/lib/systemd/system/*' \
  '%{_libexecdir}/rpm-ostree*' \
  '%{_datadir}/polkit-1/actions/*.policy' \
  '%{_datadir}/dbus-1/system-services' \
  '%{_datadir}/bash-completion/completions/*'

$PYTHON autofiles.py > files.lib \
  '%{_libdir}/*.so.*' \
  '%{_libdir}/girepository-1.0/*.typelib'

$PYTHON autofiles.py > files.devel \
  '%{_libdir}/lib*.so' \
  '%{_includedir}/*' \
  '%{_datadir}/dbus-1/interfaces/org.projectatomic.rpmostree1.xml' \
  '%{_libdir}/pkgconfig/*' \
  '%{_datadir}/gtk-doc/html/*' \
  '%{_datadir}/gir-1.0/*-1.0.gir'

%files -f files
%doc COPYING.GPL COPYING.LGPL LICENSE README.md

%files libs -f files.lib

%files devel -f files.devel
%changelog
* Wed Feb 05 2020 Jonathan Lebon <jonathan@jlebon.com> - 2020.3-1
- New upstream version
  https://github.com/coreos/rpm-ostree/releases/tag/v2020.3

* Fri May 15 2020 Jonathan Lebon <jonathan@jlebon.com> - 2020.2-3
- Backport https://github.com/coreos/rpm-ostree/pull/2096
  See https://github.com/coreos/fedora-coreos-tracker/issues/481

* Fri May 15 2020 Colin Walters <walters@verbum.org> - 2020.2-2
- https://github.com/coreos/rpm-ostree/releases/tag/v2020.2

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2020.1.80.g3ec5e287-2
- Rebuild (json-c)

* Mon Apr 20 2020 Jonathan Lebon <jonathan@jlebon.com> - 2020.1.80.g3ec5e287-1
- git master snapshot for using strict mode and lockfile-repos in FCOS:
  https://github.com/coreos/rpm-ostree/pull/1858
  https://github.com/coreos/rpm-ostree/pull/2058
  https://github.com/coreos/fedora-coreos-tracker/issues/454

* Fri Mar 13 2020 Colin Walters <walters@verbum.org> - 2020.1.21.ge9011530-2
- Backport https://github.com/coreos/rpm-ostree/pull/2015
  See https://github.com/coreos/fedora-coreos-tracker/issues/343

* Thu Feb 27 2020 Jonathan Lebon <jonathan@jlebon.com> - 2020.1.21.ge9011530-1
- git master snapshot for using base initramfs kargs in RHCOS:
  https://github.com/coreos/rpm-ostree/pull/1998
  https://github.com/coreos/rpm-ostree/pull/1997
  https://bugzilla.redhat.com/show_bug.cgi?id=1806588

* Wed Feb 05 2020 Jonathan Lebon <jonathan@jlebon.com> - 2020.1-1
- New upstream version

* Tue Feb 04 2020 Jonathan Lebon <jonathan@jlebon.com> - 2019.7.31.g70c38563-1
- git master snapshot for Silverblue rawhide compose fixes
  https://pagure.io/releng/failed-composes/issue/717
  https://pagure.io/releng/failed-composes/issue/929
  https://github.com/rpm-software-management/libdnf/pull/885

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Jonathan Lebon <jonathan@jlebon.com> - 2019.7-2
- Backport patch for Silverblue composes:
  https://pagure.io/releng/failed-composes/issue/717

* Thu Dec 19 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.7-1
- New upstream version

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 2019.6.24.gfec61ce5-2
- Fix missing #includes for gcc-10

* Thu Oct 31 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.6.27.g3b8a1ec6-1
- git master snapshot for dracut cpio cap_mknod fix:
  https://github.com/coreos/rpm-ostree/pull/1946

* Thu Oct 31 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.6.24.gfec61ce5-1
- git master snapshot for HMAC path fix for FIPS:
  https://github.com/coreos/rpm-ostree/pull/1934

* Wed Sep 25 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.6-1
- New upstream version

* Thu Aug 22 2019 Colin Walters <walters@verbum.org> - 2019.5.7.gcac5aa41-3
- New upstream git snapshot, mainly for backporting the arch-includes conditionals
  to aid Fedora CoreOS on s390x.

* Wed Jul 31 2019 Stephen Gallagher <sgallagh@redhat.com> - 2019.5-2
- Fix libmodulemd dependencies

* Thu Jul 25 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.5-1
- New upstream version

* Fri Jul 19 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.4.39.g8d90d03d-1
- git master snapshot for --parent and lockfile overrides
  https://github.com/projectatomic/rpm-ostree/pull/1871
  https://github.com/projectatomic/rpm-ostree/pull/1867

* Fri Jul 12 2019 Colin Walters <walters@verbum.org> - 2019.4.28.g44395673-3
- Update rpmostree-rust.h in sources

* Fri Jul 12 2019 Colin Walters <walters@verbum.org> - 2019.4.28.g44395673-2
- Update with git snapshot for zstd support

* Wed Jul 10 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.4.27.gb381e029-1
- git master snapshot for add-commit-metadata
  https://github.com/projectatomic/rpm-ostree/pull/1865/

* Fri Jun 14 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.4.15.gbbc9aa9f-1
- git master snapshot for OSTree layers
  https://github.com/projectatomic/rpm-ostree/pull/1830/

* Mon Jun 10 22:13:22 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019.4.10.gc1cc0827-3
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:05 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019.4.10.gc1cc0827-2
- Rebuild for RPM 4.15

* Thu Jun 06 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.4.10.gc1cc0827-1
- git master snapshot for lockfile
  https://github.com/projectatomic/rpm-ostree/pull/1745/

* Tue May 28 2019 Dusty Mabe <dusty@dustymabe.com> - 2019.4-3
- Add back in ppc64le and ppc64

* Thu May 23 2019 Dusty Mabe <dusty@dustymabe.com> - 2019.4-2
- Backport patch for db diff --format=json

* Tue May 21 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.4-1
- New upstream version

* Mon May 06 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.3.5.g0da9f997-2
- Add temporary hack to avoid UTF-8 for Bodhi
  https://pagure.io/releng/issue/8330

* Tue Apr 09 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.3.5.g0da9f997-1
- git master snapshot to test coreos-continuous tag

* Wed Mar 27 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.3-1
- New upstream version

* Thu Feb 14 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.2-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Jonathan Lebon <jonathan@jlebon.com> - 2019.1-1
- New upstream version

* Fri Dec 14 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.10-1
- New upstream version

* Tue Dec 04 2018 Jonathan Lebon <jonathan@jlebon.com>
- Simplify Rust conditionals

* Fri Nov 02 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.9-3
- Backport patch for https://pagure.io/dusty/failed-composes/issue/956

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.9-2
- Rebuild for libsolv 0.7

* Sun Oct 28 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.9-1
- New upstream version

* Tue Sep 11 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.8-1
- New upstream version

* Thu Aug 09 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.7-1
- New upstream version

* Wed Aug 01 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.6.42.gda27b94b-1
- git master snapshot for https://bugzilla.redhat.com/show_bug.cgi?id=1565647

* Mon Jul 30 2018 Colin Walters <walters@verbum.org> - 2018.6-4
- Backport patch for https://bugzilla.redhat.com/show_bug.cgi?id=1607223
  from https://github.com/projectatomic/rpm-ostree/pull/1469
- Also https://github.com/projectatomic/rpm-ostree/pull/1461

* Mon Jul 16 2018 Colin Walters <walters@verbum.org> - 2018.6-3
- Make build python3-only compatible for distributions that want that

* Fri Jun 29 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.6-2
- Rebuild for yummy Rusty bitsy

* Fri Jun 29 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.6-1
- New upstream version

* Tue May 15 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.5-1
- New upstream version

* Mon Mar 26 2018 Jonathan Lebon <jonathan@jlebon.com> - 2018.4-1
- New upstream version

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2018.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Jonathan Lebon <jlebon@redhat.com> - 2018.3-3
- Add BR on gcc-c++

* Thu Mar 01 2018 Dusty Mabe <dusty@dustymabe.com> - 2018.3-2
- backport treating FUSE as netfs
- See https://github.com/projectatomic/rpm-ostree/pull/1285

* Sun Feb 18 2018 Jonathan Lebon <jlebon@redhat.com> - 2018.3-1
- New upstream version (minor bugfix release)

* Fri Feb 16 2018 Jonathan Lebon <jlebon@redhat.com> - 2018.2-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Dusty Mabe <dusty@dustymabe.com> - 2018.1-2
- Revert the ostree:// formatting in the output.
- See https://github.com/projectatomic/rpm-ostree/pull/1136#issuecomment-358122137

* Mon Jan 15 2018 Colin Walters <walters@verbum.org> - 2018.1-1
- https://github.com/projectatomic/rpm-ostree/releases/tag/v2018.1

* Tue Dec 05 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.11-1
- New upstream version

* Wed Nov 22 2017 Colin Walters <walters@verbum.org> - 2017.10-3
- Backport patch for NFS issues
- https://pagure.io/atomic-wg/issue/387

* Sun Nov 12 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.10-2
- Backport fix for --repo handling
  https://github.com/projectatomic/rpm-ostree/pull/1101

* Thu Nov 02 2017 Colin Walters <walters@verbum.org> - 2017.10-1
- https://github.com/projectatomic/rpm-ostree/releases/tag/v2017.10

* Mon Sep 25 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.9-1
- New upstream version

* Mon Aug 21 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.8-2
- Patch to allow metadata_expire=0
  https://github.com/projectatomic/rpm-ostree/issues/930

* Fri Aug 18 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.8-1
- New upstream version

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.7-7
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.7-6
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.7-3
- Tweak new pkg name to rpm-ostree-libs to be more consistent with the main
  package name and ostree's ostree-libs.

* Fri Jul 21 2017 Colin Walters <walters@verbum.org> - 2017.7-2
- Enable introspection, rename shared lib to librpmostree
  Due to an oversight, we were not actually building with introspection.
  Fix that.  And while we are here, split out a shared library package,
  so that e.g. containers can do `from gi.repository import RpmOstree`
  without dragging in the systemd service, etc. (RHBZ#1473701)

* Mon Jul 10 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.7-1
- New upstream version

* Sat Jun 24 2017 Colin Walters <walters@verbum.org>
- Update to git snapshot to help debug compose failure

* Wed May 31 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.6-3
- Make sure we don't auto-provide libdnf (RHBZ#1457089)

* Fri May 26 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.6-2
- Bump libostree dep

* Fri May 26 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.6-1
- New upstream version

* Fri Apr 28 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.5-2
- Bump libostree dep and rebuild in override

* Fri Apr 28 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.5-1
- New upstream version

* Fri Apr 14 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.4-2
- Backport patch to allow unprivileged `rpm-ostree status`

* Thu Apr 13 2017 Jonathan Lebon <jlebon@redhat.com> - 2017.4-1
- New upstream version.

* Fri Apr 07 2017 Colin Walters <walters@verbum.org> - 2017.3-4
- Backport patch to add API devices for running on CentOS 7
  https://github.com/projectatomic/rpm-ostree/issues/727

* Thu Mar 16 2017 Colin Walters <walters@verbum.org> - 2017.3-3
- Add patch to fix f26 altfiles

* Fri Mar 10 2017 Colin Walters <walters@verbum.org> - 2017.3-2
- Backport patch for running in koji

* Mon Mar 06 2017 Colin Walters <walters@verbum.org> - 2017.3-1
- New upstream version
  Fixes: CVE-2017-2623
  Resolves: #1422157

* Fri Mar 03 2017 Colin Walters <walters@verbum.org> - 2017.2-5
- Add patch to bump requires for ostree

* Mon Feb 27 2017 Colin Walters <walters@verbum.org> - 2017.2-4
- Add requires on ostree

* Sat Feb 18 2017 Colin Walters <walters@verbum.org> - 2017.2-3
- Add patch for gperf 3.1 compatibility
  Resolves: #1424268

* Wed Feb 15 2017 Colin Walters <walters@verbum.org> - 2017.2-2
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Colin Walters <walters@verbum.org> - 2017.1-3
- Back out netns usage for now for https://pagure.io/releng/issue/6602

* Sun Jan 22 2017 Colin Walters <walters@verbum.org> - 2017.1-2
- New upstream version

* Mon Dec 12 2016 walters@redhat.com - 2016.13-1
- New upstream version

* Sat Nov 26 2016 walters@redhat.com - 2016.12-4
- Backport patch to fix install-langs

* Tue Nov 15 2016 walters@redhat.com - 2016.11-2
- New upstream version

* Mon Oct 24 2016 walters@verbum.org - 2016.11-1
- New upstream version

* Fri Oct 07 2016 walters@redhat.com - 2016.10-1
- New upstream version

* Thu Sep 08 2016 walters@redhat.com - 2016.9-1
- New upstream version

* Thu Sep 08 2016 walters@redhat.com - 2016.8-1
- New upstream version

* Thu Sep 01 2016 walters@redhat.com - 2016.7-4
- Add requires on fuse https://github.com/projectatomic/rpm-ostree/issues/443

* Wed Aug 31 2016 Colin Walters <walters@verbum.org> - 2016.7-3
- Backport patch for running inside mock

* Sat Aug 13 2016 walters@redhat.com - 2016.6-3
- New upstream version

* Sat Aug 13 2016 Colin Walters <walters@verbum.org> - 2016.6-2
- Backport patches from master to fix non-containerized composes

* Thu Aug 11 2016 walters@redhat.com - 2016.6-1
- New upstream version

* Mon Jul 25 2016 Colin Walters <walters@verbum.org> - 2016.5-1
- New upstream version

* Fri Jul 08 2016 walters@verbum.org - 2016.4-2
- Require bubblewrap

* Fri Jul 08 2016 walters@redhat.com - 2016.4-1
- New upstream version

* Thu Jul 07 2016 Colin Walters <walters@verbum.org> - 2016.3.5.g4219a96-1
- Backport fixes from https://github.com/projectatomic/rpm-ostree/commits/2016.3-fixes

* Wed Jun 15 2016 Colin Walters <walters@verbum.org> - 2016.3.3.g17fb980-2
- Backport fixes from https://github.com/projectatomic/rpm-ostree/commits/2016.3-fixes

* Fri May 20 2016 Colin Walters <walters@redhat.com> - 2016.3-2
- New upstream version

* Thu Mar 31 2016 Colin Walters <walters@redhat.com> - 2016.1-3
- Backport patch to fix Fedora composes writing data into source file:/// URIs

* Thu Mar 24 2016 Colin Walters <walters@redhat.com> - 2016.1-2
- New upstream version

* Tue Feb 23 2016 Colin Walters <walters@redhat.com> - 2015.11.43.ga2c052b-2
- New git snapshot, just getting some new code out there
- We are now bundling a copy of libhif, as otherwise coordinated releases with
  PackageKit/dnf would be required, and we are not ready for that yet.

* Wed Feb 10 2016 Matthew Barnes <mbarnes@redhat.com> - 2015.11-3
- Fix URL: https://github.com/projectatomic/rpm-ostree

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Colin Walters <walters@redhat.com> - 2015.11-1
- New upstream version

* Sat Nov 21 2015 Colin Walters <walters@redhat.com> - 2015.10-1
- New upstream version

* Mon Nov 09 2015 Colin Walters <walters@redhat.com> - 2015.9-4
- Fix files list for -devel, which should in turn fix Anaconda
  builds which pull in rpm-ostree, but should not have devel bits.

* Sat Oct 31 2015 Colin Walters <walters@redhat.com> - 2015.9-3
- Add patch that should fix bodhis use of --workdir-tmpfs

* Sat Sep 05 2015 Kalev Lember <klember@redhat.com> - 2015.9-2
- Rebuilt for librpm soname bump

* Wed Aug 26 2015 Colin Walters <walters@redhat.com> - 2015.9-2
- New upstream version

* Tue Aug 04 2015 Colin Walters <walters@redhat.com> - 2015.8-1
- New upstream version

* Mon Jul 27 2015 Colin Walters <walters@redhat.com> - 2015.7-5
- rebuilt

* Mon Jul 20 2015 Colin Walters <walters@redhat.com> - 2015.7-4
- Rebuild for CentOS update to libhif

* Tue Jun 16 2015 Colin Walters <walters@redhat.com> - 2015.7-3
- Rebuild to pick up hif_source_set_required()

* Mon Jun 15 2015 Colin Walters <walters@redhat.com> - 2015.7-2
- New upstream version

* Tue Jun 09 2015 Colin Walters <walters@redhat.com> - 2015.6-2
- New upstream version

* Tue May 12 2015 Colin Walters <walters@redhat.com> - 2015.5-3
- Add patch to fix rawhide composes

* Mon May 11 2015 Colin Walters <walters@redhat.com> - 2015.5-2
- New upstream release
  Adds shared library and -devel subpackage

* Fri Apr 10 2015 Colin Walters <walters@redhat.com> - 2015.4-2
- New upstream release
  Port to libhif, drops dependency on yum.

* Thu Apr 09 2015 Colin Walters <walters@redhat.com> - 2015.3-8
- Cherry pick f21 patch to disable read only /etc with yum which
  breaks when run inside docker

* Wed Apr 08 2015 Colin Walters <walters@redhat.com> - 2015.3-7
- Add patch to use yum-deprecated
  Resolves: #1209695

* Fri Feb 27 2015 Colin Walters <walters@redhat.com> - 2015.3-5
- Drop /usr/bin/atomic, now provided by the "atomic" package

* Fri Feb 06 2015 Dennis Gilmore <dennis@ausil.us> - 2015.3-4
- add git to BuildRequires

* Thu Feb 05 2015 Colin Walters <walters@redhat.com> - 2015.3-3
- Adapt to Hawkey 0.5.3 API break

* Thu Feb 05 2015 Dennis Gilmore <dennis@ausil.us> - 2015.3-3
- rebuild for libhawkey soname bump

* Fri Jan 23 2015 Colin Walters <walters@redhat.com> - 2015.3-2
- New upstream release

* Thu Jan 08 2015 Colin Walters <walters@redhat.com> - 2015.2-1
- New upstream release

* Wed Dec 17 2014 Colin Walters <walters@redhat.com> - 2014.114-2
- New upstream release

* Tue Nov 25 2014 Colin Walters <walters@redhat.com> - 2014.113-1
- New upstream release

* Mon Nov 24 2014 Colin Walters <walters@redhat.com> - 2014.112-1
- New upstream release

* Mon Nov 17 2014 Colin Walters <walters@redhat.com> - 2014.111-1
- New upstream release

* Fri Nov 14 2014 Colin Walters <walters@redhat.com> - 2014.110-1
- New upstream release

* Fri Oct 24 2014 Colin Walters <walters@redhat.com> - 2014.109-1
- New upstream release

* Sat Oct 04 2014 Colin Walters <walters@redhat.com> - 2014.107-2
- New upstream release

* Mon Sep 08 2014 Colin Walters <walters@redhat.com> - 2014.106-3
- New upstream release
- Bump requirement on ostree

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Colin Walters <walters@verbum.org> - 2014.105-2
- New upstream release

* Sun Jul 13 2014 Colin Walters <walters@verbum.org>
- New upstream release

* Sat Jun 21 2014 Colin Walters <walters@verbum.org>
- New upstream release
- Bump OSTree requirements
- Enable hawkey package diff, we have new enough versions
  of libsolv/hawkey
- Enable /usr/bin/atomic symbolic link

* Tue Jun 10 2014 Colin Walters <walters@verbum.org>
- New upstream git snapshot

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Colin Walters <walters@verbum.org>
- New upstream release

* Fri May 23 2014 Colin Walters <walters@verbum.org>
- Previous autobuilder code is split off into rpm-ostree-toolbox

* Sun Apr 13 2014 Colin Walters <walters@verbum.org>
- New upstream release

* Tue Apr 08 2014 Colin Walters <walters@verbum.org>
- Drop requires on yum to allow minimal images without it

* Mon Mar 31 2014 Colin Walters <walters@verbum.org>
- New upstream release

* Sat Mar 22 2014 Colin Walters <walters@verbum.org> - 2014.6.3.g5707fa7-2
- Bump ostree version requirement

* Sat Mar 22 2014 Colin Walters <walters@verbum.org> - 2014.6.3.g5707fa7-1
- New git snapshot, add rpm-ostree-sign to file list

* Sat Mar 22 2014 Colin Walters <walters@verbum.org> - 2014.6-1
- New upstream version

* Fri Mar 07 2014 Colin Walters <walters@verbum.org> - 2014.5-1
- Initial package

