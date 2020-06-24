%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-pg
Version:        8.1.0
Release:        1%{?dist}
Summary:        PostgreSQL client for Node.js - pure JavaScript and libpq with the same API

# License text is included in README.md
License:        MIT
URL:            https://www.npmjs.com/package/pg
Source0:        https://github.com/brianc/node-postgres/archive/pg@%{version}/%{name}-%{version}.tar.gz
# Work around timeouts resolving names in koji
Patch0:         nodejs-pg-timeout.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(async)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(buffer-writer)
BuildRequires:  npm(co)
BuildRequires:  npm(js-string-escape)
BuildRequires:  npm(packet-reader)
BuildRequires:  npm(pgpass)
BuildRequires:  npm(pg-connection-string)
BuildRequires:  npm(pg-native)
BuildRequires:  npm(pg-pool)
#BuildRequires:  npm(pg-protocol)
BuildRequires:  npm(pg-types)
BuildRequires:  npm(semver)
BuildRequires:  postgresql-server
%endif


%description
PostgreSQL client for Node.js with pure JavaScript client and native
libpq bindings that share the same API.

Supported PostgreSQL features include:
 - parameterized queries
 - named statements with query plan caching
 - asynchronous notifications with LISTEN/NOTIFY
 - bulk import & export with COPY TO/COPY FROM
 - extensible js<->postgresql data-type coercion


%prep
%autosetup -p1 -n node-postgres-pg-%{version}
rm -rf packages/pg-*
cd packages/pg
%nodejs_fixdep pg-connection-string "^2.1.0"
%nodejs_fixdep --remove pg-protocol
%nodejs_fixdep pg-types "^3.0.0"
%nodejs_fixdep semver "^5.1.0"
%nodejs_fixdep --dev pg-native


%build


%install
cd packages/pg
mkdir -p %{buildroot}%{nodejs_sitelib}/pg
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/pg
%nodejs_symlink_deps


# https://github.com/brianc/node-postgres/wiki/Testing
%if 0%{?enable_tests}
%check
cd packages/pg
%nodejs_symlink_deps --check
# Remove test that needs pg-copy-streams
rm test/integration/gh-issues/699-tests.js
# Remove test that requires SSL support
rm test/integration/gh-issues/2085-tests.js
# Ensure consistent behaviour of timestamps
export TZ=UTC
# Start a postgres server
pg_ctl initdb -D pg_data -o "-A trust -E utf8"
pg_ctl start -w -D pg_data -l pg_log -o "-k $PWD -p 12345"
createdb -h $PWD -p 12345 test
# Run tests
PGHOST=localhost PGPORT=12345 PGDATABASE=test make test-unit
PGHOST=localhost PGPORT=12345 PGDATABASE=test make test-integration
PGHOST=localhost PGPORT=12345 PGDATABASE=test make test-native
PGHOST=localhost PGPORT=12345 PGDATABASE=test make test-missing-native
# Stop the postgres server
pg_ctl stop -D pg_data
%endif


%files
%doc README.md CHANGELOG.md SPONSORS.md
%license LICENSE
%{nodejs_sitelib}/pg


%changelog
* Fri May  8 2020 Tom Hughes <tom@compton.nu> - 8.1.0-1
- Update to 8.1.0 upstream release

* Wed Apr 22 2020 Tom Hughes <tom@compton.nu> - 8.0.3-1
- Update to 8.0.3 upstream release

* Thu Apr  9 2020 Tom Hughes <tom@compton.nu> - 8.0.2-1
- Update to 8.0.2 upstream release

* Thu Apr  9 2020 Tom Hughes <tom@compton.nu> - 8.0.1-1
- Update to 8.0.1 upstream release

* Mon Mar 30 2020 Tom Hughes <tom@compton.nu> - 8.0.0-1
- Update to 8.0.0 upstream release

* Thu Feb 20 2020 Tom Hughes <tom@compton.nu> - 7.18.2-1
- Update to 7.18.2 upstream release

* Thu Jan 30 2020 Tom Hughes <tom@compton.nu> - 7.18.1-1
- Update to 7.18.1 upstream release

* Thu Jan 30 2020 Tom Hughes <tom@compton.nu> - 7.18.0-1
- Update to 7.18.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Tom Hughes <tom@compton.nu> - 7.17.1-1
- Update to 7.17.1 upstream release

* Thu Jan  9 2020 Tom Hughes <tom@compton.nu> - 7.17.0-1
- Update to 7.17.0 upstream release

* Sun Dec 29 2019 Tom Hughes <tom@compton.nu> - 7.16.1-1
- Update to 7.16.1 upstream release

* Wed Dec 18 2019 Tom Hughes <tom@compton.nu> - 7.15.1-1
- Update to 7.15.1 upstream release

* Wed Dec 11 2019 Tom Hughes <tom@compton.nu> - 7.13.0-1
- Update to 7.13.0 upstream release

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 7.12.1-1
- Update to 7.12.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Tom Hughes <tom@compton.nu> - 7.11.0-3
- Update npm(pg-types) dependency

* Wed Jun 19 2019 Tom Hughes <tom@compton.nu> - 7.11.0-2
- Update npm(pg-connection-string) dependency

* Wed May 15 2019 Tom Hughes <tom@compton.nu> - 7.11.0-1
- Update to 7.11.0 upstream release

* Tue Apr 16 2019 Tom Hughes <tom@compton.nu> - 7.10.0-1
- Update to 7.10.0 upstream release

* Fri Mar  8 2019 Tom Hughes <tom@compton.nu> - 7.8.2-1
- Update to 7.8.2 upstream release

* Fri Feb 22 2019 Tom Hughes <tom@compton.nu> - 7.8.1-2
- Fix npm(pg-types) dependency

* Thu Feb 21 2019 Tom Hughes <tom@compton.nu> - 7.8.1-1
- Update to 7.8.1 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Tom Hughes <tom@compton.nu> - 7.4.3-1
- Update to 7.4.3 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Tom Hughes <tom@compton.nu> - 7.4.1-1
- Update to 7.4.1 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  1 2016 Tom Hughes <tom@compton.nu> - 4.5.4-3
- Update npm(pgpass) dependency

* Mon Jun  6 2016 Tom Hughes <tom@compton.nu> - 4.5.4-2
- Fix npm(pgpass) dependency

* Wed Apr 27 2016 Tom Hughes <tom@compton.nu> - 4.5.4-1
- Update to 4.5.4 upstream release

* Thu Mar 31 2016 Tom Hughes <tom@compton.nu> - 4.5.2-1
- Update to 4.5.2 upstream release

* Sat Feb 27 2016 Tom Hughes <tom@compton.nu> - 4.5.1-1
- Update to 4.5.1 upstream release

* Tue Feb 16 2016 Tom Hughes <tom@compton.nu> - 4.4.6-1
- Update to 4.4.6 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 4.4.4-1
- Update to 4.4.4 upstream release

* Thu Dec 10 2015 Tom Hughes <tom@compton.nu> - 4.4.3-3
- Bump npm(semver) dependency for nodejs 4.2

* Thu Dec 10 2015 Tom Hughes <tom@compton.nu> - 4.4.3-2
- Correct npm(semver) dependency

* Wed Dec  9 2015 Tom Hughes <tom@compton.nu> - 4.4.3-1
- Update to 4.4.3 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.3-4
- rebuild for icu-53 (via v8)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.12.3-2
- restrict to compatible arches

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.12.3-1
- initial package
