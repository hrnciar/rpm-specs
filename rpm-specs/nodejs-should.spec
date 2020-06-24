%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-should
Version:    8.4.0
Release:    9%{?dist}
Summary:    A test framework agnostic BDD-style assertions for Node.js
# License text is included in Readme.md
License:    MIT
URL:        https://github.com/shouldjs/should.js
Source0:    https://registry.npmjs.org/should/-/should-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-%{version}.tar.bz2
Source10:   dl-tests.sh

# should-promised is now part of should
Obsoletes:  nodejs-should-promised < 0.3.1-2

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(should-equal)
BuildRequires:  npm(should-format)
BuildRequires:  npm(should-type)
%endif

Patch0001: 0001-Fix-flaky-tests.patch

%description
should is an expressive, readable, test framework agnostic, behavior-driven
development (BDD)-style assertion library for Node.js.

It extends the Object prototype with a single non-enumerable getter that
allows you to express how that object should behave.

should literally extends Node's assert module. For example,
should.equal(str, 'foo') will work, just as assert.equal(str, 'foo') would,
and should.AssertionError is assert.AssertionError, meaning any test framework
supporting this constructor will function properly with should.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
%patch0001 -p1
rm -f should.min.js
find . -type f -exec chmod -x '{}' \;


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/should
cp -pr package.json index.js lib/ should.js \
    %{buildroot}%{nodejs_sitelib}/should

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --ui exports test/**/*.test.js
%endif


%files
%doc Readme.md History.md CONTRIBUTING.md
%license LICENSE
%{nodejs_sitelib}/should


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Stephen Gallagher <sgallagh@redhat.com> - 8.4.0-2
- Add upstream patch to fix tests on Node.js 6.5+

* Sun May 22 2016 Tom Hughes <tom@compton.nu> - 8.4.0-1
- Update to 8.4.0 upstream release

* Thu May 19 2016 Tom Hughes <tom@compton.nu> - 8.3.2-1
- Update to 8.3.2 upstream release

* Fri Apr 15 2016 Tom Hughes <tom@compton.nu> - 8.3.1-1
- Update to 8.3.1 upstream release

* Thu Mar 24 2016 Tom Hughes <tom@compton.nu> - 8.3.0-1
- Update to 8.3.0 upstream release

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 8.2.2-1
- Update to 8.2.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 8.2.1-1
- update to upstream release 8.2.1

* Sun Jan 24 2016 Tom Hughes <tom@compton.nu> - 8.2.0-1
- update to upstream release 8.2.0

* Tue Jan 12 2016 Tom Hughes <tom@compton.nu> - 8.1.1-1
- update to upstream release 8.1.1

* Mon Jan 11 2016 Tom Hughes <tom@compton.nu> - 8.1.0-1
- update to upstream release 8.1.0

* Sun Dec 20 2015 Piotr Popieluch <piotr1212@gmail.com> - 8.0.2-2
- added obsoletes nodejs-should-promised

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 8.0.2-1
- update to upstream release 8.0.2

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 7.1.1-2
- update should-equal dependency

* Tue Oct 20 2015 Tom Hughes <tom@compton.nu> - 7.1.1-1
- update to upstream release 7.1.1

* Mon Sep  7 2015 Tom Hughes <tom@compton.nu> - 7.1.0-1
- update to upstream release 7.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.3.1-1
- update to upstream release 3.3.1

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.1.3-1
- update to upstream release 3.1.3

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.2-3
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.2-2
- rebuild for missing npm(should) provides on EL6

* Sun Feb 24 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.2-1
- update to upstream release 1.2.2
- fix typo in description

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-1
- initial package
