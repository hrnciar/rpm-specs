Name:           nodejs-should-http
Version:        0.0.4
Release:        10%{?dist}
Summary:        Http requests, response assertions for should.js

License:        MIT
URL:            https://github.com/shouldjs/http
Source0:        https://registry.npmjs.org/should-http/-/should-http-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should)


%description
%{summary}.


%prep
%setup -q -n package
sed -i 's/\r$//' History.md
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/should-http
cp -pr package.json index.js http.js %{buildroot}%{nodejs_sitelib}/should-http
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha test/**.test.js


%files
%doc Readme.md History.md
%license LICENSE
%{nodejs_sitelib}/should-http


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.0.4-2
- Fix line endings

* Thu Aug 27 2015 Tom Hughes <tom@compton.nu> - 0.0.4-1
- Initial build of 0.0.4
