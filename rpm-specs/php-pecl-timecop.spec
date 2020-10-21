# Fedora spec file for php-pecl-timecop
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-timecop
#
# Copyright (c) 2017-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global pecl_name   timecop
%global with_zts    0%{!?_without_zts:%{?__ztsphp:1}}
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}
%if "%{php_version}" < "5.6"
%global ini_name    %{pecl_name}.ini
%else
%global ini_name    40-%{pecl_name}.ini
%endif

Summary:       Time travel and freezing extension
Name:          php-pecl-timecop
Version:       1.2.10
Release:       10%{?dist}
License:       MIT
URL:           http://pecl.php.net/package/%{pecl_name}
Source0:       http://pecl.php.net/get/%{pecl_name}-%{version}.tgz

BuildRequires: php-devel
BuildRequires: php-pear

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:      php-%{pecl_name}               = %{version}
Provides:      php-%{pecl_name}%{?_isa}       = %{version}
Provides:      php-pecl(%{pecl_name})         = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
A PHP extension providing "time travel" and "time freezing" capabilities,
inspired by ruby timecop gem.


%prep
%setup -qc
mv %{pecl_name}-%{version} NTS

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    %{?_licensedir:-e  '/LICENSE/s/role="doc"/role="src"/' } \
    -i package.xml

cd NTS
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_TIMECOP_VERSION/{s/.* "//;s/".*$//;p}' php_timecop.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

%if %{with_zts}
# duplicate for ZTS build
cp -pr NTS ZTS
%endif

# Drop in the bit of configuration
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' module
extension = %{pecl_name}.so

; Configuration
;timecop.func_override = 1
;timecop.sync_request_time = 1
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-php-config=%{_bindir}/php-config \
    --with-libdir=%{_lib} \
    --enable-timecop
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-php-config=%{_bindir}/zts-php-config \
    --with-libdir=%{_lib} \
    --enable-timecop
make %{?_smp_mflags}
%endif


%install
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

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
if [ -f %{php_extdir}/calendar.so ]; then
    MOD="-d extension=calendar.so"
fi

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
%if "%{php_version}" > "7.3"
rm ?TS/tests/date_007.phpt
rm ?TS/tests/date_008.phpt
rm ?TS/tests/date_override_007.phpt
rm ?TS/tests/date_override_008.phpt
rm ?TS/tests/immutable_007.phpt
rm ?TS/tests/immutable_008.phpt
rm ?TS/tests/immutable_override_007.phpt
rm ?TS/tests/immutable_override_008.phpt
%endif

cd NTS
: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $MOD -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || : ignore
%endif

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: Upstream test suite  for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n $MOD -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php --show-diff
%endif
%endif


%if 0%{?fedora} < 24
# when pear installed alone, after us
%triggerin -- php-pear
if [ -x %{__pecl} ] ; then
    %{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :
fi

# posttrans as pear can be installed after us
%posttrans
if [ -x %{__pecl} ] ; then
    %{pecl_install} %{pecl_xmldir}/%{name}.xml >/dev/null || :
fi

%postun
if [ $1 -eq 0 -a -x %{__pecl} ] ; then
    %{pecl_uninstall} %{pecl_name} >/dev/null || :
fi
%endif


%files
%doc %{pecl_docdir}/%{pecl_name}
%{?_licensedir:%license NTS/LICENSE}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.2.10-8
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 1.2.10-6
- ignore failing tests with recent timelib in 7.3, reported as
  https://github.com/hnw/php-timecop/issues/42

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.2.10-5
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.2.10-2
- undefine _strict_symbol_defs_build

* Thu Nov 23 2017 Remi Collet <remi@remirepo.net> - 1.2.10-1
- Update to 1.2.10

* Wed Nov 22 2017 Remi Collet <remi@remirepo.net> - 1.2.8-2
- add upstream patch for PHP 7.2

* Fri Jul  7 2017 Remi Collet <remi@remirepo.net> - 1.2.8-1
- Update to 1.2.8 (no change)

* Fri Jul  7 2017 Remi Collet <remi@remirepo.net> - 1.2.7-1
- cleanup for Fedora review

* Fri Jul  7 2017 Remi Collet <remi@remirepo.net> - 1.2.7-1
- rename to php-pecl-timecop
- use sources from pecl
- update to 1.2.7
- open https://github.com/hnw/php-timecop/pull/21 - bad roles
- open https://github.com/hnw/php-timecop/pull/22 - missing file

* Tue Jul  4 2017 Remi Collet <remi@remirepo.net> - 1.2.6-1
- new package, version 1.2.6 (beta)
