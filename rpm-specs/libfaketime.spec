Summary: Manipulate system time per process for testing purposes
Name: libfaketime
Version: 0.9.8
Release: 6%{?dist}
License: GPLv2+
Url: https://github.com/wolfcw/libfaketime
Source: libfaketime-0.9.8.tar.xz
Patch0: libfaketime-0.9.8-FORCE_PTHREAD_NONVER.patch

Provides: faketime

BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-Time-HiRes

%description
libfaketime intercepts various system calls which programs use to
retrieve the current date and time. It can then report faked dates and
times (as specified by you, the user) to these programs. This means you
can modify the system time a program sees without having to change the
time system- wide.

%prep
%setup -q
%patch0 -p1

%build
cd src

# https://github.com/wolfcw/libfaketime/blob/master/README.packagers
# Upstream libfaketime requires a mess of different compile time flags for different glibc versions and architectures.
# https://github.com/wolfcw/libfaketime/pull/178
# Goal is to build time autodetect these with autotools in the next release ...

FAKETIME_COMPILE_CFLAGS="BOGUS"
%if 0%{?el7}
  %ifarch x86_64
    echo "force_monotonic https://github.com/wolfcw/libfaketime/issues/202"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX"
  %endif
  %ifarch aarch64 ppc64le
    echo "force_monotonic and pthread_nonver https://github.com/wolfcw/libfaketime/issues/205"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
  %endif
  %ifarch armv7hl
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif
%if 0%{?fedora} == 30 || 0%{?el8}
  # only ppc64le needs a workaround
  %ifarch ppc64le
    echo "pthread_nonver https://github.com/wolfcw/libfaketime/issues/204"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
  %else
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif
%if 0%{?fedora} >= 31
  # for reasons we don't know the old glibc workaround is required here but not on archv7hl and aarch64 ...
  %ifarch i686 x86_64 s390x
    echo "force_monotonic"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX"
  %endif
  %ifarch ppc64le
    echo "force_monotonic and pthread_nonver"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
  %endif
  %ifarch armv7hl aarch64
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif

if [ "$FAKETIME_COMPILE_CFLAGS" == "BOGUS" ]; then
  echo "SHOULD NEVER REACH HERE ... YOU HAVE AN UNTESTED VERSION+ARCH, see rpm spec for details ... ABORT"
  exit 1
fi

CFLAGS="%{optflags} -Wno-nonnull-compare -Wno-strict-aliasing" make %{?_smp_mflags} \
         PREFIX="%{_prefix}" LIBDIRNAME="/%{_lib}/faketime" all

%check
%if 0%{?fedora} >= 32
    FAKETIME_COMPILE_CFLAGS="-Wno-error=deprecated-declarations" \
%endif
make %{?_smp_mflags} -C test

%install
make PREFIX="%{_prefix}" DESTDIR=%{buildroot} LIBDIRNAME="/%{_lib}/faketime" install
rm -r %{buildroot}/%{_docdir}/faketime
# needed for stripping/debug package
chmod a+rx %{buildroot}/%{_libdir}/faketime/*.so.*


%files
%{_bindir}/faketime
%dir %attr(0755, root, root) %{_libdir}/faketime/
%attr(0755, root, root) %{_libdir}/faketime/libfaketime*so.*
%license COPYING
%doc README NEWS README.developers
%{_mandir}/man1/*

%changelog
* Sat Feb 08 2020 Pablo Greco <pgreco@centosproject.org> - 0.9.8-6
- Fix build with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Paul Wouters <pwouters@redhat.com> - 0.9.8-5
- Resolves: rhbz#1766749 libfaketime rfe: please add Provides:faketime
- Use license tag, remove duplicate README entry, update make test target

* Tue Sep 03 2019 Warren Togami <warren@blockstream.com> - 0.9.8-4
- upstream says to use FORCE_PTHREAD_NONVER on any glibc+arch that gets stuck
  For Fedora 31+ "make test" gets stuck on i686 x86_64 ppc64le s390x

* Wed Aug 28 2019 Warren Togami <warren@blockstream.com> - 0.9.8-3
- 0.9.8
- x86_64  EL7: DFORCE_MONOTONIC_FIX
  aarch64 EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le F30+ FORCE_PTHREAD_NONVER

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Paul Wouters <pwouters@redhat.com> - 0.9.6-4
- Add support for CLOCK_BOOTTIME (patch by Mario Pareja <pareja.mario@gmail.com>)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Paul Wouters <pwouters@redhat.com> - 0.9.6-1
- Upgraded to 0.9.6 which adds option to disable monotonic time faking
- fix permissions for symbol stripping for debug package

* Tue Oct 15 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-4
- Infinite recursion patch is still needed, make test causes
  segfaults otherwise.

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-3
- Work around from upstream for autodetecting glibc version bug on i686

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-2
- Remove use of ifarch for _lib macro for multilib

* Sun Oct 13 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-1
- Initial package
