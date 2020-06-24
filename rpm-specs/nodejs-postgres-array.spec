%{?nodejs_find_provides_and_requires}

Name:           nodejs-postgres-array
Version:        2.0.0
Release:        3%{?dist}
Summary:        Parse postgres array columns

License:        MIT
URL:            https://www.npmjs.com/package/postgres-array
Source0:        https://github.com/bendrucker/postgres-array/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(ap)


%description
%{summary}.


%prep
%autosetup -n postgres-array-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/postgres-array
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/postgres-array
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test.js


%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/postgres-array


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
