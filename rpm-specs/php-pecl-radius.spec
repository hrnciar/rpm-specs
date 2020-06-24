# Fedora spec file for php-pecl-radius
#
# Copyright (c) 2009-2016 Remi Collet
# Copyright (c) 2006-2009 Christopher Stone
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global pecl_name  radius
%global with_zts   0%{?__ztsphp:1}
%global ini_name   40-%{pecl_name}.ini
%global prever     b1

Name:           php-pecl-radius
Version:        1.4.0
Release:        0.12.%{prever}%{?dist}
Summary:        Radius client library

License:        BSD
URL:            http://pecl.php.net/package/radius
Source0:        http://pecl.php.net/get/radius-%{version}%{?prever}.tgz

BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-posix
BuildRequires:  php-sockets

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This package is based on the libradius of FreeBSD, with some modifications
and extensions.  This PECL provides full support for RADIUS authentication
(RFC 2865) and RADIUS accounting (RFC 2866), works on Unix and on Windows.
Its an easy way to authenticate your users against the user-database of your
OS (for example against Windows Active-Directory via IAS).


%prep
%setup -qc

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

mv %{pecl_name}-%{version}%{?prever} NTS
cd NTS

extver=$(sed -n '/#define PHP_RADIUS_VERSION/{s/.* "//;s/".*$//;p}' php_radius.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif


%build
cd NTS
%{_bindir}/phpize
%configure  --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure  --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# Install XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# install config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -Dpm644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
cd NTS
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
DEP=
[ -f %{php_extdir}/posix.so ]   && DEP="$DEP -d extension=posix.so"
[ -f %{php_extdir}/sockets.so ] && DEP="$DEP -d extension=sockets.so"

%if "%{php_version}" > "5.5"
# used fake_server is not compatible with php 5.5
# Deprecated: Non-static method xxx should not be called statically
rm -f $(grep -l fake_server ?TS/tests/*phpt)
%endif

# simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite for NTS extension
cd NTS
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $DEP -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php

%if %{with_zts}
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite for ZTS extension
cd ../ZTS
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n $DEP -d extension=$PWD/modules/%{pecl_name}.so" \
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.12.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.4.0-0.11.b1
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.10.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.9.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.4.0-0.8.b1
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.7.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.6.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.4.0-0.5.b1
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.4.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-0.2.b1
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.4.0-0.1.b1
- Update to 1.4.0b1 (beta)

* Mon Feb 15 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 (stable)
- don't install/register tests
- fix license installation

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 1.2.7-10
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.2.7-6
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Remi Collet <rcollet@redhat.com> - 1.2.7-4
- add numerical prefix to extension configuration file

* Sun Mar 16 2014 Remi Collet <remi@fedoraproject.org> - 1.2.7-3
- run upstream test suite
- install doc in pecl_docdir
- install tests in pecl_testdir
- add missing License file (extracted from headers)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Remi Collet <remi@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7 (security)
- build ZTS extension
- spec cleanups

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 1.2.5-16
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 1.2.5-13
- build against php 5.4 with patch from upstream
- fix filters

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul  6 2011  Remi Collet <Fedora@FamilleCollet.com> - 1.2.5-11
- fix php_zend_api usage, fix FTBFS #715846

* Sat Oct 23 2010  Remi Collet <Fedora@FamilleCollet.com> - 1.2.5-10
- add filter_provides to avoid private-shared-object-provides ncurses.so

* Sat Aug 28 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.2.5-9
- clean define
- use more macros
- add simple load test in %%check

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Remi Collet <Fedora@FamilleCollet.com> - 1.2.5-7
- rebuild for new PHP 5.3.0 ABI (20090626)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 19 2008 Christopher Stone <chris.stone@gmail.com> 1.2.5-5
- Fix Requires for post/postun sections (bz #442699)

* Fri Feb 22 2008 Christopher Stone <chris.stone@gmail.com> 1.2.5-4
- Properly register package

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.5-3
- Autorebuild for GCC 4.3

* Sun Sep 30 2007 Christopher Stone <chris.stone@gmail.com> 1.2.5-2
- Update to new standards

* Sat Sep 08 2007 Christopher Stone <chris.stone@gmail.com> 1.2.5-1
- Upstream sync

* Sun Mar 11 2007 Christopher Stone <chris.stone@gmail.com> 1.2.4-2
- Use new ABI check for FC-6
- Create directory to untar sources
- Remove %%{release} from Provides

* Sat Jul 01 2006 Christopher Stone <chris.stone@gmail.com> 1.2.4-1
- Initial release
