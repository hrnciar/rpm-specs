Name:           nodejs-sphericalmercator
Version:        1.0.4
Release:        9%{?dist}
Summary:        Transformations between Spherical Mercator and Lat/Lon

License:        BSD
URL:            https://github.com/mapbox/node-sphericalmercator
Source0:        http://registry.npmjs.org/sphericalmercator/-/sphericalmercator-%{version}.tgz
BuildArch:      noarch

BuildRequires:  nodejs-devel

BuildRequires:  npm(tape)

%description
Provides projection math for converting between mercator meters, screen
pixels (of 256x256 or configurable-size tiles), and latitude/longitude.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/sphericalmercator
cp -pr package.json sphericalmercator.js %{buildroot}/%{nodejs_sitelib}/sphericalmercator
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test/*.test.js


%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/sphericalmercator


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Update to 1.0.4 upstream release
- Switch to %%license for the license file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Initial build of 1.0.2
