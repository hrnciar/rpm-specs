%{?nodejs_find_provides_and_requires}

Name:           nodejs-postgres-date
Version:        1.0.5
Release:        1%{?dist}
Summary:        Postgres date column parser

License:        MIT
URL:            https://www.npmjs.com/package/postgres-date
Source0:        https://github.com/bendrucker/postgres-date/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
%{summary}.


%prep
%autosetup -n postgres-date-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/postgres-date
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/postgres-date
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test.js


%files
%doc readme.md
%license license
%{nodejs_sitelib}/postgres-date


%changelog
* Mon Apr 13 2020 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr  3 2019 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Update to 1.0.4 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul  7 2016 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release

* Fri May 20 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
