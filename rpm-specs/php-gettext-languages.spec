Name:       php-gettext-languages
Version:    2.4.0
Release:    4%{?dist}
BuildArch:  noarch

License:    MIT and Unicode
Summary:    Generate gettext language lists with plural rules
URL:        https://github.com/mlocati/cldr-to-gettext-plural-rules
# Upstream removes the tests from the archive, so the tarball is manually built from a checkout.
# https://github.com/mlocati/cldr-to-gettext-plural-rules/issues/11
#
# To build the tarball:
#
# $ git clone git@github.com:mlocati/cldr-to-gettext-plural-rules.git
# $ cd cldr-to-gettext-plural-rules
# $ rm .gitattributes
# $ touch .gitattributes
# $ git archive -o cldr-to-gettext-plural-rules-VERSION.tar.gz --prefix cldr-to-gettext-plural-rules-VERSION/ --worktree-attributes VERSION
Source0:    cldr-to-gettext-plural-rules-%{version}.tar.gz

BuildRequires: php-composer(fedora/autoloader)
BuildRequires: phpunit 

Requires:   php(language) >= 5.4.0
Requires:   php-cli
Requires:   php-dom
Requires:   php-iconv
Requires:   php-json
Requires:   php-pcre
Requires:   php-spl

Provides:   php-composer(gettext/languages) = %{version}


%description
A library that can generate gettext language lists automatically
generated from CLDR data.


%prep
%autosetup -p1 -n cldr-to-gettext-plural-rules-%{version}

sed -i "s:require_once.*:require_once '%{_datadir}/php/Gettext/Languages/autoloader.php';:" bin/export-plural-rules.php
echo "#!/usr/bin/env php" > bin/export-plural-rules.sh
cat bin/export-plural-rules.sh bin/export-plural-rules.php > bin/export-plural-rules


%install
install -d -p -m 0755 %{buildroot}/%{_bindir}
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext/Languages

cp -a bin/export-plural-rules %{buildroot}/%{_bindir}/%{name}-export-plural-rules
chmod 755 %{buildroot}/%{_bindir}/%{name}-export-plural-rules

cp -ar src/* %{buildroot}/%{_datadir}/php/Gettext/Languages/


%check
sed -i "s:require_once.*:require_once '%{buildroot}/%{_datadir}/php/Gettext/Languages/autoloader.php';:" tests/bootstrap.php

sed -i "s:require_once.*:require_once '%{buildroot}/%{_datadir}/php/Gettext/Languages/autoloader.php';:" bin/export-plural-rules.php
phpunit --bootstrap tests/bootstrap.php


%files
%license LICENSE
%license UNICODE-LICENSE.txt
%doc composer.json
%doc README.md
%{_bindir}/%{name}-export-plural-rules
%{_datadir}/php/Gettext


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0 (#1594776).
- https://github.com/mlocati/cldr-to-gettext-plural-rules/releases/tag/2.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (#1435488).

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.3-4
- Move the sed on tests/bootstrap.php into the check section to get rid of a lint warning.

* Wed Feb 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.3-3
- Add an export cli.
- Include a patch that adds a shebang to the export CLI.

* Sat Jan 21 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.3-2
- Use a git snapshot instead of the version tag so that we get the
  tests and the docs (See
  https://github.com/mlocati/cldr-to-gettext-plural-rules/issues/11 )
- Run the tests.
- Modify the test bootstrap and export.php to use the library
  installation location instead of the local path.

* Sun Jan 15 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.3-1
- Initial release.
