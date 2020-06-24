%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-numeric
Version:        1.0.2
Release:        2%{?dist}
Summary:        A reader for the PostgreSQL binary format for numeric values, producing a string

License:        ISC
URL:            https://www.npmjs.com/package/pg-numeric
Source0:        https://github.com/charmander/pg-numeric/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
%{summary}.


%prep
%autosetup -n pg-numeric-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-numeric
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-numeric
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test/index.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/pg-numeric


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Initial build of 1.0.2.
