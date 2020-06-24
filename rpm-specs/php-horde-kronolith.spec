# remirepo/fedora spec file for php-horde-kronolith
#
# Copyright (c) 2012-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name    kronolith
%global pear_channel pear.horde.org

Name:           php-horde-kronolith
Version:        4.2.27
Release:        5%{?dist}
Summary:        A web based calendar

License:        GPLv2
URL:            http://www.horde.org/apps/kronolith
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  php(language) >= 5.3.0
BuildRequires:  php-pear(PEAR) >= 1.7.0
BuildRequires:  php-channel(%{pear_channel})
BuildRequires:  php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-pear(%{pear_channel}/Horde_Test) >= 2.1.0 with php-pear(%{pear_channel}/Horde_Test) < 3)
BuildRequires: (php-pear(%{pear_channel}/Horde_Core) >= 2.5.0 with php-pear(%{pear_channel}/Horde_Core) < 3)
BuildRequires: (php-pear(%{pear_channel}/content)    >= 2.0.5 with php-pear(%{pear_channel}/content)    < 3)
%else
BuildRequires:  php-pear(%{pear_channel}/Horde_Test) >= 2.1.0
BuildRequires:  php-pear(%{pear_channel}/Horde_Core) >= 2.5.0
BuildRequires:  php-pear(%{pear_channel}/content) >= 2.0.5
%endif

Requires(post): %{__pear}
Requires(postun): %{__pear}

# Web stuff
Requires:       php(httpd)
Requires:       httpd
# From package.xml required
Requires:       php(language) >= 5.3.0
Requires:       php-gettext
Requires:       php-json
Requires:       php-simplexml
Requires:       php-pear(PEAR) >= 1.7.0
Requires:       php-pear(Date)
Requires:       php-pear(Date_Holidays) >= 0.21.0
Requires:       php-channel(%{pear_channel})
Requires:       php-pear(%{pear_channel}/Horde_Role) >= 1.0.0
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-pear(%{pear_channel}/content)            >= 2.0.5  with php-pear(%{pear_channel}/content)            < 3)
Requires:      (php-pear(%{pear_channel}/horde)              >= 5.0.0  with php-pear(%{pear_channel}/horde)              < 6)
Requires:      (php-pear(%{pear_channel}/Horde_Auth)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Auth)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Autoloader)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_Autoloader)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Core)         >= 2.21.0 with php-pear(%{pear_channel}/Horde_Core)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Data)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Data)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Date)         >= 2.0.8  with php-pear(%{pear_channel}/Horde_Date)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Dav)          >= 1.0.0  with php-pear(%{pear_channel}/Horde_Dav)          < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Date_Parser)  >= 2.0.0  with php-pear(%{pear_channel}/Horde_Date_Parser)  < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Exception)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Exception)    < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Form)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Form)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Group)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Group)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Http)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Http)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_History)      >= 2.1.0  with php-pear(%{pear_channel}/Horde_History)      < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Icalendar)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Icalendar)    < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Image)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Image)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Lock)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Lock)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_LoginTasks)   >= 2.0.0  with php-pear(%{pear_channel}/Horde_LoginTasks)   < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mail)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Mail)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Mime)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Mime)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Nls)          >= 2.0.0  with php-pear(%{pear_channel}/Horde_Nls)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Notification) >= 2.0.0  with php-pear(%{pear_channel}/Horde_Notification) < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Perms)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Perms)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Serialize)    >= 2.0.0  with php-pear(%{pear_channel}/Horde_Serialize)    < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Share)        >= 2.0.0  with php-pear(%{pear_channel}/Horde_Share)        < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Support)      >= 2.0.0  with php-pear(%{pear_channel}/Horde_Support)      < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Text_Filter)  >= 2.0.0  with php-pear(%{pear_channel}/Horde_Text_Filter)  < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Timezone)     >= 1.0.0  with php-pear(%{pear_channel}/Horde_Timezone)     < 2)
Requires:      (php-pear(%{pear_channel}/Horde_Url)          >= 2.0.0  with php-pear(%{pear_channel}/Horde_Url)          < 3)
Requires:      (php-pear(%{pear_channel}/Horde_Util)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_Util)         < 3)
Requires:      (php-pear(%{pear_channel}/Horde_View)         >= 2.0.0  with php-pear(%{pear_channel}/Horde_View)         < 3)
# From package.xml, optional
Recommends:    (php-pear(%{pear_channel}/nag) >= 4.2.0  with php-pear(%{pear_channel}/nag) < 5)
%else
Requires:       php-pear(%{pear_channel}/content) >= 2.0.5
Requires:       php-pear(%{pear_channel}/content) <  3.0.0
Requires:       php-pear(%{pear_channel}/horde) >= 5.0.0
Requires:       php-pear(%{pear_channel}/horde) <  6.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Auth) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Autoloader) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Autoloader) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Core) >= 2.21.0
Requires:       php-pear(%{pear_channel}/Horde_Core) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Data) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Date) >= 2.0.8
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
Requires:       php-pear(%{pear_channel}/Horde_Http) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Http) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_History) >= 2.1.0
Requires:       php-pear(%{pear_channel}/Horde_History) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Icalendar) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Image) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Image) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Lock) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Lock) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_LoginTasks) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_LoginTasks) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mail) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Mime) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Nls) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Nls) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Notification) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Notification) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Perms) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Serialize) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Share) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Support) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Text_Filter) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Text_Filter) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Timezone) >= 1.0.0
Requires:       php-pear(%{pear_channel}/Horde_Timezone) <  2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Url) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_Util) <  3.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) >= 2.0.0
Requires:       php-pear(%{pear_channel}/Horde_View) <  3.0.0
# From package.xml, optional
Requires:       php-pear(%{pear_channel}/nag) >= 4.2.0
Requires:       php-pear(%{pear_channel}/nag) <  5
%endif
# Optional and implicitly required: Horde_Db
# Optional and skiped as non-free: Horde_ActiveSync
# TODO pear.horde.org/timeobjects >= 2.0.0
# From phpcompatinfo report for version 4.1.5
Requires:       php-date
Requires:       php-intl
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-session
Requires:       php-spl
Requires:       php-xmlwriter

Provides:       php-pear(%{pear_channel}/kronolith) = %{version}
Provides:       php-composer(horde/kronolith) = %{version}
Obsoletes:      kronolith < 4
Provides:       kronolith  = %{version}


%description
Kronolith is the Horde calendar application. It provides web-based
calendars backed by a SQL database or a Kolab server. Supported features
include Ajax and mobile interfaces, shared calendars, remote calendars,
invitation management (iCalendar/iTip), free/busy management, resource
management, alarms, recurring events, and a sophisticated day/week view
which handles arbitrary numbers of overlapping events.


%prep
%setup -q -c

cat <<EOF | tee httpd.conf
<DirectoryMatch %{pear_hordedir}/%{pear_name}/(config|lib|locale|templates)>
     Deny from all
</DirectoryMatch>

<Directory %{pear_hordedir}/%{pear_name}/feed/>
  <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond   %%{REQUEST_FILENAME}  !-d
    RewriteCond   %%{REQUEST_FILENAME}  !-f
    RewriteRule   ^(.*)\$ index.php?c=\$1 [QSA,L]
  </IfModule>
</Directory>
EOF

cd %{pear_name}-%{version}

# Don't install .po and .pot files
# Remove checksum for .mo, as we regenerate them
sed -e '/%{pear_name}.po/d' \
    -e '/htaccess/d' \
    -e '/Event.php/s/md5sum=.*name=/name=/' \
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
cd %{pear_name}-%{version}/test/Kronolith

ret=0
for cmd in php php70 php71 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap bootstrap.php \
      --filter '^((?!(testBasicVersion1)).)*$' \
      --verbose . || ret=1
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
%doc %{pear_testdir}/kronolith
%{_bindir}/kronolith-agenda
%{_bindir}/kronolith-convert-datatree-shares-to-sql
%{_bindir}/kronolith-convert-sql-shares-to-sqlng
%{_bindir}/kronolith-convert-to-utc
%{_bindir}/kronolith-import-icals
%{_bindir}/kronolith-import-openxchange
%{_bindir}/kronolith-import-squirrelmail-calendar
%dir %{pear_hordedir}/%{pear_name}
%dir %{pear_hordedir}/%{pear_name}/locale
%{pear_hordedir}/%{pear_name}/*.php
%{pear_hordedir}/%{pear_name}/calendars
%{pear_hordedir}/%{pear_name}/config
%{pear_hordedir}/%{pear_name}/feed
%{pear_hordedir}/%{pear_name}/js
%{pear_hordedir}/%{pear_name}/lib
%{pear_hordedir}/%{pear_name}/migration
%{pear_hordedir}/%{pear_name}/resources
%{pear_hordedir}/%{pear_name}/templates
%{pear_hordedir}/%{pear_name}/themes


%changelog
* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 4.2.27-5
- requires php(httpd)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  8 2019 Remi Collet <remi@remirepo.net> - 4.2.27-1
- update to 4.2.27 (no change)

* Mon Jan  7 2019 Remi Collet <remi@remirepo.net> - 4.2.26-1
- update to 4.2.26
- use range dependencies

* Thu Sep 27 2018 Remi Collet <remi@remirepo.net> - 4.2.25-1
- update to 4.2.25

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Remi Collet <remi@remirepo.net> - 4.2.24-1
- update to 4.2.24

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Remi Collet <remi@remirepo.net> - 4.2.23-2
- add temporary patch for PHP 7.2, FTBFS from Koschei

* Tue Sep 19 2017 Remi Collet <remi@remirepo.net> - 4.2.23-1
- Update to 4.2.23

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 4.2.22-1
- Update to 4.2.22

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May  3 2017 Remi Collet <remi@remirepo.net> - 4.2.21-1
- Update to 4.2.21

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 4.2.20-1
- Update to 4.2.20

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Remi Collet <remi@fedoraproject.org> - 4.2.19-2
- Update to 4.2.19
- use upstream locale files

* Wed Sep 07 2016 Remi Collet <remi@fedoraproject.org> - 4.2.18-1
- Update to 4.2.18

* Sat Jul 02 2016 Remi Collet <remi@fedoraproject.org> - 4.2.17-1
- Update to 4.2.17

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 4.2.16-1
- Update to 4.2.16

* Wed Feb 17 2016 Remi Collet <remi@fedoraproject.org> - 4.2.15-1
- Update to 4.2.15

* Thu Feb 11 2016 Remi Collet <remi@fedoraproject.org> - 4.2.14-1
- Update to 4.2.14

* Tue Feb  9 2016 Remi Collet <remi@fedoraproject.org> - 4.2.13-1
- Update to 4.2.13

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 4.2.11-1
- Update to 4.2.11

* Sat Aug 01 2015 Remi Collet <remi@fedoraproject.org> - 4.2.9-1
- Update to 4.2.9

* Fri Jun 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.8-1
- Update to 4.2.8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.7-1
- Update to 4.2.7

* Wed Apr 29 2015 Remi Collet <remi@fedoraproject.org> - 4.2.6-1
- Update to 4.2.6

* Tue Feb 10 2015 Remi Collet <remi@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5
- add provides php-composer(horde/kronolith)

* Wed Dec 03 2014 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- Update to 4.2.4

* Wed Oct 29 2014 Remi Collet <remi@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Sat Sep 06 2014 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Mon Aug 04 2014 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Wed Jul 23 2014 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0
- raise dep on nag, Horde_Date

* Mon Jul 07 2014 Remi Collet <remi@fedoraproject.org> - 4.1.6-1
- Update to 4.1.6
- raise dependency on Horde_Data >= 2.0.8
- run test suite during build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Remi Collet <remi@fedoraproject.org> - 4.1.5-2
- fix from review #1087772
- preserve timestamp of package.xml

* Mon Mar 10 2014 Remi Collet <remi@fedoraproject.org> - 4.1.5-1
- Update to 4.1.5

* Tue Oct 29 2013 Remi Collet <remi@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4

* Wed Aug 28 2013 Remi Collet <remi@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Wed Jul 17 2013 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Tue Jun 18 2013 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Wed Jun 05 2013 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0
- new dependency on Horde_Dav

* Fri May 31 2013 Remi Collet <remi@fedoraproject.org> - 4.0.5-1
- Update to 4.0.5
- switch from Conflicts to Requires

* Tue Feb 12 2013 Remi Collet <remi@fedoraproject.org> - 4.0.4-1
- Update to 4.0.4

* Sat Jan 12 2013 Remi Collet <remi@fedoraproject.org> - 4.0.3-2
- obsoletes/provides kronolith

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Tue Nov 27 2012 Remi Collet <remi@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Fri Nov 23 2012 Remi Collet <remi@fedoraproject.org> - 4.0.1-2
- fix httpd configuration

* Thu Nov 22 2012 Remi Collet <remi@fedoraproject.org> - 4.0.1-1
- Initial package