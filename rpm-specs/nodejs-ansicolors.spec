%{?nodejs_find_provides_and_requires}

Name:           nodejs-ansicolors
Version:        0.3.2
Release:        14%{?dist}
Summary:        Functions that surround a string with ansi color codes so it prints in color
License:        MIT
Url:            http://registry.npmjs.org/ansicolors/-/ansicolors-0.3.2.tgz
Source0:        http://registry.npmjs.org/ansicolors/-/ansicolors-0.3.2.tgz
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildRequires:  nodejs-devel

%description
Functions that surround a string with ansi color codes so it prints in color.
%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/ansicolors
cp -pr ansicolors.js package.json %{buildroot}%{nodejs_sitelib}/ansicolors

%nodejs_symlink_deps
%check 

node test/ansicolors.js

%files
%{nodejs_sitelib}/ansicolors

%doc LICENSE README.md

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-4
- restrict to compatible arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-2
- remove buildroot
- fix typo in summary

* Wed Mar 12 2014 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-1
- Initial package build

