# Fedora spec file for php-pecl-pq
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-pq
#
# Copyright (c) 2014-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts   0%{?__ztsphp:1}
%global pecl_name  pq
# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}
%global ini_name   50-%{pecl_name}.ini

Summary:        PostgreSQL client library (libpq) binding
Name:           php-pecl-%{pecl_name}
Version:        2.1.7
Release:        1%{?dist}
License:        BSD
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}%{?rcver}.tgz

BuildRequires:  libpq-devel > 9
BuildRequires:  gcc
BuildRequires:  php-devel > 7
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  php-pecl-raphf-devel >= 1.1.0
%if %{with_tests}
BuildRequires:  postgresql-server
BuildRequires:  postgresql-contrib
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}
Requires:       php-raphf%{?_isa}  >= 1.1.0

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
PostgreSQL client library (libpq) binding.

Documents: http://devel-m6w6.rhcloud.com/mdref/pq

Highlights:
* Nearly complete support for asynchronous usage
* Extended type support by pg_type
* Fetching simple multi-dimensional array maps
* Working Gateway implementation


%prep
%setup -q -c
mv %{pecl_name}-%{version}%{?rcver} NTS

# Don't install tests nor LICENSE
sed -e '/role="test"/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PQ_VERSION/{s/.* "//;s/".*$//;p}' php_pq.h)
if test "x${extver}" != "x%{version}%{?rcver}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?rcver}.
   exit 1
fi
cd ..

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{summary}" extension module
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
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: ignore tests with erratic results
rm ?TS/tests/cancel001.phpt
rm ?TS/tests/flush001.phpt


OPT="-n"
[ -f %{php_extdir}/json.so ]  && OPT="$OPT -d extension=json.so"
[ -f %{php_extdir}/raphf.so ] && OPT="$OPT -d extension=raphf.so"

: Minimal load test for NTS extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_zts}
: Minimal load test for ZTS extension
%{__ztsphp} $OPT \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}
%endif

%if %{with_tests}
RET=0

: Running a server
DATABASE=$PWD/data
%ifarch x86_64
PORT=5440
%else
PORT=5436
%endif
pg_ctl initdb -D $DATABASE
cat <<EOF >>$DATABASE/postgresql.conf
unix_socket_directories = '$DATABASE'
port = $PORT
EOF
pg_ctl -D $DATABASE -l $PWD/server.log -w -t 200  start
createdb -h localhost -p $PORT rpmtest

cd NTS
sed -e "/PQ_DSN/s/\"host.*\"/'host=localhost port=$PORT dbname=rpmtest'/" \
    -i tests/_setup.inc

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="$OPT -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || RET=1

%if %{with_zts}
cd ../ZTS
sed -e "/PQ_DSN/s/\"host.*\"/'host=localhost port=$PORT dbname=rpmtest'/" \
    -i tests/_setup.inc

: Upstream test suite  for ZTS extension
TEST_PHP_EXECUTABLE=%{_bindir}/zts-php \
TEST_PHP_ARGS="$OPT -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{_bindir}/zts-php -n run-tests.php --show-diff || RET=1
%endif

cd ..
: Cleanup
psql -h localhost -p $PORT -c "SELECT version()" rpmtest
pg_ctl -D $DATABASE -w stop
rm -rf $DATABASE

exit $RET
%endif


%files
%doc %{pecl_docdir}/%{pecl_name}
%license NTS/LICENSE
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 2.1.7-1
- update to 2.1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Remi Collet <remi@remirepo.net> - 2.1.6-1
- update to 2.1.6

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.1.5-4
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Remi Collet <remi@remirepo.net> - 2.1.5-1
- update to 2.1.5

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.1.4-3
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Remi Collet <remi@remirepo.net> - 2.1.4-1
- update to 2.1.4 (stable)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 2.1.3-2
- undefine _strict_symbol_defs_build

* Wed Jan 10 2018 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3 (stable)

* Fri Nov 10 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-6
- ignore 1 test with erratic results

* Mon Oct 23 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-5
- fix botstraping for postgresql 10, FTBFS from Koschei

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.1.2-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul  3 2017 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2 (stable)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-3
- add upstream patch for 7.1
  https://github.com/m6w6/ext-pq/issues/23

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- update to 2.1.1 (php 7, stable)

* Fri May 20 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1 (php 5, stable)
- open https://github.com/m6w6/ext-pq/issues/19 failed tests
  so temporarily ignore them with pgsql < 9.3 on EL-7
- open https://github.com/m6w6/ext-pq/issues/18 pgsql < 9.3

* Wed May  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (stable)

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- cleanup for Fedora review #1299907
- drop scriptlets (replaced by file triggers in php-pear)
- ignore 1 failed test with PHP 5.4.16

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (stable)

* Mon Dec  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.RC1
- Update to 1.0.0RC1 (beta)

* Sat Sep  5 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 (beta)

* Wed Jul 29 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.3.RC2
- allow build against rh-php56 (as more-php56)

* Tue Jul 28 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.2.RC2
- Update to 0.6.0RC2 (beta)
- raise dependency on raphf 1.1.0

* Wed Jun 10 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-0.1.RC1
- Update to 0.6.0RC1
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 0.5.5-1.1
- Fedora 21 SCL mass rebuild

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Sat Oct 18 2014 Remi Collet <remi@fedoraproject.org> - 0.5.2-2
- launch a postgresql server for test
- enable upstream test suite during build

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- initial package, version 0.5.1 (beta)
