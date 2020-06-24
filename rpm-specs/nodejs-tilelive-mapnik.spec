Name:           nodejs-tilelive-mapnik
Version:        0.6.18
Release:        13%{?dist}
Summary:        Mapnik backend for tilelive

License:        BSD
URL:            https://github.com/mapbox/tilelive-mapnik
Source0:        https://github.com/mapbox/tilelive-mapnik/archive/v%{version}/tilelive-mapnik-%{version}.tar.gz
# https://github.com/mapbox/tilelive-mapnik/pull/115
Patch0:         nodejs-tilelive-mapnik-mime.patch
# Relax error thresholds
Patch1:         nodejs-tilelive-mapnik-threshold.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc64 s390x

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(generic-pool)
BuildRequires:  npm(mapnik) >= 3.4.11
BuildRequires:  npm(mime) >= 2.0.3
BuildRequires:  npm(step)
BuildRequires:  ImageMagick

%description
Renderer backend for tilelive.js that uses node-mapnik to render
tiles and grids from a Mapnik XML file. tilelive-mapnik implements
the Tilesource API.


%prep
%autosetup -p 1 -n tilelive-mapnik-%{version}
%nodejs_fixdep generic-pool "^2.0.3"
%nodejs_fixdep mime "^2.0.3"
%nodejs_fixdep step "^1.0.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/tilelive-mapnik
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/tilelive-mapnik
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec --timeout 10000


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/tilelive-mapnik


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct  4 2017 Tom Hughes <tom@compton.nu> - 0.6.18-8
- Add patch for mime 2.x support
- Fix npm(mime) dependency

* Wed Oct 04 2017 Jared Smith <jsmith@fedoraproject.org> - 0.6.18-7
- Relax dependency on npm(mime)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Tom Hughes <tom@compton.nu> - 0.6.18-4
- Fix npm(step) dependency

* Fri Dec 23 2016 Tom Hughes <tom@compton.nu> - 0.6.18-3
- Exclude big endian architectures as mapnik does not support them

* Mon Mar  7 2016 Tom Hughes <tom@compton.nu> - 0.6.18-2
- Fix npm(mime) dependency

* Sun Mar  6 2016 Tom Hughes <tom@compton.nu> - 0.6.18-1
- Update to 0.6.18 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 0.6.17-1
- Update to 0.6.17 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 0.6.12-2
- Fix generic-pool dependency

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 0.6.12-1
- Update to 0.6.12 upstream release

* Fri Sep  5 2014 Tom Hughes <tom@compton.nu> - 0.6.11-1
- Update to 0.6.11 upstream release

* Tue Jul 29 2014 Tom Hughes <tom@compton.nu> - 0.6.10-1
- Update to 0.6.10 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.9-2
- fix version of npm(underscore) dependency

* Thu Apr  3 2014 Tom Hughes <tom@compton.nu> - 0.6.9-1
- Update to 0.6.9 upstream release

* Fri Mar 14 2014 Tom Hughes <tom@compton.nu> - 0.6.8-1
- Update to 0.6.8 upstream release

* Fri Feb 28 2014 Tom Hughes <tom@compton.nu> - 0.6.7-1
- Update to 0.6.7 upstream release

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.5-2
- fix underscore for 1.5.1

* Fri Jan 10 2014 Tom Hughes <tom@compton.nu> - 0.6.5-1
- Update to 0.6.5 upstream release

* Tue Nov 19 2013 Tom Hughes <tom@compton.nu> - 0.6.4-1
- Update to 0.6.4 upstream release

* Mon Oct  7 2013 Tom Hughes <tom@compton.nu> - 0.6.3-1
- Update to 0.6.3 upstream release

* Fri Sep 27 2013 Tom Hughes <tom@compton.nu> - 0.6.2-1
- Update to 0.6.2 upstream release

* Thu Sep 12 2013 Tom Hughes <tom@compton.nu> - 0.6.1-1
- Update to 0.6.1 upstream release

* Wed Sep 11 2013 Tom Hughes <tom@compton.nu> - 0.5.0-4
- Rebuild against nodejs-mapnik 1.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Tom Hughes <tom@compton.nu> - 0.5.0-2
- Rebuild against nodejs-mapnik 1.1.0

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Initial build of 0.5.0
