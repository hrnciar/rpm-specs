# remirepo/fedora spec file for php-pear-crypt-gpg
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Crypt_GPG
%if 0%{?rhel}
# All features require GnuPG v1 (under investigation)
%global with_tests 0%{?_with_tests:1}
%else
%global with_tests 0%{!?_without_tests:1}
%endif

Name:           php-pear-crypt-gpg
Version:        1.6.4
Release:        2%{?dist}
Summary:        GNU Privacy Guard (GnuPG)

License:        LGPLv2+
URL:            http://pear.php.net/package/%{pear_name}
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

# Use /usr/bin/gpg1 if available
Patch0:         %{pear_name}-gpg1.patch

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)
%if %{with_tests}
# for tests
BuildRequires:  phpunit7
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 6
BuildRequires:  %{_bindir}/gpg1
%else
BuildRequires:  %{_bindir}/gpg
%endif
BuildRequires:  %{_bindir}/gpg-agent
BuildRequires:  %{_bindir}/ps
%endif
BuildRequires:  php-fedora-autoloader-devel

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 6
Requires:       %{_bindir}/gpg1
%else
Requires:       %{_bindir}/gpg
%endif
# From package.pear
Requires:       php(language) >= 5.4.8
Requires:       php-pear(Console_CommandLine) >= 1.1.10
Requires:       php-mbstring
# From phpcompatinfo report for version 1.4.1
Requires:       php-ctype
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Optional
Requires:       php-posix
Requires:       php-composer(fedora/autoloader)

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/crypt_gpg) = %{version}
Provides:       php-autoloader(pear/crypt_gpg) = %{version}


%description
This package provides an object oriented interface to 
GNU Privacy Guard (GnuPG).

Though GnuPG can support symmetric-key cryptography, this package
is intended only to facilitate public-key cryptography.

Autoloader: %{pear_phpdir}/Crypt/GPG/autoload.php


%prep
%setup -q -c

%{?_licensedir:sed -e '/LICENSE/d' -i package.xml}

cd %{pear_name}-%{version}
if [ -x %{_bindir}/gpg1 ]; then
%patch0 -p1 -b .rpm
sed -e '/Engine.php/s/md5sum="[^"]*"//' \
    -i ../package.xml
fi

mv  ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

phpab --template fedora --output Crypt/GPG/autoload.php Crypt


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

# Autoloader
install -pm 644 Crypt/GPG/autoload.php %{buildroot}/%{pear_phpdir}/Crypt/GPG/autoload.php


%if %{with_tests}
%check
cd %{pear_name}-%{version}/tests

: Upstream test suite
ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit7 \
      --include-path=%{buildroot}%{pear_phpdir} \
      --verbose . || ret=1
  fi
done
exit $ret
%endif


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi


%files
%{?_licensedir:%license %{pear_name}-%{version}/LICENSE}
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}
%{_bindir}/crypt-gpg-pinentry
%dir %{pear_phpdir}/Crypt
     %{pear_phpdir}/Crypt/GPG*


%changelog
* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 1.6.4-2
- update to 1.6.4
- add classmap autoloader

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Remi Collet <remi@remirepo.net> - 1.6.3-3
- fix FTBFS, use gpg1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 1.6.3-1
- update to 1.6.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep  4 2017 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2
- open https://pear.php.net/bugs/bug.php?id=21240 - PHP 7.2 test failure

* Sun Aug 27 2017 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Remi Collet <remi@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3

* Mon Jun 20 2016 Remi Collet <remi@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Apr 17 2016 Remi Collet <remi@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- Initial package, version 1.4.0 (stable)
- open https://github.com/pear/Crypt_GPG/pull/19 for fsf address
