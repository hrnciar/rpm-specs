Name:           nodejs-xmlbuilder
Version:        4.2.1
Release:        10%{?dist}
Summary:        An XML builder for Node.js

License:        MIT
URL:            https://github.com/oozcitak/xmlbuilder-js
Source0:        https://github.com/oozcitak/xmlbuilder-js/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(coffee-script)
BuildRequires:  npm(mocha)
BuildRequires:  npm(lodash)

%description
An XMLBuilder for Node.js similar to java-xmlbuilder.


%prep
%autosetup -p 1 -n xmlbuilder-js-%{version}
sed -i -e "/coffee-coverage/d" test/mocha.opts 
rm -rf node_modules


%build
%{nodejs_sitelib}/coffee-script/bin/coffee -co lib/ src/*.coffee


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/xmlbuilder
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/xmlbuilder
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/xmlbuilder


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 4.2.1-9
- Rebuild against lodash 4.x

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Tom Hughes <tom@compton.nu> - 4.2.1-1
- Update to 4.2.1 upstream release

* Fri Dec 18 2015 Tom Hughes <tom@compton.nu> - 4.2.0-1
- Update to 4.2.0 upstream release

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Update to 4.1.0 upstream release

* Sat Nov 14 2015 Tom Hughes <tom@compton.nu> - 2.4.6-3
- Add upstream patch for new coffee-script

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Tom Hughes <tom@compton.nu> - 2.4.6-1
- Update to 2.4.6 upstream release

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 2.4.5-1
- Update to 2.4.5 upstream release

* Wed Sep 10 2014 Tom Hughes <tom@compton.nu> - 2.4.4-1
- Update to 2.4.4 upstream release

* Fri Aug 15 2014 Tom Hughes <tom@compton.nu> - 2.4.3-1
- Update to 2.4.3 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tom Hughes <tom@compton.nu> - 2.2.1-2
- Remove underscore dependency

* Thu Apr 24 2014 Tom Hughes <tom@compton.nu> - 2.2.1-1
- Update to 2.2.1 upstream release

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-3
- fix version of npm(underscore) dependency

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.0-2
- fix underscore for 1.5.1

* Wed Jan  1 2014 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Sun Dec 29 2013 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Sat Dec 14 2013 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Tue Dec 10 2013 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Mon Dec  2 2013 Tom Hughes <tom@compton.nu> - 1.0.2-2
- Remove last traces of enable_tests macro

* Thu Nov 28 2013 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Initial build of 1.0.2
