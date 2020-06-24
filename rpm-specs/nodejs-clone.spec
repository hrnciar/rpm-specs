Name:           nodejs-clone
Version:        1.0.4
Release:        4%{?dist}
Summary:        Deep cloning of objects and arrays

License:        MIT
URL:            https://www.npmjs.com/package/clone
Source0:        https://github.com/pvorb/clone/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  nodeunit


%description
Offers foolproof deep cloning of variables in JavaScript.

%prep
%autosetup -n clone-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/clone
cp -pr package.json clone.js %{buildroot}%{nodejs_sitelib}/clone

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
nodeunit test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/clone


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Tom Hughes <tom@compton.nu> - 1.0.4-2
- Install files to correct directory

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Update to 1.0.4 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.2-1
- Update to new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.2.0-1
- updated to latest upstream

* Sat Dec  6 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.1.18-2
- Added LICENSE to %%files
- Added rm -rf node_modules to %%prep
- Capitalized summary
- Removed Group tag

* Fri Nov 21 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.1.18-1
- Initial package
