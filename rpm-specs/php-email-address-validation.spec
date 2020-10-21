Name:		php-email-address-validation
Version:	2.0.1
Release:	1%{?dist}
Summary:	A PHP class for validating email addresses
License:	BSD

%global repo_owner	aziraphale
%global repo_name	email-address-validator
URL:		https://github.com/%{repo_owner}/%{repo_name}
Source0:	%{URL}/archive/%{version}/%{repo_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-composer(phpunit/phpunit) >= 5.7

Requires:	php
Requires:	php-common
Requires:	php-pcre

Provides:	php-composer(aziraphale/email-address-validator) = %{version}


%description
This PHP class is used to check email addresses for technical validity.


%prep
%setup -q -n %{repo_name}-%{version}
# Replace \r\n endlines with \n
sed -i 's/\r$//g' ./EmailAddressValidator.php tests/EmailAddressValidatorTest.php


%build
# nothing to do here


%install
install -d -p %{buildroot}%{_datadir}/php/%{name}
cp -rp EmailAddressValidator.php %{buildroot}%{_datadir}/php/%{name}/


%check
phpunit --verbose --bootstrap %{buildroot}%{_datadir}/php/%{name}/EmailAddressValidator.php


%files
%doc tests/
%doc composer.json
%{_datadir}/php/%{name}


%changelog
* Mon Aug 31 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.1-1
- Switch main source to a fork (composer: aziraphale/email-address-validator)
- Run the test suite during %%check

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.3.20090910svn
- Add php dependency

* Thu Sep 10 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.2.20090910svn
- Improved description
- Add comments to indicate source generation.
- Add php-common dependency

* Thu Aug 06 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.1.20090806svn
- Initial package
