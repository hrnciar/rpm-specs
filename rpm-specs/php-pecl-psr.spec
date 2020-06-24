# Fedora spec file for php-pecl-psr
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-psr
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global pecl_name   psr
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global with_tests  0%{!?_without_tests:1}
%global ini_name    40-%{pecl_name}.ini

%global upstream_version 1.0.0
#global upstream_prever  RC4

Summary:       PSR interfaces
Name:          php-pecl-psr
Version:       %{upstream_version}
Release:       1%{?dist}
Source0:       https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz
License:       BSD
URL:           https://pecl.php.net/package/psr

BuildRequires: gcc
BuildRequires: php-devel >= 7.0
BuildRequires: php-pear

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:      php-%{pecl_name}               = %{version}
Provides:      php-%{pecl_name}%{?_isa}       = %{version}
Provides:      php-pecl(%{pecl_name})         = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension provides the accepted PSR interfaces,
so they can be used in an extension.

See http://www.php-fig.org/psr/


%package devel
Summary:       %{name} developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}

%description devel
These are the files needed to compile programs using %{name}.


%prep
%setup -q -c
# rename source folder
mv %{pecl_name}-%{upstream_version}%{?upstream_prever} NTS

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd NTS
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PSR_VERSION/{s/.* "//;s/".*$//;p}' php_psr.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --enable-psr \
    --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --enable-psr \
    --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
# Install the NTS stuff
make -C NTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
# Install the ZTS stuff
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Test & Documentation
cd NTS
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i       %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"'  ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
# simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_zts}
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}
%endif

%if %{with_tests}
cd NTS
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff

%if %{with_zts}
cd ../ZTS
: Upstream test suite for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php --show-diff
%endif
%else
: Upstream test suite disabled
%endif


%files
%license NTS/LICENSE.md
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%{php_extdir}/%{pecl_name}.so
%config(noreplace) %{php_inidir}/%{ini_name}

%if %{with_zts}
%{php_ztsextdir}/%{pecl_name}.so
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%endif


%files devel
%doc %{pecl_testdir}/%{pecl_name}
%{php_incldir}/ext/%{pecl_name}

%if %{with_zts}
%{php_ztsincldir}/ext/%{pecl_name}
%endif


%changelog
* Wed Feb 19 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- update to 1.0.0 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 0.7.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 0.7.0-1
- update to 0.7.0
- raise minimal PHP version to 7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Remi Collet <remi@remirepo.net> - 0.6.1-1
- update to 0.6.1 (no change)

* Mon Nov 12 2018 Remi Collet <remi@remirepo.net> - 0.6.0-1
- update to 0.6.0
- raise dependency on PHP 5.6

* Tue Oct 30 2018 Remi Collet <remi@remirepo.net> - 0.5.1-1
- update to 0.5.1

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 0.5.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Tue Sep 11 2018 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 0.4.0-2
- License is BSD, from review #1551913

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 0.4.0-1
- cleanup for Fedora review

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 0.4.0-1
- Update to 0.4.0

* Fri Feb  9 2018 Remi Collet <remi@remirepo.net> - 0.3.0-1
- update to 0.3.0 (stable)

* Sat Aug 12 2017 Remi Collet <remi@remirepo.net> - 0.3.0~RC4-1
- update to 0.3.0RC4

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 0.3.0~RC3-1
- initial package
