# unversionned doc dir F20 change https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:				davix
Version:			0.7.6
Release:			1%{?dist}
Summary:			Toolkit for Http-based file management
License:			LGPLv2+
URL:				http://dmc.web.cern.ch/projects/davix/home
# Blessed release tarballs found in https://github.com/cern-fts/davix/releases
Source0:		        davix-0.7.6.tar.gz
# ./packaging/make-dist.sh 
# the tar.gz is in the build folder
#main lib dependencies
BuildRequires:                  cmake
BuildRequires:                  doxygen
BuildRequires:                  libxml2-devel
BuildRequires:                  openssl-devel
%{?el6:BuildRequires: python-argparse}
# davix-copy dependencies
BuildRequires:                  gsoap-devel
BuildRequires:                  libuuid-devel
# unit tests and abi check
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildRequires:                  abi-compliance-checker
%endif

Requires:                       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:                       libuuid


%description
Davix is a toolkit designed for file operations
with Http based protocols (WebDav, Amazon S3, ...).
Davix provides an API and a set of command line tools.

%package libs
Summary:			Development files for %{name}

%description libs
Libraries for %{name}. Davix is a toolkit designed for file operations
with Http based protocols (WebDav, Amazon S3, ...).


%package devel
Summary:			Development files for %{name}
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}
Requires:			pkgconfig

%description devel
Development files for %{name}. Davix is a toolkit designed for file operations
with Http based protocols (WebDav, Amazon S3, ...).

%package doc
Summary:			Documentation for %{name}
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch:	noarch
%endif

%description doc
Documentation and examples for %{name}. Davix is a toolkit designed 
for file operations with Http based protocols (WebDav, Amazon S3, ...).

%clean
rm -rf %{buildroot}
make clean

%prep
%setup -q

# remove useless embedded components
rm -rf test/pywebdav/

%build
%cmake \
-DDOC_INSTALL_DIR=%{_pkgdocdir} \
-DENABLE_THIRD_PARTY_COPY=TRUE \
-DENABLE_HTML_DOCS=TRUE \
-DUNIT_TESTS=TRUE \
.
make %{?_smp_mflags}
make doc

%check
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
#make abi-check
%endif
ctest -V -T Test


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%{_libdir}/libdavix.so.*
%{_libdir}/libdavix_copy.so.*
%{_mandir}/man3/*


%files devel
%{_libdir}/libdavix.so
%{_libdir}/libdavix_copy.so
%dir %{_includedir}/davix
%{_includedir}/davix/*
%{_libdir}/pkgconfig/*

%files doc
%{_pkgdocdir}/LICENSE
%{_pkgdocdir}/RELEASE-NOTES.md
%{_pkgdocdir}/html/


%changelog
* Wed Apr 29 2020 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.6-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.5-1
- New upstream release

* Thu Aug 22 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.4-3
- Rebuilt for gsoap

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.4-1
- New upstream release

* Wed May 08 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.3-1
- New upstream release

* Wed Mar 20 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.2-2
- Drop build dependency on sphinx

* Fri Feb 15 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.2-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.7.1-2
- Rebuild for new gsoap

* Wed Oct 24 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.7.1-1
- New upstream release

* Tue Oct 02 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.9-1
- New upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.8-1
- davix 0.68 release see RELEASE-NOTES for changes

* Mon Mar 26 2018 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.7-4
- Stop depending on unneeded gtest-devel and boost packages

* Mon Feb 12 2018 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.7-3
- Rebuild for new gsoap

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.7-1
 - New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 0.6.6-5
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.6-3
- Rebuilt for Boost 1.64

* Wed Jun 28 2017 Andrea Manzi <andrea.manzi at cern.ch> - 0.6.6-2
 - Rebuild for gsoap 2.8.48t (Fedora 27)

* Thu May 11 2017 Georgios Bitzes <georgios.bitzes at cern.ch> - 0.6.6-1
 - davix 0.6.6 release, see RELEASE-NOTES for changes

* Tue Feb 07 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.5-1
- New upstream release

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 0.6.4-5
- Rebuilt for libgsoapssl++ soname bump

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.4-4
- Rebuilt for Boost 1.63

* Thu Jan 26 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.4-3
- Remove trailing whitespaces on CMakeGeneratePkgConfig.cmake
- Patch for openssl 1.1.0

* Thu Aug 18 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.4-1
- davix 0.6.4 release, see RELEASE-NOTES for changes

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.6.3-3
- Rebuilt for linker errors in boost (#1331983)

* Fri Apr 22 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.3-2
- Rebuild for gsoap 2.8.30 (Fedora 25)

* Fri Apr 15 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.6.3-1
- davix 0.6.3 release, see RELEASE-NOTES for changes

* Wed Mar 02 2016 Georgios Bitzes <georgios.bitzes@cern.ch> - 0.6.0-1
- davix 0.6.0 release, see RELEASE-NOTES for changes

* Tue Feb 02 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.5.0-3
- Rebuilt for gsoap 2.8.28

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-2
- Rebuilt for Boost 1.60

* Mon Sep 14 2015 Adrien Devresse <adev@adev.name> - 0.5.0-1
 - Update to davix 0.5.0, see release note for details

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.4.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.4.1-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Adrien Devresse <adevress at cern.ch> - 0.4.1-3 
 - Update to version 0.4.1, see release-note for details

* Thu Apr 16 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 0.4.0-5
 - Recompile for another Rawhide C+++ ABI change

* Tue Mar 03 2015 Adrien Devresse <adevress at cern.ch> - 0.4.0-4
 - Recompile for Rawhide C++ ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.4.0-3
- Rebuild for boost 1.57.0

* Mon Jan 26 2015 Adrien Devresse <adevress at cern.ch> - 0.4.0-2
 - Rebuilt due to gSOAP update

* Fri Dec 05 2014 Adrien Devresse <adevress at cern.ch> - 0.4.0-1
 - davix 0.4.0 release, see RELEASE-NOTES for changes

* Tue Aug 12 2014 Adrien Devresse <adevress at cern.ch> - 0.3.6-1
 - davix 0.3.6 release, see RELEASE-NOTES for changes

* Tue Jul 22 2014 Adrien Devresse <adevress at cern.ch> - 0.3.4-1
 - Update to release 0.3.4

* Wed Jun 04 2014 Adrien Devresse <adevress at cern.ch> - 0.3.1-1
 - davix 0.3.1 release, see RELEASE-NOTES for changes

* Tue Jun 03 2014 Adrien Devresse <adevress at cern.ch> - 0.3.0-1
 - davix 0.3.0 release, see RELEASE-NOTES for changes

* Tue Jan 28 2014 Adrien Devresse <adevress at cern.ch> - 0.2.10-1
 - davix 0.2.10 release, see RELEASE-NOTES for details

* Mon Oct 28 2013 Adrien Devresse <adevress at cern.ch> - 0.2.7-3
 - New update of davix, see RELEASE-NOTES for details


* Tue Sep 03 2013 Adrien Devresse <adevress at cern.ch> - 0.2.6-1
 - Release 0.2.6 of davix, see RELEASE-NOTES for details


* Wed Jun 05 2013 Adrien Devresse <adevress at cern.ch> - 0.2.2-2
 - Initial EPEL release
 
 
