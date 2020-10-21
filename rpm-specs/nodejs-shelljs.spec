%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-shelljs
Version:        0.8.4
Release:        2%{?dist}
Summary:        Portable Unix shell commands for Node.js

# The bulk of the project is licensed under BSD license.
# src/cp.js and src/rm.js contain MIT licensed code.
# https://fedorahosted.org/fpc/ticket/413
License:        BSD and MIT
URL:            http://github.com/arturadib/shelljs
Source0:        http://github.com/arturadib/shelljs/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(glob)

%if 0%{?enable_tests}
BuildRequires:  coffee-script
BuildRequires:  npm(ava)
%endif

%description
%{summary}.

%prep
%autosetup -p 1 -n shelljs-%{version}
sed -i '1s/env //' bin/shjs
%nodejs_fixdep glob

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/shelljs
cp -pr package.json commands.js global.js make.js plugin.js shell.js src/ \
    %{buildroot}%{nodejs_sitelib}/shelljs
mkdir -p %{buildroot}%{nodejs_sitelib}/shelljs/bin
install -p -m0755 bin/shjs %{buildroot}%{nodejs_sitelib}/shelljs/bin
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/shelljs/bin/shjs %{buildroot}%{_bindir}/shjs
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ava test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md RELEASE.md
%{nodejs_sitelib}/shelljs
%{_bindir}/shjs

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Update to latest upstream release 0.8.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Tom Hughes <tom@compton.nu> - 0.8.3-1
- Update to 0.8.3 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 06 2017 Jared Smith <jsmith@fedoraproject.org> - 0.7.3-1
- Update to upstream 0.7.3 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.0-1
- update to upstream release 0.3.0
- fix License tag
- patch out jshint tests
- include copy of the MIT license

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.6-1
- initial package
