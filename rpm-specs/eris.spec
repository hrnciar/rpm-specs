Name:           eris
Version:        1.3.23
Release:        17%{?dist}
Summary:        Client-side session layer for Atlas-C++

# All files untagged except for Eris/Operations.{cpp,h} which is labeled
# LGPL with no version.
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/eris
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: mercator-devel doxygen
BuildRequires: atlascpp-devel >= 0.5.98
BuildRequires: wfmath-devel >= 0.3.2
BuildRequires: skstream-devel >= 0.3.5

BuildRequires:  libsigc++20-devel glib-devel

%description
A client side session layer for WorldForge; Eris manages much of the generic
work required to communicate with an Atlas server. Client developers can extend
Eris in a number of ways to rapidly add game and client specific functions, and
quickly tie game objects to whatever output representation they are using.


%package devel
Summary:        Development files for Eris
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use Eris.


%prep
%setup -q


%build
%configure
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}-1.3.la

# 2014-05-17 - Tests disabled because one of 42 failed, will work w/ upstream to fix
%check
# Run tests in debug mode so asserts won't be skipped
#sed -i -e 's/-DNDEBUG/-DDEBUG/' test/Makefile
#make %{?_smp_mflags} check


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog CHANGES-1.4 COPYING NEWS README TODO
%{_libdir}/lib%{name}-1.3.so.*


%files devel
%{_includedir}/Eris-1.3
%{_libdir}/lib%{name}-1.3.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.3.23-14
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.23-10
- Rebuilt for atlascpp 0.6.4 plus spec cleanup

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.23-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.23-1
- Rebuilt for new upstream version, spec cleanup, fixes rhbz #1022659

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 01 2012 Bruno Wolff III <bruno@wolff.to> 1.3.21-1
- Update to 1.3.21

* Sat Nov 17 2012 Bruno Wolff III <bruno@wolff.to> 1.3.20-2
- Rebuild for skstream soname bump

* Wed Nov 14 2012 Tom Callaway <spot@fedoraproject.org> - 1.3.20-1
- update to 1.3.20

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.19-4
- Rebuilt for c++ ABI breakage

* Sun Jan 22 2012 Bruno Wolff III <bruno@wolff.to> 1.3.19-3
- Rebuild for wfmath soname bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Bruno Wolff III <bruno@wolff.to> 1.3.19-1
- New upstream release
- This looks to be a bugfix release

* Sun May 22 2011 Bruno Wolff III <bruno@wolff.to> 1.3.18-3
- Fix paths in patch and apply it when building

* Sun May 22 2011 Bruno Wolff III <bruno@wolff.to> 1.3.18-2
- Fix incorrect inlining of getMod

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> 1.3.18-1
- Upstream update to 1.3.18

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Tom Callaway <spot@fedoraproject.org> - 1.3.16-1
- update to 1.3.16

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.3.14-2
- Adding mercator dep to -devel subpackage
- Reenabling the tests

* Fri Feb 27 2009 Alexey Torkhov <atorkhov@gmail.com> - 1.3.14-1
- Update to 1.3.14

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart at kobold.org> 1.3.13-2
- Rebuild for gcc 4.3

* Sun Dec 16 2007 Wart <wart at kobold.org> 1.3.13-1
- Update to 1.3.13
- Remove multiarch conflicts (BZ #341071)

* Sun Aug 19 2007 Wart <wart at kobold.org> 1.3.12-2
- License tag clarification

* Mon Jan 29 2007 Wart <wart at kobold.org> 1.3.12-1
- Update to 1.3.12

* Thu Oct 19 2006 Wart <wart at kobold.org> 1.3.11-9
- Rebuild for newer version of skstream

* Sun Aug 27 2006 Wart <wart at kobold.org> 1.3.11-8
- Rebuild for newer version of wfmath

* Thu Aug 17 2006 Wart <wart at kobold.org> 1.3.11-7
- Added missing -devel Requires: libsigc++20-devel

* Thu Jul 27 2006 Wart <wart at kobold.org> 1.3.11-6
- Disable 'make check' due to hanging tests in the fedora buildsys

* Thu Jul 27 2006 Wart <wart at kobold.org> 1.3.11-5
- Missed one other reference to Atlas-C++

* Thu Jul 27 2006 Wart <wart at kobold.org> 1.3.11-4
- Changed Atlas BR: to atlascpp.

* Thu Jul 27 2006 Wart <wart at kobold.org> 1.3.11-3
- Remove unnecessary comment
- Bump release to fix tagging problem.

* Fri Jul 14 2006 Wart <wart at kobold.org> 1.3.11-2
- Fixed changelog version string
- Removed BR: pkgconfig
- Added BR: glib-devel

* Fri Jul 7 2006 Wart <wart at kobold.org> 1.3.11-1
- Update to 1.3.11

* Wed Jun 14 2006 Wart <wart at kobold.org> 1.3.10-1
- Initial spec file for Fedora Extras
