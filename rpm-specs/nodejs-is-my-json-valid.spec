Name:           nodejs-is-my-json-valid
Version:        2.12.4
Release:        10%{?dist}
Summary:        A JSONSchema validator that uses code generation to be extremely fast

License:        MIT
URL:            https://github.com/mafintosh/is-my-json-valid
Source0:        https://registry.npmjs.org/is-my-json-valid/-/is-my-json-valid-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(jsonpointer)
BuildRequires:  npm(generate-object-property)
BuildRequires:  npm(generate-function)
BuildRequires:  npm(xtend)


%description
%{summary}.


%prep
%autosetup -n package
%nodejs_fixdep end-of-stream ~1.x
%nodejs_fixdep jsonpointer
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-my-json-valid
cp -pr package.json formats.js index.js require.js %{buildroot}%{nodejs_sitelib}/is-my-json-valid
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
tape test/*.js

%files
%doc README.md example.js
%license LICENSE
%{nodejs_sitelib}/is-my-json-valid


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 2.12.4-8
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.12.4-1
- Update to 2.12.4

* Tue Nov 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.12.3-1
- Update to 2.12.3

* Wed Nov 11 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.12.2-1
- Initial packaging
