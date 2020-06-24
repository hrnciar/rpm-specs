%global		github_user	craig5n
%global		github_app	webcalendar
%global		basepath	%{_datadir}/%{name}
%global		manualVersion	0.9.43

#	The main tarball in this package is a downgraded version of the
#		upstream tarball, because of menu icon license issues.
#	To rebuild it from upstream tarball, submit the following commands:
#
# wget									\
#  "https://github.com/%{github_user}/%{github_app}/archive/v%{version}.tar.gz"
# tar xzf v%{version}.tar.gz 
# rm -rf webwalendar-%{version}/includes/menu/icons
# tar czf WebCalendar-%{version}-clean.tar.gz webcalendar-%{version}/
#
#	Upstream tarball MD5 sum:
#		9fcbf34ac58757b54a21616a7c1532b8  v1.2.9.tar.gz
#
#	Source tarball WebCalendar-1.2.0-newmenuicons.tar.gz is Fedora-
#		specific and thus, has no "upstream".

Name:		WebCalendar
Summary:	Single/multi-user web-based calendar application
Version:	1.2.9
Release:	6%{?dist}
License:	GPLv2
Source0:	WebCalendar-%{version}-clean.tar.gz
Source1:	WebCalendar-1.2.0-newmenuicons.tar.gz
Source2:	WebCalendar-http.conf
Source3:	WebCalendar-taglang.php
Patch1:		WebCalendar-1.2.9-newmenuicons.patch
Patch2:		WebCalendar-1.2.0-extmenu.patch
Patch3:		WebCalendar-1.2.0-extcaptcha.patch
Patch4:		WebCalendar-1.2.0-deftimezone.patch
Patch5:		WebCalendar-1.2.0-reset_reminder.patch
Patch6:		WebCalendar-1.2.0-offsetdays.patch
Patch7:		WebCalendar-1.2.0-approve.patch
Patch8:		WebCalendar-1.2.0-httpauthpub.patch
Patch9:		WebCalendar-1.2.0-eventstatus.patch
Patch10:	WebCalendar-1.2.9-php53.patch
Patch11:	WebCalendar-1.2.0-daylightbug.patch
Patch12:	WebCalendar-1.2.0-viewothers.patch
Patch13:	WebCalendar-1.2.3-nonuser.patch
Patch14:	WebCalendar-1.2.9-usercase.patch
Patch15:	WebCalendar-1.2.3-authsettings.patch
Patch16:	WebCalendar-1.2.3-etp.patch
Patch17:	WebCalendar-1.2.3-canadd.patch
Patch18:	WebCalendar-1.2.9-php7.patch
Patch19:	WebCalendar-1.2.7-groupsarrayinit.patch
URL:		http://www.k5n.us/webcalendar.php
Requires:	webserver
Requires:	php >= 5.3.0
Requires:	php-gd php_database
Requires:	php-hkit php-PHPMailer php-captchaphp
Requires:	JSCookMenu
Requires:	crontabs
BuildRequires:	perl-generators
BuildRequires:	php-cli
Buildarch:	noarch

%description
  WebCalendar is a PHP-based calendar application that can be configured as a
single-user calendar, a multi-user calendar for groups of users, or as an
event calendar viewable by visitors. MySQL, PostgreSQL, Oracle, DB2,
Interbase, MS SQL Server, or ODBC is required.
  WebCalendar can be setup in a variety of ways, such as...
	* A schedule management system for a single person
	* A schedule management system for a group of people, allowing one or
	  more assistants to manage the calendar of another user
	* An events schedule that anyone can view, allowing visitors to submit
	  new events
	* A calendar server that can be viewed with iCal-compliant calendar
	  applications like Mozilla Sunbird, Apple iCal or GNOME Evolution or
	  RSS-enabled applications like Firefox, Thunderbird, RSSOwl, or
	  FeedDemon, or BlogExpress.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -n webcalendar-%{version}

#	Install the new menu icons.  WARNING: do not dissociate "newmenuicons"
#		patch and tarball.

%setup -q -D -T -a 1 -n webcalendar-%{version}
%patch1 -p 1

#	Unbundle JSCookMenu.

%patch2 -p 1
rm -rf includes/menu/JSCookMenu.js

#	Unbundle Captcha PHP.

%patch3 -p 1
rm -rf includes/classes/captcha

#	Apply other fixes.

%patch4 -p 1
%patch5 -p 1
%patch6 -p 1
%patch7 -p 1
%patch8 -p 1
%patch9 -p 1
%patch10 -p 1
%patch11 -p 1
%patch12 -p 1
%patch13 -p 1
%patch14 -p 1
%patch15 -p 1
%patch16 -p 1
%patch17 -p 1
%patch18 -p 1
%patch19 -p 1


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	There are some scripts with shebang referencing /usr/local/bin.
#	In a normal installation, processors are in %{_bindir}.

set +e
find . -type f | while read file
do	line=`head -n 1 "${file}" | grep '^#![	 ]*/usr/local/bin/'`
	if [ "${line}" ]
	then sed -i -e "1s#/usr/local/bin#%{_bindir}#" "${file}"
	fi
done


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

rm -rf "${RPM_BUILD_ROOT}"

#	install directories.

install -d -m 755 "${RPM_BUILD_ROOT}/%{basepath}"

for DIR in docs icons images includes install themes tools translations
do	cp -a "${DIR}" "${RPM_BUILD_ROOT}/%{basepath}/${DIR}"
done

#	Install files.

install -p -m 644 *.php "${RPM_BUILD_ROOT}/%{basepath}/"
install -p -m 644 UPGRADING.html "${RPM_BUILD_ROOT}/%{basepath}/"
install -p -m 644 AUTHORS "${RPM_BUILD_ROOT}/%{basepath}/"

#	Replace bundled libraries by external ones.

(
	cd "${RPM_BUILD_ROOT}/%{basepath}/includes/classes/hKit"
	rm -rf hkit.class.php
	ln -s "%{_datadir}/php/hkit/hkit.class.php" .
)

(
	cd "${RPM_BUILD_ROOT}/%{basepath}/includes/classes/phpmailer"
	rm -rf class.phpmailer.php
	ln -s "%{_datadir}/php/PHPMailer/class.phpmailer.php" .
	rm -rf class.smtp.php
	ln -s "%{_datadir}/php/PHPMailer/class.smtp.php" .
)


#	Remove *.orig file created by patches.

find "${RPM_BUILD_ROOT}/%{basepath}" -name '*.orig' -print0 | xargs -0 -r rm -f

#	Remove unneeded doc files.

pushd "${RPM_BUILD_ROOT}%{basepath}/docs"
rm -rf README *.pl Makefile
popd

#	Fix permissions.

find "${RPM_BUILD_ROOT}%{basepath}" -type f -print0 | xargs -0 -r chmod ugo-x
find "${RPM_BUILD_ROOT}%{basepath}/tools" -type f -name '*.php' -print0	|
	xargs -0 -r chmod ugo+x
find "${RPM_BUILD_ROOT}%{basepath}/tools" -type f -name '*.pl' -print0	|
	xargs -0 -r chmod ugo+x

#	Java control panel is not (yet) operational.

rm -f "${RPM_BUILD_ROOT}%{basepath}/controlpanel.php"

#	Process the configuration files.

install -p -m 644 includes/settings.php.orig				\
	"${RPM_BUILD_ROOT}%{basepath}/includes/"
install -d -m 755 "${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}"
cp -a "${RPM_BUILD_ROOT}%{basepath}/includes/settings.php.orig"		\
	"${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/settings.php"
ln -s "%{_sysconfdir}/%{name}/settings.php"				\
	"${RPM_BUILD_ROOT}%{basepath}/includes/settings.php"
mv "${RPM_BUILD_ROOT}%{basepath}/includes/site_extras.php"		\
	"${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/"
ln -s "%{_sysconfdir}/%{name}/site_extras.php"				\
	"${RPM_BUILD_ROOT}%{basepath}/includes/site_extras.php"
mv "${RPM_BUILD_ROOT}%{basepath}/includes/auth-settings.php"		\
	"${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/"
ln -s "%{_sysconfdir}/%{name}/auth-settings.php"			\
	"${RPM_BUILD_ROOT}%{basepath}/includes/auth-settings.php"

#	Install Apache configuration file.

install -d "${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d"
sed 's#@BASEPATH@#%{basepath}#g' < "%{SOURCE2}"				\
	> "${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/%{name}.conf"

#	Install cron file for reminders.

install -d "${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d"
cat > "${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d/%{name}" <<'EOF'

#	Send WebCalendar reminders.
#
#	Uncomment the next line to enable it (every minute).

# * * * * * apache cd %{basepath}/tools; sleep 30; %{_bindir}/php -d magic_quotes_gpc=0 send_reminders.php
EOF


#	Generate base path file list, tagging translation files.

(
	cd "${RPM_BUILD_ROOT}%{basepath}"
	find . -type d | sed -e "s#^\.#%dir %{basepath}#"
	find . -type f | sed -e "s#^\.#%{basepath}#" | php "%{SOURCE3}"
	find . ! \( -type d -o -type f \) | sed -e "s#^\.#%{basepath}#"
) > basepath.filelist

#-------------------------------------------------------------------------------
%files -f basepath.filelist
#-------------------------------------------------------------------------------

%defattr(-, root, root, -)
%doc AUTHORS NEWS
%doc GPL.html README.html
%attr(775, root, apache) %dir %{_sysconfdir}/%{name}
%attr(660, root, apache) %config(noreplace) %ghost %{_sysconfdir}/%{name}/settings.php
%attr(640, root, apache) %config(noreplace) %{_sysconfdir}/%{name}/auth-settings.php
%config(noreplace) %{_sysconfdir}/%{name}/site_extras.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config(noreplace) %{_sysconfdir}/cron.d/%{name}


#-------------------------------------------------------------------------------
%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

#-------------------------------------------------------------------------------

* Fri Sep 29 2017 Patrick Monnerat <patrick@monnerat.net> 1.2.9-1
- New upstream release. Fixes CVE-2017-10840 and CVE-2017-10841.
- Upstream moved from sourceforge to github.
- PHP >= 5.3 required.
- Adjust httpd configuration to support PHP FCGI.

* Wed Jul 26 2017 Patrick Monnerat <patrick@monnerat.net> 1.2.7-9
- Patch "php7" for PHP version 7 compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=1471128.
- Patch "groupsarrayinit" to fix an array initialization in menu/index.php.
  https://bugzilla.redhat.com/show_bug.cgi?id=1471128.
- PHP 4 support dropped.
- Patch "adminthemexss" to check validity of admin theme upon change.
  https://github.com/craigk5n/webcalendar/commit/eae6dfb

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.2.7-3
- Perl 5.18 rebuild

* Sat Jul 27 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> 1.2.7-2
- Add a missing requirement on crontabs to spec file.

* Tue Jul 23 2013 Patrick Monnerat <pm@datasphere.ch> 1.2.7-1
- New upstream release.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.5-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Patrick Monnerat <pm@datasphere.ch> 1.2.5-2
- Apache configuration file migrated to version 2.4. A specific version
  requirement cannot be introduced in this spec file since "Provides:webserver"
  is unversioned.

* Wed Mar 28 2012 Patrick Monnerat <pm@datasphere.ch> 1.2.5-1
- New upstream release.

* Fri Feb 17 2012 Patrick Monnerat <pm@datasphere.ch> 1.2.4-3
- Patch "cve2012_0846" fixes CVE-2012-0846 and some other XSS vulnerabilities.
  http://sourceforge.net/tracker/?func=detail&aid=3472745&group_id=3870&atid=103870

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Patrick Monnerat <pm@datasphere.ch> 1.2.4-1
- New upstream release.
- Patch "cve2011_3814" to fix CVE-2011-3814 vulnerability.
  http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-3814
  https://sourceforge.net/tracker/?func=detail&aid=3414999&group_id=3870&atid=303870
- Patch "canadd" to fix event addition control.
  https://sourceforge.net/tracker/?func=detail&aid=3304491&group_id=3870&atid=303870

* Fri Apr 15 2011 Patrick Monnerat <pm@datasphere.ch> 1.2.3-4
- Patch "nonuser" to fix handling of non-user calendars.
  https://sourceforge.net/tracker/?func=detail&aid=3287576&group_id=3870&atid=303870
- Patch "etp" to fix a possible bad URL.
  https://sourceforge.net/tracker/?func=detail&aid=3272636&group_id=3870&atid=303870
- Drop inoperational java control panel.

* Fri Nov 19 2010 Patrick Monnerat <pm@datasphere.ch> 1.2.3-2
- Patch "authsettings" to move authentication schemes settings into a
  separate configuration file (BZ 654479).
  https://sourceforge.net/tracker/?func=detail&aid=3112746&group_id=3870&atid=303870

* Fri Oct  8 2010 Patrick Monnerat <pm@datasphere.ch> 1.2.3-1
- New upstream version (bugfix release).

* Wed Jul  7 2010 Patrick Monnerat <pm@datasphere.ch> 1.2.1-1
- New upstream version.
- Patch "php53" to get rid of PHP 5.3 deprecated features.
  https://sourceforge.net/tracker/?func=detail&aid=2873491&group_id=3870&atid=303870
- Patch "daylightbug" to fix day offset by one when crossing daylight saving
  active/inactive date.
  https://sourceforge.net/tracker/?func=detail&aid=2877076&group_id=3870&atid=303870
- Patch "viewothers" to allow viewing other users calendar when access control
  is off.
  https://sourceforge.net/tracker/?func=detail&aid=2880387&group_id=3870&atid=303870
- Include AUTHORS in product directory too: needed by the "about" box.

* Fri Aug 14 2009 Patrick Monnerat <pm@datasphere.ch> 1.2.0-8
- Use a custom source tarball to get rid of upstream icons with license issue.

* Fri Aug 14 2009 Patrick Monnerat <pm@datasphere.ch> 1.2.0-7
- Patch and tarball "newmenuicons" to replace menu icons that have an unclear
  license.
- Upstream patch references added.

* Tue Jun 23 2009 Patrick Monnerat <pm@datasphere.ch> 1.2.0-6
- Patch "eventstatus" to allow rejecting an accepted event.
  https://sourceforge.net/tracker/?func=detail&aid=2809120&group_id=3870&atid=303870
- Replace "ed" by "sed -i" in build script to get rid of ed requirement.
- Tag translation files.
- Relocate external classes to the proper subdirectories.

* Fri Jun  5 2009 Patrick Monnerat <pm@datasphere.ch> 1.2.0-5
- Patch "approve" to fix event invitation approval.
  https://sourceforge.net/tracker/?func=detail&aid=2801019&group_id=3870&atid=303870
- Use the hKit class from an external package.
- Use the PHPMailer class from an external package.
- Path "httpauthpub" to accept unconfigured http authenticated user for
  public access. https://sourceforge.net/tracker/?func=detail&aid=2802940&group_id=3870&atid=303870
- Patch "extcaptcha" to use a new version of class captchaphp from an
  external package.
- Patch "extmenu" to use a new version of JSCookMenu from an external package.

* Mon Jan 26 2009 Patrick Monnerat <pm@datasphere.ch> 1.2.0-4
- Path "offsetdays" to ignore offset days in daily repetitions.
  https://sourceforge.net/tracker/?func=detail&aid=2537718&group_id=3870&atid=103870

* Fri Dec  5 2008 Patrick Monnerat <pm@datasphere.ch> 1.2.0-3
- Patch "reset_reminder" to reset reminder upon entry change.
  https://sourceforge.net/tracker/?func=detail&aid=2393257&group_id=3870&atid=303870

* Wed Nov 12 2008 Patrick Monnerat <pm@datasphere.ch> 1.2.0-2
- Patch "nolangwarn" to suppress mb_language() warning.
  https://sourceforge.net/forum/forum.php?thread_id=2692495&forum_id=11588
- Patch "weektimebar" to properly display week timebar view.
  https://sourceforge.net/tracker/?func=detail&aid=2261841&group_id=3870&atid=303870
- Patch "deftimezone" to enable configuration of default client timezone.
  https://sourceforge.net/tracker/?func=detail&aid=2269623&group_id=3870&atid=303870

* Fri Nov  7 2008 Patrick Monnerat <pm@datasphere.ch> 1.2.0-1
- Initial packaging.
- Patch "usercase" to add username case-insensitive flag in configuration.
  https://sourceforge.net/tracker/?func=detail&aid=1425442&group_id=3870&atid=303870
- Patch "shebang" to add a missing shebang in a PHP script.
  https://sourceforge.net/tracker/?func=detail&aid=2261885&group_id=3870&atid=303870
