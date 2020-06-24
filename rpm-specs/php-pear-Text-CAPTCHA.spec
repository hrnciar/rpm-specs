# spec file for php-pear-Text-CAPTCHA
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Text_CAPTCHA

Name:           php-pear-Text-CAPTCHA
Version:        1.0.2
Release:        2%{?dist}
Summary:        Generation of CAPTCHAs

License:        BSD
URL:            http://pear.php.net/package/Text_CAPTCHA
# remove tests which use non-free stuff (fonts)
# pear download Text_CAPTCHA-%%{version}
# ./strip.sh %%{version}
Source0:        %{pear_name}-%{version}-strip.tgz
Source1:        strip.sh

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-gd
Requires:       php-pear(PEAR)
Requires:       php-pear(Text_Password) >= 1.1.1
# Optional
Requires:       php-pear(Numbers_Words)
Requires:       php-pear(Text_Figlet)
Requires:       php-pear(Image_Text) >= 0.7.0

Provides:       php-pear(%{pear_name}) = %{version}

%description
Implementation of CAPTCHAs (completely automated public Turing test to tell
computers and humans apart)


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Text/CAPTCHA
%{pear_phpdir}/Text/CAPTCHA.php


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- Update to 1.0.2 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (stable) - no change since 0.5.0

* Wed Aug 07 2013 Remi Collet <remi@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0 (beta)
- strip sources from non-free stuff (fonts)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Remi Collet <remi@fedoraproject.org> - 0.4.6-1
- Version 0.4.6 (alpha) - API 0.4.0 (alpha)

* Sat Jan 26 2013 Remi Collet <remi@fedoraproject.org> - 0.4.5-1
- Version 0.4.5 (alpha) - API 0.4.0 (alpha) - no change

* Fri Jan 25 2013 Remi Collet <remi@fedoraproject.org> - 0.4.4-1
- Version 0.4.4 (alpha) - API 0.4.0 (alpha)
- LICENSE is now provided by upstream

* Wed Jan 16 2013 Remi Collet <remi@fedoraproject.org> - 0.4.3-1
- Initial package
