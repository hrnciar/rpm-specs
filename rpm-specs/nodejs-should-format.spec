Name:           nodejs-should-format
Version:        0.3.2
Release:        10%{?dist}
Summary:        Formatting of objects for should.js

License:        MIT
URL:            https://github.com/shouldjs/format
Source0:        https://registry.npmjs.org/should-format/-/should-format-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should-type)

Patch0001: 0001-Fix-tests-for-Node.js-6.5.patch

%description
%{summary}.


%prep
%setup -q -n package
%patch0001 -p1
sed -i 's/\r$//' README.md
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/should-format
cp -pr package.json index.js util.js %{buildroot}%{nodejs_sitelib}/should-format
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --ui bdd tests/test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/should-format


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.3.2-3
- Fix tests for Node.js 6.5+

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 0.3.2-1
- Update to 0.3.2 upstream release

* Tue Oct 20 2015 Tom Hughes <tom@compton.nu> - 0.3.1-1
- Update to 0.3.1 upstream release

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.3.0-2
- FIx line endings

* Thu Aug 27 2015 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Initial build of 0.3.0
