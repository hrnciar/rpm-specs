Name:           nodejs-mbtiles
Version:        0.8.2
Release:        11%{?dist}
Summary:        Utilities and tilelive integration for the MBTiles format

License:        BSD
URL:            https://github.com/mapbox/node-mbtiles
Source0:        https://github.com/mapbox/node-mbtiles/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape) >= 3.0.0
BuildRequires:  npm(sphericalmercator)
BuildRequires:  npm(sqlite3) >= 3.0.0
BuildRequires:  npm(tiletype)

%description
%{summary}.


%prep
%setup -q -n node-mbtiles-%{version}
%nodejs_fixdep sqlite3 "^4.0.0"
%nodejs_fixdep tiletype "^0.3.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -pr lib/schema.sql %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{nodejs_sitelib}/mbtiles
cp -pr package.json %{buildroot}/%{nodejs_sitelib}/mbtiles
mkdir -p %{buildroot}/%{nodejs_sitelib}/mbtiles/lib
cp -pr lib/*.js %{buildroot}/%{nodejs_sitelib}/mbtiles/lib
ln -s %{_datadir}/%{name}/schema.sql  %{buildroot}/%{nodejs_sitelib}/mbtiles/lib
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test/*.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/mbtiles
%{_datadir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Tom Hughes <tom@compton.nu> - 0.8.2-7
- Fix sqlite3 dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Tom Hughes <tom@compton.nu> - 0.8.2-2
- Update tiletype dependency

* Sat Oct 31 2015 Tom Hughes <tom@compton.nu> - 0.8.2-1
- Update to 0.8.2 upstream release

* Thu Oct 15 2015 Tom Hughes <tom@compton.nu> - 0.8.1-1
- Update to 0.8.1 upstream release

* Thu Sep 10 2015 Tom Hughes <tom@compton.nu> - 0.8.0-3
- Fix sqlite3 dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Tom Hughes <tom@compton.nu> - 0.8.0-1
- Update to 0.8.0 upstream release

* Thu Mar 12 2015 Tom Hughes <tom@compton.nu> - 0.7.9-1
- Update to 0.7.9 upstream release

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 0.7.8-1
- Update to 0.7.8 upstream release

* Tue Jan  6 2015 Tom Hughes <tom@compton.nu> - 0.7.7-1
- Update to 0.7.7 upstream release

* Wed Dec 17 2014 Tom Hughes <tom@compton.nu> - 0.7.6-1
- Update to 0.7.6 upstream release

* Thu Dec 11 2014 Tom Hughes <tom@compton.nu> - 0.7.5-1
- Update to 0.7.5 upstream release

* Mon Dec  8 2014 Tom Hughes <tom@compton.nu> - 0.7.4-2
- Update tiletype dependency

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 0.7.4-1
- Update to 0.7.4 upstream release

* Fri Nov 14 2014 Tom Hughes <tom@compton.nu> - 0.7.3-1
- Update to 0.7.3 upstream release

* Wed Nov 12 2014 Tom Hughes <tom@compton.nu> - 0.7.2-1
- Update to 0.7.2 upstream release

* Sat Nov  1 2014 Tom Hughes <tom@compton.nu> - 0.7.1-1
- Update to 0.7.1 upstream release

* Wed Oct  1 2014 Tom Hughes <tom@compton.nu> - 0.6.1-1
- Update to 0.6.1 upstream release

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 0.6.0-1
- Update to 0.6.0 upstream release
- Switch to using github as source so we get tests

* Mon Sep 22 2014 Tom Hughes <tom@compton.nu> - 0.5.0-2
- Update sqlite3 dependency

* Tue Aug 26 2014 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Update to 0.5.0 upstream release

* Mon Jun 30 2014 Tom Hughes <tom@compton.nu> - 0.4.3-1
- Update to 0.4.3 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Tom Hughes <tom@compton.nu> - 0.4.2-1
- Update to 0.4.2 upstream release

* Wed Jan 15 2014 Tom Hughes <tom@compton.nu> - 0.4.1-2
- Rebuild against nodejs-sqlite3 2.2.0

* Sat Dec 14 2013 Tom Hughes <tom@compton.nu> - 0.4.1-1
- Update to 0.4.1 upstream release

* Fri Dec  6 2013 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release

* Sun Jul 28 2013 Tom Hughes <tom@compton.nu> - 0.3.2-1
- Update to 0.3.2 upstream release

* Mon Jul 15 2013 Tom Hughes <tom@compton.nu> - 0.3.1-1
- Update to 0.3.1 upstream release
- Update to latest nodejs packaging standards
- Switch to running tests using mocha

* Tue Apr 16 2013 Tom Hughes <tom@compton.nu> - 0.2.8-3
- Rebuild against nodejs-optimist 0.4.0

* Tue Mar 19 2013 Tom Hughes <tom@compton.nu> - 0.2.8-2
- Avoid deleting schema.sql in %%install
- Add manual pages

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.2.8-1
- Initial build of 0.2.8
