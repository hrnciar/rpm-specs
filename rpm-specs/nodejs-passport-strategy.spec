%global enable_tests 1

Name:           nodejs-passport-strategy
Version:        1.0.0
Release:        11%{?dist}
Summary:        An abstract class implementing Passport's strategy API

License:        MIT
URL:            https://github.com/jaredhanson/passport-strategy
Source0:        http://registry.npmjs.org/passport-strategy/-/passport-strategy-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated using Source10, which pulls from the upstream
# version control repository.
Source1:        passport-strategy-tests-v%{version}.tar.bz2
Source10:       passport-strategy-dl-tests.sh
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
%endif

%description
This module exports an abstract Strategy class that is intended to be
subclassed when implementing concrete authentication strategies. Once
implemented, such strategies can be used by applications that utilize
Passport middleware for authentication.


%prep
%setup -q -n package
%setup -T -D -a 1 -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/passport-strategy
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/passport-strategy
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --reporter spec --require test/bootstrap/node test/*.test.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/passport-strategy


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

* Sun Aug 18 2013 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
