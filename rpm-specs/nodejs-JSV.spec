Name:           nodejs-JSV
Version:        4.0.2
Release:        16%{?dist}
Summary:        JSON Schema Validator

# License text is in lib/jsv.js
License:        BSD
URL:            https://github.com/garycourt/JSV
Source0:        http://registry.npmjs.org/JSV/-/JSV-%{version}.tgz
# Use external uri-js instead of bundled version
Patch0:         nodejs-JSV-uri-js.patch
BuildArch:      noarch

BuildRequires:  nodejs-devel

BuildRequires:  npm(uri-js)

%description
JSV is a JavaScript implementation of a extendable, fully compliant
JSON Schema validator with the following features:

* The fastest extendable JSON validator available!
* Complete implementation of all current JSON Schema draft revisions.
* Supports creating individual environments (sandboxes) that validate
  using a particular schema specification.
* Provides an intuitive API for creating new validating schema
  attributes, or whole new custom schema schemas.
* Supports self, full and described by hyper links.
* Validates itself, and is bootstrapped from the JSON Schema schemas.
* Includes over 1100 unit tests for testing all parts of the specifications.
* Works in all ECMAScript 3 environments, including all web browsers
  and Node.js.
* Licensed under the FreeBSD License, a very open license.


%prep
%setup -q -n package
sed -i -e 's/\r//' package.json lib/*.js README.md CHANGELOG.md
%patch0 -p1
rm -rf node_modules lib/uri


%build


%check
# Tests are only runnable in a web browser at present
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/JSV
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/JSV
%nodejs_symlink_deps


%files
%doc README.md CHANGELOG.md docs examples
%{nodejs_sitelib}/JSV


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun  7 2018 Tom Hughes <tom@compton.nu> - 4.0.2-12
- Update npm(uri-js) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun  6 2015 Tom Hughes <tom@compton.nu> - 4.0.2-6
- Really update for nodejs-uri-js dependency change

* Fri Jun  5 2015 Tom Hughes <tom@compton.nu> - 4.0.2-5
- Update for nodejs-uri-js dependency change

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Tom Hughes <tom@compton.nu> - 4.0.2-2
- Unbundle uri-js

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 4.0.2-1
- Initial build of 4.0.2
