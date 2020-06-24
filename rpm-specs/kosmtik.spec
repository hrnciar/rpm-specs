Name:           kosmtik
Version:        0.0.17
Release:        6%{?dist}
Summary:        Make maps with OpenStreetMap and Mapnik

License:        WTFPL
URL:            https://github.com/kosmtik/kosmtik
Source0:        https://registry.npmjs.org/kosmtik/-/kosmtik-%{version}.tgz
# Use system fonts
Patch0:         kosmtik-fonts.patch
# Don't test for exact mapnik output
Patch1:         kosmtik-mapnik.patch
# https://github.com/kosmtik/kosmtik/pull/277
Patch2:         kosmtik-world.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc64 s390x

Requires:       font(dejavusans)
Requires:       font(firasans)
Requires:       font(firasanslight)

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(carto)
BuildRequires:  npm(js-yaml)
BuildRequires:  npm(mapnik)
BuildRequires:  npm(mapnik-pool)
BuildRequires:  npm(nomnom)
BuildRequires:  npm(npm)
BuildRequires:  npm(request)

%description
Very lite but extendable mapping framework to create Mapnik
ready maps with OpenStreetMap data (and more).

For now, only Carto based projects are supported (with .mml or
.yml config), but in the future we hope to plug in MapCSS too.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep carto "^0.15.3"
%nodejs_fixdep mapnik "^3.5.14"
%nodejs_fixdep npm "^6.4.1"
%nodejs_fixdep request "^2.67.0"
rm -rf node_modules src/front/fonts


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/kosmtik
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/kosmtik
mkdir -p %{buildroot}%{nodejs_sitelib}/kosmtik/src
mkdir -p %{buildroot}%{_datadir}/kosmtik
pushd src
  for file in $(find . -type f -name '*.js' -print)
  do
    cp -p --parents "${file}" "%{buildroot}%{nodejs_sitelib}/kosmtik/src"
  done
  for file in $(find . -type f ! -name '*.js' -print)
  do
    cp -p --parents "${file}" "%{buildroot}%{_datadir}/kosmtik"
    mkdir -p "%{buildroot}%{nodejs_sitelib}/kosmtik/src/$(dirname ${file})"
    ln -s "%{_datadir}/kosmtik/${file}" "%{buildroot}%{nodejs_sitelib}/kosmtik/src/${file}"
  done
popd
mkdir -p %{buildroot}%{_datadir}/kosmtik/front/fonts
ln -s %{_datadir}/fonts/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/kosmtik/front/fonts
ln -s %{_datadir}/fonts/mozilla-fira/FiraSans-Bold.otf %{buildroot}%{_datadir}/kosmtik/front/fonts
ln -s %{_datadir}/fonts/mozilla-fira/FiraSans-Light.otf %{buildroot}%{_datadir}/kosmtik/front/fonts
ln -s %{_datadir}/fonts/mozilla-fira/FiraSans-Regular.otf %{buildroot}%{_datadir}/kosmtik/front/fonts
ln -s %{_datadir}/kosmtik/front/fonts %{buildroot}%{nodejs_sitelib}/kosmtik/src/front
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/kosmtik/index.js %{buildroot}%{_bindir}/kosmtik
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha


%files
%doc README.md
%{nodejs_sitelib}/kosmtik
%{_datadir}/kosmtik
%{_bindir}/kosmtik


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Tom Hughes <tom@compton.nu> - 0.0.17-3
- Update npm(npm) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May  2 2018 Tom Hughes <tom@compton.nu> - 0.0.17-1
- Update to 0.0.17 upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep  5 2017 Tom Hughes <tom@compton.nu> - 0.0.16-1
- Update to 0.0.16 upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Tom Hughes <tom@compton.nu> - 0.0.15-3
- Update npm(npm) dependency

* Fri May  5 2017 Tom Hughes <tom@compton.nu> - 0.0.15-2
- Relax npm(mapnik) dependency

* Thu Feb 16 2017 Tom Hughes <tom@compton.nu> - 0.0.15-1
- Update to 0.0.15 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Tom Hughes <tom@compton.nu> - 0.0.13-14
- Exclude big endian architectures as mapnik does not support them

* Wed Sep 28 2016 Tom Hughes <tom@compton.nu> - 0.0.13-13
- Update npm(leaflet) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Tom Hughes <tom@compton.nu> - 0.0.13-11
- Update dependencies

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.0.13-10
- Update request and semver dependencies

* Sat Jan  2 2016 Tom Hughes <tom@compton.nu> - 0.0.13-9
- Remove semver fixdep for nodejs 4.2

* Sat Jan  2 2016 Tom Hughes <tom@compton.nu> - 0.0.13-8
- Update semver dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.0.13-7
- Remove js-yaml fixdep

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 0.0.13-6
- Remove semver fixdep for nodejs 4.2

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 0.0.13-5
- Put back semver fixdep

* Fri Dec 11 2015 Tom Hughes <tom@compton.nu> - 0.0.13-4
- Remove mapnik fixdep

* Mon Dec  7 2015 Tom Hughes <tom@compton.nu> - 0.0.13-3
- Remove semver fixdep

* Thu Nov 12 2015 Tom Hughes <tom@compton.nu> - 0.0.13-2
- Fix leaflet dependency

* Thu Nov 12 2015 Tom Hughes <tom@compton.nu> - 0.0.13-1
- Update to 0.0.13 upstream release

* Wed Oct  7 2015 Tom Hughes <tom@compton.nu> - 0.0.12-1
- Update to 0.0.12 upstream release

* Thu Aug 27 2015 Tom Hughes <tom@compton.nu> - 0.0.11-3
- Fix dependencies

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 0.0.11-2
- Fix dependencies

* Tue Aug 25 2015 Tom Hughes <tom@compton.nu> - 0.0.11-1
- Update to 0.0.11 upstream release

* Tue Aug 25 2015 Tom Hughes <tom@compton.nu> - 0.0.9-5
- Fix carto dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  9 2014 Tom Hughes <tom@compton.nu> - 0.0.9-3
- Update for mozilla-fira-sans 3.111

* Mon Dec  8 2014 Tom Hughes <tom@compton.nu> - 0.0.9-2
- Remove fonts from package
- Move non-js files to %%{_datadir}

* Wed Nov 26 2014 Tom Hughes <tom@compton.nu> - 0.0.9-1
- Update to 0.0.9 upstream release

* Sun Nov 16 2014 Tom Hughes <tom@compton.nu> - 0.0.8-2
- Add patch to support projects in the current directory

* Sun Nov 16 2014 Tom Hughes <tom@compton.nu> - 0.0.8-1
- Update to 0.0.8 upstream release

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.0.7-1
- Initial build of 0.0.7
