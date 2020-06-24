Name:           nodejs-chai-passport-strategy
Version:        1.0.1
Release:        6%{?dist}
Summary:        Helpers for testing Passport strategies with Chai

License:        MIT
URL:            https://github.com/jaredhanson/chai-passport-strategy
Source0:        https://github.com/jaredhanson/chai-passport-strategy/archive/v{%version}/chai-passport-strategy-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)

%description
Helpers for testing Passport strategies with the Chai assertion library.


%prep
%autosetup -p 1 -n chai-passport-strategy-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/chai-passport-strategy
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/chai-passport-strategy
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --reporter spec \
  --require test/bootstrap/node test/*.test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/chai-passport-strategy


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct  1 2017 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 26 2014 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release

* Sun Aug 18 2013 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Initial build of 0.1.0
