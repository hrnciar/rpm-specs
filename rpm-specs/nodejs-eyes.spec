%{?nodejs_find_provides_and_requires}

Name:           nodejs-eyes
Version:        0.1.8
Release:        14%{?dist}
Summary:        A customizable value inspector for Node.js

License:        MIT
URL:            https://www.npmjs.com/package/eyes
Source0:        https://registry.npmjs.org/eyes/-/eyes-%{version}.tgz
# https://github.com/cloudhead/eyes.js/pull/38
Patch0:         nodejs-eyes-node12.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
%{summary}


%prep
%autosetup -p 1 -n package


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/eyes
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/eyes
%nodejs_symlink_deps


%check
%__nodejs test/*-test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/eyes


%changelog
* Wed Feb  5 2020 Tom Hughes <tom@compton.nu> - 0.1.8-14
- Modernise spec file and patch tests for node 12.x support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.8-3
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.8-2
- rebuild for missing npm(eyes) provides on EL6

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.8-1
- initial package
