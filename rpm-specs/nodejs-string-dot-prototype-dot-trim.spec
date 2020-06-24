%{?nodejs_find_provides_and_requires}

Name:           nodejs-string-dot-prototype-dot-trim
Version:        1.2.0
Release:        2%{?dist}
Summary:        ES5 spec-compliant shim for String.prototype.trim

License:        MIT
URL:            https://github.com/es-shims/String.prototype.trim
Source0:        https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-%{version}.tgz
# Patch out use of npm(functions-have-names)
Patch0:         nodejs-string-dot-prototype-dot-trim-fhn.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(define-properties)
BuildRequires:  npm(es-abstract)
BuildRequires:  npm(function-bind)


%description
An ES5 spec-compliant String.prototype.trim shim. Invoke its "shim"
method to shim String.prototype.trim if it is unavailable.


%prep
%autosetup -p 1 -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/string.prototype.trim
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/string.prototype.trim
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test/shimmed.js
%__nodejs test/index.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/string.prototype.trim


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Initial build of 1.1.1
