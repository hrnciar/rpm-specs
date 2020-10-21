%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-ms
Version:        2.0.0
Release:        9%{?dist}
Summary:        Tiny milliseconds conversion utility for Node.js

License:        MIT
URL:            https://www.npmjs.com/package/ms
Source0:        https://github.com/zeit/ms/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(expect.js)
BuildRequires:  npm(mocha)
%endif

%description
This module is a tiny milliseconds conversion utility for Node.js.

It does the following:
 - If a number is supplied to ms, a string with a unit is returned.
 - If a string that contains the number is supplied, it returns it as a
   number (e.g: it returns 100 for '100').
 - If you pass a string with a number and a valid unit, the number of
   equivalent milliseconds is returned.


%prep
%autosetup -n ms-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ms
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/ms

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha tests.js
%endif


%files
%doc readme.md
%license license.md
%{nodejs_sitelib}/ms


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 0.7.1-1
- update to 0.7.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.2-1
- update to upstream release 0.6.2

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.1-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.1-1
- update to upstream release 0.6.1

* Sat Mar 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.0-1
- update to upstream release 0.6.0
- History.md is now not included in the npm tarball
- tests are now not included in the npm tarball, so download separately

* Fri Mar 15 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-1
- update to upstream release 0.5.1

* Fri Feb 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-2
- add a copy of the MIT license to comply with license requirements

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- initial package
