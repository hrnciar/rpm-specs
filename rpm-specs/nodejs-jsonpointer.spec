Name:           nodejs-jsonpointer
Version:        3.0.1
Release:        3%{?dist}
Summary:        Simple JSON Addressing

License:        MIT
URL:            https://www.npmjs.com/package/jsonpointer
Source0:        https://registry.npmjs.org/jsonpointer/-/jsonpointer-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -qn package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jsonpointer
cp -pr package.json jsonpointer.js %{buildroot}%{nodejs_sitelib}/jsonpointer
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test.js


%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/jsonpointer


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Tom Hughes <tom@compton.nu> - 3.0.1-1
- Update to 3.0.1 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.0-1
- Initial package
