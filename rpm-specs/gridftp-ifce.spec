%define __cmake_in_source_build 1
# unversionned doc dir F20 change https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:						gridftp-ifce
Version:					2.3.1
Release:					16%{?dist}
Summary:					GridFTP library for FTS and lcgutil
License:					ASL 2.0
URL:						https://svnweb.cern.ch/trac/lcgutil
# svn export http://svn.cern.ch/guest/lcgutil/gridftp-ifce/trunk gridftp-ifce
Source0:					http://grid-deployment.web.cern.ch/grid-deployment/dms/lcgutil/tar/%{name}/%{name}-%{version}.tar.gz 

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:				cmake
BuildRequires:				globus-gass-copy-devel

Requires:					globus-gass-copy%{?_isa}

%description
gridFTP-ifce is client side library for the gridFTP protocol 
using the globus toolkit.

%package devel
Summary:					Client side headers and development files
Requires:					%{name}%{?_isa} = %{version}-%{release}
Requires:					globus-gass-copy-devel%{?_isa}

%description devel
This package contains development files for %{name}

%prep
%setup -q

%build
%cmake \
-DDOC_INSTALL_DIR=%{_pkgdocdir} \
. 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install

%ldconfig_scriptlets

%files devel
%{_libdir}/libgridftp_ifce.so
%{_includedir}/gridftp-ifce.h
%{_pkgdocdir}/RELEASE-NOTES

%files
%{_libdir}/libgridftp_ifce.so.*
%{_pkgdocdir}/README
%{_pkgdocdir}/VERSION
%{_pkgdocdir}/LICENSE

%changelog
* Wed Sep 23 2020 Jeff Law <law@redhat.com> - 2.3.1-16
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Adrien Devresse <adevress at cern.ch> - 2.3.1-1
 - fix unversionned documentation problem
 - Release 2.3.1 for EPEL
 
* Thu Mar 14 2013 Michail Salichos <msalicho at cern.ch> - 2.3.1-0
 - replace globus wait with cond_timed_wait
 
* Thu Nov 29 2012 Adrien Devresse <adevress at cern.ch> - 2.3.0-0
 - switch to CMake
 - correct a stack corruption problem for lcg-util in case of wrong protocol support

* Fri Nov 23 2012 Alejandro Alvarez <aalvarez at cern.ch> - 2.2.5-0
 - using CMake

* Fri Jul 20 2012 Adrien Devresse <adevress at cern.ch> - 2.2.0-0
 - gridftp version 2 support
 - EMI 2 Update synchronisation

* Wed Apr 18 2012 Zsolt Molnar <zsolt.molnar@cern.ch> - 2.1.4-2
 - fix memory leaks, disable unused code

* Wed Jan 18 2012 Adrien Devress <adevress at cern.ch> - 2.1.3-4
 - add missing dist tag

* Sun Jan 15 2012 Adrien Devress <adevress at cern.ch> - 2.1.3-3
 - correct buildroot tag
 - add a valid Source URL
 
* Wed Jan 11 2012 <adevress at cern.ch> - 2.1.3-2
 - updating description
 - updating documentation management
 - create separated branch
 
* Tue Dec 13 2011 <adevress at cern.ch> - 2.1.3-1
 - Initial build 
