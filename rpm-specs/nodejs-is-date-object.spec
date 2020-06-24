%{?nodejs_find_provides_and_requires}

Name:           nodejs-is-date-object
Version:        1.0.2
Release:        2%{?dist}
Summary:        Is this value a JS Date object?

License:        MIT
URL:            https://github.com/ljharb/is-date-object
Source0:        https://registry.npmjs.org/is-date-object/-/is-date-object-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
Is this value a JS Date object? This module works cross-realm/iframe, and
despite ES6 @@toStringTag.


%prep
%autosetup -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-date-object
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-date-object
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony --es-staging test


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-date-object


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tom Hughes <tom@compton.nu> - 1.0.2-1
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
