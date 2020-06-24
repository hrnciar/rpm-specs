%global mapnik_version 3.0.20
%global mapnik_vector_tile_version 1.6.1
%global protozero_version 1.5.1

Name:           nodejs-mapnik
Version:        3.7.2
Release:        12%{?dist}
Summary:        Bindings to Mapnik tile rendering library for Node.js

License:        BSD
URL:            https://github.com/mapnik/node-mapnik
Source0:        https://github.com/mapnik/node-mapnik/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable use of binary builds via pre-gyp
Patch0:         nodejs-mapnik-pregyp.patch
# Build against system libraries
Patch1:         nodejs-mapnik-system-libraries.patch
# Relax some tests (https://github.com/mapnik/node-mapnik/issues/569)
Patch2:         nodejs-mapnik-relax-tests.patch
# Use modules from the global namespace
Patch3:         nodejs-mapnik-global-namespace.patch
# Patch some test differences for boost 1.66.0
Patch4:         nodejs-mapnik-boost.patch
# Patch for Node 10.x support
#  https://github.com/mapnik/node-mapnik/commit/a8e9226a918eaaac0bf015274d638f3f3ebf68fb
#  https://github.com/mapnik/node-mapnik/pull/878
Patch5:         nodejs-mapnik-node10.patch
# Patch some test differences for gdal 2.3.x
Patch6:         nodejs-mapnik-gdal.patch
# Patch for Node 11.x support
#  https://github.com/mapnik/node-mapnik/pull/922
Patch7:         nodejs-mapnik-node12.patch
# Patch for proj 6.x support
Patch8:         nodejs-mapnik-proj6.patch

ExclusiveArch:  %{nodejs_arches}

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc64 s390x

# Bundled version is forked, and includes patches that only work
# when it is compiled as part of another project with defines that
# change types to match those in the surrounding project
Provides:       bundled(polyclipping) = 6.4.0

BuildRequires:  git-core
BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  mapnik-devel >= %{mapnik_version}
BuildRequires:  mapnik-static >= %{mapnik_version}
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  protozero-static >= %{protozero_version}
BuildRequires:  boost-devel
BuildRequires:  libicu-devel
BuildRequires:  freetype-devel
BuildRequires:  sparsehash-devel
BuildRequires:  cairo-devel
BuildRequires:  polyclipping-devel
BuildRequires:  protobuf-lite-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  npm(mapnik-vector-tile) >= %{mapnik_vector_tile_version}

BuildRequires:  mapnik-utils
BuildRequires:  npm(mocha)
BuildRequires:  npm(sphericalmercator)
BuildRequires:  npm(nan) >= 2.8.0

%{?nodejs_default_filter}

%description
%summary


%prep
%autosetup -S git -p 1 -n node-mapnik-%{version}
%nodejs_fixdep --remove protozero
%nodejs_fixdep --dev --move nan
%nodejs_fixdep --dev --move mapnik-vector-tile
rm -rf deps node_modules
echo '{}' > common.gypi


%build
%nodejs_symlink_deps --build
ls -l node_modules
%ifarch aarch64 ppc64le
export CXXFLAGS="%{optflags} -O1"
%else
export CXXFLAGS="%{optflags}"
%endif
export LDFLAGS="%{?__global_ldflags}"
node-gyp configure -- -Denable_sse=false -Dmodule_name=mapnik -Dmodule_path=lib/binding
node-gyp build
mkdir -p lib/binding
cp -p build/lib/binding/mapnik.node lib/binding
echo "
module.exports.paths = {
    'fonts':         '$(mapnik-config --fonts)',
    'input_plugins': '$(mapnik-config --input-plugins)',
    'mapnik_index':  '$(which mapnik-index)',
    'shape_index':   '$(which shapeindex)'
};
module.exports.env = {
    'ICU_DATA':      '$(mapnik-config --icu-data)',
    'GDAL_DATA':     '$(mapnik-config --gdal-data)',
    'PROJ_LIB':      '$(mapnik-config --proj-lib)'
};
" > lib/binding/mapnik_settings.js


%install
mkdir -p %{buildroot}/%{nodejs_sitearch}/mapnik
cp -pr package.json bin lib %{buildroot}/%{nodejs_sitearch}/mapnik
mkdir -p %{buildroot}/%{_bindir}
ln -s  %{nodejs_sitelib}/mapnik/bin/mapnik-inspect.js %{buildroot}/%{_bindir}/mapnik-inspect
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
cat lib/binding/mapnik_settings.js
%{nodejs_sitelib}/mocha/bin/mocha -R spec -t 10000


%files
%doc README.md CHANGELOG.md CONTRIBUTING.md docs
%license LICENSE.txt
%{nodejs_sitearch}/mapnik
%{_bindir}/mapnik-*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 3.7.2-10
- Rebuild for Node.js 12.4.0

* Tue Feb  5 2019 Tom Hughes <tom@compton.nu> - 3.7.2-9
- Rebuilt for proj 5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Tom Hughes <tom@compton.nu> - 3.7.2-7
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.7.2-5
- Rebuild for ICU 62

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 3.7.2-4
- Rebuild for Node.js 10.5.0

* Mon Apr 30 2018 Tom Hughes <tom@compton.nu> - 3.7.2-3
- Relax test thresholds for libwebp 1.0.0 changes

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.7.2-2
- Rebuild for ICU 61.1

* Sun Apr 22 2018 Tom Hughes <tom@compton.nu> - 3.7.2-1
- Update to 3.7.2 upstream release

* Tue Mar  6 2018 Tom Hughes <tom@compton.nu> - 3.7.1-2
- Rebuild against mapnik 3.0.19

* Sat Mar  3 2018 Tom Hughes <tom@compton.nu> - 3.7.1-1
- Update to 3.7.1 upstream release

* Tue Feb 27 2018 Tom Hughes <tom@compton.nu> - 3.7.0-1
- Update to 3.7.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.6.2-6.1
- Rebuild for ICU 60.1

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 3.6.2-5.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.6.2-2.1
- Rebuilt for Boost 1.64

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 3.6.2-1.1
- Rebuild for Node.js 8.1.2

* Wed Jun 21 2017 Tom Hughes <tom@compton.nu> - 3.6.2-1.{?dist}
- Update to 3.6.2 upstream release

* Fri Jun 16 2017 Tom Hughes <tom@compton.nu> - 3.6.1-2
- Rebuild against mapnik 3.0.15

* Wed Jun 14 2017 Tom Hughes <tom@compton.nu> - 3.6.1-1
- Update to 3.6.1 upstream release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May  4 2017 Tom Hughes <tom@compton.nu> - 3.6.0-1
- Update to 3.6.0 upstream release

* Wed Feb 15 2017 Tom Hughes <tom@compton.nu> - 3.5.14-4
- Patch tests for change in mapnik 3.0.13

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Tom Hughes <tom@compton.nu> - 3.5.14-2
- Exclude big endian architectures as mapnik does not support them
- Disable some tests that are failing on ppc64le

* Sat Sep 10 2016 Tom Hughes <tom@compton.nu> - 3.5.14-1
- Update to 3.5.14 upstream release

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 3.5.12-3
- Rebuild for Node.js 6.5.0

* Mon Aug 22 2016 Tom Hughes <tom@compton.nu> - 3.5.12-2
- Rebuild for Node.js 6.1.0 upgrade

* Tue Apr 19 2016 Tom Hughes <tom@compton.nu> - 3.5.12-1
- Update to 3.5.12 upstream release

* Sat Apr 16 2016 Tom Hughes <tom@compton.nu> - 3.5.11-1
- Update to 3.5.11 upstream release

* Thu Apr 14 2016 Tom Hughes <tom@compton.nu> - 3.5.10-1
- Update to 3.5.10 upstream release

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 3.5.8-1
- Update to 3.5.8 upstream release

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 3.5.6-2
- Rebuild for Node.js 5.x

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 3.5.6-1
- Update to 3.5.6 upstream release

* Thu Mar 24 2016 Tom Hughes <tom@compton.nu> - 3.5.5-1
- Update to 3.5.5 upstream release

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 3.5.4-2
- Rebuild for Node.js 4.4.x

* Tue Mar 22 2016 Tom Hughes <tom@compton.nu> - 3.5.4-1
- Update to 3.5.4 upstream release

* Thu Mar  3 2016 Tom Hughes <tom@compton.nu> - 3.5.2-1
- Update to 3.5.2 upstream release

* Wed Mar  2 2016 Tom Hughes <tom@compton.nu> - 3.5.1-1
- Update to 3.5.1 upstream release

* Sat Feb 13 2016 Tom Hughes <tom@compton.nu> - 3.4.16-5
- Remove architecture specific test disablements

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 3.4.16-4
- Rebuild for Node.js 4.3.x

* Tue Feb  2 2016 Tom Hughes <tom@compton.nu> - 3.4.16-3
- Remove -fno-if-conversion and patch floating point comparisons

* Sat Jan 30 2016 Tom Hughes <tom@compton.nu> - 3.4.16-2
- Add -fno-if-conversion to avoid gcc 6 bug

* Sat Jan 23 2016 Tom Hughes <tom@compton.nu> - 3.4.16-1
- Update to 3.4.16 upstream release

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 3.4.15-1
- Update to 3.4.15 upstream release

* Thu Jan 21 2016 Tom Hughes <tom@compton.nu> - 3.4.14-1
- Update to 3.4.14 upstream release

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 3.4.13-3
- Rebuild for nodejs 4

* Fri Jan  8 2016 Tom Hughes <tom@compton.nu> - 3.4.13-2
- Patch out node-pre-gyp correctly

* Fri Jan  8 2016 Tom Hughes <tom@compton.nu> - 3.4.13-1
- Update to 3.4.13 upstream release

* Wed Dec 30 2015 Tom Hughes <tom@compton.nu> - 3.4.12-3
- Update expected output for libwebp 0.5.x

* Wed Dec 23 2015 Tom Hughes <tom@compton.nu> - 3.4.12-2
- Rebuild for mapnik-vector-tile 0.14.2

* Sat Dec 19 2015 Tom Hughes <tom@compton.nu> - 3.4.12-1
- Update to 3.4.12 upstream release

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 3.4.11-2
- Drop mapnik-render from bindir as mapnik now provides it

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 3.4.11-1
- Update to 3.4.11 upstream release

* Fri Oct 30 2015 Tom Hughes <tom@compton.nu> - 1.4.17-11
- Rebuild for ICU 56.1

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 Tom Hughes <tom@compton.nu> - 1.4.17-9
- Rebuild for boost 1.58.0

* Sat Jul 18 2015 Tom Hughes <tom@compton.nu> - 1.4.17-8
- Rebuild for boost 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.17-6
- Rebuilt for protobuf soname bump

* Wed Jan 28 2015 Tom Hughes <tom@compton.nu> - 1.4.17-5
- Fixed to build with nan 1.6

* Wed Jan 28 2015 Tom Hughes <tom@compton.nu> - 1.4.17-4
- Rebuild for boost 1.57.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.4.17-3
- Rebuild for boost 1.57.0

* Tue Oct 28 2014 Tom Hughes <tom@compton.nu> - 1.4.17-2
- Loosen mapnik-vector-tile dependency

* Tue Sep 30 2014 Tom Hughes <tom@compton.nu> - 1.4.17-1
- Update to 1.4.17 upstream release

* Tue Aug 26 2014 Tom Hughes <tom@compton.nu> - 1.4.13-1
- Update to 1.4.13 upstream release

* Mon Aug 18 2014 Tom Hughes <tom@compton.nu> - 1.4.12-1
- Update to 1.4.12 upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Tom Hughes <tom@compton.nu> - 1.4.10-1
- Update to 1.4.10 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Tom Hughes <tom@compton.nu> - 1.4.5-1
- Update to 1.4.5 upstream release

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 1.4.4-2
- Rebuild for boost 1.55.0

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 1.4.4-1
- Update to 1.4.4 upstream release

* Fri May  9 2014 Tom Hughes <tom@compton.nu> - 1.4.3-1
- Update to 1.4.3 upstream release

* Thu Apr  3 2014 Tom Hughes <tom@compton.nu> - 1.4.2-1
- Update to 1.4.2 upstream release

* Mon Mar  3 2014 Tom Hughes <tom@compton.nu> - 1.4.0-2
- Remove nodejs-pre-gyp dependency

* Sun Mar  2 2014 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release
- Switch to source from github as npm no longer includes tests

* Fri Feb 28 2014 Tom Hughes <tom@compton.nu> - 1.3.4-1
- Update to 1.3.4 upstream release

* Wed Feb 26 2014 Tom Hughes <tom@compton.nu> - 1.3.2-1
- Update to 1.3.2 upstream release

* Sat Feb 22 2014 Tom Hughes <tom@compton.nu> - 1.3.1-1
- Update to 1.3.1 upstream release

* Wed Feb 19 2014 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.3-2
- rebuild for icu-53 (via v8)

* Fri Jan 10 2014 Tom Hughes <tom@compton.nu> - 1.2.3-1
- Update to 1.2.3 upstream release

* Fri Nov  8 2013 Tom Hughes <tom@compton.nu> - 1.2.2-1
- Update to 1.2.2 upstream release

* Fri Sep 27 2013 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Tue Sep 10 2013 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Mon Aug 26 2013 Tom Hughes <tom@compton.nu> - 1.1.3-2
- Don't strip the compiled extension module

* Fri Aug 16 2013 Tom Hughes <tom@compton.nu> - 1.1.3-1
- Update to 1.1.3 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.1.0-3
- Rebuild for boost 1.54.0

* Tue Jul 16 2013 Tom Hughes <tom@compton.nu> - 1.1.0-2
- Correct system font paths

* Mon Jul 15 2013 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release
- Remove mapnik-vector-tile from run time dependencies

* Tue Jul  9 2013 Tom Hughes <tom@compton.nu> - 1.0.0-2
- Add upstream patch for numeric precision issue

* Fri Jul  5 2013 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.7.22-1
- Initial build of 0.7.22
