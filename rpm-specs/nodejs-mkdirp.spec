%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-mkdirp
Version:        0.5.1
Release:        11%{?dist}
Summary:        Recursive directory creation module for Node.js

License:        MIT
URL:            https://github.com/substack/node-mkdirp
Source0:        https://registry.npmjs.org/mkdirp/-/mkdirp-%{version}.tgz
Patch0:         nodejs-mkdirp-mockfs4.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(mock-fs) >= 4.0.0
%endif


%description
Creates directories recursively, like `mkdir -p`.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep minimist "^1.2.0"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mkdirp
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/mkdirp
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__tap test/*.js
%endif


%files
%doc readme.markdown examples
%license LICENSE
%{nodejs_sitelib}/mkdirp


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb  6 2017 Tom Hughes <tom@compton.nu> - 0.5.1-5
- Patch tests for changes in mock-fs 4.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Tom Hughes <tom@compton.nu> - 0.5.1-3
- Enable tests

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.5.1-2
- Update npm(minimist) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.5.1-1
- Update to 0.5.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-2
- add macro for EPEL6 dependency generation

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-1
- new upstream release 0.3.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.4-2
- add missing build section
- improve summary/description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.4-1
- new upstream release 0.3.4
- clean up for submission

* Wed May 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-1
- New upstream release 0.3.2

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.1-2
- guard Requires for F17 automatic depedency generation

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.1-1
- New upstream release 0.3.1

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Thu Dec 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-1
- initial package
