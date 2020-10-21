# remirepo/fedora spec file for php-htmLawed
#
# Copyright (c) 2012-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global libname    htmLawed
%global libversion 1242

Name:           php-%{libname}
Version:        1.2.4.2
Release:        4%{?dist}
Summary:        PHP code to purify and filter HTML
License:        LGPLv3 and GPLv2+
URL:            http://www.bioinformatics.org/phplabware/internal_utilities/htmLawed/

Source0:        http://www.bioinformatics.org/phplabware/downloads/%{libname}%{libversion}.zip

BuildArch:      noarch

Requires:       php-ctype
Requires:       php-pcre


%description
PHP code to purify and filter HTML

* make HTML markup in text secure and standard-compliant
* process text for use in HTML, XHTML or XML documents
* restrict HTML elements, attributes or URL protocols
  using black or white-lists
* balance tags, check element nesting, transform deprecated
  attributes and tags, make relative URLs absolute, etc.
* fast, highly customizable, well-documented
* single, 48 kb file
* simple HTML Tidy alternative
* free and licensed under LGPL v3 and GPL v2+
* use to filter, secure and sanitize HTML in blog comments or
  forum posts, generate XML-compatible feed items from web-page
  excerpts, convert HTML to XHTML, pretty-print HTML, scrape
  web-pages, reduce spam, remove XSS code, etc.


%prep
%setup -qc

chmod -x *


%build
# nothing to build


%install
install -d %{buildroot}%{_datadir}/php/%{libname}
install -pm 0644 %{libname}.php %{buildroot}%{_datadir}/php/%{libname}


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE*
%doc *README* *TESTCASE* htmLawedTest.php
%{_datadir}/php/%{libname}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Remi Collet <remi@remirepo.net> - 1.2.4.2-1
- Update to 1.2.4.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep  6 2017 Remi Collet <remi@remirepo.net> - 1.2.4-1
- Update to 1.2.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Remi Collet <remi@remirepo.net> - 1.2.2-1
- Update to 1.2.2

* Tue May 23 2017 Remi Collet <remi@remirepo.net> - 1.2.1-1
- Update to 1.2.1

* Thu Mar 30 2017 Remi Collet <remi@remirepo.net> - 1.2-1
- Update to 1.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar  7 2016 Remi Collet <remi@fedoraproject.org> - 1.1.22-1
- update to 1.1.22

* Tue Mar  1 2016 Remi Collet <remi@fedoraproject.org> - 1.1.21-1
- update to 1.1.21

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 1.1.20-1
- update to 1.1.20

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Remi Collet <remi@fedoraproject.org> - 1.1.19-1
- update to 1.1.19

* Sun Aug 17 2014 Remi Collet <remi@fedoraproject.org> - 1.1.18-1
- update to 1.1.18 (security)
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Remi Collet <remi@fedoraproject.org> - 1.1.17-1
- update to 1.1.17, improves php 5.5 compatibility

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.1.16-1
- update to 1.1.16, fix for a potential security vulnerability
  arising from specialy encoded space characters in URL schemes/protocols

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 1.1.15-2
- new upstream sources with Licenses included

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 1.1.15-1
- update to 1.1.15

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug  9 2012 Remi Collet <remi@fedoraproject.org> - 1.1.14-1
- update to 1.1.14

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Remi Collet <remi@fedoraproject.org> - 1.1.12-1
- update to 1.1.12
- add License files
- fix source0 to permanent URL.

* Wed Jul 04 2012 Remi Collet <remi@fedoraproject.org> - 1.1.11-2
- fix License per review comment (#836587)

* Fri Jun 29 2012 Remi Collet <remi@fedoraproject.org> - 1.1.11-1
- initial package

