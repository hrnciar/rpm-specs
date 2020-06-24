Name:           nodejs-chai
Version:        3.5.0
Release:        11%{?dist}
Summary:        BDD/TDD assertion library for Node.js and the browser

License:        MIT
URL:            http://chaijs.com
Source0:        https://github.com/chaijs/chai/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(assertion-error)
BuildRequires:  npm(deep-eql)

Patch0001: fix-tests-on-nodejs65.patch

%description
Chai is a BDD / TDD assertion library for node and the browser that
can be delightfully paired with any JavaScript testing framework.


%prep
%setup -q -n chai-%{version}
%patch0001 -p1
%nodejs_fixdep type-detect "^2.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/chai
cp -r package.json index.js chai.js lib %{buildroot}/%{nodejs_sitelib}/chai
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --require ./test/bootstrap --reporter dot --ui tdd test/*.js


%files
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md History.md ReleaseNotes.md
%{nodejs_sitelib}/chai


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Stephen Gallagher <sgallagh@redhat.com> - 3.5.0-4
- Fix broken tests on Node.js 6.5+

* Mon Mar 14 2016 Tom Hughes <tom@compton.nu> - 3.5.0-3
- Update npm(type-detect) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 3.5.0-1
- Update to 3.5.0 upstream release

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 3.4.1-1
- Update to 3.4.1 upstream release

* Wed Oct 21 2015 Tom Hughes <tom@compton.nu> - 3.4.0-1
- Update to 3.4.0 upstream release

* Mon Sep 21 2015 Tom Hughes <tom@compton.nu> - 3.3.0-1
- Update to 3.3.0 upstream release

* Mon Jul 20 2015 Tom Hughes <tom@compton.nu> - 3.2.0-1
- Update to 3.2.0 upstream release

* Fri Jul 17 2015 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Update to 3.1.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun  4 2015 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Mon Apr 27 2015 Tom Hughes <tom@compton.nu> - 2.3.0-1
- Update to 2.3.0 upstream release

* Fri Mar 27 2015 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Mon Mar 16 2015 Tom Hughes <tom@compton.nu> - 2.1.2-1
- Update to 2.1.2 upstream release

* Fri Mar  6 2015 Tom Hughes <tom@compton.nu> - 2.1.1-3
- Fix typo

* Fri Mar  6 2015 Tom Hughes <tom@compton.nu> - 2.1.1-2
- Relax assertion-error dependency

* Thu Mar  5 2015 Tom Hughes <tom@compton.nu> - 2.1.1-1
- Update to 2.1.1 upstream release

* Fri Feb 13 2015 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Wed Nov 12 2014 Tom Hughes <tom@compton.nu> - 1.10.0-1
- Update to 1.10.0 upstream release

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 1.9.2-1
- Update to 1.9.2 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Tom Hughes <tom@compton.nu> - 1.9.1-1
- Update to 1.9.1 upstream release
- Switch to using github as source so we get tests

* Fri Jan 31 2014 Tom Hughes <tom@compton.nu> - 1.9.0-1
- Update to 1.9.0 upstream release

* Sat Aug 17 2013 Tom Hughes <tom@compton.nu> - 1.7.2-1
- Initial build of 1.7.2
