Name:           nodejs-utilities
Version:        1.0.5
Release:        7%{?dist}
Summary:        A classic collection of JavaScript utilities

License:        ASL 2.0
URL:            https://github.com/mde/utilities
Source0:        https://github.com/mde/utilities/archive/v1.0.5/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(jake)

%description
%{summary}.


%prep
%autosetup -n utilities-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/utilities
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/utilities
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
jake test


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/utilities


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar  5 2017 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Tom Hughes <tom@compton.nu> - 1.0.4-2
- Enable tests

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Initial build of 1.0.4
