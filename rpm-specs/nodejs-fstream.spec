%{?nodejs_find_provides_and_requires}

Name:           nodejs-fstream
Version:        1.0.12
Release:        1%{?dist}
Summary:        Advanced file system stream objects for Node.js

License:        BSD
URL:            https://github.com/isaacs/fstream
Source0:        https://registry.npmjs.org/fstream/-/fstream-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(inherits)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)
BuildRequires:	npm(tap)

%description
Provides advanced file system stream objects for Node.js.  These objects are
like FS streams, but with stat on them, and support directories and
symbolic links, as well as normal files.  Also, you can use them to set
the stats on a file, even if you don't change its contents, or to create
a symlink, etc.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fstream
cp -pr package.json fstream.js lib %{buildroot}%{nodejs_sitelib}/fstream
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%{_bindir}/tap examples/*.js

%files
%doc README.md examples
%license LICENSE
%{nodejs_sitelib}/fstream

%changelog
* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.12-1
- Update to latest upstream release 1.0.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.11-1
- Update to upstream 1.0.11 release
- Add tests

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.0.8-2
- Remove npm(mkdirp) fixdep

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 1.0.8-1
- Update to 1.0.8 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.24-1
- new upstream release 0.1.24

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.23-1
- new upstream release 0.1.23

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-2
- add macro for EPEL6 dependency generation

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-1
- new upstream release 0.1.22

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-3
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-2
- add missing build section
- fix summary/description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.21-1
- new upstream release 0.1.21
- clean up for submission

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.18-1
- New upstream release 0.1.18

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- new upstream release 0.1.12

* Sat Jan 21 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package
