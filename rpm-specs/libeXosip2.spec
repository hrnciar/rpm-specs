Summary: A library that hides the complexity of using the SIP protocol
Name: libeXosip2
Version: 3.6.0
Release: 22%{?dist}
License: GPLv2+
URL: http://savannah.nongnu.org/projects/eXosip
Source0: http://download.savannah.nongnu.org/releases/exosip/libeXosip2-%{version}.tar.gz
Patch0:  libeXosip2-aarch64.patch
Patch1:  libeXosip2-3.6.0-openssl_110.patch

BuildRequires:  gcc
BuildRequires: c-ares-devel
BuildRequires: ortp-devel >= 0.14.2
BuildRequires: libosip2-devel >= 3.6.0
BuildRequires: openssl-devel
BuildRequires: doxygen

%description
A library that hides the complexity of using the SIP protocol for
mutlimedia session establishement. This protocol is mainly to be used
by VoIP telephony applications (endpoints or conference server) but
might be also useful for any application that wish to establish
sessions like multiplayer games.

%package devel
Summary: Development files for libeXosip2
Requires: %{name} = %{version}-%{release}
Requires: libosip2-devel

%description devel
Development files for libeXosip2.

%prep
%setup -q
%patch0 -p1 -b .aarch64
%patch1 -p1 -b .openssl_110


%build
%configure --disable-static
make %{_smp_mflags}
make doxygen

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/%{name}.la

mkdir -p %{buildroot}%{_mandir}/man3
cp help/doxygen/doc/man/man3/*.3* %{buildroot}%{_mandir}/man3


%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README

%{_bindir}/sip_reg
%{_libdir}/libeXosip2.so.7*

%files devel
%doc help/doxygen/doc/html help/doxygen/doc/latex

%{_includedir}/eXosip2
%{_libdir}/libeXosip2.so
%{_mandir}/man3/*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.6.0-17
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Robert Scheck <robert@fedoraproject.org> - 3.6.0-15
- Added patch to build with OpenSSL >= 1.1.0 (#1423847)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-6
- add aarch64 patch (#925719)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-2
- BR: c-ares-devel

* Mon Dec 26 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.6.0-1
- libeXosip2-3.6.0

* Fri Sep  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.5.0-1
- libeXosip2-3.5.0
- add BR: openssl-devel
- drop gcc43 patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.1.0-1
- Update to 3.1.0

* Tue Feb  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-3
- Apply patch from Adam Tkac that fixes compilation with GCC 4.3.

* Mon Feb  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-2
- Update to new patchlevel release.

* Tue Aug 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 3.0.3-1
- Update to 3.0.3

* Mon Aug 28 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-3
- Bump release and rebuild.

* Mon Jun  5 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-2
- Add BR for doxygen.

* Mon May 29 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.3-1
- Update to 2.2.3

* Mon Feb 20 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.2-4
- Bump release for rebuild.

* Mon Feb 13 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 2.2.2-3
- Bump release and rebuild for gcc 4.1 and glibc.

* Wed Jan  4 2006 Jeffrey C. Ollie <jeff@max1.ocjtech.us> - 2.2.2
- Update to 2.2.2.
- Bump release because forgot to upload new source.

* Sat Oct 29 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.5.pre17
- Update to next prerelease.

* Mon Oct 24 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.4.pre16
- Remove INSTALL from %%doc - not needed in an RPM package

* Sun Oct 23 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.3.pre16
- Added -n to BuildRoot
- BR libosip2-devel for -devel subpackage.

* Sun Oct 16 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.2.pre16
- Changed BuildRoot to match packaging guidelines.
- Remove extraneous %%dir in -devel %%files
- Replace %%makeinstall with proper invocation.

* Fri Oct 14 2005 Jeffrey C. Ollie <jcollie@lt16585.campus.dmacc.edu> - 1.9.1-0.1.pre16
- Initial build.

