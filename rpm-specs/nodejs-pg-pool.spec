%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-pg-pool
Version:        3.2.1
Release:        1%{?dist}
Summary:        A connection pool for node-postgres

License:        MIT
URL:            https://www.npmjs.com/package/pg-pool
Source0:        https://registry.npmjs.org/pg-pool/-/pg-pool-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(co)
BuildRequires:  npm(expect.js)
BuildRequires:  npm(lodash)
BuildRequires:  npm(pg)
BuildRequires:  npm(pg-cursor)
BuildRequires:  postgresql-server
%endif


%description
%{summary}.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep --dev pg
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-pool
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-pool
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
# Start a postgres server
pg_ctl initdb -D pg_data -o "-A trust -E utf8"
pg_ctl start -w -D pg_data -l pg_log -o "-k $PWD -p 12345"
createdb -h $PWD -p 12345 test
# Run tests
PGPORT=12345 PGDATABASE=test %{_bindir}/mocha
# Stop the postgres server
pg_ctl stop -D pg_data
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/pg-pool


%changelog
* Sun May 17 2020 Tom Hughes <tom@compton.nu> - 3.2.1-1
- Update to 3.2.1 upstream release

* Fri May  8 2020 Tom Hughes <tom@compton.nu> - 3.2.0-1
- Update to 3.2.0 upstream release

* Wed Apr 22 2020 Tom Hughes <tom@compton.nu> - 3.1.1-2
- Re-enable tests

* Wed Apr 22 2020 Tom Hughes <tom@compton.nu> - 3.1.1-1
- Update to 3.1.1 upstream release

* Thu Apr  9 2020 Tom Hughes <tom@compton.nu> - 3.1.0-1
- Update to 3.1.0 upstream release

* Mon Mar 30 2020 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Thu Jan 30 2020 Tom Hughes <tom@compton.nu> - 2.0.10-1
- Update to 2.0.10 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Tom Hughes <tom@compton.nu> - 2.0.9-1
- Update to 2.0.9 upstream release

* Thu Dec 19 2019 Tom Hughes <tom@compton.nu> - 2.0.8-1
- Update to 2.0.8 upstream release

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 2.0.7-1
- Update to 2.0.7 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Tom Hughes <tom@compton.nu> - 2.0.6-1
- Update to 2.0.6 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Initial build of 2.0.3.
