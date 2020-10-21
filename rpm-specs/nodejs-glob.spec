%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-glob
Version:        6.0.4
Release:        11%{?dist}
Summary:        A little globber for Node.js

License:        BSD
URL:            https://github.com/isaacs/node-glob
Source0:        https://github.com/isaacs/node-glob/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix tests to work with older version of tap
Patch0:         nodejs-glob-tap.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(inflight)
BuildRequires:  npm(path-is-absolute)
BuildRequires:  npm(rimraf)
%endif


%description
This is a glob implementation in pure JavaScript. It uses the minimatch library
to do its matching.


%prep
%autosetup -p 1 -n node-glob-%{version}
%nodejs_fixdep once "^1.1.1"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/glob
cp -pr package.json glob.js sync.js common.js \
  %{buildroot}%{nodejs_sitelib}/glob
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md examples
%license LICENSE
%{nodejs_sitelib}/glob


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  9 2016 Tom Hughes <tom@compton.nu> - 6.0.4-1
- Update to 6.0.4 upstream release
- Enable tests

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 6.0.3-1
- Update to 6.0.3 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.2.6-1
- new upstream release 3.2.6

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.2.3-1
- new upstream release 3.2.3

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.2.1-1
- new upstream release 3.2.1

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.21-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.21-2
- add macro for EPEL6 dependency generation

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.21-1
- new upstream release 3.1.21

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.20-1
- new upstream release 3.1.20

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.14-2
- add missing build section
- adjust summary/description slightly

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.14-1
- new upstream release 3.1.14
- clean up for submission

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.9-1
- new upstream release 3.1.9

* Fri Mar 16 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 3.1.6-1
- initial package
