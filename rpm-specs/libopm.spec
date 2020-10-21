Summary:        Blitzed open proxy monitor library
Name:           libopm
Version:        0.1
Release:        27.20050731cvs%{?dist}
License:        GPLv2+
URL:            http://wiki.blitzed.org/BOPM
# cvs -z3 -d:pserver:anon@cvs.blitzed.org:/ co -D "20050731 23:59" libopm
# find libopm -type f -name .cvsignore -exec rm -f {} ';'
# find libopm -type d -name CVS -exec rm -rf {} 2>/dev/null ';'
# mv -f libopm libopm-$(grep AC_INIT libopm/configure.in | sed -e 's/.*\[\(.*\)\].*/\1/')
Source:         %{name}-%{version}.tar.gz
Patch:          libopm-0.1-multilib.patch
BuildRequires:  gcc, doxygen

%description
An open proxy detection library, developed by the blitzed
IRC network team. Its original use was to detect open proxies
running on clients connecting to various IRC servers, but it
has evolved to become a generic open proxy detection library.

%package devel
Summary:        Headers and development libraries for libopm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libopm-devel package contains the header files and libraries
necessary for developing applications which use libopm.

%prep
%setup -q
%patch -p1 -b .multilib

%build
%configure --disable-static
%make_build
cd doc && doxygen && mv -f api html

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%doc doc/libopm-api.txt doc/html
%{_includedir}/opm*
%{_libdir}/%{name}.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-22.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-17.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-16.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9.20050731cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.1-8.20050731cvs
- Rebuild against gcc 4.4 and rpm 4.6

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 0.1-7.20050731cvs
- Rebuild against gcc 4.3

* Fri Dec 14 2007 Robert Scheck <robert@fedoraproject.org> 0.1-6.20050731cvs
- Solved multilib problems by removing doxygen timestamps (#342301)

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 0.1-5.20050731cvs
- Updated the license tag according to the guidelines
- Generate API documentation, added buildrequirement to doxygen

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 0.1-4.20050731cvs
- Rebuild

* Mon Nov 06 2006 Robert Scheck <robert@fedoraproject.org> 0.1-3.20050731cvs
- Changes to match with Fedora Packaging Guidelines (#212894 #c2, #c3, #c6)

* Tue Oct 03 2006 Robert Scheck <robert@fedoraproject.org> 0.1-2.20050731cvs
- Upgrade to CVS 20050731

* Fri May 05 2006 Robert Scheck <robert@fedoraproject.org> 0.1-1.20030106cvs
- Upgrade to CVS 20030106 (equals with libopm from BOPM 3.1.2)
- Initial spec file for Fedora Core
