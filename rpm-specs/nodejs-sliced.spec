%{?nodejs_find_provides_and_requires}

Name:           nodejs-sliced
Version:        1.0.1
Release:        5%{?dist}
Summary:        A faster alternative to [].slice.call(arguments)

License:        MIT
URL:            https://www.npmjs.com/package/sliced
Source0:        https://github.com/aheckmann/sliced/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)


%description
%{summary}.


%prep
%autosetup -n sliced-%{version}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sliced
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/sliced
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/sliced


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar  8 2018 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build of 1.0.1.
