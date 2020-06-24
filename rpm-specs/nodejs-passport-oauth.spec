%global enable_tests 1

Name:           nodejs-passport-oauth
Version:        1.0.0
Release:        11%{?dist}
Summary:        OAuth 1.0 and 2.0 authentication strategies for Passport

License:        MIT
URL:            https://github.com/jaredhanson/passport-oauth
Source0:        http://registry.npmjs.org/passport-oauth/-/passport-oauth-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated using Source10, which pulls from the upstream
# version control repository.
Source1:        passport-oauth-tests-v%{version}.tar.bz2
Source10:       passport-oauth-dl-tests.sh
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
BuildRequires:  npm(chai-passport-strategy)
BuildRequires:  npm(passport-oauth1)
BuildRequires:  npm(passport-oauth2)
%endif

%description
General-purpose OAuth 1.0 and OAuth 2.0 authentication strategies for
Passport.

This module lets you authenticate using OAuth in your Node.js
applications. By plugging into Passport, OAuth authentication can be
easily and unobtrusively integrated into any application or framework
that supports Connect-style middleware, including Express.

Note that this strategy provides generic OAuth support. In many cases,
a provider-specific strategy can be used instead, which cuts down on
unnecessary configuration, and accommodates any provider-specific
quirks. See the list below for supported providers.


%prep
%setup -q -n package
%setup -T -D -a 1 -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/passport-oauth
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/passport-oauth
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --reporter spec --require test/bootstrap/node test/*.test.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/passport-oauth


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Tom Hughes <tom@compton.nu> - 0.1.15-1
- Update to 0.1.15 upstream release

* Mon Mar 11 2013 Tom Hughes <tom@compton.nu> - 0.1.14-3
- Link node_modules for tests
- BuildRequire oauth, passport and pkginfo for tests
- Improve description

* Sat Feb 23 2013 Tom Hughes <tom@compton.nu> - 0.1.14-2
- Update pkginfo dependency

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.1.14-1
- Initial build of 0.1.14
