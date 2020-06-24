# Fedora spec file for php-pecl-inotify
# Without SCL compatibility from:
#
# remirepo spec file for php-pecl-inotify
#
# Copyright (c) 2013-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts   0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name  inotify
%global ini_name   40-%{pecl_name}.ini

Summary:        Inotify
Name:           php-pecl-%{pecl_name}
Version:        2.0.0
Release:        10%{?dist}
License:        PHP
URL:            http://pecl.php.net/package/%{pecl_name}
Source0:        http://pecl.php.net/get/%{pecl_name}-%{version}.tgz

BuildRequires:  php-devel > 7
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
The inotify extension allows to use inotify functions in a PHP script.


%prep
%setup -q -c
mv %{pecl_name}-%{version} NTS
mv package2.xml package.xml

sed -e '/inotify.php/s/role="php"/role="doc"/' \
    -e '/tail.php/s/role="php"/role="doc"/' \
    -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_INOTIFY_VERSION/{s/.* "//;s/".*$//;p}' php_inotify.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi
cd ..

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/php-config

make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{_bindir}/zts-php-config

make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}

install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
cd NTS
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for NTS extension
cd NTS
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php


%if %{with_zts}
: Minimal load test for ZTS extension
cd ../ZTS
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.0.0-9
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.0.0-6
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.0.0-3
- undefine _strict_symbol_defs_build

* Wed Oct 04 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Tue Aug 22 2017 Remi Collet <remi@remirepo.net> - 2.0.0-1
- cleanup for Fedora review

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 2.0.0-6
- rebuild for PHP 7.2.0beta1 new API

* Sun Feb  5 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-4
- use package2.xml for correct registration

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-4
- rebuild with PHP 7.1.0 GA

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-3
- rebuild for PHP 7.1 new API version

* Sat Mar  5 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- adapt for F24

* Fri Jan 29 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 for PHP 7 (stable)
- don't install/register tests
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 0.1.6-5.1
- Fedora 21 SCL mass rebuild

* Tue Aug 26 2014 Remi Collet <rcollet@redhat.com> - 0.1.6-5
- improve SCL build

* Wed Apr 16 2014 Remi Collet <remi@fedoraproject.org> - 0.1.6-4
- add numerical prefix to extension configuration file

* Thu Mar 20 2014 Remi Collet <rcollet@redhat.com> - 0.1.6-3
- adapt for SCL

* Sun Nov 24 2013 Remi Collet <remi@fedoraproject.org> - 0.1.6-2
- install doc in pecl doc_dir
- install tests in pecl test_dir (in devel)
- cleanups for Copr

* Sun Oct  6 2013 Remi Collet <remi@fedoraproject.org> - 0.1.6-1
- initial package, version 0.1.6 (stable)

