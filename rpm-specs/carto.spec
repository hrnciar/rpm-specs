Name:           carto
Version:        0.15.3
Release:        13%{?dist}
Summary:        Mapnik style sheet compiler

License:        ASL 2.0
URL:            https://github.com/mapbox/carto
Source0:        https://github.com/mapbox/carto/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/mapbox/carto/pull/406
Patch0:         carto-underscore.patch
# https://github.com/mapbox/carto/commit/d240d6b2e6eb8deb2d81a11ea12229f11e150e2b
Patch1:         carto-reference.patch
# Update test results for new stable sort in v8 7.x
Patch2:         carto-stablesort.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       npm(millstone)

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(mapnik-reference) >= 8.8.0
BuildRequires:  npm(optimist)
BuildRequires:  npm(sax)
BuildRequires:  npm(underscore)

%description
Carto is a style sheet compiler for Mapnik. It's an evolution of
the Cascadenik idea and language, with an emphasis on speed and
flexibility.


%prep
%autosetup -p 1 -n carto-%{version}
%nodejs_fixdep mapnik-reference "^8.6.0"
%nodejs_fixdep optimist "^0.6.1"
%nodejs_fixdep underscore "^1.8.3"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/carto
cp -pr package.json bin lib %{buildroot}/%{nodejs_sitelib}/carto
mkdir -p %{buildroot}/%{nodejs_sitelib}/carto/bin
mkdir -p %{buildroot}/%{_bindir}
ln -s %{nodejs_sitelib}/carto/bin/carto %{buildroot}/%{_bindir}/carto
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man/*.1 %{buildroot}%{_mandir}/man1
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec -t 30000 test/*.test.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/carto
%{_bindir}/carto
%{_mandir}/man1/carto.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Dan Callaghan <dcallagh@redhat.com> - 0.15.3-9
- Relax underscore dependency

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Tom Hughes <tom@compton.nu> - 0.15.3-5
- Fix mapnik-reference dependency

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 0.15.3-5
- Relax dependency on npm(optimist)

* Thu Feb 11 2016 Tom Hughes <tom@compton.nu> - 0.15.3-4
- Add BR on optimist

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.15.3-2
- Increase timeout for tests

* Fri Oct  9 2015 Tom Hughes <tom@compton.nu> - 0.15.3-1
- Update to 0.15.3 upstream release

* Tue Oct  6 2015 Tom Hughes <tom@compton.nu> - 0.15.2-2
- Fix underscore dependency

* Wed Sep 23 2015 Tom Hughes <tom@compton.nu> - 0.15.2-1
- Update to 0.15.2 upstream release

* Sat Sep 12 2015 Tom Hughes <tom@compton.nu> - 0.15.1-1
- Update to 0.15.1 upstream release

* Mon Aug 24 2015 Tom Hughes <tom@compton.nu> - 0.15.0-1
- Update to 0.15.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Tom Hughes <tom@compton.nu> - 0.14.1-2
- Update mapnik-reference dependency
- Switch to %%license for the license file

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 0.14.1-1
- Update to 0.14.1 upstream release

* Fri Sep 26 2014 Tom Hughes <tom@compton.nu> - 0.14.0-1
- Update to 0.14.0 upstream release

* Fri Sep  5 2014 Tom Hughes <tom@compton.nu> - 0.13.0-1
- Update to 0.13.0 upstream release

* Mon Aug  4 2014 Tom Hughes <tom@compton.nu> - 0.12.1-1
- Update to 0.12.1 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Tom Hughes <tom@compton.nu> - 0.11.0-1
- Update to 0.11.0 upstream release

* Tue Apr 29 2014 Tom Hughes <tom@compton.nu> - 0.9.6-4
- Fix mapnik-reference dependency properly

* Mon Apr 28 2014 Tom Hughes <tom@compton.nu> - 0.9.6-3
- Fix mapnik-reference dependency

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.6-2
- fix version of npm(underscore) dependency

* Wed Apr 16 2014 Tom Hughes <tom@compton.nu> - 0.9.6-1
- Update to 0.9.6 upstream release
- Switch to source from github to get tests

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-4
- fix underscore for 1.5.1

* Thu Dec  5 2013 Tom Hughes <tom@compton.nu> - 0.9.5-3
- Fix xml2js dependency

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.9.5-2
- Fix dependencies

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.9.5-1
- Update to 0.9.5 upstream release
- Update to latest nodejs packaging standards
- Enable tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.9.4-1
- Initial build of 0.9.4
