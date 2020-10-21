
Name:		php-oojs-oojs-ui
Version:	0.34.1
Release:	2%{?dist}
Summary:	Object-Oriented JavaScript – User Interface

License:	MIT
URL:		http://www.mediawiki.org/wiki/OOjs_UI
# Wikimedia changed server software and now doesn't support downloads
# https://phabricator.wikimedia.org/T111887
Source0:	https://github.com/wikimedia/oojs-ui/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  php-theseer-autoload

Requires:	php(language) >= 5.4.0
Requires:	php-json
Requires:	php-pcre
Requires:	php-spl

Provides:	php-composer(oojs/oojs-ui) = %{version}

%description
OOjs UI (Object-Oriented JavaScript – User Interface) is a library that allows
developers to rapidly create front-end web applications that operate
consistently across a multitude of browsers.


%prep
%setup -q -n oojs-ui-%{version}


%build
# dirty hack since autoloader isn't working
sed -i '5i require "/usr/share/php/OOUI/mixins/AccessKeyedElement.php";' php/widgets/InputWidget.php
phpab --output php/autoload.php php


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/OOUI
cp -rp php/* %{buildroot}%{_datadir}/php/OOUI


%files
%license LICENSE-MIT
%doc AUTHORS.txt History.md README.md
%{_datadir}/php/OOUI


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Michael Cronenworth <mike@cchtml.com> - 0.34.1-1
- version update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 0.31.3-1
- version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Michael Cronenworth <mike@cchtml.com> - 0.29.2-1
- version update

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michael Cronenworth <mike@cchtml.com> - 0.21.2-1
- version update

* Fri Feb 24 2017 Michael Cronenworth <mike@cchtml.com> - 0.17.10-1
- version update
- tests were removed by upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.11.6-2
- Drop the non-ascii character in the summary field

* Thu Jun 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.11.6-1
- Initial package

