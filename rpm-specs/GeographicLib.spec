# Needed as builddir needs to be the same on every arch, otherwise doxygen produces differently named outputs
%global __cmake_in_source_build 1

#global commit 2a6ccdf99f9b580aff4ef4725720172235fa9da0
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder geographiclib-code-%{commit}
%else
%global source_folder %{name}-%{version}
%endif

# For octave scriptlets
%global octpkg geographiclib

Name:           GeographicLib
Version:        1.50.1
Release:        5%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Library for geographic coordinate transformations

License:        MIT
URL:            http://geographiclib.sourceforge.net/
%if 0%{?commit:1}
Source0:        https://sourceforge.net/code-snapshots/git/g/ge/geographiclib/code.git/geographiclib-code-%{commit}.zip
%else
Source0:        http://downloads.sourceforge.net/geographiclib/%{name}-%{version}.tar.gz
%endif
# Bundle MATLAB scripts into octave packages
# Not yet submitted upstream
Patch1:         %{name}-1.48-octave.patch
# Install nodejs files to arch-independent path
Patch2:         %{name}-1.48-nodejs.patch
# Adapt test conditions to handle some cases -0.000
Patch3:         %{name}-1.48-test.patch
# Fix C++17 issues for gcc-11
Patch4:		%{name}-gcc11.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  nodejs-packaging
BuildRequires:  octave-devel
BuildRequires:  python3-devel

%description
GeographicLib is a small set of C++ classes for performing conversions 
between geographic, UTM, UPS, MGRS, geocentric, and local Cartesian 
coordinates, for gravity (e.g., EGM2008), geoid height and geomagnetic 
field (e.g., WMM2010) calculations, and for solving geodesic problems. 
The emphasis is on returning accurate results with errors close to round-off 
(about 5–15 nanometers). New accurate algorithms for Geodesics on an 
ellipsoid of revolution and Transverse Mercator projection have been 
developed for this library. The functionality of the library can be accessed 
from user code, from the Utility programs provided, or via the 
Implementations in other languages.


%package devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%package doc
Summary:        Development documentation for %name
BuildArch:      noarch

%description doc
This package contains doxygen-generated html API documentation for
the %{name} library.


%package -n python3-%{name}
Summary:        Python 3 implementation of %{name}
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
A translation of the GeographicLib::Geodesic class to Python 3


%package -n octave-%{name}
Summary:        Octave implementation of %{name}
BuildArch:      noarch
Requires:         octave >= 3.4
Requires(post):   octave
Requires(postun): octave

%description -n octave-%{name}
A translation of some of the GeographicLib C++ functionality to Octave


%package -n nodejs-%{name}
Summary:        NodeJS implementation of %{name}
BuildArch:      noarch
Requires:       nodejs

%description -n nodejs-%{name}
A translation of some of the GeographicLib C++ functionality to NodeJS


%prep
%autosetup -p1 -n %{source_folder}
# Use python macros to install python lib so that egg-info is also installed
# rhbz#1724031
sed -i "s|add_subdirectory (python/geographiclib)||" CMakeLists.txt

%build
%cmake \
  -DGEOGRAPHICLIB_DATA="%{_datadir}/%{name}" \
  -DCOMMON_INSTALL_PATH=ON \
  -DGEOGRAPHICLIB_DOCUMENTATION=ON \
  -DUSE_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DPython_ADDITIONAL_VERSIONS=3
%cmake_build

pushd python
%py3_build
popd

%install
%cmake_install
pushd python
%py3_install
popd

rm -rf %{buildroot}/%{_datadir}/doc
rm -rf %{buildroot}/%{_libexecdir}

mkdir -p %{buildroot}%{_datadir}/%{name}


%check
%ctest


%ldconfig_scriptlets

%post -n octave-%{name}
%octave_cmd pkg rebuild

%preun -n octave-%{name}
%octave_pkg_preun

%postun -n octave-%{name}
%octave_cmd pkg rebuild


%files
%doc AUTHORS NEWS
%license LICENSE.txt
%{_bindir}/CartConvert
%{_bindir}/ConicProj
%{_bindir}/GeoConvert
%{_bindir}/GeodSolve
%{_bindir}/GeodesicProj
%{_bindir}/GeoidEval
%{_bindir}/Gravity
%{_bindir}/MagneticField
%{_bindir}/Planimeter
%{_bindir}/RhumbSolve
%{_bindir}/TransverseMercatorProj
%{_sbindir}/geographiclib-get-geoids
%{_sbindir}/geographiclib-get-gravity
%{_sbindir}/geographiclib-get-magnetic
%{_libdir}/libGeographic.so.19*
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*
%{_mandir}/man8/*.8.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libGeographic.so
%{_libdir}/cmake/GeographicLib
%{_libdir}/pkgconfig/geographiclib.pc

%files doc
%license LICENSE.txt
%doc %{__cmake_builddir}/doc/html

%files -n python3-%{name}
%license LICENSE.txt
%{python3_sitelib}/geographiclib/
%{python3_sitelib}/geographiclib-1.50-py%{python3_version}.egg-info

%files -n octave-%{name}
%license LICENSE.txt
%{_datadir}/octave/packages/%{octpkg}-%{version}/

%files -n nodejs-%{name}
%license LICENSE.txt
%{nodejs_sitelib}/geographiclib/


%changelog
* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.50.1-5
- Fix to work with C++17 (streamoff is in std:: not std::ios::)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.50.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 1.50.1-1
- Update to 1.50.1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.50-1
- Update to 1.50

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.49-11
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Rich Mattes <richmattes@gmail.com> - 1.49-9
- Use setup.py to install python library (rhbz#1724031)

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.49-8
- Rebuild for octave 5.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.49-6
- Subpackage python2-GeographicLib has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.49-5
- Rebuild for octave 4.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.49-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.49-1
- Update to 1.49

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.48-5
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.48-2
- Define %%octpkg for octave scriptlets

* Wed Jun 07 2017 Sandro Mani <manisandro@gmail.com> - 1.48-1
- Update to 1.48

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.43-8
- Rebuild for Python 3.6

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 1.43-7
- Rebuild for octave 4.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 3 2015 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.43-3
- Add Python 3 subpackage

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Rich Mattes <richmattes@gmail.com> - 1.43-1
- Update to release 1.43

* Mon May 04 2015 Rich Mattes <richmattes@gmail.com> - 1.42-1
- Update to release 1.42
- Add octave subpackage

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.40-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 02 2015 Rich Mattes <richmattes@gmail.com> - 1.40-1
- Update to release 1.40

* Sat Oct 04 2014 Rich Mattes <richmattes@gmail.com> - 1.38-2
- Fix cmake installation directory

* Sat Oct 04 2014 Rich Mattes <richmattes@gmail.com> - 1.38-1
- Update to 1.38
- Change BR from python2 to python2-devel
- Remove buildroot cleanup from install section

* Fri Sep 19 2014 Rich Mattes <richmattes@gmail.com> - 1.37-1
- Initial package
