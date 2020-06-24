%{?nodejs_find_provides_and_requires}

Name:           nodejs-npm-user-validate
Version:        0.1.2
Release:        9%{?dist}
Summary:        Username, password, and e-mail validation for the npm registry

License:        BSD
URL:            https://github.com/robertkowalski/npm-user-validate
Source0:        http://registry.npmjs.org/npm-user-validate/-/npm-user-validate-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)

%description
This library validates usernames, passwords, and e-mail addresses to the
standards required by the npm registry.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-user-validate
cp -pr package.json npm-user-validate.js %{buildroot}%{nodejs_sitelib}/npm-user-validate
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/npm-user-validate


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 0.1.2-1
- Update to 0.1.2 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- new upstream release 0.0.3

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-3
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-2
- fix License tag

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-1
- initial package
