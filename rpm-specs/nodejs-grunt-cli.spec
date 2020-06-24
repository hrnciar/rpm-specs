%global srcname grunt-cli

Name:           nodejs-grunt-cli
Version:        1.2.0
Release:        9%{?dist}
Summary:        Command-line interface for Grunt, the JavaScript testing framework
License:        MIT
URL:            https://github.com/gruntjs/grunt-cli
Source0:        https://github.com/gruntjs/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
Requires:       npm(grunt)


%description
Grunt is the JavaScript task runner.

Grunt-cli gives you access to the grunt command-line interface anywhere on
your system, which is useful when running a locally installed Grunt for your
project.


%prep
%setup -q -n %{srcname}-%{version}
%nodejs_fixdep findup-sync '~0.3'
%nodejs_fixdep nopt '^3.0.6'
%nodejs_fixdep resolve '^1.1.6'

sed -i '1 s|#!/usr/bin/env node|#!/usr/bin/node|' bin/grunt


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-cli
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/grunt-cli

install -p -D -m0755 bin/grunt \
    %{buildroot}%{nodejs_sitelib}/grunt-cli/bin/grunt-cli
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/grunt-cli/bin/grunt-cli \
    %{buildroot}%{_bindir}/grunt

# Bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
sed '1{\@^#!/bin/bash@d}' completion/bash \
    > %{buildroot}%{_datadir}/bash-completion/completions/grunt
chmod 0644 %{buildroot}%{_datadir}/bash-completion/completions/grunt
touch -r completion/bash %{buildroot}%{_datadir}/bash-completion/completions/grunt


%nodejs_symlink_deps


%files
%doc AUTHORS CHANGELOG.md README.md
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-cli
%{_bindir}/grunt
%{_datadir}/bash-completion/completions/grunt


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Tom Hughes <tom@compton.nu> - 1.2.0-6
- Update npm(findup-sync) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.2.0-1
- Update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 0.1.13-5
- Update npm(nopt) dependency

* Fri Jan  8 2016 Tom Hughes <tom@compton.nu> - 0.1.13-4
- Update npm(resolve) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.13-1
- update to upstream release 0.1.13

* Sat Jan 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.11-1
- update to upstream release 0.1.11
- improve description and summary
- install bash-completion file in the correct place

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.9-1
- initial package
