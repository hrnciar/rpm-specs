Name:           nodejs-xml2js
Version:        0.4.22
Release:        3%{?dist}
Summary:        Simple XML to JavaScript object converter

License:        MIT
URL:            https://github.com/Leonidas-from-XIV/node-xml2js
Source0:        https://github.com/Leonidas-from-XIV/node-xml2js/archive/%{version}/%{name}-%{version}.tar.gz
# Patch out use of shim that is not needed by modern Node.js
Patch0:         nodejs-xml2js-promisify.patch

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(zap)
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(sax)
BuildRequires:  npm(diff)
BuildRequires:  npm(xmlbuilder) >= 2.4.6

%description
Ever had the urge to parse XML? And wanted to access the data in
some sane, easy way? Don't want to compile a C parser, for whatever
reason? Then xml2js is what you're looking for!


%prep
%autosetup -p 1 -n node-xml2js-%{version}
%nodejs_fixdep xmlbuilder "^4.2.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/xml2js
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/xml2js
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/zap/bin/zap


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/xml2js


%changelog
* Mon May 11 2020 Tom Hughes <tom@compton.nu> - 0.4.22-3
- Remove npm(sax) dependency fix

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep  3 2019 Tom Hughes <tom@compton.nu> - 0.4.22-1
- Update to 0.4.22 upstream release

* Mon Sep  2 2019 Tom Hughes <tom@compton.nu> - 0.4.21-1
- Update to 0.4.21 upstream release

* Sun Sep  1 2019 Tom Hughes <tom@compton.nu> - 0.4.20-1
- Update to 0.4.20 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Tom Hughes <tom@compton.nu> - 0.4.19-1
- Update to 0.4.19 upstream release

* Tue Aug 15 2017 Tom Hughes <tom@compton.nu> - 0.4.18-1
- Update to 0.4.18 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul  6 2016 Tom Hughes <tom@compton.nu> - 0.4.17-1
- Update to 0.4.17 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Tom Hughes <tom@compton.nu> - 0.4.16-1
- Update to 0.4.16 upstream release

* Sat Oct 31 2015 Tom Hughes <tom@compton.nu> - 0.4.15-1
- Update to 0.4.15 upstream release

* Thu Oct 15 2015 Tom Hughes <tom@compton.nu> - 0.4.13-1
- Update to 0.4.13 upstream release

* Sun Sep  6 2015 Tom Hughes <tom@compton.nu> - 0.4.12-1
- Update to 0.4.12 upstream release

* Tue Sep  1 2015 Tom Hughes <tom@compton.nu> - 0.4.11-1
- Update to 0.4.11 upstream release

* Sun Aug  9 2015 Tom Hughes <tom@compton.nu> - 0.4.10-1
- Update to 0.4.10 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Tom Hughes <tom@compton.nu> - 0.4.9-1
- Update to 0.4.9 upstream release
- Switch to %%license for the license file

* Sat Apr 18 2015 Tom Hughes <tom@compton.nu> - 0.4.8-1
- Update to 0.4.8 upstream release

* Sun Mar 15 2015 Tom Hughes <tom@compton.nu> - 0.4.6-1
- Update to 0.4.6 upstream release

* Wed Feb 11 2015 Tom Hughes <tom@compton.nu> - 0.4.5-2
- Patch test result for xmlbuilder 2.4.6 support

* Wed Feb 11 2015 Tom Hughes <tom@compton.nu> - 0.4.5-1
- Update to 0.4.5 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Tom Hughes <tom@compton.nu> - 0.4.4-1
- Update to 0.4.4 upstream release

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.4.3-1
- Update to 0.4.3 upstream release

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.2-2
- fix version of npm(sax) dependency

* Sun Mar 30 2014 Tom Hughes <tom@compton.nu> - 0.4.2-1
- Update to 0.4.2 upstream release
- Switch to using github as source so we get tests

* Fri Jan  3 2014 Tom Hughes <tom@compton.nu> - 0.4.1-1
- Update to 0.4.1 upstream release

* Mon Nov 25 2013 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Tom Hughes <tom@compton.nu> - 0.2.8-1
- Update to 0.2.8 upstream release

* Tue May  7 2013 Tom Hughes <tom@compton.nu> - 0.2.7-1
- Update to 0.2.7 upstream release

* Wed Mar  6 2013 Tom Hughes <tom@compton.nu> - 0.2.6-2
- Update sax dependency

* Mon Mar  4 2013 Tom Hughes <tom@compton.nu> - 0.2.6-1
- Update to 0.2.6 release
- Add tests, which are now separate
- BuildRequire coffee-script and sax for tests

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.2.4-1
- Initial build of 0.2.4
