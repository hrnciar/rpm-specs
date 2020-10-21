Summary:	Implementation of an E-component of Network Intrusion Detection System
Name:		libnids
Version:	1.24
Release:	21%{?dist}
License:	GPLv2+
URL:		http://libnids.sourceforge.net/
Source:		http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		libnids-1.24-inline.patch
BuildRequires:	libnet-devel, glib2-devel, libpcap-devel, pkgconfig
BuildRequires:	libtool, automake

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.x and offers
IP defragmentation, TCP stream assembly and TCP port scan detection.

Using libnids, one has got a convenient access to data carried by a
TCP stream, no matter how artfully obscured by an attacker.

%package devel
Summary:	Development files for libnids
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package package includes header files and libraries necessary
for developing programs which use the libnids library. It contains
the API documentation of the library, too.

%prep
%setup -q
%patch0 -p1 -b .inline
libtoolize --force

# Needed for ppc64, automake can't be run here
cp -f %{_datadir}/automake-*/config.* .

%build
%configure --enable-shared
%make_build

%install
%make_install install_prefix=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libnids.a

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGES CREDITS MISC README
%{_libdir}/libnids.so.*

%files devel
%doc doc/* samples/
%{_libdir}/libnids.so
%{_includedir}/nids.h
%{_mandir}/man3/libnids.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 Robert Scheck <robert@fedoraproject.org> - 1.24-12
- Avoid some functions being inline to unbreak dependent builds

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Jonathan Ciesla <limburgher@gmail.com> - 1.24-4
- Rebuild for updated libnet.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 1.24-1
- Upgrade to 1.24

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> 1.23-3
- Added patch to correct the wrong elif preprocessor statement

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.23-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Fri May 23 2008 Robert Scheck <robert@fedoraproject.org> 1.23-1
- Upgrade to 1.23

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 1.22-4
- Rebuilt against gcc 4.3

* Thu Nov 29 2007 Robert Scheck <robert@fedoraproject.org> 1.22-3
- Rebuilt against fixed libnet package (#400831)

* Mon Nov 26 2007 Robert Scheck <robert@fedoraproject.org> 1.22-2
- Build with -fPIC, because 64 bit archs are complaining

* Sun Nov 25 2007 Robert Scheck <robert@fedoraproject.org> 1.22-1
- Upgrade to 1.22
- Initial spec file for Fedora and Red Hat Enterprise Linux
