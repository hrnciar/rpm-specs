%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-native
Version:        3.0.0
Release:        5%{?dist}
Summary:        High performance native bindings between node.js and PostgreSQL

License:        MIT
URL:            https://www.npmjs.com/package/pg-native
Source0:        https://registry.npmjs.org/pg-native/-/pg-native-%{version}.tgz
# https://github.com/brianc/node-pg-native/pull/74
Patch0:         nodejs-pg-native-notify.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(async)
BuildRequires:  npm(concat-stream)
BuildRequires:  npm(libpq)
BuildRequires:  npm(lodash)
BuildRequires:  npm(okay)
BuildRequires:  npm(pg-types)
BuildRequires:  npm(semver)
BuildRequires:  postgresql-server
BuildRequires:  postgresql-test-rpm-macros


%description
High performance native bindings between node.js and PostgreSQL via
libpq with a simple API.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep --remove readable-stream
%nodejs_fixdep pg-types "^3.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-native
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/pg-native
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%postgresql_tests_run
PGPASSWORD=$(id -un) %{_bindir}/mocha -t 20000


%files
%doc README.md
%{nodejs_sitelib}/pg-native


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Tom Hughes <tom@compton.nu> - 3.0.0-4
- Fix npm(pg_types) dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Tom Hughes <tom@compton.nu> - 3.0.0-2
- Fix npm(pg-types) dependency

* Sat Feb  2 2019 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release
- Use new postgres test macro
- Fix failing test

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Initial build of 2.2.0
