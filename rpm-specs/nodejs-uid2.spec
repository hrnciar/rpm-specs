%{?nodejs_find_provides_and_requires}

Name:           nodejs-uid2
Version:        0.0.3
Release:        13%{?dist}
Summary:        Node.js module to generate strong unique IDs

License:        MIT
URL:            https://github.com/Coreh/uid2
Source0:        http://registry.npmjs.org/uid2/-/uid2-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/uid2
cp -r package.json index.js %{buildroot}/%{nodejs_sitelib}/uid2
%nodejs_symlink_deps


%files
%doc LICENSE
%{nodejs_sitelib}/uid2


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.3-3
- add nodejs_find_provides_and_requires macro

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.3-2
- add ExclusiveArch logic for EL6

* Sat Aug 17 2013 Tom Hughes <tom@compton.nu> - 0.0.3-1
- Initial build of 0.0.3
