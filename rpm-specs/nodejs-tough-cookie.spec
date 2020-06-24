Name:           nodejs-tough-cookie
Version:        2.3.4
Release:        4%{?dist}
Summary:        RFC6265 Cookies and Cookie Jar for Node.js

# The entire source is BSD except for "public_suffix_list.dat" which is MPLv2.0
# and "lib/pubsuffix.js" which is partially MPLv2.0 and BSD
License:        BSD and MPLv2.0
URL:            https://www.npmjs.com/package/tough-cookie
Source0:        https://github.com/salesforce/tough-cookie/archive/v%{version}/tough-cookie-%{version}.tar.gz
# Adjust tests for changes in assert module
Patch0:         nodejs-tough-cookie-assert.patch
# Adjust expiry dates in tests
Patch1:         nodejs-tough-cookie-expiry.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(async)
BuildRequires:  npm(string.prototype.repeat)
BuildRequires:  npm(vows)

%description
%{summary}.

%prep
%autosetup -p 1 -n tough-cookie-%{version}
%nodejs_fixdep punycode "^2.0.0"
rm -rf node_modules


%build



%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tough-cookie
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/tough-cookie
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
vows --spec test/*_test.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/tough-cookie


%changelog
* Fri Feb  7 2020 Tom Hughes <tom@compton.nu> - 2.3.4-4
- Patch date related test failure

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 2.3.4-1
- Update to 2.3.4 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 2.3.2-2
- Update npm(punycode) dependency

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 2.3.2-1
- Update to 2.3.2 upstream release
- Patch date related test failure

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Piotr Popieluch <piotr1212@gmail.com> - - 2.3.1-1
- Update to 2.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.2.0-1
- Initial package
