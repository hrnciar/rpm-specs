%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-pg-cursor
Version:        2.2.1
Release:        1%{?dist}
Summary:        Use a PostgreSQL result cursor from node with an easy to use API

License:        MIT
URL:            https://www.npmjs.com/package/pg-cursor
Source0:        https://registry.npmjs.org/pg-cursor/-/pg-cursor-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(pg)
BuildRequires:  postgresql-server
%endif


%description
%{summary}.


%prep
%autosetup -p1 -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-cursor
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-cursor
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
%{nodejs_sitelib}/pg-cursor


%changelog
* Sun May 17 2020 Tom Hughes <tom@compton.nu> - 2.2.1-1
- Update to 2.2.1 upstream release

* Wed May 13 2020 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Fri May  8 2020 Tom Hughes <tom@compton.nu> - 2.1.11-1
- Update to 2.1.11 upstream release

* Wed Apr 22 2020 Tom Hughes <tom@compton.nu> - 2.1.10-1
- Update to 2.1.10 upstream release

* Thu Apr  9 2020 Tom Hughes <tom@compton.nu> - 2.1.9-1
- Update to 2.1.9 upstream release

* Thu Apr  9 2020 Tom Hughes <tom@compton.nu> - 2.1.8-1
- Update to 2.1.8 upstream release

* Mon Mar 30 2020 Tom Hughes <tom@compton.nu> - 2.1.7-1
- Update to 2.1.7 upstream release

* Thu Feb 20 2020 Tom Hughes <tom@compton.nu> - 2.1.6-1
- Update to 2.1.6 upstream release

* Thu Jan 30 2020 Tom Hughes <tom@compton.nu> - 2.1.5-1
- Update to 2.1.5 upstream release

* Thu Jan 30 2020 Tom Hughes <tom@compton.nu> - 2.1.4-1
- Update to 2.1.4 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Tom Hughes <tom@compton.nu> - 2.1.3-1
- Update to 2.1.3 upstream release

* Thu Jan  9 2020 Tom Hughes <tom@compton.nu> - 2.1.2-1
- Update to 2.1.2 upstream release

* Sun Dec 29 2019 Tom Hughes <tom@compton.nu> - 2.1.1-1
- Update to 2.1.1 upstream release

* Wed Dec 18 2019 Tom Hughes <tom@compton.nu> - 2.0.2-1
- Update to 2.0.2 upstream release

* Wed Oct 30 2019 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Initial build of 1.3.0.
