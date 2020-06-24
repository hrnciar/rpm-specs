%{?nodejs_find_provides_and_requires}

Name:           nodejs-make-arrow-function
Version:        1.2.0
Release:        1%{?dist}
Summary:        Function that returns an arbitrary arrow function

License:        MIT
URL:            https://github.com/ljharb/make-arrow-function
Source0:        https://registry.npmjs.org/make-arrow-function/-/make-arrow-function-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
Function that returns an arbitrary arrow function, or undefined
if arrow function syntax is unsupported.


%prep
%autosetup -p 1 -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/make-arrow-function
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/make-arrow-function
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/make-arrow-function


%changelog
* Tue Jan 28 2020 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 1.1.0-2
- Apply upstream patch for tests

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Initial build of 1.1.0
