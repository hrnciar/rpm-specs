#
# Fedora spec file for atoum
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    35714b3044ccbfea6d9d78a7a7107347ee1b5ce9
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})

Name:           atoum
Version:        3.4.1
Release:        2%{?dist}
Summary:        PHP Unit Testing framework

License:        BSD
URL:            http://atoum.org
Source0:        https://github.com/%{name}/%{name}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch

BuildRequires:       php(language) >= 5.6
BuildRequires:       php-hash
BuildRequires:       php-json
BuildRequires:       php-session
BuildRequires:       php-tokenizer
BuildRequires:       php-xml

BuildRequires:       php-mbstring

BuildRequires:       php-cli
BuildRequires:       php-date
BuildRequires:       php-dom
BuildRequires:       php-pcre
BuildRequires:       php-phar
BuildRequires:       php-reflection
BuildRequires:       php-spl

# From composer.json, 	"require": {
#        "php": "^5.6.0 || ^7.0.0 <7.4.0",
#        "ext-hash": "*",
#        "ext-json": "*",
#        "ext-tokenizer": "*",
#        "ext-xml": "*"
Requires:       php(language) >= 5.6
Requires:       php-hash
Requires:       php-json
Requires:       php-tokenizer
Requires:       php-xml
# From composer.json, 	"suggest": {
#        "ext-mbstring": "Provides support for UTF-8 strings"
#        "atoum/stubs": "Provides IDE support (like autocompletion) for atoum",
#        "ext-xdebug": "Provides code coverage report (>= 2.3)"
Requires:       php-mbstring
# From phpcompatinfo report for version 3.2.0
Requires:       php-cli
Requires:       php-date
Requires:       php-dom
Requires:       php-pcre
Requires:       php-phar
Requires:       php-reflection
Requires:       php-spl
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Suggests:       php-pecl-xdebug
%endif

Provides: php-composer(atoum/atoum) = %{version}

%if %{?runselftest}%{!?runselftest:1}
%global with_tests   0%{!?_without_tests:1}
%else
%global with_tests   0%{?_with_tests:1}
%endif


%description
A simple, modern and intuitive unit testing framework for PHP!

It has been designed from the start with the following ideas in mind :
* Can be implemented rapidly ;
* Simplify test development ;
* Allow for writing reliable, readable, and clear unit tests ;

To accomplish that, it massively uses capabilities provided by PHP 5.3,
to give the developer a whole new way of writing unit tests.
Also, thanks to its fluid interface, it allows for writing unit tests in
a fashion close to natural language.
It also makes it easier to implement stubbing within tests, thanks to
intelligent uses of anonymous functions and closures.
atoum natively, and by default, performs the execution of each unit test
within a separate PHP process, to warrant isolation.
Of course, it can be used seamlessly for continuous integration, and given its
design, it can be made to cope with specific needs extremely easily.
atoum also accomplishes all of this without affecting performance, since it
has been developed to boast a reduced memory footprint while allowing for
hastened test execution.
It can also generate unit test execution reports in the Xunit format,
which makes it compatible with continuous integration tools such as Jenkins.
atoum also generates code coverage reports, in order to make it possible
to supervise unit tests.

Optional dependency:
- php-pecl-xdebug for code coverage reports


%prep
%setup -qn %{name}-%{gh_commit}

rm resources/configurations/.gitignore
rm scripts/git/.tag tests/units/classes/scripts/git/.tag
sed -i bin/%{name} \
    -e "s|__DIR__ . '/../|'%{_datadir}/%{name}/|"

sed -i constants.php \
    -e "s/dev-master/%{version}/"


%build
# Empty build section


%install
# create needed directories
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
install -m 0644 -p constants.php %{buildroot}%{_datadir}/%{name}
install -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
cp -pr classes   %{buildroot}%{_datadir}/%{name}
cp -pr resources %{buildroot}%{_datadir}/%{name}
cp -pr scripts   %{buildroot}%{_datadir}/%{name}
cp -pr tests     %{buildroot}%{_datadir}/%{name}


%check
%if %{with_tests}
cd tests/units
echo "date.timezone=UTC" >php.ini
export PHPRC=$(pwd)/php.ini

ret=0
for cmd in php php72 php73 php74; do
  if which $cmd; then
    $cmd runner.php --use-dot-report --max-children-number 4 --directories . || ret=1
  fi
done

if [ $(php -r 'echo PHP_VERSION_ID;') -lt 70400 ]
then
  exit $ret
fi
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc ABOUT *.md
%doc composer.json
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Remi Collet <remi@remirepo.net> - 3.4.1-1
- update to 3.4.1

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 3.4.0-2
- update to 3.4.0
- fix reported version
- ignore test suite results with 7.4 for now

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Remi Collet <remi@remirepo.net> - 3.3.0-1
- update to 3.3.0
- undefine __brp_mangle_shebangs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep  7 2017 Remi Collet <remi@remirepo.net> - 3.2.0-1
- Update to 3.2.0

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0
- run test suite against SCL if installed

* Wed Feb 22 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 5.6

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 2.9.0-1
- update to 2.9.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.8.1-2
- Apply upstream patch for PHP 7.1 compatibility (see https://github.com/atoum/atoum/commit/82ce0c58fb9a63da0ae15dbd2d94cfa3598670bd)

* Sat Jul  2 2016 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- update to 2.8.1

* Fri Jul  1 2016 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- update to 2.8.0

* Sat May 21 2016 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- update to 2.7.0

* Fri Apr  8 2016 Remi Collet <remi@fedoraproject.org> - 2.6.1-1
- update to 2.6.1

* Wed Mar  9 2016 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- update to 2.6.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Remi Collet <remi@fedoraproject.org> - 2.5.2-1
- update to 2.5.2

* Mon Jan 18 2016 Remi Collet <remi@fedoraproject.org> - 2.5.1-1
- update to 2.5.1

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Mon Dec  7 2015 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Fri Oct 23 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0
- drop patch merged upstream

* Fri Sep 25 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-2
- open https://github.com/atoum/atoum/pull/502 to fix
  inconsistency in setTestNamespace/getTestNamespace
  causing erratic test results in Koschei

* Thu Sep 17 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- update to 2.2.2

* Thu Aug 27 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Thu Aug 27 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-2
- open https://github.com/atoum/atoum/pull/491 to fix
  inconsistency in setTestMethodPrefix/getTestMethodPrefix
  causing erratic test results in Koschei

* Sun Aug  2 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- XDebug is optional
- update source0
- add backport stuff

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.0.1-1
- Last upstream release

* Wed Jun 11 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 0-0.11.gite1f64c2
- Add provides for registered Packagist package

* Mon Jun 09 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 0-0.10.gite1f64c2
- Last upstream commit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git35a880e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.0.8.git35a880e
- Last upstream commit

* Sun Dec 08 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.0.7.gita68f365
- Last upstream commit

* Wed Aug 07 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.0.6.git587a130
- Last upstream commit

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gita0452f6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.0.4.gita0452f6
- Last upstream commit

* Fri May 10 2013 Johan Cwiklinski <johan AT x-tnd DOt be> - 0.0.3.git3118d58
- Last upstream commit

* Sun Feb 10 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.0.2.gitdbfb82f
- Last upstream commit
- Rename package from php-atoum to atoum
- add missing requires
- change path to %%{_datadir}/%%{name}
- add tests and relevant BR

* Sun Jan 13 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0-0.2.git724d3ee
- Use %%{real_name} instead of %%{name} in path

* Sun Jan 13 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0-0.1.git724d3ee
- Initial Release
