%undefine __cmake_in_source_build

Name:       cscppc
Version:    1.8.1
Release:    1%{?dist}
Summary:    A compiler wrapper that runs cppcheck in background

License:    GPLv3+
URL:        https://github.com/kdudka/%{name}
Source0:    https://github.com/kdudka/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: asciidoc
BuildRequires: cmake
BuildRequires: gcc

# The test-suite runs automatically trough valgrind if valgrind is available
# on the system.  By not installing valgrind into mock's chroot, we disable
# this feature for production builds on architectures where valgrind is known
# to be less reliable, in order to avoid unnecessary build failures (see RHBZ
# #810992, #816175, and #886891).  Nevertheless developers are free to install
# valgrind manually to improve test coverage on any architecture.
%ifarch %{ix86} x86_64
BuildRequires: valgrind
%endif

# csmock copies the resulting cscppc binary into mock chroot, which may contain
# an older (e.g. RHEL-5) version of glibc, and it would not dynamically link
# against the old version of glibc if it was built against a newer one.
# Therefor we link glibc statically.
%if (0%{?fedora} >= 12 || 0%{?rhel} >= 6)
BuildRequires: glibc-static
%endif

# the {cwe} field in --template option is supported since cppcheck-1.85
Requires: cppcheck >= 1.85

# older versions of csdiff do not read CWE numbers from Cppcheck output
Conflicts: csdiff < 1.8.0

%description
This package contains the cscppc compiler wrapper that runs cppcheck in
background fully transparently.

%package -n csclng
Summary: A compiler wrapper that runs Clang in background
Requires: clang
Conflicts: csmock-plugin-clang < 1.5.0

%description -n csclng
This package contains the csclng compiler wrapper that runs the Clang analyzer
in background fully transparently.

%package -n csgcca
Summary: A compiler wrapper that runs 'gcc -fanalyzer' in background

%description -n csgcca
This package contains the csgcca compiler wrapper that runs 'gcc -fanalyzer'
in background fully transparently.

%package -n csmatch
Summary: A compiler wrapper that runs smatch in background
Requires: clang

%description -n csmatch
This package contains the csmatch compiler wrapper that runs the smatch analyzer
in background fully transparently.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
CFLAGS="$CFLAGS"' -DPATH_TO_CSCPPC=\"%{_libdir}/cscppc\"'
CFLAGS="$CFLAGS"' -DPATH_TO_CSCLNG=\"%{_libdir}/csclng\"'
CFLAGS="$CFLAGS"' -DPATH_TO_CSGCCA=\"%{_libdir}/csgcca\"'
CFLAGS="$CFLAGS"' -DPATH_TO_CSMATCH=\"%{_libdir}/csmatch\"'
%ifnarch %{arm}
export LDFLAGS="$RPM_OPT_FLAGS -static -pthread"
%endif
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

install -m0755 -d "$RPM_BUILD_ROOT%{_libdir}"{,/cs{cppc,clng,gcca,match}}

for i in cc gcc %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cscppc "$RPM_BUILD_ROOT%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng "$RPM_BUILD_ROOT%{_libdir}/csclng/$i"
    ln -s ../../bin/csgcca "$RPM_BUILD_ROOT%{_libdir}/csgcca/$i"
    ln -s ../../bin/csmatch "$RPM_BUILD_ROOT%{_libdir}/csmatch/$i"
done

for i in c++ g++ %{_arch}-redhat-linux-c++ %{_arch}-redhat-linux-g++
do
    ln -s ../../bin/cscppc   "$RPM_BUILD_ROOT%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng++ "$RPM_BUILD_ROOT%{_libdir}/csclng/$i"
done

%files
%{_bindir}/cscppc
%{_datadir}/cscppc
%{_libdir}/cscppc
%{_mandir}/man1/%{name}.1*
%doc COPYING README

%files -n csclng
%{_bindir}/csclng
%{_bindir}/csclng++
%{_libdir}/csclng
%{_mandir}/man1/csclng.1*
%doc COPYING

%files -n csgcca
%{_bindir}/csgcca
%{_libdir}/csgcca
%doc COPYING

%files -n csmatch
%{_bindir}/csmatch
%{_libdir}/csmatch
%doc COPYING

%changelog
* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 1.8.1-1
- update to latest upstream release

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> 1.3.4-3
- add explicit BR for the gcc compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 1.3.4-1
- update to latest upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to latest upstream release

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream

* Fri Aug 28 2015 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Kamil Dudka <kdudka@redhat.com> 1.2.0-2
- add missing dependency of csclng on clang

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to latest upstream

* Fri Sep 19 2014 Kamil Dudka <kdudka@redhat.com> 1.1.2-1
- update to latest upstream

* Wed Aug 20 2014 Kamil Dudka <kdudka@redhat.com> 1.1.0-1
- update to latest upstream (introduces the csclng subpackage)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.0.5-1
- update to latest upstream

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to latest upstream

* Mon Mar 10 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- abandon RHEL-5 compatibility (#1066026)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
