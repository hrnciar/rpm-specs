%global npmname simple-markdown

Name:           nodejs-%{npmname}
Version:        0.4.4
Release:        5%{?dist}
Summary:        Javascript markdown parsing, made simple

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

# Tests not included.
Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz

BuildRequires:  nodejs-packaging

BuildRequires:  mocha

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
simple-markdown is a markdown-like parser designed for simplicity
and extensibility.

%prep
%autosetup -n package #cowsay-%{version}

# Change makefile to use system copy of mocha for testing.
sed 's,./node_modules/.bin/mocha,mocha,g' -i Makefile

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a simple-markdown.js index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

# Unfortunately, tests currently require react, which is a... heavy
# unpackaged dependency. I'll do it if I have to, but I'd prefer not to.
#make test

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.4.4-1
- Update to latest upstream release, fix CVE-2019-9844 (rhbz#1695304,
  rhbz#1695303).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.4.1-1
- Updated to latest upstream release (rhbz#1579339).

* Mon Apr 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.4.0-1
- Updated to latest upstream release (#1554105).

* Tue Mar 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.3.2-1
- Updated to latest upstream release (#1531831).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.3.1-1
- Update to 0.3.1 (#1491489)

* Sun Sep 03 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 (#1487934)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.2.1-1
- Initial package.
