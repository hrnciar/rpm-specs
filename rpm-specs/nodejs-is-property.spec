Name:           nodejs-is-property
Version:        1.0.2
Release:        10%{?dist}
Summary:        Tests if a json property can be safely accessed using the .syntax

License:        MIT
URL:            https://github.com/mikolalysenko/is-property
Source0:        https://registry.npmjs.org/is-property/-/is-property-%{version}.tgz
Source1:        https://raw.githubusercontent.com/mikolalysenko/is-property/master/test/test.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(tape)

%description
%{summary}.


%prep
%autosetup -n package
rm -rf node_modules
mkdir test
cp -p %{SOURCE1} ./test

%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-property
cp -pr package.json is-property.js %{buildroot}%{nodejs_sitelib}/is-property
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
tap test/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/is-property


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Tom Hughes <tom@compton.nu> - 1.0.2-8
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.2-1
- Initial packaging

