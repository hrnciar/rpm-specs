%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-types
Version:        3.0.0
Release:        2%{?dist}
Summary:        Query result type converters for node-postgres

License:        MIT
URL:            https://www.npmjs.com/package/pg-types
Source0:        https://github.com/brianc/node-pg-types/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(ap)
BuildRequires:  npm(pff)
BuildRequires:  npm(pg-int8)
BuildRequires:  npm(pg-numeric)
BuildRequires:  npm(postgres-array)
BuildRequires:  npm(postgres-bytea)
BuildRequires:  npm(postgres-date)
BuildRequires:  npm(postgres-interval)


%description
%{summary}.


%prep
%autosetup -n node-pg-types-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-types
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/pg-types
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
TZ=UTC %{nodejs_sitelib}/tape/bin/tape test/*.js


%files
%doc README.md
%{nodejs_sitelib}/pg-types


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Thu Apr 25 2019 Tom Hughes <tom@compton.nu> - 2.0.1-2
- Update npm(postgres-bytea) dependency

* Thu Apr  4 2019 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Thu Feb 21 2019 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Tom Hughes <tom@compton.nu> - 1.13.0-1
- Update to 1.13.0 upstream release

* Tue Aug 22 2017 Tom Hughes <tom@compton.nu> - 1.12.1-1
- Update to 1.12.1 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Tom Hughes <tom@compton.nu> - 1.12.0-1
- Update to 1.12.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 24 2016 Tom Hughes <tom@compton.nu> - 1.11.0-1
- Update to 1.11.0 upstreamrelease

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  9 2015 Tom Hughes <tom@compton.nu> - 1.10.0-2
- Enable tests

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 1.10.0-1
- Initial build of 1.10.0
