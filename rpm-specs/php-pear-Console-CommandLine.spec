# remirepo/fedora spec file for php-pear-Console-CommandLine
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Console_CommandLine

Name:           php-pear-Console-CommandLine
Version:        1.2.2
Release:        9%{?dist}
Summary:        A full featured command line options and arguments parser

License:        MIT
URL:            http://pear.php.net/package/%{pear_name}
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
BuildRequires:  php-dom

Requires:       php-dom
Requires:       php-xml
Requires:       php-pcre
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/console_commandline) = %{version}


%description
Console_CommandLine is a full featured package for managing command-line
options and arguments highly inspired from python optparse module, it allows
the developer to easily build complex command line interfaces.

Main features:
* handles sub commands (i.e. $ my-script.php -q sub-command -f file),
* can be completely built from an XML definition file,
* generate --help and --version options automatically,
* can be completely customized,
* built-in support for i18n,
* and much more...


%prep
%setup -qc
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install

cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -d %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
cd %{pear_name}-%{version}
%{__pear} run-tests tests | tee ../tests.log
grep "FAILED TESTS" ../tests.log && exit 1 || exit 0


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_datadir}/%{pear_name}
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/Console


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct  5 2017 Remi Collet <remi@fedoraproject.org> - 1.2.2-4
- fix FTBFS from Koschei

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- provide php-composer(pear/console_commandline)
- fix test suite https://github.com/pear/Console_CommandLine/pull/8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  9 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-4
- fix FTBFS, use "pear run-tests" instead of "phpunit"

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 (stable) - API 1.2.0 (stable)
- fix for https://pear.php.net/bugs/18682
  columnWrap() in Default Renderer eats up lines with only a EOL
- fix for https://pear.php.net/bugs/19683
  Unit tests are broken
- clean requires
- keep doc in /usr/share/doc/pear

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 1.1.3-8
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.1.3-7
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Christof Damian <christof@damian.net> - 1.1.3-3
- removed global channel

* Sat Nov  6 2010 Christof Damian <christof@damian.net> - 1.1.3-2
- changed pear channel requirement
- fixed license
- move examples to toplevel doc dir
- added check section
- own Console directory

* Mon Nov  1 2010 Christof Damian <christof@damian.net> - 1.1.3-1
- initial spec file

