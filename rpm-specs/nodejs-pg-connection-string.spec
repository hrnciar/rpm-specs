%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-connection-string
Version:        2.2.3
Release:        1%{?dist}
Summary:        Functions for dealing with a PostgresSQL connection string

License:        MIT
URL:            https://www.npmjs.com/package/pg-connection-string
Source0:        https://github.com/brianc/node-postgres/archive/pg-connection-string@%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)


%description
%{summary}.


%prep
%autosetup -n node-postgres-pg-connection-string-%{version}
rm -rf packages/pg packages/pg-cursor packages/pg-protocol packages/pg-pool packages/pg-query-stream
cd packages/pg-connection-string
rm -rf node_modules


%build


%install
cd packages/pg-connection-string
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-connection-string
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-connection-string
%nodejs_symlink_deps


%check
cd packages/pg-connection-string
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/pg-connection-string


%changelog
* Sun May 17 2020 Tom Hughes <tom@compton.nu> - 2.2.3-1
- Update to 2.2.3 upstream release

* Sun Mar 22 2020 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jun 19 2019 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.1.3-1
- Initial build of 0.1.3
