%{?nodejs_find_provides_and_requires}

Name:           nodejs-read
Version:        1.0.7
Release:        9%{?dist}
Summary:        An implementation of read(1) for node programs
License:        BSD
URL:            https://github.com/isaacs/read
Source0:        https://github.com/isaacs/read/archive/v%{version}/read-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(mute-stream)

%description
A method for reading user input from stdin in node.js.  Similar to readline's
"question()" method, but with a few more features.


%prep
%autosetup -p 1 -n read-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/read
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/read
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test/*.js


%files
%doc README.md example
%license LICENSE
%{nodejs_sitelib}/read


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.0.7-1
- Update to 1.0.7 upstream release
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-1
- new upstream release 1.0.5

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-8
- restrict to compatible arches

* Fri May 03 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.4-7
- Fix dist macro usage

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-6
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-4
- add missing build section

* Mon Jan 07 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-2
- fix description
- add no-op build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-1
- new upstream release 1.0.4
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-2
- guard Requires for F17 automatic depedency generation

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-1
- New upstream release 0.0.2

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package
