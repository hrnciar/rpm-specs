Name:           nodejs-generate-object-property
Version:        1.2.0
Release:        10%{?dist}
Summary:        Generate safe JS code that can used to reference a object property

License:        MIT
URL:            https://www.npmjs.org/package/generate-object-property
Source0:        https://registry.npmjs.org/generate-object-property/-/generate-object-property-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(is-property)
BuildRequires:  npm(tape)

%description
%{summary}.


%prep
%autosetup -n package
rm -rf node_

%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/generate-object-property
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/generate-object-property
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
tape test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/generate-object-property


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Tom Hughes <tom@compton.nu> - 1.2.0-8
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2.0-1
- Initial package
