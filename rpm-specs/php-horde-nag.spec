# remirepo/fedora spec file for php-horde-nag
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    nag
%global pear_channel pear.horde.org

Name:           php-horde-nag
Version:        4.2.19
Release:        5%{?dist}
Summary:        A web based task list manager

License:        GPLv2
URL:            http://www.horde.org/apps/nag
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Core) >= 2.6.1

Requires(post): %{__pear}
Requires(postun): %{__pear}

# Web stuff
Requires:       php(httpd)
Requires:       httpd
# From package.xml required
Requires:       php(language) >= 5.3.0
Requires:       php-gettext
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
Requires:       php-pear(%{pear_channel}/content) >= 2.0.5
Requires:       php-pear(%{pear_channel}/content) <  3.0.0
Requires:       php-pear(%{pear_channel}/horde) >= 5.0.0
Requires:       php-pear(%{pear_channel}/horde) <  6.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Core) >= 2.6.1
Requires:       php-pear(%{pear_channel}/Horde_Core) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Dav) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date_Parser) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date_Parser) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Exception) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Form) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Form) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Group) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Group) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_History) >= 2.1.0
Requires:       php-pear(%{pear_channel}/Horde_History) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Prefs) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Prefs) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Routes) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Routes) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Text_Filter) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Text_Filter) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) <  3.0.0
# Optional and implicitly required: Horde_Db
# From pĥpcompatinfo report for version 4.1.4
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(horde/nag) = %{version}
Provides:       nag = %{version}


%description
Nag is a web-based application built upon the Horde Application Framework
which provides a simple, clean interface for managing online task lists
(i.e., todo lists). It also includes strong integration with the other
Horde applications and allows users to share task lists or enable
light-weight project management.


%prep
%setup -q -c

cat <<EOF >httpd.conf
<DirectoryMatch %{pear_hordedir}/%{pear_name}/(config|lib|locale|templates)>
     Deny from all
</DirectoryMatch>
EOF

cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/htaccess/d' \
    -e '/%{pear_name}.mo/s/md5sum=.*name=/name=/' \
    ../package.xml >%{name}.xml
touch -r ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}

# Regenerate the locales
for po in $(find locale -name \*.po)
do
   : msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


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

# Locales
for loc in locale/?? locale/??_??
do
    lang=$(basename $loc)
    echo "%%lang(${lang%_*}) %{pear_hordedir}/%{pear_name}/$loc"
done | tee ../%{pear_name}.lang


%check
cd %{pear_name}-%{version}/test/Nag

ret=0
for cmd in php php70 php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php --verbose . || ret=1
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


%files -f %{pear_name}.lang
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0770,apache,apache) %dir %{_sysconfdir}/horde/%{pear_name}
%attr(0640,apache,apache) %config %{_sysconfdir}/horde/%{pear_name}/*.dist
%attr(0660,apache,apache) %config(noreplace) %{_sysconfdir}/horde/%{pear_name}/*.php
%attr(0660,apache,apache) %config %{_sysconfdir}/horde/%{pear_name}/*.xml
%doc %{pear_testdir}/%{pear_name}
%{_bindir}/nag-convert-datatree-shares-to-sql
%{_bindir}/nag-convert-sql-shares-to-sqlng
%{_bindir}/nag-create-missing-add-histories-sql
%{_bindir}/nag-import-openxchange
%{_bindir}/nag-import-vtodos
%dir %{pear_hordedir}/%{pear_name}
%dir %{pear_hordedir}/%{pear_name}/locale
%{pear_hordedir}/%{pear_name}/*.php
%{pear_hordedir}/%{pear_name}/app
%{pear_hordedir}/%{pear_name}/config
%{pear_hordedir}/%{pear_name}/js
%{pear_hordedir}/%{pear_name}/lib
%{pear_hordedir}/%{pear_name}/migration
%{pear_hordedir}/%{pear_name}/tasklists
%{pear_hordedir}/%{pear_name}/task
%{pear_hordedir}/%{pear_name}/tasks
%{pear_hordedir}/%{pear_name}/templates
%{pear_hordedir}/%{pear_name}/themes


%changelog
* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 4.2.19-5
- requires php(httpd)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Remi Collet <remi@remirepo.net> - 4.2.19-1
- update to 4.2.19

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Remi Collet <remi@remirepo.net> - 4.2.18-1
- update to 4.2.18

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Remi Collet <remi@remirepo.net> - 4.2.17-1
- Update to 4.2.17

* Tue Aug 15 2017 Remi Collet <remi@remirepo.net> - 4.2.16-1
- Update to 4.2.16

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 4.2.15-1
- Update to 4.2.15

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 4.2.14-1
- Update to 4.2.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 4.2.13-2
- use upstream locale files

* Wed Nov 09 2016 Remi Collet <remi@fedoraproject.org> - 4.2.13-1
- Update to 4.2.13

* Wed Nov 09 2016 Remi Collet <remi@fedoraproject.org> - 4.2.12-1
- Update to 4.2.12

* Wed Sep 07 2016 Remi Collet <remi@fedoraproject.org> - 4.2.11-1
- Update to 4.2.11

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 4.2.10-1
- Update to 4.2.10

* Tue Apr 05 2016 Remi Collet <remi@fedoraproject.org> - 4.2.9-1
- Update to 4.2.9

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 4.2.8-1
- Update to 4.2.8

* Tue Feb  9 2016 Remi Collet <remi@fedoraproject.org> - 4.2.7-1
- Update to 4.2.7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Remi Collet <remi@fedoraproject.org> - 4.2.6-1
- Update to 4.2.6

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- Update to 4.2.4
- add provides php-composer(horde/nag)

* Fri Nov 21 2014 Remi Collet <remi@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Wed Oct 29 2014 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Mon Aug 04 2014 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Wed Jul 23 2014 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 4.1.5-1
- Update to 4.1.5
- run test suite during build (all ignored for now)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-3
- preserve package.xml timestamp

* Fri May 16 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-2
- cleanup from review #1087740
- license is GPLv2

* Mon Mar 10 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- add dependency on Horde_Dav

* Tue Oct 29 2013 Remi Collet <remi@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Tue Aug 27 2013 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Wed Jul 17 2013 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Wed Jun 05 2013 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3
- switch from Conflicts to Requires

* Thu Jan 10 2013 Remi Collet <RPMS@FamilleCollet.com> - 4.0.2-1
- Update to 4.0.2 for remi repo

* Tue Nov 27 2012 Remi Collet <RPMS@FamilleCollet.com> - 4.0.1-1
- Update to 4.0.1 for remi repo

* Mon Nov 19 2012 Remi Collet <RPMS@FamilleCollet.com> - 4.0.0-2
- requires Horde_Routes

* Sun Nov 18 2012 Remi Collet <RPMS@FamilleCollet.com> - 4.0.0-1
- Initial package
