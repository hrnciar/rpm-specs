Name:		php-email-address-validation
Version:	0
Release:	0.18.20090910svn%{?dist}
Summary:	A PHP class for validating email addresses
License:	BSD
URL:		http://code.google.com/p/php-email-address-validation/
# The source for this package was pulled from the upstream's vcs.
# The following commands can be used to generate the tarball.
# svn export -r10 http://php-email-address-validation.googlecode.com/svn/trunk/ php-email-address-validation
# tar cjvf rpmbuild/SOURCES/php-email-address-validation-0-0.1.20090910svn.tar.bz2 php-email-address-validation/ 
Source0:	%{name}-0-0.2.20090910svn.tar.bz2
BuildArch:	noarch
Requires:	php-common
Requires:	php

%description
This PHP class is used to check email addresses for technical validity.

%prep
%setup -q -n %{name}
sed -i 's/\r//' tests/EmailAddressValidatorTest.php

%build
# nothing to do here

%install
rm -rf $RPM_BUILD_ROOT
install -d -p $RPM_BUILD_ROOT%{_datadir}/php/%{name}
cp -rp EmailAddressValidator.php $RPM_BUILD_ROOT%{_datadir}/php/%{name}/



%files
%doc tests/
%{_datadir}/php/%{name}

%changelog
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
