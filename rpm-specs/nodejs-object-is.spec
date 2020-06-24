%{?nodejs_find_provides_and_requires}

Name:           nodejs-object-is
Version:        1.1.2
Release:        1%{?dist}
Summary:        ES6-compliant shim for Object.is

License:        MIT
URL:            https://github.com/ljharb/object-is
Source0:        https://registry.npmjs.org/object-is/-/object-is-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(define-properties)
BuildRequires:  npm(es-abstract)


%description
ES6-compliant shim for Object.is - differentiates between -0 and +0.


%prep
%autosetup -n package
%nodejs_fixdep es-abstract "^1.17.3"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/object-is
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/object-is
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/object-is


%changelog
* Tue Apr 14 2020 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Tue Apr 14 2020 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Tue Apr 14 2020 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build of 1.0.1
