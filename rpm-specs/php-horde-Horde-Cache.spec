# remirepo/fedora spec file for php-horde-Horde-Cache
#
# Copyright (c) 2012-2019 Nick Bebout, Remi Collet
#
# License: MIT
# https://fedoraproject.org/wiki/Licensing:MIT#Modern_Style_with_sublicense
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Cache
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Cache
Version:        2.5.5
Release:        8%{?dist}
Summary:        Horde Caching API

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
#BuildRequires:  php-pecl(APC)

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-hash
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Compress_Fast) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Compress_Fast) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# From package.xml, optional
%if 0%{?fedora} > 21 || 0%{?rhel} >= 8
Recommends:     php-pear(%{pear_channel}/Horde_HashTable) >= 1.0.0
Recommends:     php-pear(%{pear_channel}/Horde_HashTable) <  2.0.0
Suggests:       php-pear(%{pear_channel}/Horde_Mongo) >= 1.0.0
Suggests:       php-pear(%{pear_channel}/Horde_Mongo) <  2.0.0
%else
Requires:       php-pear(%{pear_channel}/Horde_HashTable) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_HashTable) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mongo) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mongo) <  2.0.0
%endif
# From phpcompatinfo report for version 2.5.0
Requires:       php-date
Requires:       php-spl
# Optional and omitted to avoid circular dep : Horde_Db
# Optional and implicitly requires Horde_Memcache, Horde_Log

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
This package provides a simple, functional caching API, with the option to
store the cached data on the filesystem, in one of the PHP opcode cache
systems (APC, eAcclerator, XCache, or Zend Performance Suite's content
cache), memcached, or an SQL table.


%prep
%setup -q -c

cd %{pear_name}-%{version}
cp ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
cd %{pear_name}-%{version}/test/$(echo %{pear_name} | sed -e s:_:/:g)

ret=0
for cmd in php php56 php70 php71 php72 php73; do
  if which $cmd; then
    $cmd -d apc.enable_cli=1 %{_bindir}/phpunit . || ret=1
  fi
done
exit $ret


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Cache
%{pear_phpdir}/Horde/Cache.php
%{pear_datadir}/%{pear_name}
%doc %{pear_testdir}/%{pear_name}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@fedoraproject.org> - 2.5.5-5
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Remi Collet <remi@fedoraproject.org> - 2.5.5-1
- Update to 2.5.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Remi Collet <remi@fedoraproject.org> - 2.5.4-1
- Update to 2.5.4 (no change)

* Tue Jun 28 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-2
- Horde_Mongo is optional

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3
- PHP 7 compatible version

* Mon Feb  8 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2
- add and run upstream test suite

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Fri Apr 04 2014 Remi Collet <remi@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2
- drop optional dependency on Horde_Log (implicit)

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Sat Jan 25 2014 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0
- add (optional) requires for Horde_HashTable, Horde_Mongo

* Tue Oct 08 2013 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Wed Jun 19 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-2
- fix typo

* Wed Jun 19 2013 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- switch from Conflicts to Requires

* Sat May 04 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- drop optional dependency on Horde_Db (avoid circular)
- Update to 2.1.0

* Tue Apr 09 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- Requires Horde_Compress_Fast is now mandatory
- Requires Horde_Db and Horde_Memcache (optional)

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3
- requires Horde_Compress_Fast instead of LZF
- fix License

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Nick Bebout <nb@fedoraproject.org> - 2.0.1-2
- Fix packaging issues

* Wed Dec 12 2012 Nick Bebout <nb@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Jun 21 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.5-1
- Upgrade to 1.0.5

* Sat Jan 28 2012 Nick Bebout <nb@fedoraproject.org> - 1.0.4-1
- Initial package
