%{?nodejs_find_provides_and_requires}

Name:           nodejs-rimraf
Version:        3.0.2
Release:        1%{?dist}
Summary:        A deep deletion module for node.js

License:        MIT
URL:            https://github.com/isaacs/rimraf
Source0:        https://github.com/isaacs/rimraf/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(glob)
BuildRequires:  npm(mkdirp)

%description
%summary (like `rm -rf`).

%prep
%autosetup -p 1 -n rimraf-%{version}
%nodejs_fixdep glob

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rimraf
cp -pr package.json rimraf.js bin.js %{buildroot}%{nodejs_sitelib}/rimraf
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%tap test/basic.js

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/rimraf

%changelog
* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.2-1
- Update to latest upstream release 3.0.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Jared Smith <jsmith@fedoraproject.org> - 2.6.1-1
- Update to upstream 2.6.1 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org> - 2.5.4-1
- Update to upstream 2.5.4 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 2.5.0-1
- Update to 2.5.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.2-1
- new upstream release 2.2.2

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-1
- new upstream release 2.2.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-2
- add macro for EPEL6 dependency generation

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-1
- new upstream release 2.1.4

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-2
- guard Requires for F17 automatic depedency generation

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-1
- new upstream release 2.0.1

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.9-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- initial package
