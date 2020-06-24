Name:           php-lightopenid
Version:        0.6
Release:        12%{?dist}
Summary:        PHP OpenID library

License:        MIT
URL:            http://code.google.com/p/lightopenid/
Source0:        http://lightopenid.googlecode.com/files/lightopenid-%{version}.tgz

Requires:       php-curl
Requires:       php-pcre
BuildArch:      noarch

%description
Lightweight OpenID library.

%prep
%setup -q -n lightopenid

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/php/lightopenid
cp -p openid.php %{buildroot}%{_datadir}/php/lightopenid/openid.php

%files
%doc example.php example-google.php
%{_datadir}/php/lightopenid


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 14 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.6-2
- Fixed package guidelines issues

* Tue Oct 01 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.6-1
- Initial packaging
