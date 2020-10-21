# remirepo/fedora spec file for php-phpmailer6
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please preserve changelog entries
#
# Github
%global gh_commit    917ab212fa00dc6eacbb26e8bc387ebe40993bc1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     PHPMailer
%global gh_project   PHPMailer
# Packagist
%global pk_vendor    phpmailer
%global pk_project   phpmailer
# Namespace
%global ns_vendor    PHPMailer
%global ns_project   PHPMailer
# don't change major version used in package name
%global major        6
%bcond_without       tests
%global php_home     %{_datadir}/php

Name:           php-%{pk_project}%{major}
Version:        6.1.8
Release:        1%{?dist}
Summary:        Full-featured email creation and transfer class for PHP

License:        LGPLv2
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
# Simple unit test for packaging
Source2:        PHPMailerRpmTest.php

# Fix path to match RPM installation layout
Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-filter
BuildRequires:  php-hash
BuildRequires:  php-imap
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-fedora-autoloader-devel
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "^2.2",
#        "phpunit/phpunit": "^4.8 || ^5.7",
#        "doctrine/annotations": "^1.2",
BuildRequires:  php-phpunit-PHPUnit >= 4.8
BuildRequires:  %{_sbindir}/smtp-sink
%endif

# From composer.json, "require": {
#    "require": {
#        "php": ">=5.5.0",
#        "ext-ctype": "*",
#        "ext-filter": "*",
#        "ext-hash": "*"
Requires:       php(language) >= 5.5
Requires:       php-ctype
Requires:       php-filter
Requires:       php-hash
# from phpcompatinfo report on version 6.1.3
Requires:       php-date
Requires:       php-imap
Requires:       php-intl
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
# From composer.json, "suggest": {
#        "psr/log": "For optional PSR-3 debug logging",
#        "league/oauth2-google": "Needed for Google XOAUTH2 authentication",
#        "hayageek/oauth2-yahoo": "Needed for Yahoo XOAUTH2 authentication",
#        "stevenmaguire/oauth2-microsoft": "Needed for Microsoft XOAUTH2 authentication",
#        "ext-mbstring": "Needed to send email in multibyte encoding charset",
#        "symfony/polyfill-mbstring": "To support UTF-8 if the Mbstring PHP extension is not enabled (^1.2)"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Suggests:       php-composer(psr/log)
%endif

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
PHPMailer - A full-featured email creation and transfer class for PHP

Class Features
* Probably the world's most popular code for sending email from PHP!
* Used by many open-source projects:
  WordPress, Drupal, 1CRM, SugarCRM, Yii, Joomla! and many more
* Integrated SMTP support - send without a local mail server
* Send emails with multiple To, CC, BCC and Reply-to addresses
* Multipart/alternative emails for mail clients that do not read HTML email
* Add attachments, including inline
* Support for UTF-8 content and 8bit, base64, binary, and quoted-printable
  encodings
* SMTP authentication with LOGIN, PLAIN, CRAM-MD5 and XOAUTH2 mechanisms
  over SSL and SMTP+STARTTLS transports
* Validates email addresses automatically
* Protect against header injection attacks
* Error messages in 47 languages!
* DKIM and S/MIME signing support
* Compatible with PHP 5.5 and later
* Namespaced to prevent name clashes
* Much more!


Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1

cp %{SOURCE2} test/PHPMailerRpmTest.php

cat << 'EOF' | tee src/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\PHPMailer\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional(array(
    '%{php_home}/Psr/Log/autoload.php',
));
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}
cp -pr language %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/language


%check
%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\Test\\', dirname(__DIR__) . '/test');
EOF

sed -e '/colors/d;s/logging/nologging/' travis.phpunit.xml.dist > phpunit.xml

: Start fake MTA and test environment
PORT=$(expr 2500 + %{?fedora}%{?rhel})
sed -e "s/2500/$PORT/" test/testbootstrap-dist.php > test/testbootstrap.php

mkdir -p build/logs
chmod +x test/fakesendmail.sh

pushd build
  smtp-sink -d "%%d.%%H.%%M.%%S" localhost:$PORT 1000 &>/dev/null &
  SMTPPID=$!
popd

: Run upstream test suite
ret=0
for cmd in php php71 php72 php73 php74 php80; do
  if which $cmd; then
    $cmd  -d "sendmail_path=$PWD/test/fakesendmail.sh -t -i " \
      %{_bindir}/phpunit --exclude slow,pop3,languages --verbose || ret=1
  fi
done

: Cleanup
kill $SMTPPID

exit $ret
%endif


%files
%license LICENSE
%license COMMITMENT
%doc *.md
%doc examples
%doc composer.json
%{php_home}/%{ns_vendor}


%changelog
* Sat Oct 10 2020 Remi Collet <remi@remirepo.net> - 6.1.8-1
- update to 6.1.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Remi Collet <remi@remirepo.net> - 6.1.7-1
- update to 6.1.7

* Wed May 27 2020 Remi Collet <remi@remirepo.net> - 6.1.6-2
- update to 6.1.6

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 6.1.5-1
- update to 6.1.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Remi Collet <remi@remirepo.net> - 6.1.4-1
- update to 6.1.4

* Thu Nov 21 2019 Remi Collet <remi@remirepo.net> - 6.1.3-1
- update to 6.1.3

* Thu Nov 14 2019 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Mon Sep 30 2019 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 6.0.7-1
- update to 6.0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Remi Collet <remi@remirepo.net> - 6.0.6-1
- update to 6.0.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Remi Collet <remi@remirepo.net> - 6.0.5-1
- update to 6.0.5 (no change)

* Tue Mar 27 2018 Remi Collet <remi@remirepo.net> - 6.0.4-1
- update to 6.0.4
- add patch to fix lang_path with RPM layout

* Sun Jan  7 2018 Remi Collet <remi@remirepo.net> - 6.0.3-1
- Update to 6.0.3

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 6.0.2-1
- Update to 6.0.2

* Wed Nov 15 2017 Remi Collet <remi@remirepo.net> - 6.0.1-1
- initial rpm, version 6.0.1
- open https://github.com/PHPMailer/PHPMailer/issues/1243 for FSF address
