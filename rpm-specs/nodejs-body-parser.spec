%global npmname body-parser

Name:           nodejs-%{npmname}
Version:        1.18.3
Release:        5%{?dist}
Summary:        Node.js body parsing middleware

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

# Pull sources from github, with unit tests, not npm.
# Source0:        https://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz
Source0:        https://github.com/expressjs/body-parser/archive/%{version}/%{npmname}-%{version}.tar.gz

# Patch required because a test requires a newer nodejs-supertest than Fedora ships.
Patch0:         nodejs-body-parser-disable-json-test.patch

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-debug, nodejs-bytes, nodejs-content-type, nodejs-depd,
BuildRequires:  nodejs-http-errors, nodejs-iconv-lite, nodejs-on-finished, nodejs-qs,
BuildRequires:  nodejs-raw-body, nodejs-type-is, nodejs-safe-buffer

# Unit tests.
BuildRequires:  mocha, nodejs-methods, nodejs-supertest

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Parse incoming request bodies in a middleware before your handlers,
available under the req.body property.

This does not handle multipart bodies, due to their complex and
typically large nature.

%prep
%autosetup -n %{npmname}-%{version} -p1

# Remove forced versions from package.json
%nodejs_fixdep bytes
%nodejs_fixdep content-type
%nodejs_fixdep debug
%nodejs_fixdep depd
%nodejs_fixdep http-errors
%nodejs_fixdep iconv-lite
%nodejs_fixdep on-finished
%nodejs_fixdep qs
%nodejs_fixdep raw-body
%nodejs_fixdep type-is

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a lib/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a index.js %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
pwd
# Run tests with mocha.
mocha --require test/support/env --reporter spec --check-leaks --bail test/

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE
%doc README.md HISTORY.md


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.18.3-1
- Update to latest upstream release (rhbz#1578166).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Jared Smith <jsmith@fedoraproject.org> - 1.18.2-1
- Update to upstream 1.18.2 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.17.2-1
- Updated to latest upstream release.

* Wed Mar 22 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.17.1-1
- Update to latest upstream release.
- Fix a typo in the package description.

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.16.1-1
- Update to latest upstream release.

* Thu Feb 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.16.0-1
- Initial package.
