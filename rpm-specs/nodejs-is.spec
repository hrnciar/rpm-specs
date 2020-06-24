Name:           nodejs-is
Version:        3.2.1
Release:        7%{?dist}
Summary:        The definitive JavaScript type testing library

License:        MIT
URL:            https://github.com/enricomarino/is
Source0:        https://registry.npmjs.org/is/-/is-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(foreach)
BuildRequires:  npm(make-generator-function)
BuildRequires:  npm(tape)


%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{nodejs_sitelib}/is


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Tom Hughes <tom@compton.nu> - 3.2.1-1
- Update to 3.2.1 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 28 2016 Tom Hughes <tom@compton.nu> - 3.2.0-1
- Update to 3.2.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Initial build of 3.1.0
