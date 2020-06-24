#
# Fedora spec file for php-symfony-polyfill
#
# Copyright (c) 2015-2020 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      polyfill
%global github_version   1.17.0
%global github_commit    de7e60ee00ab492b93283795257c7d850fc3b1ff

%global composer_vendor  symfony
%global composer_project polyfill

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
# raise dependency on PHP 7 and ignore *_compat
%global php_min_ver 7.0
%else
# "php": ">=5.3.3"
%global php_min_ver 5.3.3
# "ircmaxell/password-compat": "~1.0"
%global ircmaxell_password_compat_min_ver 1.0
%global ircmaxell_password_compat_max_ver 2.0
# "paragonie/random_compat": "~1.0|~2.0|~9.99"
%global paragonie_random_compat_min_ver 1.0
%global paragonie_random_compat_max_ver 3.0
%endif

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Symfony polyfills backporting features to lower PHP versions

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with_tests}
BuildRequires: php-composer(phpunit/phpunit)
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
%if 0%{?fedora} < 27 && 0%{?rhel} < 8
BuildRequires: php-composer(ircmaxell/password-compat) <  %{ircmaxell_password_compat_max_ver}
BuildRequires: php-composer(ircmaxell/password-compat) >= %{ircmaxell_password_compat_min_ver}
BuildRequires: php-composer(paragonie/random_compat) <  %{paragonie_random_compat_max_ver}
BuildRequires: php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver}
%endif
## phpcompatinfo (computed from version 1.8.0)
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
%if 0%{?fedora} < 27 && 0%{?rhel} < 8
Requires:      php-composer(ircmaxell/password-compat) <  %{ircmaxell_password_compat_max_ver}
Requires:      php-composer(ircmaxell/password-compat) >= %{ircmaxell_password_compat_min_ver}
Requires:      php-composer(paragonie/random_compat) <  %{paragonie_random_compat_max_ver}
Requires:      php-composer(paragonie/random_compat) >= %{paragonie_random_compat_min_ver}
%endif
# phpcompatinfo (computed from version 1.8.0)
Requires:      php-hash
Requires:      php-iconv
Requires:      php-intl
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})       = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-mbstring) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-util)  = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php54) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php55) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php56) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php70) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php71) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php72) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php73) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php74) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php80) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Symfony/Polyfill/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Docs
mkdir -p docs/{Mbstring,Php54,Php55,Php56,Php70,Php71,Php72,Php73,Php74,Php80,Util}
mv *.md composer.json docs/
mv src/Mbstring/{*.md,composer.json}  docs/Mbstring/
mv src/Php54/{*.md,composer.json} docs/Php54/
mv src/Php55/{*.md,composer.json} docs/Php55/
mv src/Php56/{*.md,composer.json} docs/Php56/
mv src/Php70/{*.md,composer.json} docs/Php70/
mv src/Php71/{*.md,composer.json} docs/Php71/
mv src/Php72/{*.md,composer.json} docs/Php72/
mv src/Php73/{*.md,composer.json} docs/Php73/
mv src/Php74/{*.md,composer.json} docs/Php74/
mv src/Php80/{*.md,composer.json} docs/Php80/
mv src/Util/{*.md,composer.json}  docs/Util/

: Remove unneeded polyfills as extensions are available
rm -rf {src,tests}/{Apcu,Ctype,Iconv,Intl,Uuid,Xml}


%build
: Create autoloader classmap
%{_bindir}/phpab --template fedora --tolerant --output src/autoload.php src/
cat src/autoload.php

: Create autoloader
cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__ . '/bootstrap.php',
    __DIR__ . '/Mbstring/bootstrap.php',
    __DIR__ . '/Php54/bootstrap.php',
    __DIR__ . '/Php55/bootstrap.php',
    __DIR__ . '/Php56/bootstrap.php',
    __DIR__ . '/Php70/bootstrap.php',
    __DIR__ . '/Php71/bootstrap.php',
    __DIR__ . '/Php72/bootstrap.php',
    __DIR__ . '/Php73/bootstrap.php',
    __DIR__ . '/Php74/bootstrap.php',
));
\Fedora\Autoloader\Dependencies::optional(array(
    '%{phpdir}/password_compat/password.php',
    '%{phpdir}/random_compat/autoload.php',
));
AUTOLOAD


%install

: Library
mkdir -p %{buildroot}%{phpdir}/Symfony/Polyfill
cp -rp src/* %{buildroot}%{phpdir}/Symfony/Polyfill/


%check
%if %{with_tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit)
for PHP_EXEC in "" %{?rhel:php54 php55 php56 php70} php71 php72 php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Symfony/Polyfill/autoload.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc docs/*
%dir %{phpdir}/Symfony
     %{phpdir}/Symfony/Polyfill
%exclude %{phpdir}/Symfony/Polyfill/*/LICENSE


%changelog
* Wed May 13 2020 Remi Collet <remi@remirepo.net> - 1.17.0-1
- update to 1.17.0

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 1.15.0-1
- update to 1.15.0

* Mon Feb 17 2020 Remi Collet <remi@remirepo.net> - 1.14.0-1
- update to 1.14.0
- provides symfony/polyfill-php80

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 1.13.1-1
- update to 1.13.1 (no change)

* Thu Nov 28 2019 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.13.0

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0
- add symfony/polyfill-php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Mon Aug 27 2018 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 1.8.0-3
- raise dependency on PHP 7 and ignore dependencies on
  ircmaxell/password-compat and paragonie/random_compat

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May  4 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- add symfony/polyfill-php73
- use range dependencies

* Wed Apr 11 2018 Remi Collet <remi@remirepo.net> - 1.7.0-2
- add symfony/polyfill-mbstring for mb_chr, mb_ord, mb_scrub
- add dependency on iconv and intl extensions

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Updated to 1.5.0 (RHBZ #1482156)
- Added version constraints to ircmaxell/password-compat
- Added max version constraint to paragonie/random_compat BuildeRequires
- Removed php-mbstring dependency

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1460473)
- Provide php-composer(symfony/polyfill-php72)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Updated to 1.3.0
- provide php-composer(symfony/polyfill-php71)
- switch to fedora/autoloader

* Thu Jun 16 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (RHBZ #1301791)

* Tue Apr 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Updated to 1.1.1 (RHBZ #1301791)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Updated to 1.0.1 (RHBZ #1294916)

* Mon Dec 07 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-3
- Fixed Util docs
- Added "%%dir %%{phpdir}/Symfony" to %%files

* Sun Dec 06 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-2
- Always include ALL polyfills

* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
