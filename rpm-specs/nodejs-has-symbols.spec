%{?nodejs_find_provides_and_requires}

Name:           nodejs-has-symbols
Version:        1.0.1
Release:        2%{?dist}
Summary:        Determine if the JS environment has Symbol support

License:        MIT
URL:            https://www.npmjs.com/package/has-symbols
Source0:        https://registry.npmjs.org/has-symbols/-/has-symbols-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
Determine if the JS environment has Symbol support. Supports spec, or shams.


%prep
%autosetup -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/has-symbols
cp -pr package.json index.js shams.js %{buildroot}%{nodejs_sitelib}/has-symbols
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test
%__nodejs --harmony --es-staging test
%__nodejs test/shams/get-own-property-symbols.js
%__nodejs test/shams/core-js.js


%files
%doc CHANGELOG.md README.md
%license LICENSE
%{nodejs_sitelib}/has-symbols


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
