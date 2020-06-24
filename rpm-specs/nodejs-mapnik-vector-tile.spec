%global mapnik_version 3.0.18
%global protozero_version 1.5.2
%global geometry_version 0.9.2
%global wagyu_version 0.4.3
%global protobuf_version 3.3.0

%global geometry_test_data_commit b61dc6ed3f340483850883504a3030abbc1156fa

Name:           nodejs-mapnik-vector-tile
Version:        1.6.1
Release:        6%{?dist}
Summary:        Mapnik API for working with vector tiles

License:        BSD
URL:            https://github.com/mapbox/mapnik-vector-tile
Source0:        https://github.com/mapbox/mapnik-vector-tile/archive/v%{version}/mapnik-vector-tile-%{version}.tar.gz
Source1:        https://github.com/mapnik/geometry-test-data/archive/%{geometry_test_data_commit}/geometry-test-data-%{geometry_test_data_commit}.tar.gz
# Patch out attempts to clone dependencies from github
Patch0:         nodejs-mapnik-vector-tile-dependencies.patch
# https://github.com/mapbox/mapnik-vector-tile/commit/29fae7a166861e74d03d8e23a5622c70db14ab95
Patch1:         nodejs-mapnik-vector-tile-ambiguous-encode.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# Exclude big endian architectures as mapnik does not support them
# https://github.com/mapnik/mapnik/issues/2313
# https://bugzilla.redhat.com/show_bug.cgi?id=1395208
ExcludeArch:    ppc64 s390x

# Bundled version is forked, and includes patches that only work
# when it is compiled as part of another project with defines that
# change types to match those in the surrounding project
Provides:       bundled(polyclipping) = 6.4.0

BuildRequires:  nodejs-packaging
BuildRequires:  node-gyp
BuildRequires:  protobuf-compiler
BuildRequires:  perl-interpreter

BuildRequires:  mapnik-devel >= %{mapnik_version}
BuildRequires:  mapnik-static >= %{mapnik_version}
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  protozero-static >= %{protozero_version}
BuildRequires:  geometry-hpp-devel >= %{geometry_version}
BuildRequires:  geometry-hpp-static >= %{geometry_version}
BuildRequires:  wagyu-devel >= %{wagyu_version}
BuildRequires:  wagyu-static >= %{wagyu_version}
BuildRequires:  boost-devel
BuildRequires:  cairo-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libicu-devel
BuildRequires:  protobuf-lite-devel >= %{protobuf_version}

Requires:       mapnik-devel >= %{mapnik_version}
Requires:       protozero-devel >= %{protozero_version}
Requires:       geometry-hpp-devel >= %{geometry_version}
Requires:       wagyu-devel >= %{wagyu_version}

%description
A high performance library for working with vector tiles from the
team at MapBox.

Provides C++ headers that support rendering geodata into vector tiles
and rendering vector tiles into images.


%prep
%autosetup -p 1 -n mapnik-vector-tile-%{version}
mkdir -p deps/clipper
tar --extract --file=%{SOURCE1} --gunzip --strip-components=1 --directory=test/geometry-test-data
rm -rf node_modules


%build
make %{?_smp_mflags} SSE_MATH=false


%install
mkdir -p %{buildroot}/%{nodejs_sitearch}/mapnik-vector-tile
cp -pr package.json include_dirs.js proto src %{buildroot}/%{nodejs_sitearch}/mapnik-vector-tile
%nodejs_symlink_deps


%check
rm ./test/geometry-test-data/input/multipolygon-both-clockwise.json
rm ./test/geometry-test-data/input/multipolygon-both-counter-clockwise.json
rm ./test/geometry-test-data/input/multipolygon-overlap-different-orientations.json
rm ./test/geometry-test-data/input/multi-polygon-with-duplicate-polygon.json
rm ./test/geometry-test-data/input/multi-polygon-with-shared-edge.json
rm ./test/geometry-test-data/input/multi-polygon-with-spikes.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-clockwise-hole-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-clockwise-hole-counter-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-counter-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-counter-clockwise-hole-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-clockwise-inner-counter-clockwise-hole-counter-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-clockwise-hole-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-clockwise-hole-counter-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-counter-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-counter-clockwise-hole-clockwise.json
rm ./test/geometry-test-data/input/nested-multi-polygon-outer-counter-clockwise-inner-counter-clockwise-hole-counter-clockwise.json
rm ./test/geometry-test-data/input/overlapping-multi-polygon.json
make %{?_smp_mflags} test


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitearch}/mapnik-vector-tile


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Tom Hughes <tom@compton.nu> - 1.6.1-3
- Add upstream patch for geometry.hpp 1.x support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Tom Hughes <tom@compton.nu> - 1.6.1-1
- Update to 1.6.1 upstream release

* Thu Feb  8 2018 Tom Hughes <tom@compton.nu> - 1.6.0-1
- Update to 1.6.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Tom Hughes <tom@compton.nu> - 1.5.0-1
- Update to 1.5.0 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Thu May  4 2017 Tom Hughes <tom@compton.nu> - 1.3.0-2
- Add requires for development packages

* Wed May  3 2017 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Tom Hughes <tom@compton.nu> - 1.2.2-2
- Exclude big endian architectures as mapnik does not support them

* Sat Sep 10 2016 Tom Hughes <tom@compton.nu> - 1.2.2-1
- Update to 1.2.2 upstream release

* Wed Apr 20 2016 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Tue Apr 19 2016 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Sat Apr 16 2016 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Thu Apr 14 2016 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 1.0.6-1
- Update to 1.0.6 upstream release

* Tue Mar 22 2016 Tom Hughes <tom@compton.nu> - 1.0.5-1
- Update to 1.0.5 upstream release

* Wed Mar  9 2016 Tom Hughes <tom@compton.nu> - 1.0.4-1
- Update to 1.0.4 upstream release

* Thu Mar  3 2016 Tom Hughes <tom@compton.nu> - 1.0.3-1
- Update to 1.0.3 upstream release

* Tue Mar  1 2016 Tom Hughes <tom@compton.nu> - 1.0.2-1
- Update to 1.0.2 upstream release

* Sat Feb 27 2016 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release

* Thu Feb 25 2016 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Sat Feb 13 2016 Tom Hughes <tom@compton.nu> - 0.14.3-4
- Remove architecture specific patch now that -ffloat-store is used

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 0.14.3-2
- Use correct test data
- Re-enable some tests

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 0.14.3-1
- Update to 0.14.3 upstream release

* Wed Dec 23 2015 Tom Hughes <tom@compton.nu> - 0.14.2-1
- Update to 0.14.2 upstream release

* Sun Dec  6 2015 Tom Hughes <tom@compton.nu> - 0.14.1-2
- Patch out some tests on non-x86_64 platforms
- Fix build dependencies

* Sat Dec  5 2015 Tom Hughes <tom@compton.nu> - 0.14.1-1
- Update to 0.14.1 upstream release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.2-10
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 Tom Hughes <tom@compton.nu> - 0.6.2-8
- Rebuild for boost 1.58.0

* Sat Jul 18 2015 Tom Hughes <tom@compton.nu> - 0.6.2-7
- Rebuild for boost 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 25 2015 Tom Hughes <tom@compton.nu> - 0.6.2-5
- Rebuild for protobuf 2.6 support

* Sun Feb  8 2015 Tom Hughes <tom@compton.nu> - 0.6.2-4
- Add patch fof gcc 5 support

* Wed Jan 28 2015 Tom Hughes <tom@compton.nu> - 0.6.2-3
- Rebuild for boost 1.57.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.6.2-2
- Rebuild for boost 1.57.0

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 0.6.2-1
- Update to 0.6.2 upstream release

* Mon Oct 27 2014 Tom Hughes <tom@compton.nu> - 0.6.1-1
- Update to 0.6.1 upstream release

* Wed Oct 22 2014 Tom Hughes <tom@compton.nu> - 0.6.0-1
- Update to 0.6.0 upstream release

* Thu Aug 14 2014 Tom Hughes <tom@compton.nu> - 0.5.2-1
- Update to 0.5.2 upstream release

* Sat Jun  7 2014 Tom Hughes <tom@compton.nu> - 0.5.1-1
- Update to 0.5.1 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Tom Hughes <tom@compton.nu> - 0.5.0-3
- Include image_compositing header so node-mapnik compiles

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.5.0-2
- Rebuild for boost 1.55.0

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Update to 0.5.0 upstream release

* Fri Feb 28 2014 Tom Hughes <tom@compton.nu> - 0.4.2-1
- Update to 0.4.2 upstream release

* Tue Feb 25 2014 Tom Hughes <tom@compton.nu> - 0.4.1-1
- Update to 0.4.1 upstream release

* Wed Feb 19 2014 Tom Hughes <tom@compton.nu> - 0.4.0-1
- Update to 0.4.0 upstream release

* Tue Feb 18 2014 Tom Hughes <tom@compton.nu> - 0.3.7-1
- Update to 0.3.7 upstream release

* Wed Jan  8 2014 Tom Hughes <tom@compton.nu> - 0.3.4-1
- Update to 0.3.4 upstream release

* Wed Nov  6 2013 Tom Hughes <tom@compton.nu> - 0.3.3-1
- Update to 0.3.3 upstream release

* Sun Aug  4 2013 Tom Hughes <tom@compton.nu> - 0.3.2-1
- Update to 0.3.2 upstream release

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.3.1-2
- Rebuild for boost 1.54.0

* Tue Jul 30 2013 Tom Hughes <tom@compton.nu> - 0.3.1-1
- Update to 0.3.1 upstream release

* Sun Jul 28 2013 Tom Hughes <tom@compton.nu> - 0.2.4-1
- Update to 0.2.4 upstream release

* Thu Jul 18 2013 Tom Hughes <tom@compton.nu> - 0.2.3-1
- Update to 0.2.3 upstream release
- Remove x86_64 restriction on tests

* Wed Jul 17 2013 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release
- Restrict tests to x86_64 for now

* Mon Jul 15 2013 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Updated to 0.1.0 upstream release

* Thu Jul  4 2013 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Initial build of 0.0.6
