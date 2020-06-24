Name:           nodejs-uri-js
Version:        4.2.2
Release:        6%{?dist}
Summary:        URI parsing/validating/resolving library for Javascript

# License text is in README.md
License:        BSD
URL:            https://github.com/garycourt/uri-js
Source0:        http://registry.npmjs.org/uri-js/-/uri-js-%{version}.tgz
BuildArch:      noarch

BuildRequires:  nodejs-devel

%description
URI.js is an RFC 3986 compliant, scheme extendable URI
parsing/validating/resolving library for all JavaScript 
environments (browsers, Node.js, etc).


%prep
%setup -q -n package
%nodejs_fixdep punycode "^2.0.0"
sed -i -e 's/\r//' README.md
rm -rf node_modules bin/closure src/externs.js


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/uri-js
cp -pr package.json dist src %{buildroot}/%{nodejs_sitelib}/uri-js
%nodejs_symlink_deps


%check
# Tests are only runnable in a web browser at present
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"


%files
%doc README.md
%{nodejs_sitelib}/uri-js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun  7 2018 Tom Hughes <tom@compton.nu> - 4.2.2-2
- Update npm(punycode) dependency

* Thu Jun  7 2018 Tom Hughes <tom@compton.nu> - 4.2.2-1
- Update to 4.2.2 upstream release

* Thu Jun  7 2018 Tom Hughes <tom@compton.nu> - 4.2.0-1
- Update to 4.2.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  9 2015 Tom Hughes <tom@compton.nu> - 2.1.1-1
- Update to 2.1.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Fri Jun  5 2015 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Tom Hughes <tom@compton.nu> - 1.4.2-2
- Remove DOS line endings from README.md

* Sun Mar 17 2013 Tom Hughes <tom@compton.nu> - 1.4.2-1
- Initial build of 1.4.2
