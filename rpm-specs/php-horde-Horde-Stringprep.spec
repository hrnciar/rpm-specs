# remirepo/fedora spec file for php-horde-Horde-Stringprep
#
# Copyright (c) 2014-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%{!?_pkgdocdir:   %global _pkgdocdir   %{_datadir}/doc/%{name}-%{version}}

%global pear_name    Horde_Stringprep
%global pear_channel pear.horde.org

Name:           php-horde-Horde-Stringprep
Version:        1.0.4
Release:        6%{?dist}
Summary:        Preparation of Internationalized Strings ("stringprep")

License:        LGPLv3
URL:            http://www.horde.org/
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

# use system library instead of bundled copy
Patch0:         %{pear_name}-syslib.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
# Unbundled library
Requires:       php-composer(znerol/php-stringprep)

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-stringprep) = %{version}


%description
Horde wrapper around the znerol/php-stringprep package.


%prep
%setup -q -c
cd %{pear_name}-%{version}

%patch0 -p1 -b .syslib

sed -e '/bundle\//d' \
    -e '/Stringprep.php/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


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

# Handle license file (keep upstream location, linked to fedora one)
%if 0%{?_licensedir:1}
DEST=$(echo %{_pkgdocdir} | sed -e 's:%_docdir:%_licensedir:')
ln -sf $DEST/COPYING %{buildroot}%{pear_docdir}/%{pear_name}/COPYING
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
%{?_licensedir:%license %{pear_name}-%{version}/doc/Horde/Stringprep/COPYING}
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/Horde
%{pear_phpdir}/Horde/Stringprep.php


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 1.0.4-1
- Update to 1.0.4 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 03 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (no change)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-2
- fix license handling per review #1222799

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2
- add provides php-composer(horde/horde-stringprep)

* Tue Nov 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sun Nov  9 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Initial package, version 1.0.0