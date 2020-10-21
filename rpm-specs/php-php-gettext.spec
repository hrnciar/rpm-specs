Summary:	Gettext emulation in PHP
Name:		php-php-gettext
Version:	1.0.12
Release:	9%{?dist}
License:	GPLv2+
URL:		https://launchpad.net/php-gettext
Source0:	http://launchpad.net/php-gettext/trunk/%{version}/+download/php-gettext-%{version}.tar.gz
Patch0:		php-php-gettext-1.0.11-php7.patch
%if 0%{?rhel}%{?fedora} > 4
Requires:	php-common
%endif
Requires:	php-mbstring
Obsoletes:	php-gettext < 1.0.11-5
BuildArch:	noarch

%description
This library provides PHP functions to read MO files even when gettext is 
not compiled in or when appropriate locale is not present on the system.

%prep
%setup -q -n php-gettext-%{version}
%patch0 -p1 -b .php7

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/php/gettext/
install -p -m 644 gettext.php streams.php gettext.inc $RPM_BUILD_ROOT%{_datadir}/php/gettext/

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README AUTHORS
%{_datadir}/php/gettext/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Robert Scheck <robert@fedoraproject.org> 1.0.12-1
- Upgrade to 1.0.12 (#1367462)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 04 2015 Robert Scheck <robert@fedoraproject.org> 1.0.11-12
- Added a patch for compatibility with PHP 7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 16 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.11-9
- increase php-gettext obs_ver (bug 1008026 and retire php-gettext)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Robert Scheck <robert@fedoraproject.org> 1.0.11-4
- Removed the dependency to php-common at EPEL 4

* Mon Sep 19 2011 Robert Scheck <robert@fedoraproject.org> 1.0.11-3
- Renamed package from php-gettext to php-php-gettext (#727000)

* Mon Aug 01 2011 Robert Scheck <robert@fedoraproject.org> 1.0.11-2
- Moved library data to /usr/share/php/gettext
- Added runtime dependency to php-mbstring package

* Sun Jul 31 2011 Robert Scheck <robert@fedoraproject.org> 1.0.11-1
- Upgrade to 1.0.11

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 06 2009 David Nalley <david@gnsa.us> 1.0.9-2
- corrected license field 

* Sun Dec 06 2009 David Nalley <david@gnsa.us> 1.0.9-1
- Initial Packaging
