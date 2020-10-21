%undefine __cmake_in_source_build

Name:       cswrap
Version:    1.9.0
Release:    1%{?dist}
Summary:    Generic compiler wrapper

License:    GPLv3+
URL:        https://github.com/kdudka/%{name}
Source0:    https://github.com/kdudka/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

%ifarch x86_64
# csexec (supported on x86_64 only for now) can be later moved to a subpackage
Provides:   csexec = %{version}-%{release}
%endif

# cswrap-1.3.0+ emits internal warnings per timed out scans (used by csdiff to
# eliminate false positivies that such a scan would otherwise cause) ==> force
# new enough versions of the higher-level tools that will suppress them.
Conflicts: csbuild       < 1.7.0
Conflicts: csdiff        < 1.2.0
Conflicts: csmock-common < 1.7.0

BuildRequires: asciidoc
BuildRequires: cmake3
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

# csmock copies the resulting cswrap binary into mock chroot, which may contain
# an older (e.g. RHEL-5) version of glibc, and it would not dynamically link
# against the old version of glibc if it was built against a newer one.
# Therefor we link glibc statically.
%if (0%{?fedora} >= 12 || 0%{?rhel} >= 6)
BuildRequires: glibc-static
%endif

%description
Generic compiler wrapper used by csmock to capture diagnostic messages.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"' -DPATH_TO_WRAP=\"%{_libdir}/cswrap\"'
%ifnarch %{arm}
export LDFLAGS="$RPM_OPT_FLAGS -static -pthread"
%endif
%cmake3
%cmake3_build

%check
%ctest3

%install
%cmake3_install

install -m0755 -d "$RPM_BUILD_ROOT%{_libdir}"{,/cswrap}
for i in c++ cc g++ gcc clang clang++ cppcheck smatch \
    %{_arch}-redhat-linux-c++ \
    %{_arch}-redhat-linux-g++ \
    %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cswrap "$RPM_BUILD_ROOT%{_libdir}/cswrap/$i"
done

%files
%ifarch x86_64
%{_bindir}/csexec
%{_bindir}/csexec-loader
%{_libdir}/libcsexec-preload.so
%endif
%{_bindir}/cswrap
%{_libdir}/cswrap
%{_mandir}/man1/%{name}.1*
%doc COPYING README

%changelog
* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 1.9.0-1
- update to latest upstream

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-3
- add explicit BR for the gcc compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-5
- fix intermittent test-suite failures on slow Koji build hosts

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-3
- fix intermittent test-suite failures on slow Koji build hosts

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-2
- cswrap.1: replace a reference to fedorahosted.org

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to latest upstream

* Mon Mar 21 2016 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream

* Wed Feb 03 2016 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to latest upstream

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.2.1-1
- update to latest upstream

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to latest upstream

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
- abandon RHEL-5 compatibility (#1066028)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
