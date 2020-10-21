#
# Fedora spec file for php-PHPMailer
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global github_user  PHPMailer
%global github_app   PHPMailer
%global github_tag   acba50393dd03da69a50226c139722af8b153b11
%global github_short %(c=%{github_tag}; echo ${c:0:7})

%global		arch_name	%{github_app}-%{github_tag}

Name:		php-PHPMailer
Summary:	PHP email transport class with a lot of features
Version:	5.2.28
Release:	3%{?dist}
License:	LGPLv2+
URL:		https://github.com/%{github_user}/%{github_app}

Source0:	https://github.com/%{github_user}/%{github_app}/archive/%{github_tag}/%{github_app}-%{version}-%{github_short}.tar.gz

# Fix language default path
# Don't rely on autoloader (for app which overides __construct)
Patch0:		%{github_app}-path.patch
Patch1:		PHPMailer-5.2.28-cve2020-13625.patch

Buildarch:	noarch

#for tests
BuildRequires: php-cli

# From phpcompatinfo report for 5.2.16
Requires:	php-date
Requires:	php-filter
Requires:	php-hash
Requires:	php-imap
Requires:	php-intl
Requires:	php-mbstring
Requires:	php-openssl
Requires:	php-pcre
Requires:	php-spl

Provides:	php-composer(phpmailer/phpmailer) = %{version}


%description
Full Featured Email Transfer Class for PHP. PHPMailer features:

    * Supports emails digitally signed with S/MIME encryption!
    * Supports emails with multiple TOs, CCs, BCCs and REPLY-TOs
    * Works on any platform.
    * Supports Text & HTML emails.
    * Embedded image support.
    * Multipart/alternative emails for mail clients that do not read
      HTML email.
    * Flexible debugging.
    * Custom mail headers.
    * Redundant SMTP servers.
    * Support for 8bit, base64, binary, and quoted-printable encoding.
    * Word wrap.
    * Multiple fs, string, and binary attachments (those from database,
      string, etc).
    * SMTP authentication.
    * Tested on multiple SMTP servers: Sendmail, qmail, Postfix, Gmail,
      Imail, Exchange, etc.
    * Good documentation, many examples included in download.
    * It's swift, small, and simple.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -n %{arch_name}

%patch0 -p1 -b .rpm
%patch1 -p1 -b .cve2020-13625


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Nothing to do.


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

#	install directories.

install -p -d -m 755 "${RPM_BUILD_ROOT}%{_datadir}/php/PHPMailer/"
install -p -d -m 755 "${RPM_BUILD_ROOT}%{_datadir}/PHPMailer/language/"

#	Install class files.

install -p -m 644 class.*.php PHPMailerAutoload.php \
	"${RPM_BUILD_ROOT}/%{_datadir}/php/PHPMailer/"

#	Install language files (these are not gettextized).

install -p -m 644 language/*.php					\
	"${RPM_BUILD_ROOT}%{_datadir}/PHPMailer/language"

#	Tag language files.

(
	cd "${RPM_BUILD_ROOT}"
	find ".%{_datadir}/PHPMailer/language" -name "phpmailer.lang-*.php" |
		sed -e 's/^\.//'					\
		    -e 's#^.*/phpmailer\.lang-\(.*\)\.php$#%lang(\1) &#'
) > files.list


%check
: Test autoloader and version
php -r '
require "%{buildroot}%{_datadir}/php/PHPMailer/PHPMailerAutoload.php";
$mailer = new PHPMailer();
echo "Version: " . $mailer->Version . "\n";
version_compare($mailer->Version, "%{version}", "=") or exit(1);
'


#-------------------------------------------------------------------------------
%files -f files.list
#-------------------------------------------------------------------------------

%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc examples
%doc composer.json
%{_datadir}/php/PHPMailer
%dir %{_datadir}/PHPMailer
%dir %{_datadir}/PHPMailer/language


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Patrick Monnerat <patrick@monnerat.net> 5.2.28-2
- Patch "cve2020-13625" fixes CVE-2020-13625 vulnerability. This is a backport
  of https://github.com/PHPMailer/PHPMailer/commit/c2796cb.
  https://bugzilla.redhat.com/show_bug.cgi?id=1848842

* Thu Mar 19 2020 Remi Collet <remi@remirepo.net> - 5.2.28-1
- update to 5.2.28

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Remi Collet <remi@remirepo.net> - 5.2.27-1
- update to 5.2.27

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov  6 2017 Remi Collet <remi@remirepo.net> - 5.2.26-1
- Update to 5.2.26

* Mon Aug 28 2017 Remi Collet <remi@remirepo.net> - 5.2.25-2
- Update to 5.2.25

* Thu Jul 27 2017 Patrick Monnerat <patrick@monnerat.net> 5.2.24-1
- Update to 5.2.24: fixes XSS vulnerability CVE-2017-11503.
  https://bugzilla.redhat.com/show_bug.cgi?id=1474416

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Remi Collet <remi@remirepo.net> - 5.2.23-1
- Update to 5.2.23

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Remi Collet <remi@fedoraproject.org> - 5.2.22-1
- update to 5.2.22
- fix local file disclosure vulnerability CVE-2017-5223

* Wed Dec 28 2016 Remi Collet <remi@fedoraproject.org> - 5.2.21-1
- update to 5.2.21
- fix Remote Code Execution CVE-2016-10045

* Mon Dec 26 2016 Remi Collet <remi@fedoraproject.org> - 5.2.19-1
- update to 5.2.19
- fix Remote Code Execution CVE-2016-10033
- drop documentation removed by upstream

* Sat Jun 25 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 5.2.16-3
- missing requires

* Sat Jun 25 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 5.2.16-2
- bad git hash
- add a check on version

* Sat Jun 25 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 5.2.16-1
- update to 5.2.16
- change URL to github project

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Patrick Monnerat <patrick.monnerat@dh.com> 5.2.14-1
- New upstream release: fixes CVE-2015-8476.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 26 2014 Remi Collet <remi@fedoraproject.org> - 5.2.9-1
- update to 5.2.9

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 5.2.8-1
- update to 5.2.8
- provide php-composer(phpmailer/phpmailer)
- explicit dependencies
- fix license handling
- fix language dir using a patch instead of sed
- provide upstream autoloader

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Patrick Monnerat <pm@datasphere.ch> 5.2.6-1
- New upstream release: source moved to github.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 5.2.2-1
- Latest upstream release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 20 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 5.2.1-1
- Latest upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Patrick Monnerat <pm@datasphere.ch> 5.1-4
- Patch "sign" to fix mail signing.
  https://sourceforge.net/tracker/?func=detail&aid=3370322&group_id=26031&atid=385709

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Patrick Monnerat <pm@datasphere.ch> 5.1-2
- Get rid of dos2unix build requirement and of BuildRoot rpm tag.

* Fri Jan 15 2010 Patrick Monnerat <pm@datasphere.ch> 5.1-1
- New upstream release.
- Moved endline conversion and default language path update from prep to
  build section.
- Patch "php53" to remove PHP 5.3 deprecated features.

* Mon Aug  3 2009 Patrick Monnerat <pm@datasphere.ch> 5.0.2-3
- Home page change.
- Package description from new home page.
- Requires php-mbstring.

* Fri Jun 19 2009 Patrick Monnerat <pm@datasphere.ch> 5.0.2-2
- Suppress "ed" build requirement.
- Tag language files.
- Move class files to a package-specific directory.

* Tue Jun  2 2009 Patrick Monnerat <pm@datasphere.ch> 5.0.2-1
- Initial RPM spec file.
