# remirepo/fedora spec file for php-pear-CAS
#
# Copyright (c) 2010-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    40c0769ce05a30c8172b36ceab11124375c8366e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     apereo
%global gh_project   phpCAS


Name:           php-pear-CAS
Version:        1.3.8
Release:        2%{?dist}
Summary:        Central Authentication Service client library in php

License:        ASL 2.0
URL:            https://wiki.jasig.org/display/CASC/phpCAS

Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
# only for pear macros
BuildRequires:  php-pear
# for %%check
BuildRequires:  php-cli

Requires:       php-curl
Requires:       php-date
Requires:       php-dom
Requires:       php-hash
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-session
Requires:       php-spl
# Optional: php-imap (when use Proxied Imap)
Requires:       php-composer(fedora/autoloader)

Provides:       php-pear(__uri/CAS) = %{version}
Provides:       php-composer(jasig/phpcas) = %{version}
Provides:       php-composer(apereo/phpcas) = %{version}
# this library is mostly known as phpCAS
Provides:       phpCAS = %{version}-%{release}


%description
This package is a PEAR library for using a Central Authentication Service.

Autoloader '%{pear_phpdir}/CAS/Autoload.php';


%prep
%setup -q -n %{gh_project}-%{gh_commit}



%build
# Rewrite a classmap autoloader (upstream is broken)
%{_bindir}/phpab \
    --template fedora \
    --output source/CAS/Autoload.php  \
             source


%install
mkdir -p %{buildroot}%{pear_phpdir}
cp -pr source/* %{buildroot}%{pear_phpdir}/


%check
: Ensure our autoloader works
php -r '
require "%{buildroot}%{pear_phpdir}/CAS/Autoload.php";
if (!class_exists("phpCAS")) {
  echo "Class not found\n";
  exit(1);
}
if (phpCAS::getVersion() != "%{version}") {
  echo "Bad version (found=" . phpCAS::getVersion()  . ", expected=%{version})\n";
  exit(1);
}
echo "Ok\n";
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc NOTICE *.md
%{pear_phpdir}/CAS
%{pear_phpdir}/CAS.php


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Remi Collet <remi@remirepo.net> - 1.3.8-1
- update to 1.3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 1.3.7-1
- update to 1.3.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Remi Collet <remi@remirepo.net> - 1.3.6-1
- update to 1.3.6
- new github and packagist owner

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Remi Collet <remi@remirepo.net> - 1.3.5-1
- update to 1.3.5
- sources from github
- add minimal check for our autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Remi Collet <remi@fedoraproject.org> - 1.3.4-3
- fix broken autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.4
- add provides php-composer(jasig/phpcas)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 28 2014 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to Version 1.3.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 29 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to Version 1.3.2, security fix for
  CVE-2012-5583 Missing CN validation of CAS server certificate
- add requires for all needed php extensions

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to Version 1.3.1

* Wed Mar 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- License is ASL 2.0, https://github.com/Jasig/phpCAS/issues/32
- New sources,        https://github.com/Jasig/phpCAS/issues/31

* Tue Mar 13 2012 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to Version 1.3.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 11 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.2-1
- update to Version 1.2.2 (stable) - API 1.2.2 (stable)

* Wed Mar 30 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.1-1
- update to Version 1.2.1 (stable) - API 1.2.1 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.2.0-1
- update to Version 1.2.0 (stable) - API 1.2.0 (stable)
- dont requires domxml-php4-to-php5 anymore
- fix URL
- link %%doc to pear_docdir

* Mon Oct 04 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.3-1
- update to 1.1.3
- fix CVE-2010-3690, CVE-2010-3691, CVE-2010-3692
- set timezone during build

* Tue Aug 03 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.2-1
- update to 1.1.2
- fix  CVE-2010-2795, CVE-2010-2796, #620753

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.1-1
- update to 1.1.1

* Thu May 20 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-1
- update to 1.1.0 finale

* Sun Mar 14 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.1.0-0.1.RC7
- initial packaging (using pear make-rpm-spec CAS-1.1.0RC7.tgz)

