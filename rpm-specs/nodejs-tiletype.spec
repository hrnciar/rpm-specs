Name:           nodejs-tiletype
Version:        0.3.0
Release:        10%{?dist}
Summary:        Detect common map tile formats from a buffer

License:        BSD
URL:            https://github.com/mapbox/tiletype
Source0:        https://registry.npmjs.org/tiletype/-/tiletype-%{version}.tgz
# https://github.com/mapbox/tiletype/pull/13
Patch0:         nodejs-tiletype-node4.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)

%description
Detect common map tile formats from a buffer.


%prep
%autosetup -p 1 -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tiletype
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/tiletype
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test/test.js


%files
%doc readme.md
%license LICENSE
%{nodejs_sitelib}/tiletype


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.3.0-2
- Patch for changes in test output with nodejs 4

* Wed Nov 18 2015 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release

* Sun Dec  7 2014 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release

* Tue Aug 26 2014 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Update to 0.1.0 upstream release

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.0.3-1
- Initial build of 0.0.3
