Name:           nodejs-passport-oauth1
Version:        1.1.0
Release:        8%{?dist}
Summary:        OAuth 1.0 authentication strategy for Passport

License:        MIT
URL:            https://github.com/jaredhanson/passport-oauth1
Source0:        https://github.com/jaredhanson/passport-oauth1/archive/v%{version}/passport-oauth1-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
BuildRequires:  npm(chai-passport-strategy)
BuildRequires:  npm(passport-strategy)
BuildRequires:  npm(oauth)
BuildRequires:  npm(utils-merge)

%description
General-purpose OAuth 1.0 authentication strategy for Passport.

This module lets you authenticate using OAuth in your Node.js
applications. By plugging into Passport, OAuth authentication can be
easily and unobtrusively integrated into any application or framework
that supports Connect-style middleware, including Express.

Note that this strategy provides generic OAuth support. In many cases,
a provider-specific strategy can be used instead, which cuts down on
unnecessary configuration, and accommodates any provider-specific
quirks. See the list for supported providers.

Developers who need to implement authentication against an OAuth
provider that is not already supported are encouraged to sub-class
this strategy. If you choose to open source the new provider-specific
strategy, please add it to the list so other people can find it.


%prep
%autosetup -p 1 -n passport-oauth1-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/passport-oauth1
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/passport-oauth1
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --reporter spec --require test/bootstrap/node test/*.test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/passport-oauth1


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Sun Aug 18 2013 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
