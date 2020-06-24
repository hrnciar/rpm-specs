%{?nodejs_find_provides_and_requires}

Name:           nodejs-tar
Version:        6.0.2
Release:        1%{?dist}
Summary:        Tar for Node.js

License:        BSD
URL:            https://github.com/isaacs/node-tar
Source0:        https://registry.npmjs.org/tar/-/tar-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(block-stream)
BuildRequires:  npm(fstream)
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(inherits) >= 2.0.0
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)

%description
A Node.js module that supports reading and writing POSIX "tar" archives.

%prep
%autosetup -p 1 -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tar
%nodejs_fixdep glob

%check
%nodejs_symlink_deps --check
%__tap test/*.js

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/tar

%changelog
* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.0.2-1
- Update to latest upstream release 6.0.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Tom Hughes <tom@compton.nu> - 2.2.1-3
- Add test patch for node 5.x compatibility

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 2.2.1-1
- Update to 2.2.1 upstream release
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.18-1
- new upstream release 0.1.18

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-2
- add macro for EPEL6 dependency generation

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.16-1
- new upstream release 0.1.16

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-3
- add missing build section
- fix URL

* Sun Jan 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-2
- provide a better description and summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14
- clean up for submission

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package
