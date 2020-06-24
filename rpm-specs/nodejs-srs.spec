Name:           nodejs-srs
Version:        1.2.0
Release:        8%{?dist}
Summary:        Spatial reference parser for Node.js

License:        BSD
URL:            https://github.com/mapbox/node-srs
Source0:        https://registry.npmjs.org/srs/-/srs-%{version}.tgz
# Patch out tests which rely on removed files in GDAL
Patch0:         nodejs-srs-tests.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(gdal)

%description
This module tries to detect projections, also known as "spatial
reference systems". It works similiarly to gdalsrsinfo.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep gdal "^0.9.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/srs
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/srs
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec


%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{nodejs_sitelib}/srs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Wed Mar 30 2016 Tom Hughes <tom@compton.nu> - 1.1.0-3
- Update npm(gdal) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 1.0.1-2
- Really update to 1.0.1 upstream release

* Tue Nov 10 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 0.4.9-2
- Rebuild for gdal 2.0.0

* Sun Aug  9 2015 Tom Hughes <tom@compton.nu> - 0.4.9-1
- Update to 0.4.9 upstream release

* Mon Jul 27 2015 Tom Hughes <tom@compton.nu> - 0.4.8-3
- Rebuild for gdal 2.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  8 2015 Tom Hughes <tom@compton.nu> - 0.4.8-1
- Update to 0.4.8 upstream release

* Sat Apr 18 2015 Tom Hughes <tom@compton.nu> - 0.4.7-1
- Update to 0.4.7 upstream release

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 0.4.6-1
- Update to 0.4.6 upstream release

* Fri Nov 14 2014 Tom Hughes <tom@compton.nu> - 0.4.5-2
- Make nan a devDependency

* Fri Nov 14 2014 Tom Hughes <tom@compton.nu> - 0.4.5-1
- Update to 0.4.5 upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Tom Hughes <tom@compton.nu> - 0.4.3-1
- Update to 0.4.3 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.4.1-1
- Update to 0.4.1 upstream release

* Fri May  2 2014 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release

* Wed Apr 30 2014 Tom Hughes <tom@compton.nu> - 0.3.12-1
- Update to 0.3.12 upstream release

* Fri Mar 14 2014 Tom Hughes <tom@compton.nu> - 0.3.11-1
- Update to 0.3.11 upstream release

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.10-3
- rebuild for icu-53 (via v8)

* Thu Feb  6 2014 Tom Hughes <tom@compton.nu> - 0.3.10-2
- Rebuild with correct source archive

* Thu Feb  6 2014 Tom Hughes <tom@compton.nu> - 0.3.10-1
- Update to 0.3.10 upstream release

* Sun Jan 26 2014 Tom Hughes <tom@compton.nu> - 0.3.9-1
- Update to 0.3.9 upstream release

* Fri Nov  8 2013 Tom Hughes <tom@compton.nu> - 0.3.8-1
- Update to 0.3.8 upstream release

* Sun Nov  3 2013 Tom Hughes <tom@compton.nu> - 0.3.7-1
- Update to 0.3.7 upstream release

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.3.6-2
- Rebuild with correct source archive

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.3.6-1
- Update to 0.3.6 upstream release

* Tue Oct  1 2013 Tom Hughes <tom@compton.nu> - 0.3.3-3
- Don't strip the compiled extension module

* Tue Oct  1 2013 Tom Hughes <tom@compton.nu> - 0.3.3-2
- Rebuild with correct source archive

* Tue Oct  1 2013 Tom Hughes <tom@compton.nu> - 0.3.3-1
- Update to 0.3.3 upstream release

* Mon Aug 26 2013 Tom Hughes <tom@compton.nu> - 0.3.2-2
- Don't strip the compiled extension module

* Tue Aug 20 2013 Tom Hughes <tom@compton.nu> - 0.3.2-1
- Update to 0.3.2 upstream release

* Sun Aug 11 2013 Tom Hughes <tom@compton.nu> - 0.3.1-1
- Update to 0.3.1 upstream release

* Thu Aug  8 2013 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Tom Hughes <tom@compton.nu> - 0.2.20-3
- Filter out provide for Node.js native extension
- Enable tests

* Wed Mar 13 2013 Tom Hughes <tom@compton.nu> - 0.2.20-2
- Restrict supported architectures using ExclusiveArch
- Rebuild against node 0.10

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.2.20-1
- Initial build of 0.2.20
