Name:           mediawiki-HTTP302Found
Version:        2.0.1
Release:        13%{?dist}
Summary:        Forces an external HTTP 302 redirect instead of internal redirects

License:        GPLv2+
URL:            http://www.mediawiki.org/wiki/Extension:HTTP302Found
Source0:        http://puiterwijk.fedorapeople.org/releases/HTTP302Found-2.0.1.tar.gz
BuildArch:      noarch

Requires:       mediawiki >= 1.7

%description
Pushes a HTTP code 302 (Found) to the browser when there is a redirect instead
of handling it internally. The end user will not notice any difference (other
than the address to the page having an ?rd=Redirecting_page bit at the end).


%prep
%setup -q -n HTTP302Found-2.0.1
echo 'To complete installation of %{name}, add the following lines to LocalSettings.php:

    require_once("$IP/extensions/HTTP302Found/HTTP302Found.php");

for each MediaWiki instance you wish to install %{name} on.' > README.fedora


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/mediawiki/extensions/HTTP302Found/
install -cpm 644 %{_builddir}/%{buildsubdir}/*.php %{buildroot}%{_datadir}/mediawiki/extensions/HTTP302Found/



%files
%doc README.fedora COPYING
%{_datadir}/mediawiki/extensions/HTTP302Found


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 12 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.0.1-1
- Update Required to real required version
- Added a COPYING to the sources

* Sun Aug 12 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.0-1
- Complete rewrite for MediaWiki 1.19

* Mon Jun 15 2009 Ian Weller <ian@ianweller.org> - 1.0-1
- Initial package build
