Name:		php-hkit
Summary:	Simple PHP5 API for extracting common microformats from a page
Version:	0.5
Release:	19%{?dist}
License:	LGPLv2+
Source0:	http://hkit.googlecode.com/files/hkit-v%{version}.tgz
URL:		http://allinthehead.com/hkit
Requires:	php >= 5.0.0
Buildarch:	noarch

%description
  hKit is a simple toolkit for extracting common microformats from a page.
The page can be presented as a string or a URL, and the result is handed
back as a standard PHP array structure. hKit uses SimpleXML for parsing,
and therefore requires PHP5.
  Designed for humans first and machines second, microformats are a set of
simple, open data formats built upon existing and widely adopted standards.
  The only microformat module currently supported by hKit is hCard. However,
hKit makes possible for a user to write its own microformat module.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -c


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Nothing to do.


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

rm -rf "${RPM_BUILD_ROOT}"

#	install directory.

install -p -d -m 755 "${RPM_BUILD_ROOT}/%{_datadir}/php/hkit"


#	Install files.

install -p -m 644 hkit.class.php "${RPM_BUILD_ROOT}/%{_datadir}/php/hkit/"
install -p -m 644 hcard.profile.php "${RPM_BUILD_ROOT}/%{_datadir}/php/hkit/"

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%defattr(-, root, root, -)
%doc example.php
%{_datadir}/php/hkit


#-------------------------------------------------------------------------------
%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

#-------------------------------------------------------------------------------

* Thu Jul  2 2009 Patrick Monnerat <pm@datasphere.ch> 0.5-3.
- Release bump due to cvs tag problem.

* Mon Jun 22 2009 Patrick Monnerat <pm@datasphere.ch> 0.5-2
- Move class files from /usr/share/php to /usr/share/php/hkit.

* Tue Jun  2 2009 Patrick Monnerat <pm@datasphere.ch> 0.5-1
- Initial RPM spec file.
