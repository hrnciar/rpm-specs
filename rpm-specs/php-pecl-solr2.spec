# Fedora spec file for php-pecl-solr2
#
# Copyright (c) 2011-2019 Remi Collet
# Copyright (c) 2010 Johan Cwiklinski
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global pecl_name solr
%global with_zts  0%{?__ztsphp:1}
# After 20-curl, 40-json
%global ini_name  50-%{pecl_name}.ini
# For full test (using localhost server) use --with tests
# retrieve: docker pull omars/solr53
# create:   docker run -d -p 8983:8983 --name solr5 -t omars/solr53
# cleanup:  docker stop solr5 && docker rm solr5
%global with_tests 0%{?_with_tests:1}

Summary:        Object oriented API to Apache Solr
Name:           php-pecl-solr2
Version:        2.5.0
Release:        4%{?dist}
License:        PHP
URL:            http://pecl.php.net/package/solr

Source0:        http://pecl.php.net/get/%{pecl_name}-%{version}%{?prever}.tgz

BuildRequires:  php-devel > 7
BuildRequires:  php-pear
BuildRequires:  php-curl
BuildRequires:  php-json
BuildRequires:  curl-devel
BuildRequires:  libxml2-devel
BuildRequires:  pcre-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-curl%{?_isa}
Requires:       php-json%{?_isa}

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

Obsoletes:      php-pecl-solr         < 2
Provides:       php-pecl-solr         = %{version}
Provides:       php-pecl-solr%{?_isa} = %{version}


%description
It effectively simplifies the process of interacting with Apache Solr using
PHP5 and it already comes with built-in readiness for the latest features.

The extension has features such as built-in, serializable query string builder
objects which effectively simplifies the manipulation of name-value pair
request parameters across repeated requests.

The response from the Solr server is also automatically parsed into native php
objects whose properties can be accessed as array keys or object properties
without any additional configuration on the client-side.

Its advanced HTTP client reuses the same connection across multiple requests
and provides built-in support for connecting to Solr servers secured behind
HTTP Authentication or HTTP proxy servers. It is also able to connect to
SSL-enabled containers.

Please consult the documentation for more details on features.
  http://php.net/solr

Warning: PECL Solr 2 is not compatible with Solr Server < 4.0


%prep
%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

mv %{pecl_name}-%{version}%{?prever} NTS

cd NTS
# Check version
DIR=src/php$(%{__php} -r 'echo PHP_MAJOR_VERSION;')
extver=$(sed -n '/#define PHP_SOLR_VERSION /{s/.* "//;s/".*$//;p}' $DIR/php_solr_version.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi

cd ..

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable Solr extension module
extension=%{pecl_name}
EOF

%if %{with_zts}
cp -r NTS ZTS
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
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
%if %{with_tests}
sed -e '/SOLR_SERVER_CONFIGURED/s/false/true/' \
    -e '/SOLR_SERVER_HOSTNAME/s/solr.test/localhost/' \
    -i ?TS/tests/test.config.inc
%else
sed -e '/SOLR_SERVER_CONFIGURED/s/true/false/' \
    -i ?TS/tests/test.config.inc
%endif

: Minimal load test for NTS installed extension
%{__php} \
   -n \
   -d extension=curl \
   -d extension=json \
   -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
   -m | grep %{pecl_name}

: Upstream test suite for NTS extension
cd NTS
TEST_PHP_ARGS="-n -d extension=curl.so -d extension=json.so -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
NO_INTERACTION=1 \
TEST_PHP_EXECUTABLE=%{__php} \
%{__php} -n run-tests.php --show-diff

%if %{with_zts}
: Minimal load test for ZTS installed extension
%{__ztsphp} \
   -n \
   -d extension=curl \
   -d extension=json \
   -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
   -m | grep %{pecl_name}

: Upstream test suite for ZTS extension
cd ../ZTS
TEST_PHP_ARGS="-n -d extension=curl -d extension=json -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
NO_INTERACTION=1 \
TEST_PHP_EXECUTABLE=%{__ztsphp} \
%{__ztsphp} -n run-tests.php --show-diff
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.5.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Remi Collet <remi@remirepo.net> - 2.4.0-11
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add upstream patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Remi Collet <remi@remirepo.net> - 2.4.0-8
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 2.4.0-7
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Remi Collet <remi@fedoraproject.org> - 2.4.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 2.4.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Wed Mar 30 2016 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- update to 2.4.0 (stable)

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-3
- drop scriptlets (replaced by file triggers in php-pear)
- cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0 (stable)

* Sun Sep 27 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-2
- add upstream patch for zpp calls (fix broken ppc64)

* Sun Sep 27 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1 (stable)
- add option to build full test suite with a Solr server

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 18 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- don't install/register test suite

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- cleanup for review
- ignore 080.solrutils_escapequerychars.phpt on ppc64

* Mon Jun 23 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.4
- test build before 2.0.0 finale

* Thu Apr 17 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.3.beta
- add numerical prefix to extension configuration file (php 5.6)

* Tue Mar 25 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.2.beta
- allow SCL build

* Sat Mar  8 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.beta
- update to 2.0.0b (beta)
- install doc in pecl_docdir
- install tests in pecl_testdir

* Sun Oct 21 2012 Remi Collet <remi@fedoraproject.org> - 1.0.2-4
- rebuild

* Tue Nov 29 2011 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- php 5.4 build

* Tue Nov 29 2011 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Mon Nov 28 2011 Remi Collet <remi@fedoraproject.org> - 1.0.1-4.svn320130
- svn snapshot (test suite is now ok)

* Wed Nov 16 2011 Remi Collet <remi@fedoraproject.org> - 1.0.1-3
- build against php 5.4
- ignore test result because of https://bugs.php.net/60313

* Thu Oct 06 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.1-2
- ZTS extension
- spec cleanups

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 1.0.1-1
- Version 1.0.1 (stable) - API 1.0.1 (stable)
- run test suite after build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.9.11-1
- update to latest release

* Thu May 13 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.9.10-2
- consitent use of pecl_name macro
- add %%check
- fixes some typos
- thanks Remi :)

* Thu May 13 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.9.10-1
- update to latest release

* Tue Apr 27 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.9.9-2
- Add missing Requires
- Remove conditionnal 'php_zend_api' 'pecl_install' no longer required
- %%define no longer must be used
- Thanks to Remi :)

* Mon Apr 26 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.9.9-1
- Initial packaging
