Name:           nodejs-should-equal
Version:        0.8.0
Release:        8%{?dist}
Summary:        Deep comparison of two instances for should.js

License:        MIT
URL:            https://github.com/shouldjs/equal
Source0:        https://registry.npmjs.org/should-equal/-/should-equal-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should-type)


%description
%{summary}.


%prep
%setup -q -n package
sed -i 's/\r$//' README.md
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/should-equal
cp -pr package.json index.js format.js %{buildroot}%{nodejs_sitelib}/should-equal
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --ui bdd test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/should-equal


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 22 2016 Tom Hughes <tom@compton.nu> - 0.8.0-1
- Update to 0.8.0 upstream release

* Thu May 19 2016 Tom Hughes <tom@compton.nu> - 0.7.3-1
- Update to 0.7.3 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 0.7.2-1
- Update to 0.7.2 upstream release

* Sun Jan 24 2016 Tom Hughes <tom@compton.nu> - 0.7.1-1
- Update to 0.7.1 upstream release

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 0.6.0-1
- Update to 0.6.0 upstream release

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.5.0-2
- Fix line endings

* Thu Aug 27 2015 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Initial build of 0.5.0
