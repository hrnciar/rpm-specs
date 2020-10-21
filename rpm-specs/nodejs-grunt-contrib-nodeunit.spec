%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-grunt-contrib-nodeunit
Version:    2.0.0
Release:    5%{?dist}
Summary:    Run Nodeunit unit tests with grunt
License:    MIT
URL:        https://github.com/gruntjs/grunt-contrib-nodeunit
Source0:    https://github.com/gruntjs/grunt-contrib-nodeunit/archive/v%{version}/grunt-contrib-nodeunit-%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-clean)
BuildRequires:  npm(grunt-contrib-internal)
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(tap)
%endif

%description
%{summary}.


%prep
%setup -q -n grunt-contrib-nodeunit-%{version}
#find docs/ -size 0 -delete

# Update the source to refer to nodeunit-x as nodeunit.
%nodejs_fixdep nodeunit-x
sed 's/nodeunit-x/nodeunit/g' -i tasks/nodeunit.js

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-nodeunit
cp -pr package.json tasks/ \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-nodeunit

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/grunt nodeunit
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc README.md docs/
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-contrib-nodeunit


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-4
- Correctly load nodeunit-x as nodeunit.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-2
- Fix nodejs Requires on nodeunit to not be versioned.

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-1
- Update to latest upstream release.
- Disable tests for now; there are too many orphaned packages required.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.1-3
- Fix FTBFS for failing test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Tom Hughes <tom@compton.nu> - 0.4.1-1
- update to 0.4.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.3-2
- update to upstream release 0.3.3

* Mon Feb 24 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.2-1
- update to upstream release 0.3.2
- take Source0 from GitHub as the NPM tarball is missing several useful files
- add missing BuildRequires

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- initial package

