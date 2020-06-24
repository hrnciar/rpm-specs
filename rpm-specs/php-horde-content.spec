# remirepo/fedora spec file for php-horde-content
#
# Copyright (c) 2012-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    content
%global pear_channel pear.horde.org
%global with_tests   0%{!?_without_tests:1}

Name:           php-horde-content
Version:        2.0.6
Release:        6%{?dist}
Summary:        Tagging application

License:        BSD
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
%if %{with_tests}
# To run unit tests
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml, required
Requires:       php(language) >= 5.3.0
Requires:       php-gettext
Requires:       php-json
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Core) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Core) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Db) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Db) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Injector) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Injector) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Rdo) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Rdo) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
# From package.xml, pptional
Requires:       php-pear(%{pear_channel}/Horde_Argv) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Argv) <  3.0.0
# optional and implicitly required Horde_Controller, Horde_ElasticSearch
# From phpcompatinfo report for version 2.0.3
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/content) = %{version}


%description
This application provides tagging support for the other Horde applications.


%prep
%setup -q -c

cd %{pear_name}-%{version}
(
echo "<Directory %{pear_hordedir}/%{pear_name}>"
cat .htaccess
echo -e "</Directory>\n"
echo "<Directory %{pear_hordedir}/%{pear_name}/config>"
echo "    Deny from all"
echo -e "</Directory>\n"
echo "<Directory %{pear_hordedir}/%{pear_name}/lib>"
echo "    Deny from all"
echo "</Directory>"
) > ../httpd.conf
cat ../httpd.conf

# Remove htaccess as we provide httpd.conf
sed -e '/htaccess/d' \
    ../package.xml >%{name}.xml


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

# Install Apache configuration
install -Dpm 0644 ../httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Move configuration to /etc
mkdir -p %{buildroot}%{_sysconfdir}/horde
mv %{buildroot}%{pear_hordedir}/%{pear_name}/config \
   %{buildroot}%{_sysconfdir}/horde/%{pear_name}
ln -s %{_sysconfdir}/horde/%{pear_name} %{buildroot}%{pear_hordedir}/%{pear_name}/config


%check
%if %{with_tests}
cd %{pear_name}-%{version}/test/Content
phpunit \
    -d date.timezone=Europe/Paris \
    .
%else
: Test disabled
%endif


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
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0770,apache,apache) %dir %{_sysconfdir}/horde/%{pear_name}
%attr(0660,apache,apache) %config(noreplace) %{_sysconfdir}/horde/%{pear_name}/*.php
%doc %{pear_testdir}/%{pear_name}
%{_bindir}/content-object-add
%{_bindir}/content-object-delete
%{_bindir}/content-tag
%{_bindir}/content-tag-add
%{_bindir}/content-tag-delete
%{_bindir}/content-untag
%dir %{pear_hordedir}/%{pear_name}
%{pear_hordedir}/%{pear_name}/app
%{pear_hordedir}/%{pear_name}/config
%{pear_hordedir}/%{pear_name}/lib
%{pear_hordedir}/%{pear_name}/migration


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 2.0.6-1
- Update to 2.0.6 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- add provides php-composer(horde/content)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4
- run test suite during build

* Sun Apr 13 2014 Remi Collet <remi@fedoraproject.org> - 2.0.3-2
- cleanups

* Wed Jul 17 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Mar 13 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-2
- add dependency on Horde_ElasticSearch

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Sun Nov 18 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Initial package
