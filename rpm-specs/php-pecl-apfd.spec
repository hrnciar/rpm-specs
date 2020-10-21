# spec file for php-pecl-apfd
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without     tests

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts   0%{?__ztsphp:1}
%global pecl_name  apfd
%global ini_name   40-%{pecl_name}.ini

Summary:        Always Populate Form Data
Name:           php-pecl-%{pecl_name}
Version:        1.0.2
Release:        1%{?dist}
License:        BSD
URL:            http://pecl.php.net/package/%{pecl_name}
Source0:        http://pecl.php.net/get/%{pecl_name}-%{version}%{?prever}.tgz

BuildRequires:  php-devel > 5.3
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# Split off pecl/http
Conflicts:      php-pecl(http) < 2.4


%description
This tiny extension lets PHP's post handler parse `multipart/form-data` and
`application/x-www-form-urlencoded` (or any other customly registered form data
handler, like "json_post") without regard to the request's request method.

This extension does not provide any INI entries, constants, functions or classes.


%prep
%setup -q -c
mv %{pecl_name}-%{version}%{?prever} NTS

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd NTS
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_APFD_VERSION/{s/.* "//;s/".*$//;p}' php_apfd.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --enable-apfd \
    --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --enable-apfd \
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
cd NTS
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff
%endif

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite skipped as zts-php-cgi not available
%endif
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
* Tue Sep 22 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.1-18
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.0.1-15
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Remi Collet <remi@remirepo.net> - 1.0.1-12
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.0.1-11
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-6
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-4
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-4
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 25 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (stable)

* Wed Mar 18 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- cleanup SCL stuff for review

* Wed Mar 18 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (stable)

* Tue Mar 10 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.RC1
- Update to 1.0.0RC1

* Sat Feb 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0
- initial package, for upcoming version 1.0.0
