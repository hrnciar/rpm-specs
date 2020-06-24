Summary: Library for accessing ICA hardware crypto on IBM z Systems
Name: libica
Version: 3.7.0
Release: 1%{?dist}
License: CPL
URL: https://github.com/opencryptoki/
Source0: https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# annotate assembler source
# https://bugzilla.redhat.com/show_bug.cgi?id=1630582
# https://github.com/opencryptoki/libica/pull/24
Patch0: %{name}-3.7.0-annotate.patch
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: autoconf-archive
BuildRequires: perl(FindBin)
BuildRequires: perl(lib)
ExclusiveArch: s390 s390x

%description
A library of functions and utilities for accessing ICA hardware crypto on
IBM z Systems.


%package devel
Summary: Development tools for programs to access ICA hardware crypto on IBM z Systems
Requires: %{name} = %{version}-%{release}
Requires: openssl-devel

%description devel
The libica-devel package contains the header files and static
libraries necessary for developing programs accessing ICA hardware crypto on
IBM z Systems.


%prep
%autosetup -p1

sh ./bootstrap.sh


%build
%configure --disable-static --enable-fips
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libica.la


%check
# mock doesn't provide the device, so check here
# https://github.com/rpm-software-management/mock/issues/33
if [ -c /dev/hwrng -o -c /dev/prandom ]; then
    make check
fi


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS LICENSE ChangeLog
%exclude %{_pkgdocdir}/{INSTALL,README.md}
%{_bindir}/icainfo
%{_bindir}/icastats
%{_libdir}/libica.so.*
%{_mandir}/man1/icainfo.1*
%{_mandir}/man1/icastats.1*

%files devel
%{_includedir}/*
%{_libdir}/libica.so


%changelog
* Fri May 15 2020 Dan Horák <dan[at]danny.cz> - 3.7.0-1
- updated to 3.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Dan Horák <dan[at]danny.cz> - 3.6.1-1
- updated to 3.6.1

* Mon Sep 02 2019 Dan Horák <dan[at]danny.cz> - 3.6.0-1
- updated to 3.6.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Dan Horák <dan[at]danny.cz> - 3.5.0-1
- updated to 3.5.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Dan Horák <dan[at]danny.cz> - 3.4.0-1
- updated to 3.4.0

* Fri Sep 21 2018 Dan Horák <dan[at]danny.cz> - 3.3.3-4
- annotate assembler file (#1630582)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Dan Horák <dan[at]danny.cz> - 3.3.3-2
- fix executable stack in assembler code

* Tue Jun 12 2018 Dan Horák <dan[at]danny.cz> - 3.3.3-1
- updated to 3.3.3

* Tue Apr 17 2018 Dan Horák <dan[at]danny.cz> - 3.3.2-1
- updated to 3.3.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Dan Horák <dan[at]danny.cz> - 3.2.0-1
- updated to 3.2.0

* Mon Sep 11 2017 Dan Horák <dan[at]danny.cz> - 3.1.1-1
- updated to 3.1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Dan Horák <dan[at]danny.cz> - 3.0.2-3
- update BR

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Dan Horák <dan[at]danny.cz> - 3.0.2-1
- updated to 3.0.2

* Fri Jan 13 2017 Dan Horák <dan[at]danny.cz> - 3.0.1-2
- check for /dev/prandom before running the test-suite

* Fri Jan 13 2017 Dan Horák <dan[at]danny.cz> - 3.0.1-1
- updated to 3.0.1

* Tue Apr 12 2016 Dan Horák <dan[at]danny.cz> - 2.6.2-1
- updated to 2.6.2

* Thu Mar 17 2016 Dan Horák <dan[at]danny.cz> - 2.6.1-1
- updated to 2.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Dan Horák <dan[at]danny.cz> - 2.4.2-1
- updated to 2.4.2

* Wed Jun 11 2014 Dan Horák <dan[at]danny.cz> - 2.3.0-5
- fix build with recent kernels

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Dan Horák <dan[at]danny.cz> - 2.3.0-3
- add post release fix (#1066014)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 03 2013 Dan Horák <dan[at]danny.cz> - 2.3.0-1
- updated to 2.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 17 2012 Dan Horák <dan[at]danny.cz> - 2.2.0-1
- updated to 2.2.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Dan Horák <dan[at]danny.cz> - 2.1.1-1
- updated to 2.1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Dan Horák <dan[at]danny.cz> - 2.1.0-1
- updated to 2.1.0 with soname set back to 2.0

* Mon Apr 11 2011 Dan Horák <dan[at]danny.cz> - 2.0.6-1
- updated to 2.0.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Dan Horák <dan[at]danny.cz> - 2.0.4-1
- Do not use sigill to wrap all HW instructions (#665401)
- updated to 2.0.4

* Tue Nov  9 2010 Dan Horák <dhorak@redhat.com> - 2.0.3-3
- Fix the return value of old_api_sha_test() in libica_sha1_test (#624005)
- Use the right buffer length when operating in 32-bit mode (#640035)
- Resolves: #624005, #640035

* Fri May 21 2010 Dan Horák <dan[at]danny.cz> - 2.0.3-2
- rebuilt with -fno-strict-aliasing (#593779)
- Resolves: #593779

* Thu Apr 22 2010 Dan Horák <dan[at]danny.cz> - 2.0.3-1
- updated to 2.0.3 (#582607)
- Resolves: #582607

* Mon Apr 12 2010 Dan Horák <dan[at]danny.cz> - 2.0.2-3
- add SIGILL handler for add_entropy (#581520)
- Resolves: #581520

* Tue Feb 16 2010 Dan Horák <dan[at]danny.cz> - 2.0.2-2
- dropped the utils sub-package
- Related: #543948

* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.2-1.1
- Rebuilt for RHEL 6

* Mon Aug 17 2009 Dan Horák <dan[at]danny.cz> - 2.0.2-1
- update to 2.0.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Dan Horák <dan[at]danny.cz> - 2.0.1-1
- update to 2.0.1

* Mon Mar 23 2009 Dan Horák <dan[at]danny.cz> - 2.0-1
- update to 2.0
- spec file cleanup before submitting to Fedora

* Sun Sep 14 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-8.el5
- Added the icainfo tool to libica (#439484)

* Tue Apr 01 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-7.el5
- Fixed build of libica with latest AES & SHA feature (#439390)

* Tue Jan 15 2008 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-6.el5
- Added Software Support for CP Assist Instructions AES & SHA (#318971)

* Thu Nov 23 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-5.el5
- Fixed requires bug where devel packages would get wrong arch lib (#215908)

* Fri Oct 13 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-4
- Fixed bug where libica fails to initialize when no crypto hardware is
  available (#210504)
- Only build libica for s390(x), really only needed there.

* Fri Sep 08 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-3
- Build for other archs as well due to openCryptoki requirement (#184631)

* Fri Jul 14 2006 Tim Powers <timp@redhat.com> - 1.3.7-2
- rebuild

* Tue Jun 13 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.7-1
- Update to libica-1.3.7 final
- Fixed build on latest devel tree

* Tue Apr 04 2006 Phil Knirsch <pknirsch@redhat.com> - 1.3.6-rc3-1
- Initial package.
