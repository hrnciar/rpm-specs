%{?nodejs_find_provides_and_requires}

Name:           nodejs-object-dot-assign
Version:        4.1.0
Release:        3%{?dist}
Summary:        An Object.assign shim

License:        MIT
URL:            https://www.npmjs.com/package/object.assign
Source0:        https://registry.npmjs.org/object.assign/-/object.assign-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(define-properties)
BuildRequires:  npm(function-bind)
BuildRequires:  npm(has-symbols)
BuildRequires:  npm(object-keys)


%description
An Object.assign shim. Invoke its "shim" method to shim Object.assign
if it is unavailable.

This package implements the es-shim API interface. It works in an
ES3-supported environment and complies with the spec. In an ES6
environment, it will also work properly with Symbols.


%prep
%autosetup -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/object.assign
cp -pr package.json index.js implementation.js polyfill.js shim.js %{buildroot}%{nodejs_sitelib}/object.assign
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs test/index.js
%__nodejs test/shimmed.js


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{nodejs_sitelib}/object.assign


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb  4 2019 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Initial build of 4.1.0
