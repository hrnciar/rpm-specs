# OPTION: Fedora (1) or RHEL (0) Splash
%define fedora_splash 1

%define contentdir /var/www
%global snapshot 20190710

Summary: webmail client written in php
Name: squirrelmail
Version: 1.4.23
Release: 5%{?dist}.%{snapshot}
License: GPLv2+
URL: http://www.squirrelmail.org/
#Source0: http://downloads.sourceforge.net/%{name}/%{name}-webmail-%{version}.tar.bz2
Source0: http://snapshots.squirrelmail.org/squirrelmail-%{snapshot}_0200-SVN.stable.tar.bz2
Source1: squirrelmail.conf
Source2: squirrelmail-splash-fedora.png
Source3: squirrelmail-splash-rhel.png
Source4: http://prdownloads.sourceforge.net/squirrelmail/all_locales-1.4.18-20090526.tar.bz2
Source5: config_local.php

#undelete feature requested in #795333
Source6: http://www.squirrelmail.org/plugins/undelete-2.0-1.4.0.tar.gz

# bug #196017
Patch1: squirrelmail-1.4.6-zenkaku-subject-convert.patch

# bug #195452
Patch2: squirrelmail-1.4.6-japanese-multibyte-view-text.patch

# bug #194457
Patch3: squirrelmail-1.4.6-japanese-multibyte-view-body.patch

# bug #450780 - sent upstream, available here:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1855717&group_id=311&atid=100311
Patch4: squirrelmail-1.4.17-biguid.patch

# bug #508631 - use hunspell instead of aspell
Patch5: squirrelmail-1.4.19-hunspell.patch

# fix issues found post release
Patch6: squirrelmail-1.4.22-prfix.patch
Patch7: squirrelmail-1.4.22-php54strict.patch

#from upstream, for sm <= 1.4.22
Patch8: squirrelmail-1.4.22-php54hex2bin.patch
Patch9: squirrelmail-1.4.22-php54fixes.patch
Patch10: squirrelmail-1.4.22-pregfix.patch

# from upstream, for sm <= 1.4.22, CVE-2017-7692
Patch11: squirrelmail-1.4.22-escaping.patch
Patch12: squirrelmail-fix-xss-sf-bug-2831.diff

BuildArch: noarch
BuildRequires: gettext
BuildRequires: perl-generators
Requires: httpd, php(httpd), php-mbstring, perl-interpreter, tmpwatch, hunspell, hunspell-en
Requires: /usr/sbin/sendmail
Requires: crontabs

%description
SquirrelMail is a basic webmail package written in PHP4. It
includes built-in pure PHP support for the IMAP and SMTP protocols, and
all pages render in pure HTML 4.0 (with no JavaScript) for maximum
compatibility across browsers.  It has very few requirements and is very
easy to configure and install.

%prep
#setup -q -n %{name}-webmail-%{version}
%setup -q -n %{name}.stable
cd squirrelmail
mv * ..
cd ..
rmdir squirrelmail
pushd plugins
tar xvzf %{SOURCE6}
popd
%patch1 -p1 -b .patchbackup1
%patch2 -p1 -b .patchbackup2
%patch3 -p1 -b .patchbackup3
%patch4 -p1 -b .patchbackup4
%patch5 -p1 -b .patchbackup5
%patch7 -p1 -b .patchbackup6
%patch12 -p1 -b .patchbackup7

find . -name '*.patchbackup*' -delete

mkdir locale_tempdir
pushd locale_tempdir
tar xfj %SOURCE4
popd

#use utf-8 by default
sed -i 's/^ *\($default_charset *=\).*$/'"\1 'utf-8';/" config/config_default.php


%build
rm -f plugins/make_archive.pl

# Rearrange the documentation
mv README doc/
mv themes/README.themes doc/
mkdir -p doc/plugins
mv plugins/demo doc/plugins
for f in `find plugins -name "README*" -or -name INSTALL \
                   -or -name CHANGES -or -name HISTORY`; do
    mkdir -p doc/`dirname $f`
    mv $f $_
done
mv doc/plugins/squirrelspell/doc/README doc/plugins/squirrelspell
rmdir doc/plugins/squirrelspell/doc
mv plugins/squirrelspell/doc/* doc/plugins/squirrelspell
rm -f doc/plugins/squirrelspell/index.php
rmdir plugins/squirrelspell/doc
perl -pi -e "s{\.\./}{}g" doc/index.html

# Fixup various files
echo "left_refresh=300" >> data/default_pref
for f in contrib/RPM/squirrelmail.cron contrib/RPM/config.php.redhat; do
    perl -pi -e "s|__ATTDIR__|%{_localstatedir}/spool/squirrelmail/attach/|g;"\
         -e "s|__PREFSDIR__|%{_localstatedir}/lib/squirrelmail/prefs/|g;" $f
done

# Fix the version
%{__perl} -pi -e "s|^(\s*\\\$version\s*=\s*'[^']+)'|\1-%{release}'|g"\
    functions/strings.php

# replace splash screen
%if %{fedora_splash} == 1
cp %{SOURCE2} images/sm_logo.png
%else
cp %{SOURCE3} images/sm_logo.png
%endif

# Convert all locales to utf-8. Not only is this probably the right thing
# to do anyway, but SquirrelMail will corrupt charsets unless the charset
# of the user's locale is a superset of the charset of any mail they reply to
# https://sf.net/tracker/?func=detail&atid=423691&aid=1235345&group_id=311
sed -i functions/i18n.php \
    -e "s/^\(\$languages\['\([^']*\)'\]\['CHARSET'].*= '\)\([^']*\)';/\1utf-8';/" \
    -e "s/^\(\$languages\['\([^']*\)'\]\['LOCALE'].*=\).*/\1 '\2.UTF-8';/" 

# Hard-code Japanese to send iso-2022-jp, UTF-8 is unrealistic
# Without this, 1.4.6 sends eucjp which is clearly wrong
sed -i s/"$languages\['ja_JP'\]\['CHARSET'\] = 'utf-8';"/"$languages\['ja_JP'\]\['CHARSET'\] = 'iso-2022-jp';"/ functions/i18n.php
# Hard-code Korean to euc-KR, UTF-8 is unrealistic
# and not properly handled by squirrelmail
sed -i s/"$languages\['ko_KR'\]\['CHARSET'\] = 'utf-8';"/"$languages\['ko_KR'\]\['CHARSET'\] = 'euc-KR';"/ functions/i18n.php

# Hard-code Simplified Chinese charset, UTF-8 is unrealistic
sed -i s/"$languages\['zh_CN'\]\['CHARSET'\] = 'utf-8';"/"$languages\['zh_CN'\]\['CHARSET'\] = 'gb2312';"/ functions/i18n.php
sed -i s/"$languages\['zh_CN'\]\['LOCALE'\] = 'zh_CN.UTF-8';"/"$languages\['zh_CN'\]\['LOCALE'\] = 'zh_CN.GB2312';"/ functions/i18n.php
# Hard-code Traditional Chinese charset, UTF-8 is unrealistic
sed -i s/"$languages\['zh_TW'\]\['CHARSET'\] = 'utf-8';"/"$languages\['zh_TW'\]\['CHARSET'\] = 'big5';"/ functions/i18n.php
sed -i s/"$languages\['zh_TW'\]\['LOCALE'\] = 'zh_TW.UTF-8';"/"$languages\['zh_TW'\]\['LOCALE'\] = 'zh_TW.BIG5';"/ functions/i18n.php

cd locale_tempdir
for LOCALE in `ls locale/` ; do
    SKIPINVALID=
    case $LOCALE in
        ja_JP)
            # ja_JP uses iso2022-jp for email but euc-jp in its interface.
            # But why!?!?
            CHARSET=euc-jp
            ;;
        ko_KR)
            # ko_KR has broken help files in indeterminate charset. 
            # Assume it's _mostly_ EUC-KR as it's supposed to be, and let
            # iconv drop invalid characters from the input.
            SKIPINVALID=-c
            CHARSET=`grep CHARSET locale/$LOCALE/setup.php | cut -f6 -d\'`
            ;;
        *)
            CHARSET=`grep CHARSET locale/$LOCALE/setup.php | cut -f6 -d\'`
            ;;
    esac

    # Check for locales where CHARSET isn't in LOCALE.
    grep LOCALE locale/$LOCALE/setup.php | grep -vi $CHARSET  || :

    if [ "$CHARSET" != "utf-8" -a "$CHARSET" != "UTF-8" ]; then
        for a in `ls help/$LOCALE/ 2>/dev/null` ; do
            if [ "$LOCALE" == "ja_JP" ]; then continue; fi
            iconv $SKIPINVALID -f $CHARSET -t utf-8 help/$LOCALE/$a > $a.new && mv $a.new help/$LOCALE/$a
        done
        sed -e "s/CHARSET..[ ]*= [^;]*;/CHARSET'] = 'utf-8';/" \
            -e "s/LOCALE..[ ]*= [^;]*;/LOCALE'] = '$LOCALE.UTF-8';/" \
            locale/$LOCALE/setup.php  > setup.php.new ; mv setup.php.new locale/$LOCALE/setup.php
    fi
done

# do the pofiles separately since they each specify their own charset 
for POFILE in `find locale -name \*.po` ; do 
    CHARSET=`grep charset= $POFILE | cut -f2 -d= | cut -f1 -d\\\\`
    if [ "$CHARSET" != "utf-8" -a "$CHARSET" != "UTF-8" ]; then
        sed s/charset=$CHARSET/charset=utf-8/ $POFILE | iconv -f $CHARSET -t utf-8 > $POFILE.new && mv $POFILE.new $POFILE
    fi
done
for POFILE in `find . -name \*.po` ; do
    msgfmt $POFILE -c -o `echo $POFILE | sed s/\.po\$/.mo/`
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT%{_localstatedir}/lib/squirrelmail/prefs
mkdir -p -m0755 $RPM_BUILD_ROOT%{_localstatedir}/spool/squirrelmail/attach
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT%{contentdir}/html
mkdir -p -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily

# install default_pref
install -m 0644 data/default_pref \
    $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/
ln -s ../../../..%{_sysconfdir}/squirrelmail/default_pref \
    $RPM_BUILD_ROOT%{_localstatedir}/lib/squirrelmail/prefs/default_pref

# install the config files
mkdir -p -m0755 $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config
install -m 0644 config/*.php $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/
rm -f $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/config_local.php
install -m 0644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/config_local.php
ln -s ../../../..%{_sysconfdir}/squirrelmail/config_local.php \
    $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/config_local.php
install -m 0644 contrib/RPM/config.php.redhat \
    $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/config.php
ln -s ../../../..%{_sysconfdir}/squirrelmail/config.php \
    $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/config.php
install -m 0755 config/*.pl $RPM_BUILD_ROOT%{_datadir}/squirrelmail/config/

# install index.php
install -m 0644 index.php $RPM_BUILD_ROOT%{_datadir}/squirrelmail/

# copy over the rest
for d in class functions help images include locale plugins src themes; do
    cp -rp $d $RPM_BUILD_ROOT%{_datadir}/squirrelmail/
done

# install the cron script
install -m 0755 contrib/RPM/squirrelmail.cron \
    $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/

# install the config file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/

# move sqspell plugin config to /etc
rm -f $RPM_BUILD_ROOT%{_datadir}/squirrelmail/plugins/squirrelspell/sqspell_config.php
install -m 0644 plugins/squirrelspell/sqspell_config.php \
    $RPM_BUILD_ROOT%{_sysconfdir}/squirrelmail/sqspell_config.php
ln -s ../../../../..%{_sysconfdir}/squirrelmail/sqspell_config.php \
    $RPM_BUILD_ROOT%{_datadir}/squirrelmail/plugins/squirrelspell/sqspell_config.php

cd locale_tempdir
cp -r locale/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/locale/
cp -r images/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/images/
cp -r help/* $RPM_BUILD_ROOT%{_datadir}/squirrelmail/help/
cd ..
rm $RPM_BUILD_ROOT%{_datadir}/squirrelmail/locale/README.locales

#remove '\r' where needed
sed -i 's/\r//' doc/release_notes_archive/1.4/Notes-1.4.12.txt
sed -i 's/\r//' doc/release_notes_archive/1.4/Notes-1.4.13.txt

#remove unwanted files
rm $RPM_BUILD_ROOT%{_datadir}/squirrelmail/plugins/filters/bulkquery/bulkquery.c
rm $RPM_BUILD_ROOT%{_datadir}/squirrelmail/plugins/squirrelspell/modules/.htaccess

%files
%config %dir %{_sysconfdir}/squirrelmail
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/squirrelmail/*.php
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/squirrelmail/default_pref
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%doc doc/*
%dir %{_datadir}/squirrelmail
%dir %{_localstatedir}/lib/squirrelmail
%dir %{_localstatedir}/spool/squirrelmail
%{_datadir}/squirrelmail/class
%{_datadir}/squirrelmail/config
%{_datadir}/squirrelmail/functions
%{_datadir}/squirrelmail/help
%{_datadir}/squirrelmail/images
%{_datadir}/squirrelmail/include
%{_datadir}/squirrelmail/locale
%{_datadir}/squirrelmail/plugins
%{_datadir}/squirrelmail/src
%{_datadir}/squirrelmail/themes
%{_datadir}/squirrelmail/index.php
%attr(0700, apache, apache) %dir %{_localstatedir}/lib/squirrelmail/prefs
%attr(0700, apache, apache) %dir %{_localstatedir}/spool/squirrelmail/attach
%{_localstatedir}/lib/squirrelmail/prefs/default_pref
%{_sysconfdir}/cron.daily/squirrelmail.cron

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-5.20190710
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Remi Collet <remi@fedoraproject.org> - 1.4.23-4.20190710
- requires php(httpd) instead of deprecated mod_php

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-3.20190710
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-2.20190710
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Michal Hlavinka <mhlavink@redhat.com> - 1.4.23-1.20190710
- squirrelmail updated to newer snapshot

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.23-1.20180816
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Michal Hlavinka <mhlavink@redhat.com> - 1.4.23-0.20180816
- update squirrelmail to a svn snapshot, as latest stable release is over 8 years old
- fixes CVE-2018-14950, CVE-2018-14951, CVE-2018-14952, CVE-2018-14953, CVE-2018-14954,
  CVE-2018-14955

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.4.22-20
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Apr 26 2017 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-19
- fix insufficient escaping of user-supplied data (CVE-2017-7692)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-14
- fix deprecated log messages generated by preg_replace (#1047987)

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.4.22-13
- Perl 5.18 rebuild

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 1.4.22-12
- Add a missing requirement on crontabs to spec file (#989121)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.22-11
- Perl 5.18 rebuild

* Thu Jan 31 2013 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-10
- make configuration work with Apache 2.4 (#905690)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-8
- add undelete plugin

* Fri Feb 24 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-7
- php54 could cause missing subjects in some cases (#784015)

* Thu Feb 23 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-6
- prevent conflict of hex2bin() with php 5.4 native function

* Thu Feb 23 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-5
- suppress strict php 5.4 warnings (#789575)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-3
- use utf-8 encoding by default (#745382)

* Wed Jul 13 2011 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-2
- fix possible php warning

* Wed Jul 13 2011 Michal Hlavinka <mhlavink@redhat.com> - 1.4.22-1
- squirrelmail updated to 1.4.22
- fixes CVE-2010-4554, CVE-2010-4555, CVE-2011-2023

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Michal Hlavinka <mhlavink@redhat.com> - 1.4.21-1
- updated to 1.4.21
- fixes literal processing of 8-bit usernames/passwords during 
  login (CVE-2010-2813)

* Tue Jun 22 2010 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20-3
- fix CVE-2010-1637 : mail fetch plugin's port-scans via non-standard 
  POP3 server ports

* Mon Jun 07 2010 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20-2
- add note to config file that https connections are forced by default

* Mon Mar 08 2010 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20-1
- updated to 1.4.20
- translations updated

* Thu Sep 17 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20-0.rc2.20100104
- updated to 1.4.20RC2 20100104 snapshot
- fix multi-word searching (#551626)

* Thu Sep 17 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20-0.rc2.20090917
- updated to 1.4.20RC2 20090917 snapshot
- fix searching in emails (#523016)

* Wed Aug 19 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20RC2-1
- updated to 1.4.20RC2

* Thu Aug 13 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.20RC1-1
- updated to 1.4.20RC1
- fixes #517312 - CSRF issues in all forms (SA34627)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.19-3
- change default configuration to use only ssl connections

* Tue Jun 30 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.19-2
- use hunspell instead of ispell in squirrelspell plugin (#508631)

* Fri May 22 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.19-1
- updated to 1.4.19
- fixes CVE-2009-1381

* Tue May 19 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.18-2
- fix undefined variable aSpamIds (#501260)

* Tue May 12 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.18-1
- updated to 1.4.18

* Wed Mar 18 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-7
- fix: patch was not applyed

* Wed Mar 18 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-6
- don't use white text (invisible on white paper) for highlighting
  in conf.pl (#427217)

* Tue Mar 17 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-5
- don't use colored conf.pl by default (#427217)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 25 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-3
- drop versioned dependencies

* Mon Feb 23 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-2
- fix: sm. can't handle big UIDs sent from dovecot on 32bit machines
- move plugins/demo to doc directory

* Thu Dec 04 2008 Michal Hlavinka <mhlavink@redhat.com> - 1.4.17-1
- update to 1.4.17 (fixes CVE-2008-2379)

* Mon Sep 29 2008 Michal Hlavinka <mhlavink@redhat.com> - 1.4.16-1
- updates to 1.4.16 (fixes CVE-2008-3663)

* Fri Sep  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.15-1
- fix license tag
- update to 1.4.15

* Fri Dec 14 2007 Kevin Fenzi <kevin@tummy.com> - 1.4.13-1
- upgrade to new upstream 1.4.13
- note that this package was never vulnerable to CVE-2007-6348

* Wed Oct 10 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.4.11-1
- upgrade to new upstream 1.4.11

* Fri May 11 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.4.10a-1
- upgrade to new upstream 1.4.10a
- resolves: #239704: CVE-2007-1262 squirrelmail cross-site scripting flaw
- resolves: #218297: CVE-2006-6142 Three XSS issues in SquirrelMail

* Mon Apr 23 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.4.9a-2
- resolves: #237136:PHP Fatal error: Call to a member 
  function getParameter() on a non-object in 
  /usr/share/squirrelmail/functions/mime.php on line 317
- resolves: #229454: Errors in /var/log/httpd/error_log
- resolves: #222879: squirrelmail ja_JP patches break build

* Tue Apr 17 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.4.9a-1
- upgarde to new upstream 1.4.9a
- resolves: #235560 Many SM errors in apache logs

* Mon Jan 22 2007 Warren Togami <wtogami@redhat.com> 1.4.8-4
- Clean up .orig files (#223648)

* Mon Jan 15 2007 Warren Togami <wtogami@redhat.com> 1.4.8-3
- CVE-2006-6142

* Tue Aug 15 2006 Warren Togami <wtogami@redhat.com> 1.4.8-2
- more Japanese filename fixes (#195639)

* Fri Aug 11 2006 Warren Togami <wtogami@redhat.com> 1.4.8-1
- 1.4.8 release with CVE-2006-4019 and upstream bug fixes

* Tue Jul 18 2006 Warren Togami <wtogami@redhat.com> 1.4.7-5
- More JP translation updates (#194598)

* Mon Jul 10 2006 Warren Togami <wtogami@redhat.com> 1.4.7-4
- Fix fatal typo in config_local.php (#198306)

* Sun Jul 09 2006 Warren Togami <wtogami@redhat.com> 1.4.7-2
- Move sqspell_config.php to /etc and mark it %%config(noreplace) (#192236)

* Fri Jul 07 2006 Warren Togami <wtogami@redhat.com> 1.4.7-1
- 1.4.7 with CVE-2006-3174
- Reduce patch for body text (#194457)
- Better JP translation for "Check mail" (#196117)

* Fri Jun 23 2006 Warren Togami <wtogami@redhat.com> 1.4.6-8
- Japanese zenkaku subject conversion      (#196017)
- Japanese MSIE garbled download ugly hack (#195639)
- Japanese multibyte attachment view text  (#195452)
- Japanese multibyte attachment body text  (#194457)
- Do not convert Japanese Help to UTF-8    (#194599)

* Wed Jun 07 2006 Warren Togami <wtogami@redhat.com> 1.4.6-7
- CVE-2006-2842 File Inclusion Vulnerability

* Mon Jun 05 2006 Warren Togami <wtogami@redhat.com> 1.4.6-6
- buildreq gettext (194169)

* Tue Apr 04 2006 Warren Togami <wtogami@redhat.com> 1.4.6-5
- Fix Chinese and Korean too

* Fri Mar 24 2006 Warren Togami <wtogami@redhat.com> 1.4.6-4
- Fix outgoing Japanese mail to iso-2022-jp for now (#185767)

* Fri Mar 3 2006 Warren Togami <wtogami@redhat.com> 1.4.6-3
- Fix regex in doc mangling (#183943 Michal Jaegermann)

* Fri Mar 3 2006 David Woodhouse <dwmw2@redhat.com> 1.4.6-2
- Add a %%build section, move the file mangling to it.
  (#162852 Nicolas Mailhot)

* Wed Mar 1 2006 David Woodhouse <dwmw2@redhat.com> 1.4.6-1
- Upgrade to 1.4.6 proper for CVE-2006-0377 CVE-2006-0195 CVE-2006-0188
- Script the charset changes instead of using a patch
- Convert the ko_KR files to UTF-8, dropping invalid characters from
  what's theoretically supposed to be EUC-KR in the original.

* Tue Jan 17 2006 Warren Togami <wtogami@redhat.com> 1.4.6-0.cvs20050812.3
- do not remove mo files
- require php-mbstring

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 12 2005 David Woodhouse <dwmw2@redhat.com> 1.4.6-0.cvs20050812.2
- Convert all locales to UTF-8 instead of legacy character sets to
  work around bug #162852. Except for ko_KR, because iconv doesn't
  believe its help files are actually in EUC-KR as claimed.

* Sun Aug 14 2005 Warren Togami <wtogami@redhat.com> 1.4.6-0.cvs20050812.1
- snapshot of 1.4.6 because 1.4.5 upstream was a bad release
  this hopefully will also work on PHP5 too...

* Mon Jun 20 2005 Warren Togami <wtogami@redhat.com> 1.4.5-0.rc1
- 1.4.5-0.rc1

* Thu Jan 27 2005 Warren Togami <wtogami@redhat.com> 1.4.4-2
- 1.4.4
- re-include translations and Provide squirrelmail-i18n
  better compatible with upstream, but we cannot split sub-package
  due to support of existing distributions
- remove unnecessary .po files

* Fri Nov 19 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-7
- CAN-2004-1036 Cross Site Scripting in encoded text
- #112769 updated splash screens

* Thu Oct 14 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-5
- default_folder_prefix dovecot compatible by default
  /etc/squirrelmail/config_local.php if you must change it

* Wed Oct 13 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-4
- HIGASHIYAMA Masato's patch to improve Japanese support
  (coordinated by Scott A. Hughes).
- real 1.4.3a tarball

* Tue Sep 21 2004 Gary Benson <gbenson@redhat.com> 1.4.3-3
- rebuilt.

* Tue Aug 31 2004 Warren Togami <wtogami@redhat.com> 1.4.3-2
- #125638 config_local.php and default_pref in /etc/squirrelmail/
  to match upstream RPM.  This should allow smoother drop-in
  replacements and upgrades.
- other spec cleanup.

* Mon Jun  7 2004 Gary Benson <gbenson@redhat.com> 1.4.3-1
- upgrade to 1.4.3a.
- retain stuff after version when adding release to it.

* Wed Jun  2 2004 Gary Benson <gbenson@redhat.com>
- upgrade to 1.4.3.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt.

* Wed Jan 21 2004 Gary Benson <gbenson@redhat.com> 1.4.2-2
- fix calendar plugin breakage (#113902).

* Thu Jan  8 2004 Gary Benson <gbenson@redhat.com> 1.4.2-1
- upgrade to 1.4.2.
- tighten up permissions on /etc/squirrelmail/config.php (#112774).

* Mon May 12 2003 Gary Benson <gbenson@redhat.com> 1.4.0-1
- upgrade to 1.4.0.
- fix links in /usr/share/doc/squirrelmail-X.Y.Z/index.html (#90269).

* Mon Mar 24 2003 Gary Benson <gbenson@redhat.com> 1.2.11-1
- upgrade to 1.2.11 to fix CAN-2003-0160.

* Mon Feb 10 2003 Gary Benson <gbenson@redhat.com> 1.2.10-4
- fix syntax error in download.php (#82600).
- resized splash screen to be the same size as the one it replaces
  (#82790)
- remove piece of squirrelmail-1.2.10-xss.patch that changed the
  version from '1.2.10' to '1.2.11 [cvs]'

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.2.10-3
- rebuilt

* Wed Jan 15 2003 Tim Powers <timp@redhat.com> 1.2.10-2
- bump and rebuild

* Mon Dec  9 2002 Gary Benson <gbenson@redhat.com> 1.2.10-1
- patch to fix CAN-2002-1341 (#78982) and CAN-2002-1276 (#79147).

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 1.2.8-2
- fix prep macro in changelog

* Fri Sep 20 2002 Gary Benson <gbenson@redhat.com> 1.2.8-1
- upgrade to 1.2.8 to fix CAN-2002-1131 and CAN-2002-1132 (#74313)

* Tue Aug  6 2002 Preston Brown <pbrown@redhat.com> 1.2.7-4
- replacement splash screen.

* Mon Jul 22 2002 Gary Benson <gbenson@redhat.com> 1.2.7-3
- get rid of long lines in the specfile.
- remove symlink in docroot and use an alias in conf.d instead.
- work with register_globals off (#68669)

* Tue Jul 09 2002 Gary Benson <gbenson@redhat.com> 1.2.7-2
- hardwire the hostname (well, localhost) into the config file (#67635)

* Mon Jun 24 2002 Gary Benson <gbenson@redhat.com> 1.2.7-1
- hardwire the locations into the config file and cron file.
- install squirrelmail-cleanup.cron as squirrelmail.cron.
- make symlinks relative.
- upgrade to 1.2.7.
- more dependency fixes.

* Fri Jun 21 2002 Gary Benson <gbenson@redhat.com>
- summarize the summary, fix deps, and remove some redundant stuff.
- tidy up the prep section.
- replace directory definitions with standard RHL ones.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.2.6-3
- automated rebuild

* Wed Jun 19 2002 Preston Brown <pbrown@redhat.com> 1.2.6-2
- adopted Konstantin Riabitsev <icon@duke.edu>'s package for Red Hat
  Linux.  Nice job Konstantin!
