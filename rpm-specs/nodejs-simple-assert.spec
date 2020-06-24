%global commit ad723ef3c0e8e33ac55f40c0613204a3ff56c689

Name:           nodejs-simple-assert
Version:        1.0.0
Release:        12%{?dist}
Summary:        Vanilla assertions for Node.js

License:        MIT
URL:            https://github.com/chaijs/simple-assert
Source0:        https://github.com/chaijs/simple-assert/archive/%{commit}/simple-assert-%{commit}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(assertion-error)

%description
A simple assert wrapper around chaijs/assertion-error. This probably
won't be useful to the average user unless you are a minimalist; you
probably want Chai. This software is used to avoid circular dependencies
when testing Chai's dependencies.


%prep
%setup -q -n simple-assert-%{commit}
%nodejs_fixdep assertion-error "^1.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/simple-assert
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/simple-assert
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --require test/bootstrap --reporter spec test/*.js


%files
%doc README.md History.md 
%{nodejs_sitelib}/simple-assert



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Tom Hughes <tom@compton.nu> - 1.0.0-3
- Relax assertion-error-dependency
- Switch to using github as source so we get tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
