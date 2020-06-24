# remirepo/fedora spec file for php-horde-Horde-Rpc
#
# Copyright (c) 2012-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    Horde_Rpc
%global pear_channel pear.horde.org

# Single test is not a unit test (requires a web server)
# so, don't run it during rpmbuild

Name:           php-horde-Horde-Rpc
Version:        2.1.9
Release:        2%{?dist}
Summary:        Horde RPC API

License:        LGPLv2
URL:            http://pear.horde.org
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.3.0
Requires:       php-ctype
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/Horde_Core)        >= 2.5.0 with php-pear(%{pear_channel}/Horde_Core)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Dav)         >= 1.0.0 with php-pear(%{pear_channel}/Horde_Dav)         < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Exception)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Exception)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Perms)       >= 2.0.0 with php-pear(%{pear_channel}/Horde_Perms)       < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Serialize)   >= 2.0.0 with php-pear(%{pear_channel}/Horde_Serialize)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Support)     >= 2.0.0 with php-pear(%{pear_channel}/Horde_Support)     < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0 with php-pear(%{pear_channel}/Horde_Translation) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)        >= 2.0.0 with php-pear(%{pear_channel}/Horde_Util)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Xml_Element) >= 2.0.0 with php-pear(%{pear_channel}/Horde_Xml_Element) < 3)
# Optional
Recommends:     php-soap
Recommends:     php-xmlrpc
Recommends:    (php-pear(%{pear_channel}/Horde_SyncMl) >= 2.0.0 with php-pear(%{pear_channel}/Horde_SyncMl) < 3)
%else
Requires:       php-pear(%{pear_channel}/Horde_Core) >= 2.5.0
Requires:       php-pear(%{pear_channel}/Horde_Core) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) >= 2.2.0
Requires:       php-pear(%{pear_channel}/Horde_Translation) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Xml_Element) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Xml_Element) <  3.0.0
# Optional
Requires:       php-soap
Requires:       php-xmlrpc
Requires:       php-pear(%{pear_channel}/Horde_SyncMl) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_SyncMl) <  3.0.0
%endif
# Optional and implicitly requires: Horde_Http, Horde_Lock

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/horde-rpc) = %{version}


%description
A common abstracted interface to various remote methods of accessing Horde
functionality.


%prep
%setup -q -c
cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}

# Regenerate the locales
for po in $(find locale -name \*.po)
do
   msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

# Locales
for loc in locale/{??,??_??}
do
    lang=$(basename $loc)
    test -d $loc && echo "%%lang(${lang%_*}) %{pear_datadir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Horde/Rpc
%{pear_phpdir}/Horde/Rpc.php
%doc %{pear_testdir}/%{pear_name}
# own locales (non standard) directories, .mo own by find_lang
%dir %{pear_datadir}/%{pear_name}
%dir %{pear_datadir}/%{pear_name}/locale


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Remi Collet <remi@remirepo.net> - 2.1.9-1
- update to 2.1.9
- use range dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct  9 2017 Remi Collet <remi@remirepo.net> - 2.1.8-1
- Update to 2.1.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.1.7-1
- Update to 2.1.7

* Tue Feb  9 2016 Remi Collet <remi@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6
- PHP 7 compatible version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4

* Wed Feb 11 2015 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Fri Jan 09 2015 Remi Collet <remi@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- add provides php-composer(horde/horde-rpc)
- raise dependency on Horde_Translation 2.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 15 2013 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Wed Jun 05 2013 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- switch from Conflicts to Requires

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5
- don't requires Horde_Dav until stable

* Tue May 07 2013 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Tue Jan 29 2013 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3 for remi repo

* Thu Dec 27 2012 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 for remi repo
- don't use find_lang

* Wed Nov  7 2012 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 for remi repo

* Sun Nov  4 2012 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- Initial package
