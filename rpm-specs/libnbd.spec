# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# If there are patches which touch autotools files, set this to 1.
%global patches_touch_autotools %{nil}

# The source directory.
%global source_directory 1.3-development

Name:           libnbd
Version:        1.3.7
Release:        3%{?dist}
Summary:        NBD client library in userspace

License:        LGPLv2+
URL:            https://github.com/libguestfs/libnbd

Source0:        http://libguestfs.org/download/libnbd/%{source_directory}/%{name}-%{version}.tar.gz
Source1:        http://libguestfs.org/download/libnbd/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.  This contains the single
# key from here:
# https://pgp.key-server.io/pks/lookup?search=rjones%40redhat.com&fingerprint=on&op=vindex
Source2:       libguestfs.keyring

%if 0%{patches_touch_autotools}
BuildRequires: autoconf, automake, libtool
%endif

%if 0%{verify_tarball_signature}
BuildRequires:  gnupg2
%endif

# For the core library.
BuildRequires:  gcc
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gnutls-devel
BuildRequires:  libxml2-devel

# For nbdfuse.
BuildRequires:  fuse, fuse-devel

# For the Python 3 bindings.
BuildRequires:  python3-devel

# For the OCaml bindings.
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel

# Only for building the examples.
BuildRequires:  glib2-devel

# For bash-completion.
BuildRequires:  bash-completion

# Only for running the test suite.
BuildRequires:  gnutls-utils
%if 0%{?fedora} >= 31
BuildRequires:  nbdkit
BuildRequires:  nbdkit-memory-plugin
BuildRequires:  nbdkit-null-plugin
BuildRequires:  nbdkit-pattern-plugin
BuildRequires:  nbdkit-sh-plugin
%endif
BuildRequires:  nbd
BuildRequires:  qemu-img
BuildRequires:  gcc-c++


%description
NBD — Network Block Device — is a protocol for accessing Block Devices
(hard disks and disk-like things) over a Network.

This is the NBD client library in userspace, a simple library for
writing NBD clients.

The key features are:

 * Synchronous and asynchronous APIs, both for ease of use and for
   writing non-blocking, multithreaded clients.

 * High performance.

 * Minimal dependencies for the basic library.

 * Well-documented, stable API.

 * Bindings in several programming languages.


%package devel
Summary:        Development headers for %{name}
License:        LGPLv2+ and BSD
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
This package contains development headers for %{name}.


%package -n ocaml-%{name}
Summary:        OCaml language bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description -n ocaml-%{name}
This package contains OCaml language bindings for %{name}.


%package -n ocaml-%{name}-devel
Summary:        OCaml language development package for %{name}
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}


%description -n ocaml-%{name}-devel
This package contains OCaml language development package for
%{name}.  Install this if you want to compile OCaml software which
uses %{name}.


%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

# The Python module happens to be called lib*.so.  Don't scan it and
# have a bogus "Provides: libnbdmod.*".
%global __provides_exclude_from ^%{python3_sitearch}/lib.*\\.so


%description -n python3-%{name}
python3-%{name} contains Python 3 bindings for %{name}.


%package -n nbdfuse
Summary:        FUSE support for %{name}
License:        LGPLv2+ and BSD
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description -n nbdfuse
This package contains FUSE support for %{name}.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
# Don't use _isa here because it's a noarch package.  This dependency
# is just to ensure that the subpackage is updated along with libnbd.
Requires:      %{name} = %{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1
%if 0%{patches_touch_autotools}
autoreconf -i
%endif


%build
%configure \
    --disable-static \
    --with-tls-priority=@LIBNBD,SYSTEM \
    PYTHON=%{__python3} \
    --enable-python \
    --enable-ocaml \
    --enable-fuse \
    --disable-golang

make %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Delete the golang man page since we're not distributing the bindings.
rm $RPM_BUILD_ROOT%{_mandir}/man3/libnbd-golang.3*


%check
# interop/structured-read.sh fails with the old qemu-nbd in Fedora 29,
# so disable it there.
%if 0%{?fedora} <= 29
rm interop/structured-read.sh
touch interop/structured-read.sh
chmod +x interop/structured-read.sh
%endif

# All fuse tests fail in Koji with:
# fusermount: entry for fuse/test-*.d not found in /etc/mtab
# for unknown reasons but probably related to the Koji environment.
for f in fuse/test-*.sh; do
    rm $f
    touch $f
    chmod +x $f
done

# Disable the tests on 32 bit because:
# https://github.com/ocaml/ocaml/issues/9460
%ifarch aarch64 ppc64 ppc64le riscv64 s390x x86_64
make %{?_smp_mflags} check || {
    for f in $(find -name test-suite.log); do
        echo
        echo "==== $f ===="
        cat $f
    done
    exit 1
  }
%endif


%files
%doc README
%license COPYING.LIB
%{_libdir}/libnbd.so.*


%files devel
%doc TODO examples/*.c
%license examples/LICENSE-FOR-EXAMPLES
%{_includedir}/libnbd.h
%{_libdir}/libnbd.so
%{_libdir}/pkgconfig/libnbd.pc
%{_mandir}/man3/libnbd.3*
%{_mandir}/man1/libnbd-release-notes-1.*.1*
%{_mandir}/man3/libnbd-security.3*
%{_mandir}/man3/nbd_*.3*


%files -n ocaml-%{name}
%{_libdir}/ocaml/nbd
%exclude %{_libdir}/ocaml/nbd/*.a
%exclude %{_libdir}/ocaml/nbd/*.cmxa
%exclude %{_libdir}/ocaml/nbd/*.cmx
%exclude %{_libdir}/ocaml/nbd/*.mli
%{_libdir}/ocaml/stublibs/dllmlnbd.so
%{_libdir}/ocaml/stublibs/dllmlnbd.so.owner


%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml
%license ocaml/examples/LICENSE-FOR-EXAMPLES
%{_libdir}/ocaml/nbd/*.a
%{_libdir}/ocaml/nbd/*.cmxa
%{_libdir}/ocaml/nbd/*.cmx
%{_libdir}/ocaml/nbd/*.mli
%{_mandir}/man3/libnbd-ocaml.3*


%files -n python3-%{name}
%{python3_sitearch}/libnbdmod*.so
%{python3_sitearch}/nbd.py
%{python3_sitearch}/nbdsh.py
%{python3_sitearch}/__pycache__/nbd*.py*
%{_bindir}/nbdsh
%{_mandir}/man1/nbdsh.1*


%files -n nbdfuse
%{_bindir}/nbdfuse
%{_mandir}/man1/nbdfuse.1*


%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nbdfuse
%{_datadir}/bash-completion/completions/nbdsh


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-3
- Rebuilt for Python 3.9

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Thu Apr 23 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-1
- New upstream version 1.3.7.

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-5
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-4
- OCaml 4.11.0 pre-release
- Add upstream patch to fix one of the tests that fails on slow machines.

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-2
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 31 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-1
- New upstream development version 1.3.6.
- Golang bindings are contained in this release but not distributed.

* Wed Mar 11 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.5-2
- Fix bogus runtime Requires of new bash-completion package.

* Tue Mar 10 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.5-1
- New upstream development version 1.3.5.
- Add new bash-completion subpackage.

* Sat Feb 29 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.4-1
- New upstream development version 1.3.4.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-2
- OCaml 4.10.0 final.

* Wed Feb 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-1
- New upstream development version 1.3.3.

* Thu Jan 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-1
- New upstream development version 1.3.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-4
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-3
- OCaml 4.10.0+beta1 rebuild.

* Thu Dec 12 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-2
- Rebuild for OCaml 4.09.0.

* Tue Dec 03 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-1
- New upstream development version 1.3.1.

* Wed Nov 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-2
- Use gpgverify macro instead of explicit gpgv2 command.

* Thu Nov 14 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-1
- New stable release 1.2.0

* Sat Nov 09 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.9-1
- New upstream version 1.1.9.
- Add new nbdkit-release-notes-1.2(1) man page.

* Wed Nov 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-1
- New upstream version 1.1.8.

* Thu Oct 24 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.7-1
- New upstream version 1.1.7.

* Sat Oct 19 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-1
- New upstream version 1.1.6.

* Sat Oct 12 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-1
- New upstream version 1.1.5.
- New tool and subpackage nbdfuse.

* Wed Oct  9 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.4-1
- New upstream version 1.1.4.
- Contains fix for remote code execution vulnerability.
- Add new libnbd-security(3) man page.

* Tue Oct  1 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-1
- New upstream version 1.1.3.

* Tue Sep 17 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-1
- New upstream version 1.1.2.
- Remove patches which are upstream.
- Contains fix for NBD Protocol Downgrade Attack (CVE-2019-14842).

* Thu Sep 12 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-2
- Add upstream patch to fix nbdsh (for nbdkit tests).

* Sun Sep 08 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-1
- New development version 1.1.1.

* Wed Aug 28 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-1
- New upstream version 1.0.0.

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-2
- Rebuilt for Python 3.8

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.9-1
- New upstream version 0.9.9.

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.8-4
- Fix nbdkit dependencies so we're actually running the tests.
- Add glib2-devel BR so we build the glib main loop example.
- Add upstream patch to fix test error:
  nbd_connect_unix: getlogin: No such device or address
- Fix test failure on 32 bit.

* Tue Aug 20 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.8-3
- Bump and rebuild to fix releng brokenness.
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/2LIDI33G3IEIPYSCCIP6WWKNHY7XZJGQ/

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.8-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.8-1
- New upstream version 0.9.8.
- Package the new nbd_*(3) man pages.

* Mon Aug  5 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.7-1
- New upstream version 0.9.7.
- Add libnbd-ocaml(3) man page.

* Sat Aug  3 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.6-2
- Add all upstream patches since 0.9.6 was released.
- Package the ocaml bindings into a subpackage.

* Tue Jul 30 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.6-1
- New upstream verison 0.9.6.

* Fri Jul 26 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.9-1
- New upstream version 0.1.9.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.8-1
- New upstream version 0.1.8.

* Tue Jul 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.7-1
- New upstream version 0.1.7.

* Wed Jul  3 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.6-1
- New upstream version 0.1.6.

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-1
- New upstream version 0.1.5.

* Sun Jun 09 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-1
- New upstream version 0.1.4.

* Sun Jun  2 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.2-2
- Enable libxml2 for NBD URI support.

* Thu May 30 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.2-1
- New upstream version 0.1.2.

* Tue May 28 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.1-1
- Fix license in man pages and examples.
- Add nbdsh(1) man page.
- Include the signature and keyring even if validation is disabled.
- Update devel subpackage license.
- Fix old FSF address in Python tests.
- Filter Python provides.
- Remove executable permission on the tar.gz.sig file.
- Initial release.
