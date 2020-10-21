Name:		php-cssjanus
Version:	1.3.0
Release:	3%{?dist}
Summary:	Convert CSS stylesheets between left-to-right and right-to-left

License:	ASL 2.0
URL:		https://github.com/cssjanus/php-cssjanus
Source0:	https://github.com/cssjanus/php-cssjanus/archive/v%{version}.tar.gz#/php-cssjanus-%{version}.tar.gz
Source1:	https://github.com/cssjanus/cssjanus/raw/v%{version}/test/data.json#/php-cssjanus-data.json

BuildArch:	noarch

BuildRequires:	php-phpunit-PHPUnit

Requires:	php(language) >= 5.4
Requires:	php-pcre

Provides:	php-composer(cssjanus/cssjanus) = %{version}


%description
Convert CSS stylesheets between left-to-right and right-to-left.


%prep
%setup -qn php-cssjanus-%{version}
cp -p %{SOURCE1} test/data-v%{version}.json


%build


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/cssjanus
cp -p src/CSSJanus.php %{buildroot}%{_datadir}/php/cssjanus


%check
phpunit --bootstrap src/CSSJanus.php test/


%files
%license APACHE-LICENSE-2.0.txt
%doc README.md
%{_datadir}/php/cssjanus


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 1.3.0-1
- Version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michael Cronenworth <mike@cchtml.com> - 1.2.0-1
- Version update

* Mon Feb 13 2017 Michael Cronenworth <mike@cchtml.com> - 1.1.3-1
- Version update
- Add upstream patch for php 7.1 support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Michael Cronenworth <mike@cchtml.com> - 1.1.2-1
- Version update

* Wed Sep 30 2015 Michael Cronenworth <mike@cchtml.com> - 1.1.1-1
- Initial package

