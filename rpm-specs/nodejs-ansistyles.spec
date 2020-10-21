%{?nodejs_find_provides_and_requires}

Name:           nodejs-ansistyles
Version:        0.1.3
Release:        17%{?dist}
Summary:        Functions that surround a string with ansistyle codes so it prints in style
License:        MIT
Url:            https://github.com/sindresorhus/ansi-styles
Source0:        http://registry.npmjs.org/ansistyles/-/ansistyles-0.1.3.tgz
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-tap

%description
Functions that surround a string with ansistyle codes so it prints in style.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/ansistyles
cp -pr ansistyles.js package.json %{buildroot}%{nodejs_sitelib}/ansistyles

%nodejs_symlink_deps

%check
tap test/

%files
%{nodejs_sitelib}/ansistyles

%doc LICENSE README.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-6
- restrict to compatible arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-4
- add BuildArch noarch

* Tue Mar 11 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-3
- remove dot at the end of summary

* Mon Mar 10 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-2
- add nodejs-tap to build requirements
- remove whitespace

* Mon Mar 10 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-1
- Initial build

