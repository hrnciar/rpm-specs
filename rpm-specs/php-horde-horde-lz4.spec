# Fedora spec file for php-horde-horde-lz4
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global with_zts     0%{?__ztsphp:1}
%global pecl_name    horde_lz4
%global pecl_channel pear.horde.org
%global ini_name     40-%{pecl_name}.ini
%global with_tests   0%{!?_without_tests:1}

Summary:        Horde LZ4 Compression Extension
Name:           php-horde-horde-lz4
Version:        1.0.10
Release:        15%{?dist}
License:        MIT
URL:            http://www.horde.org
Source0:        http://%{pecl_channel}/get/%{pecl_name}-%{version}.tgz

BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-channel(%{pecl_channel})
BuildRequires:  lz4-devel
%if %{with_tests}
BuildRequires:  %{_bindir}/phpunit
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-channel(%{pecl_channel})

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_channel}/%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_channel}/%{pecl_name})%{?_isa} = %{version}


%description
PHP extension that implements the LZ4 compression algorithm,
an extremely fast lossless compression algorithm.


%prep
%setup -q -c

# Don't install/register tests
# Don't install bundled libz4
sed -e 's/role="test"/role="src"/' \
    -e '/name="lib/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

mv %{pecl_name}-%{version} NTS

cd NTS
# Use system library
rm -r lib

# Sanity check, really often broken
extver=$(sed -n '/#define HORDE_LZ4_EXT_VERSION/{s/.* "//;s/".*$//;p}' horde_lz4.h)
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
cat << 'EOF' | tee %{ini_name}
; Enable %{summary} module
extension=%{pecl_name}.so
EOF


%build
cd NTS
%{_bindir}/phpize
%configure \
    --with-liblz4 \
    --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure \
    --with-liblz4 \
    --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
make -C NTS install-modules INSTALL_ROOT=%{buildroot}

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

%if %{with_zts}
make -C ZTS install-modules INSTALL_ROOT=%{buildroot}

install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Documentation
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pear_docdir}/%{pecl_name}/$i
done


%check
cd NTS
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: Upstream test suite for NTS extension
%{__php} -d extension=modules/horde_lz4.so %{_bindir}/phpunit test
%endif

%if %{with_zts}
cd ../ZTS
: Minimal load test for ZTS extension
%{__ztsphp} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep %{pecl_name}

%if %{with_tests}
: Upstream test suite for ZTS extension
%{__ztsphp} -d extension=modules/horde_lz4.so %{_bindir}/phpunit test
%endif
%endif


%files
%license NTS/LICENSE
%doc %{pear_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.0.10-14
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.0.10-11
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.0.10-8
- undefine _strict_symbol_defs_build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.0.10-7
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0.10-3
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.0.10-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Wed Mar 09 2016 Remi Collet <remi@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10 (no change)
- drop scriptlets (replaced by file triggers in php-pear)

* Tue Feb 02 2016 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9 (no change)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Tue Sep 16 2014 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7
- https://github.com/horde/horde/pull/103 is merged

* Mon Sep 15 2014 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- initial package, version 1.0.6
