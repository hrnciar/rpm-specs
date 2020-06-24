Name:           nodejs-passport
Version:        0.4.0
Release:        6%{?dist}
Summary:        Simple, unobtrusive authentication for Node.js

License:        MIT
URL:            https://github.com/jaredhanson/passport
Source0:        https://github.com/jaredhanson/passport/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(pause)
BuildRequires:  npm(chai)
BuildRequires:  npm(chai-connect-middleware)
BuildRequires:  npm(chai-passport-strategy) >= 0.2.0
BuildRequires:  npm(passport-strategy)
BuildRequires:  npm(proxyquire)

%description
Passport is an authentication framework for Connect and Express, which
is extensible through "plugins" known as strategies.

Passport is designed to be a general-purpose, yet simple, modular, and
unobtrusive, authentication framework. Passport's sole purpose is to
authenticate requests. In being modular, it doesn't force any particular
authentication strategy on your application. In being unobtrusive, it
doesn't mount routes in your application. The API is simple: you give
Passport a request to authenticate, and Passport provides hooks for
controlling what occurs when authentication succeeds or fails.


%prep
%setup -q -n passport-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/passport
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/passport
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --reporter spec \
  --require test/bootstrap/node test/*.test.js test/**/*.test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/passport


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 0.3.2-1
- Update to 0.3.2 upstream release

* Mon Aug 24 2015 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release
- Switch to %%license for the license file

* Tue Sep  2 2014 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release
- Switch to source from github to get tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 26 2014 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release

* Sat Jan  4 2014 Tom Hughes <tom@compton.nu> - 0.1.18-1
- Update to 0.1.18 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Tom Hughes <tom@compton.num> - 0.1.17-1
- Update to 0.1.17 upstream release
- Enable tests

* Sat Mar  2 2013 Tom Hughes <tom@compton.nu> - 0.1.16-1
- Update to 0.1.16 upstream release
- BuildRequire pkginfo for tests
- Link node_modules for tests

* Sat Feb 23 2013 Tom Hughes <tom@compton.nu> - 0.1.15-2
- Update pkginfo dependency

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.1.15-1
- Initial build of 0.1.15
