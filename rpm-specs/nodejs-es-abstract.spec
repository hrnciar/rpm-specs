%{?nodejs_find_provides_and_requires}

Name:           nodejs-es-abstract
Version:        1.17.3
Release:        2%{?dist}
Summary:        ECMAScript spec abstract operations

License:        MIT
URL:            https://github.com/ljharb/es-abstract
Source0:        https://github.com/ljharb/es-abstract/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch out use of shims that modern Node.js already provides
Patch0:         nodejs-es-abstract-shims.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(es-to-primitive)
BuildRequires:  npm(foreach)
BuildRequires:  npm(function-bind)
BuildRequires:  npm(is-callable)
BuildRequires:  npm(is-regex)
BuildRequires:  npm(make-arrow-function)
BuildRequires:  npm(object.assign)
BuildRequires:  npm(object-is)
BuildRequires:  npm(tape)


%description
ECMAScript spec abstract operations. When different versions of the
spec conflict, the default export will be the latest version of the
abstract operation. All abstract operations will also be available
under an es5/es6/es7 exported property if you require a specific version.


%prep
%autosetup -p 1 -n es-abstract-%{version}
%nodejs_fixdep object-inspect "^1.6.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/es-abstract
cp -pr package.json *.js 5 2015 2016 2017 2018 2019 helpers %{buildroot}%{nodejs_sitelib}/es-abstract
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/index.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/es-abstract


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Tom Hughes <tom@compton.nu> - 1.17.3-1
- Update to 1.17.3 upstream release

* Wed Jan 15 2020 Tom Hughes <tom@compton.nu> - 1.17.2-1
- Update to 1.17.2 upstream release

* Wed Jan 15 2020 Tom Hughes <tom@compton.nu> - 1.17.1-1
- Update to 1.17.1 upstream release

* Mon Dec 16 2019 Tom Hughes <tom@compton.nu> - 1.16.3-1
- Update to 1.16.3 upstream release

* Sat Oct  5 2019 Tom Hughes <tom@compton.nu> - 1.15.0-1
- Update to 1.15.0 upstream release

* Sun Sep  8 2019 Tom Hughes <tom@compton.nu> - 1.14.2-1
- Update to 1.14.2 upstream release

* Wed Sep  4 2019 Tom Hughes <tom@compton.nu> - 1.14.1-1
- Update to 1.14.1 upstream release

* Tue Sep  3 2019 Tom Hughes <tom@compton.nu> - 1.14.0-1
- Update to 1.14.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Tom Hughes <tom@compton.nu> - 1.13.0-3
- Re-enable tests

* Sat Feb  9 2019 Tom Hughes <tom@compton.nu> - 1.13.0-2
- Fix npm(has) dependency
- Disable tests

* Mon Feb  4 2019 Tom Hughes <tom@compton.nu> - 1.13.0-1
- Update to 1.13.0 upstream release

* Mon Feb  4 2019 Tom Hughes <tom@compton.nu> - 1.7.0-1
- Update to 1.7.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Tom Hughes <tom@compton.nu> - 1.5.1-1
- Update to 1.5.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Tom Hughes <tom@compton.nu> - 1.5.0-2
- Patch tests for changes in es-to-primitive@1.1.1

* Mon Dec 28 2015 Tom Hughes <tom@compton.nu> - 1.5.0-1
- Update to 1.5.0 upstream release

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 1.4.3-1
- Update to 1.4.3 upstream release
- Install helpers directory

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Initial build of 1.4.0
