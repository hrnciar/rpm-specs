%{?nodejs_find_provides_and_requires}

Name:           nodejs-fstream-ignore
Version:        1.0.5
Release:        6%{?dist}
Summary:        A file stream object that can ignore files by globs
License:        BSD
URL:            https://www.npmjs.com/package/fstream-ignore
Source0:        https://github.com/npm/fstream-ignore/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch tests for changes in Node.js 8.x
Patch0:         nodejs-fstream-ignore-tests.patch

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(fstream)
BuildRequires:  npm(inherits) >= 2.0.0
BuildRequires:  npm(minimatch)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)

%description
%{summary}.


%prep
%autosetup -p 1 -n fstream-ignore-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-ignore
cp -pr ignore.js package.json %{buildroot}%{nodejs_sitelib}/fstream-ignore
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__tap test/*.js


%files
%doc README.md example
%license LICENSE
%{nodejs_sitelib}/fstream-ignore


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release
- Patch tests for changes in Node.js 8.x

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.0.3-2
- Remove npm(minimatch) fixdep

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-1
- new upstream release 0.0.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-2
- add macro for EPEL6 dependency generation

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- new upstream release 0.0.6

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-4
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-3
- add missing build section
- write better summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- clean up for submission

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package
