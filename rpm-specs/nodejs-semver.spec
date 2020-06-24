%{?nodejs_find_provides_and_requires}

Name:           nodejs-semver
Version:        7.3.2
Release:        1%{?dist}
Summary:        Semantic versioner for npm

License:        BSD
URL:            https://www.npmjs.com/package/semver
Source0:        https://github.com/npm/node-semver/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(tap)

%description
The semantic version comparison library for the Node.js package manager (npm).

%prep
%autosetup -n node-semver-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/semver
cp -pr bin package.json semver.js %{buildroot}%{nodejs_sitelib}/semver
mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/semver/bin/semver %{buildroot}%{_bindir}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%tap test/*.js

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/semver
%{_bindir}/semver

%changelog
* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.3.2-1
- Update to latest upstream release 7.3.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Tom Hughes <tom@compton.nu> - 5.3.0-1
- Update to 5.3.0 upstream release
- Switch to packaging from github to get tests

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Jared Smith <jsmith@fedoraproject.org> - 5.1.1-1
- Update to upstream 5.1.1 release
- Add tests to check section of spec file

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 5.1.0-3
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Stephen Gallagher <sgallagh@redhat.com> 5.1.0-1
- New upstream release 5.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Michal Srb <msrb@redhat.com> - 2.1.0-2
- Fix license tag (Resolves: rhbz#1057446)

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.0-1
- new upstream release 2.1.0

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.10-1
- new upstream release 2.0.10

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.7-1
- new upstream release 2.0.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-2
- add macro for EPEL6 dependency generation

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- new upstream release 1.1.3

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.2-1
- new upstream release 1.1.2

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-3
- guard Requires for F17 automatic depedency generation

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.13-1
- new upstream release 1.0.13

* Thu Nov 17 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.11-1
- new upstream release 1.0.11

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.10-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.9-1
- initial package
