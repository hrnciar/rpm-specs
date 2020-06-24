%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name  Net_IDNA2
%global with_tests 0%{!?_without_tests:1}

Summary:         PHP library for punycode encoding and decoding
Name:            php-pear-Net-IDNA2
Version:         0.2.0
Release:         8%{?dist}
License:         LGPLv2+
URL:             http://pear.php.net/package/Net_IDNA2/
Source0:         http://download.pear.php.net/package/Net_IDNA2-%{version}.tgz

BuildArch:       noarch
BuildRequires:   php(language) >= 5.4
BuildRequires:   php-pear(PEAR) >= 1.10.1
%if %{with_tests}
# For test suite
BuildRequires:   phpunit
%endif

Requires:        php(language) >= 5.4
Requires:        php-pear(PEAR) >= 1.10.1
Requires(post):  %{__pear}
Requires(postun): %{__pear}

Provides:        php-pear(%{pear_name}) = %{version}

%description
This package helps you to encode and decode punycode strings easily in
PHP.

%prep
%setup -q -c
mv package.xml %{pear_name}-%{version}/%{name}.xml

%build
# Nothing to build

%install
pushd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml


# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -D -p -m 0644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml

%if %{with_tests}
%check
cd %{pear_name}-%{version}%{?prever}
%{_bindir}/phpunit \
   --include-path %{buildroot}%{pear_phpdir} \
   --verbose tests
%endif

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null ||:

%postun
if [ "$1" -eq "0" ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null ||:
fi

%files
%dir %{pear_phpdir}/Net/
%{pear_phpdir}/Net/IDNA2
%{pear_phpdir}/Net/IDNA2.php
%{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.2.0-6
- Fix requirement for %%postun (instead of %%preun) scriptlet

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 0.2.0-1
- update to 0.2.0
- raise dependency on PHP 5.4
- raise dependency on PEAR 1.10.1
- enable test suite during the build

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.1.1-8
- Fix build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.1.1-6
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 19 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.1.1-3
- Own Net dir

* Sat Feb 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.1.1-2
- add fedoraism
- fix license

* Sat Jan 22 2011 Adam Williamson <awilliamson@mandriva.org> - 0.1.1-1
- revision: 632388
- add source
- fix source extension
- imported package php-pear-Net_IDNA2


