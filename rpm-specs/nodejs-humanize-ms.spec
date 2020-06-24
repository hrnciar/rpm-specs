%{?nodejs_find_provides_and_requires}

Name:           nodejs-humanize-ms
Version:        1.2.1
Release:        7%{?dist}
Summary:        Transform humanize time to ms

License:        MIT
URL:            https://www.npmjs.com/package/humanize-ms
Source0:        https://github.com/node-modules/humanize-ms/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
BuildRequires:  npm(ms)

%description
%{summary}.


%prep
%autosetup -n humanize-ms-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/humanize-ms
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/humanize-ms
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
make test


%files
%license LICENSE
%doc README.md History.md
%{nodejs_sitelib}/humanize-ms


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Mon Feb 20 2017 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Initial build of 1.2.0
