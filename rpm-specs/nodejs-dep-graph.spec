%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-dep-graph
Version:    1.1.0
Release:    17%{?dist}
Summary:    Simple dependency graph management in JavaScript
# License text is included in README.mdown
License:    MIT
URL:        https://github.com/TrevorBurnham/dep-graph
Source0:    http://registry.npmjs.org/dep-graph/-/dep-graph-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  coffee-script
BuildRequires:  npm(watchit)
BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(underscore)
%endif

%description
This is a Node.js module for simple dependency graph management in JavaScript.

Say you have a set of resources that depend on each other in some way. These
resources can be anything (eg, files, chains of command etc.).
All that matters is that each one has a unique string identifier, and a list
of direct dependencies.

dep-graph makes it easy to compute "chains" of dependencies, with guaranteed
logical ordering and no duplicates. That's trivial in most cases, but if A
depends on B and B depends on A, a naïve dependency graph would get trapped
in an infinite loop. dep-graph throws an error if any such "cycles" are
detected.


%prep
%setup -q -n package
%nodejs_fixdep underscore '^1.4'
# Build these from source instead.
rm -rf lib/


%build
%nodejs_symlink_deps --check
/usr/bin/cake build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/dep-graph
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/dep-graph

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
/usr/bin/cake test
%endif


%files
%doc README.mdown docs/
%{nodejs_sitelib}/dep-graph


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 1.1.0-14
- Update npm(underscore) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.0-6
- fix version of npm(underscore) dependency

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.0-5
- fix version of npm(underscore) dependency

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-4
- fix underscore for 1.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.0-2
- unconditionalize 'cake build'
- improve Summary

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.0-1
- initial package
