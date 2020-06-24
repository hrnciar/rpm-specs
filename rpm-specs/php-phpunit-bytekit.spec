%global gh_commit    ef4020bf0b2b233ffb4e85898d9ab563dda024b2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   bytekit-cli
%global php_home     %{_datadir}/php
%global pear_name    bytekit
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
%global channel pear.phpunit.de

Name:           php-phpunit-bytekit
Version:        1.1.3
Release:        15%{?dist}
Summary:        A command-line tool built on the PHP Bytekit extension

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

Patch0:         %{name}-autoload.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3

# From package.xml
Requires:       php(language) >= 5.3.3
Requires:       php-composer(symfony/finder)
Requires:       php-composer(symfony/class-loader)
Requires:       php-composer(zetacomponents/console-tools)
# From phpcomaptinfo report for version 1.1.3
Requires:       php-cli
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl

# For compatibility with pear mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}


%description
Bytekit is a PHP extension that provides userspace access to the opcodes
generated by PHP's compiler.

bytekit-cli is a command-line tool that leverages Bytekit to perform common code
analysis tasks.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
rm Bytekit/Autoload.php.*

find . -name \*.php -exec sed -e 's/@package_version@/%{version}/' -i {} \;


%build
#phpab \
#  --output   Bytekit/Autoload.php \
#  --template Bytekit/Autoload.php.in \
#  Bytekit


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr Bytekit %{buildroot}%{php_home}/Bytekit

install -D -p -m 755 bytekit.php %{buildroot}%{_bindir}/bytekit


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%doc README.markdown LICENSE
%{php_home}/Bytekit
%{_bindir}/bytekit


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Remi Collet <remi@fedoraproject.org> - 1.1.3-7
- swicth from eZ to Zeta Components

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.1.3-6
- use $fedoraClassLoader autoloader
- ensure compatibility with SCL
- fix reported version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.3-3
- sources from github

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.1.3-1
- Fix metadata location, FTBFS #914373
- upstream 1.1.3
- Symfony 2.2 patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.1.2-3
- Update dependencies

* Sun Nov 06 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.1.2-2
- Fix search and replace issue

* Sat Nov 05 2011 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.1.2-1
- upstream 1.1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 18 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.1.1-1
- upstream 1.1.1
- /usr/share/pear/Bytekit wasn't owned

* Thu Nov 26 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.0.0-2
- F-(10|11)

* Wed Oct 14 2009 Guillaume Kulakowski <guillaume DOT kulakowski AT fedoraproject DOT org> - 1.0.0-1
- Initial packaging
