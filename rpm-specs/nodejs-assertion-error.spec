Name:           nodejs-assertion-error
Version:        1.1.0
Release:        6%{?dist}
Summary:        Error constructor for test and validation frameworks

License:        MIT
URL:            https://github.com/chaijs/assertion-error
Source0:        https://github.com/chaijs/assertion-error/archive/%{version}/assertion-error-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
Error constructor for test and validation frameworks that implements
standardized AssertionError specification.


%prep
%autosetup -n assertion-error-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/assertion-error
cp -r package.json index.js %{buildroot}/%{nodejs_sitelib}/assertion-error
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/index.js


%files
%doc README.md History.md
%{nodejs_sitelib}/assertion-error


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  8 2018 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release
- Switch to using github as source so we get tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
