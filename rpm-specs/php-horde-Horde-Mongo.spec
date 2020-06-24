# remirepo/fedora spec file for php-horde-Horde-Mongo
#
# Copyright (c) 2013-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Mongo
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Mongo
Version:        1.1.0
Release:        9%{?dist}
Summary:        Horde Mongo Configuration

License:        LGPLv2
URL:            http://%{pear_channel}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

# Fix autoloader path
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:       php-pecl(mongo) >= 1.3.0
Suggests:       php-composer(alcaeus/mongo-php-adapter)
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-mongo) = %{version}


%description
Provides an API to ensure that the PECL Mongo extension can be used
consistently across various Horde packages.

Tu use this module, you also need to install
  - php-pecl-mongo (PHP 5 only)
or
  - php-pecl-mongodb (PHP 5 or 7)
  - php-alcaeus-mongo-php-adapter


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml
%patch0 -p1 -b .rpm
sed -e '/Client.php/s/md5sum="[^"]*"//' \
    -e '/name="bundle/d' \
    -i %{name}.xml


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
%dir %{pear_phpdir}/Horde
%{pear_phpdir}/Horde/Mongo


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Remi Collet <remi@remirepo.net> - 1.0.8-8
- cleanup for EL-8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- php-pecl-mongo and alcaeus/mongo-php-adapter are optional
- add patch to use system alcaeus/mongo-php-adapter

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- add provides php-composer(horde/horde-mongo)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Jun 14 2013 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Wed Jun  5 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.RC1
- update to 1.0.0RC1

* Mon May  6 2013 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.beta1
- initial package
