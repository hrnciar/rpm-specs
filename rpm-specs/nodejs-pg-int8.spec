%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-int8
Version:        1.0.1
Release:        6%{?dist}
Summary:        64-bit big-endian signed integer-to-string conversion for pg

License:        ISC
URL:            https://www.npmjs.com/package/pg-int8
Source0:        https://github.com/charmander/pg-int8/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)


%description
64-bit big-endian signed integer-to-string conversion designed for pg.


%prep
%autosetup -n pg-int8-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-int8
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-int8
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/pg-int8


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build of 1.0.1.
