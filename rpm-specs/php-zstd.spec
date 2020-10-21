# Fedora spec file for php-zstd
# without SCL compatibility from:
#
# remirepo spec file for php-zstd
#
# Copyright (c) 2018-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global pecl_name   zstd
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global ini_name    40-%{pecl_name}.ini

Summary:       Zstandard extension
Name:          php-%{pecl_name}
Version:       0.9.0
Release:       2%{?dist}
License:       MIT
URL:           https://pecl.php.net/package/%{pecl_name}
Source0:       https://pecl.php.net/get/%{pecl_name}-%{version}%{?prever}.tgz

BuildRequires: gcc
BuildRequires: php-devel
BuildRequires: php-pear
BuildRequires: pkgconfig(libzstd)

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:       php-pecl-%{pecl_name}          = %{version}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
PHP extension for compression and decompression with Zstandard library.


%package devel
Summary:       %{name} developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{name}.


%prep
%setup -qc
mv %{pecl_name}-%{version} NTS

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml
sed -e '\:"zstd/:d' -i package.xml

cd NTS
# Use the system library
rm -r zstd

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_ZSTD_EXT_VERSION/{s/.* "//;s/".*$//;p}' php_zstd.h)
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
; Enable '%{summary}' extension module
extension = %{pecl_name}.so
EOF


%build
%{?dtsenable}

cd NTS
%{_bindir}/phpize
%configure \
    --with-php-config=%{_bindir}/php-config \
    --with-libzstd \
    --with-libdir=%{_lib} \
    --enable-zstd
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-php-config=%{_bindir}/zts-php-config \
    --with-libzstd \
    --with-libdir=%{_lib} \
    --enable-zstd
make %{?_smp_mflags}
%endif


%install
%{?dtsenable}

# Install the NTS stuff
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
# Install the ZTS stuff
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Test & Documentation
for i in $(grep 'role="test"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do [ -f NTS/tests/$i ] && install -Dpm 644 NTS/tests/$i %{buildroot}%{pecl_testdir}/%{pecl_name}/tests/$i
done
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
export REPORT_EXIT_STATUS=1
%ifarch s390x
: ignore test with erratic results
rm ?TS/tests/streams_*phpt
%endif

cd NTS
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --offline --show-diff

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite  for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
%{__ztsphp} -n run-tests.php -q --offline --show-diff
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


%files devel
%doc NTS/tests
%{php_incldir}/ext/%{pecl_name}

%if %{with_zts}
%{php_ztsincldir}/ext/%{pecl_name}
%endif


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Remi Collet <remi@remirepo.net> - 0.9.0-1
- update to 0.9.0 (stable)

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 0.8.0-1
- update to 0.8.0
- sources from pecl

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 0.7.3-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 0.7.3-1
- cleanup for Fedora review

* Wed Apr 24 2019 Remi Collet <remi@remirepo.net> - 0.7.3-1
- update to 0.7.3

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 0.7.2-1
- update to 0.7.2
- use bundled libzstd 1.4.0

* Fri Apr 19 2019 Remi Collet <remi@remirepo.net> - 0.7.1-1
- update to 0.7.1

* Tue Apr 16 2019 Remi Collet <remi@remirepo.net> - 0.7.0-1
- update to 0.7.0

* Mon Apr 15 2019 Remi Collet <remi@remirepo.net> - 0.6.1-2
- test build for Stream implementation, from
  https://github.com/kjdev/php-ext-zstd/pull/17

* Thu Apr  4 2019 Remi Collet <remi@remirepo.net> - 0.6.1-1
- update to 0.6.1

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 0.6.0-1
- update to 0.6.0

* Mon Jan  7 2019 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 0.4.14-4
- ignore test suite results with newer system library

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 0.4.14-3
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 0.4.14-2
- rebuild for 7.3.0alpha4 new ABI

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 0.4.14-1
- update to 0.4.14

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 0.4.13-1
- update to 0.4.13

* Wed Jan 31 2018 Remi Collet <remi@remirepo.net> - 0.4.12-1
- update to 0.4.12 (no change, PR merged upstream)

* Tue Jan 30 2018 Remi Collet <remi@remirepo.net> - 0.4.11-1
- new package, version 0.4.11
- add patch to build with system libzstd from
  https://github.com/kjdev/php-ext-zstd/pull/7
