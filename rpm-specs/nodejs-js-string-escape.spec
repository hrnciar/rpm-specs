%{?nodejs_find_provides_and_requires}

Name:           nodejs-js-string-escape
Version:        1.0.1
Release:        5%{?dist}
Summary:        Escape any string to be a valid JavaScript string literal

License:        MIT
URL:            https://www.npmjs.com/package/js-string-escape
Source0:        https://github.com/joliss/js-string-escape/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)


%description
Escape any string to be a valid JavaScript string literal
between double quotes or single quotes.


%prep
%autosetup -n js-string-escape-%{version}
sed -i -e 's|./../node_modules/punycode/punycode.js|punycode|' test/test.js
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/js-string-escape
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/js-string-escape
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/js-string-escape


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Initial build of 1.0.1.
