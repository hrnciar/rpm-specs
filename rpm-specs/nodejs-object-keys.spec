%{?nodejs_find_provides_and_requires}

Name:           nodejs-object-keys
Version:        1.1.1
Release:        3%{?dist}
Summary:        An Object.keys replacement, in case Object.keys is not available

License:        MIT
URL:            https://github.com/ljharb/object-keys
Source0:        https://github.com/ljharb/object-keys/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Patch out indexof as node doesn't need it and it is missing
# license text and has no clear upstream
Patch0:         nodejs-object-keys-indexof.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(is)
BuildRequires:  npm(tape)


%description
%{summary}.


%prep
%autosetup -p 1 -n object-keys-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/object-keys
cp -pr package.json index.js isArguments.js %{buildroot}%{nodejs_sitelib}/object-keys
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/object-keys


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr  7 2019 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Mon Feb 11 2019 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Tom Hughes <tom@compton.nu> - 1.0.12-1
- Update to 1.0.12 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul  6 2016 Tom Hughes <tom@compton.nu> - 1.0.11-1
- Update to 1.0.11 upstream release

* Tue Jul  5 2016 Tom Hughes <tom@compton.nu> - 1.0.10-1
- Update to 1.0.10 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.0.9-1
- Initial build of 1.0.9
