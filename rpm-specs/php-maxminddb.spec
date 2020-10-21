# Fedora spec file for php-maxminddb
# Without SCL compatibility from:
#
# remirepo spec file for php-maxminddb
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit   b566d429ac9aec10594b0935be8ff38302f8d5c8
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    maxmind
%global gh_project  MaxMind-DB-Reader-php
# Extension
%global pecl_name   maxminddb
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global ini_name    40-%{pecl_name}.ini
# pure PHP library
%global pk_vendor    maxmind-db
%global pk_project   reader
%global with_tests   0%{!?_without_tests:1}

Summary:       MaxMind DB Reader extension
Name:          php-maxminddb
Version:       1.8.0
Release:       1%{?dist}
License:       ASL 2.0
URL:           https://github.com/%{gh_owner}/%{gh_project}

Source0:       %{name}-%{version}-%{gh_short}.tgz
Source1:       makesrc.sh

BuildRequires: php-devel >= 7.2
BuildRequires: php-pear  >= 1.10
BuildRequires: pkgconfig(libmaxminddb) >= 1.0.0

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city

# PECL
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

This optional PHP C Extension is a drop-in replacement for
MaxMind\Db\Reader.

Databases are available in geolite2-country and geolite2-city packages.


%package -n php-%{pk_vendor}-%{pk_project}
Summary:       MaxMind DB Reader

BuildArch:     noarch
BuildRequires: php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires: php-bcmath
BuildRequires: php-gmp
# from composer.json "require-dev": {
#        "friendsofphp/php-cs-fixer": "2.*",
#        "phpunit/phpunit": ">=8.0.0,<10.0.0",
#        "php-coveralls/php-coveralls": "^2.1",
#        "phpunit/phpcov": ">=6.0.0",
#        "squizlabs/php_codesniffer": "3.*"
BuildRequires: phpunit8
%endif

# from composer.json "require": {
#        "php": ">=5.6"
Requires:      php(language) >= 5.6
# from composer.json "suggest": {
#        "ext-bcmath": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-gmp": "bcmath or gmp is required for decoding larger integers with the pure PHP decoder",
#        "ext-maxminddb": "A C-based database decoder that provides significantly faster lookups"
Recommends:    php-bcmath
Recommends:    php-gmp
Recommends:    php-maxminddb
# from composer.json "conflict": {
#        "ext-maxminddb": "<1.6.0,>=2.0.0"
Conflicts:     php-maxminddb < %{version}
# Weak dependencies on databases
Recommends:    geolite2-country
Suggests:      geolite2-city
# From phpcompatifo report for 1.3.0
Requires:      php-filter
Requires:      php-spl

Provides:      php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description -n php-%{pk_vendor}-%{pk_project}
MaxMind DB Reader PHP API.

MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).

Databases are available in geolite2-country and geolite2-city packages.

The extension available in php-maxminddb package allow better
performance.

Autoloader: %{_datadir}/php/MaxMind/Db/Reader/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%{_bindir}/phpab \
    --template fedora \
    --output src/MaxMind/Db/Reader/autoload.php \
    src/MaxMind/Db

mv ext NTS

cd NTS

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MAXMINDDB_VERSION/{s/.* "//;s/".*$//;p}'  php_maxminddb.h)
if test "x${extver}" != "x%{version}%{?gh_date:-dev}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?gh_date:-dev}.
   exit 1
fi
cd ..

%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{pecl_name}' extension module
extension = %{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-php-config=%{_bindir}/php-config \
    --with-libdir=%{_lib} \
    --with-maxminddb
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-php-config=%{_bindir}/zts-php-config \
    --with-libdir=%{_lib} \
    --with-maxminddb
make %{?_smp_mflags}
%endif


%install
# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Install the NTS stuff
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
# Install the ZTS stuff
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

mkdir -p                %{buildroot}%{_datadir}/php/MaxMind
cp -pr src/MaxMind/Db   %{buildroot}%{_datadir}/php/MaxMind/Db


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}
%endif

%if %{with_tests}
ret=0

cd NTS
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || ret=1

%if %{with_zts}
cd ../ZTS
: Upstream test suite for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php --show-diff || ret=1
%endif

cd ..
: Upstream test suite for the library
for cmd in php php72 php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
      --verbose || ret=1
  fi
done

: Upstream test suite for the library with the extension
php --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
  %{_bindir}/phpunit8 \
    --bootstrap %{buildroot}%{_datadir}/php/MaxMind/Db/Reader/autoload.php \
    --verbose || ret=1
%endif
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%files -n php-%{pk_vendor}-%{pk_project}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/MaxMind
     %{_datadir}/php/MaxMind/Db


%changelog
* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- now available on pecl
- raise dependency on PHP 7.2
- switch to phpunit8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Dec 13 2019 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.5.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Tue Oct  1 2019 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on PHP 5.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan  5 2019 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- cleanup for Fedora review

* Wed Nov 21 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- open https://github.com/maxmind/MaxMind-DB-Reader-php/issues/79
  to report test failure on 32-bit

* Wed Nov 14 2018 Remi Collet <remi@remirepo.net> - 1.3.0-3
- add php-maxmind-db-reader sub-package providing the library
- open https://github.com/maxmind/MaxMind-DB-Reader-php/issues/77
  to report test failures on 32-bit

* Thu Nov  8 2018 Remi Collet <remi@remirepo.net> - 1.3.0-2
- add upstream patches from merged PRs
- add weak dependencies on geolite2 databases

* Wed Nov  7 2018 Remi Collet <remi@remirepo.net> - 1.3.0-1
- new package, version 1.3.0
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/73 pkg-config
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/74 MINFO
- open https://github.com/maxmind/MaxMind-DB-Reader-php/pull/75 arginfo
