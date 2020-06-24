%{?nodejs_find_provides_and_requires}

Name:           nodejs-is-regex
Version:        1.1.0
Release:        1%{?dist}
Summary:        Is this value a JS regex?

License:        MIT
URL:            https://github.com/ljharb/is-regex
Source0:        https://registry.npmjs.org/is-regex/-/is-regex-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(foreach)


%description
Is this value a JS regex? This module works cross-realm/iframe, and
despite ES6 @@toStringTag.


%prep
%autosetup -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-regex
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-regex
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony --es-staging test


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-regex


%changelog
* Thu Jun  4 2020 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Update to 1.0.4 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Initial build of 1.0.3
