# Fedora spec file for php-pecl-mcrypt
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-mcrypt
#
# Copyright (c) 2017-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts       0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name      mcrypt
%global ini_name       30-%{pecl_name}.ini

Summary:      Bindings for the libmcrypt library
Name:         php-pecl-mcrypt
Version:      1.0.3
Release:      2%{?dist}
License:      PHP
URL:          http://pecl.php.net/package/mcrypt

Source:       http://pecl.php.net/get/%{pecl_name}-%{version}%{?prever}.tgz

BuildRequires: php-devel > 7.2
BuildRequires: libmcrypt-devel
BuildRequires: php-pear

Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}

Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Obsoletes:    php-%{pecl_name} < 7.2.0
Provides:     php-%{pecl_name} = 1:%{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = 1:%{version}-%{release}


%description
Provides bindings for the unmaintained libmcrypt.



%prep 
%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    %{?_licensedir:-e '/LICENSE/s/role="doc"/role="src"/' } \
    -i package.xml

mv %{pecl_name}-%{version}%{?prever} NTS
cd NTS
sed -e '/PHP_MCRYPT_VERSION/s/PHP_VERSION/"%{version}"/' -i php_mcrypt.h

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MCRYPT_VERSION/{s/.* "//;s/".*$//;p}' php_mcrypt.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi

cd ..
: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}
EOF

%if %{with_zts}
: Duplicate sources tree for ZTS build
cp -pr NTS ZTS
%endif


%build
cd NTS
%{_bindir}/phpize
%configure \
  --with-mcrypt \
  --with-php-config=%{_bindir}/php-config

make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
  --with-mcrypt \
  --with-php-config=%{_bindir}/zts-php-config

make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}
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
export REPORT_EXIT_STATUS=1
export NO_INTERACTION=1

# Warning: Use of undefined constant MCRYPT_CBC - assumed 'MCRYPT_CBC'
rm ?TS/tests/bug8040.phpt

cd NTS
: minimal load test of NTS extension
%{_bindir}/php --no-php-ini \
    --define extension_dir=modules \
    --define extension=%{pecl_name} \
    --modules | grep %{pecl_name}

: upstream test suite for NTS extension
make test

%if %{with_zts}
cd ../ZTS
: minimal load test of ZTS extension
%{_bindir}/zts-php --no-php-ini \
    --define extension_dir=modules \
    --define extension=%{pecl_name} \
    --modules | grep %{pecl_name}

: upstream test suite for ZTS extension
make test
%endif


%files
%license NTS/LICENSE
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3 (no change)
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 1.0.1-5
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 1.0.1-2
- undefine _strict_symbol_defs_build

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- clean-up for Fedora review

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 1.0.1-4
- rebuild for PHP 7.2.0beta1 new API

* Fri Jul  7 2017 Remi Collet <remi@remirepo.net> - 1.0.1-3
- drop .so extension for configuration file

* Wed Jun 21 2017 Remi Collet <remi@remirepo.net> - 1.0.1-2
- rebuild for 7.2.0alpha2

* Wed Apr 12 2017 Remi Collet <remi@remirepo.net> - 1.0.1-1
- New spec for version 1.0.1 (PHP 7.2)
