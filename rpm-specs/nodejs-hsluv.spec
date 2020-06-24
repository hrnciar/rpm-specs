%{?nodejs_find_provides_and_requires}

Name:           nodejs-hsluv
Version:        0.0.1
Release:        6%{?dist}
Summary:        Human-friendly HSL

License:        MIT
URL:            https://www.npmjs.com/package/hsluv
Source0:        https://registry.npmjs.org/hsluv/-/hsluv-%{version}.tgz
Source1:        https://raw.githubusercontent.com/hsluv/hsluv/v%{version}/LICENSE
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
%{summary}.


%prep
%autosetup -n package
cp %{SOURCE1} .
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/hsluv
cp -pr package.json hsluv.js %{buildroot}%{nodejs_sitelib}/hsluv
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/hsluv


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Tom Hughes <tom@compton.nu> - 0.0.1-1
- Initial build of 0.0.1
