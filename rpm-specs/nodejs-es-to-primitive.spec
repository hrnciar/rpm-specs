%{?nodejs_find_provides_and_requires}

Name:           nodejs-es-to-primitive
Version:        1.2.1
Release:        2%{?dist}
Summary:        ECMAScript “ToPrimitive” algorithm

License:        MIT
URL:            https://github.com/ljharb/es-to-primitive
Source0:        https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-%{version}.tgz
Patch0:         nodejs-es-to-primitive-fpn.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(foreach)
BuildRequires:  npm(is-callable)
BuildRequires:  npm(is-date-object)
BuildRequires:  npm(is-symbol)
BuildRequires:  npm(object-is)
BuildRequires:  npm(tape)


%description
ECMAScript “ToPrimitive” algorithm. Provides ES5 and ES6 versions. When
different versions of the spec conflict, the default export will be the
latest version of the abstract operation. Alternative versions will also
be available under an es5/es6/es7 exported property if you require a
specific version.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep is-symbol "^1.0.1"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/es-to-primitive
cp -pr package.json index.js es5.js es6.js es2015.js helpers %{buildroot}%{nodejs_sitelib}/es-to-primitive
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony --es-staging test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/es-to-primitive


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Tom Hughes <tom@compton.nu> - 1.2.0-5
- Include es2015.js in packaged files

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Tom Hughes <tom@compton.nu> - 1.2.0-3
- Re-enable tests

* Sun Sep 30 2018 Tom Hughes <tom@compton.nu> - 1.2.0-2
- Fix npm(is-symbol) dependency

* Sun Sep 30 2018 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Mon Dec 28 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Initial build of 1.0.0
