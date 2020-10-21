%undefine _ld_as_needed

Name:           cgnslib
Version:        4.1.2
Release:        1%{?dist}
Summary:        Computational Fluid Dynamics General Notation System
License:        zlib
URL:            http://www.cgns.org/
Source0:        https://github.com/CGNS/CGNS/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?rhel}
BuildRequires:          cmake3, epel-rpm-macros
%global ctest3 ctest3
%else
BuildRequires:          cmake
%global cmake3 %cmake
%global ctest3 ctest
%endif
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  hdf5-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel
Requires:       hdf5%{?_isa} = %{_hdf5_version}


%description
The Computational Fluid Dynamics General Notation System (CGNS) provides a
general, portable, and extensible standard for the storage and retrieval of
computational fluid dynamics (CFD) analysisdata. It consists of a collection
of conventions, and free and open software implementing those conventions. It
is self-descriptive, machine-independent, well-documented, and administered by
an international steering committee.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hdf5-devel%{?_isa}
Requires:       gcc-gfortran%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.


%prep
%autosetup -p1 -n CGNS-%{version}

# Multi-lib path fix.
sed -i "s|\${CMAKE_INSTALL_PREFIX}/lib|\${CMAKE_INSTALL_PREFIX}/\${LIB_INSTALL_DIR}|" CMakeLists.txt
sed -i "s|DESTINATION lib|DESTINATION \${LIB_INSTALL_DIR}|" src/CMakeLists.txt

# Remove executable bit
chmod a-x src/cgnstools/utilities/cgns_to_vtk.c


%build
# This is needed for GCC10, whenever a new cgnslib release is published, check whether it is still needed
export FCFLAGS+=-fallow-argument-mismatch
%cmake -DCMAKE_SKIP_RPATH=ON \
       -DCGNS_ENABLE_TESTS=ON \
       -DCGNS_ENABLE_FORTRAN=ON \
       -DCGNS_BUILD_CGNSTOOLS=ON \
       -DCGNS_ENABLE_HDF5=ON \
       -DCMAKE_Fortran_FLAGS_RELEASE:STRING="$FCFLAGS -DNDEBUG $LDFLAGS -lhdf5 -fPIC"

# Parallel build broken
%global _smp_mflags -j1
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.a' -delete -print

# Add shebang
# NEED CHECK - really need?
sed -i -e '1i#!%{_bindir}/sh' %{buildroot}%{_bindir}/cgconfig

# Mode fortran module to correct location
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/cgns.mod %{buildroot}%{_libdir}/gfortran/modules


%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ifarch ppc64le aarch64
%ctest --force-new-ctest-process || :
%else
%ctest --force-new-ctest-process
%endif


%ldconfig_scriptlets


%files
%license license.txt
%doc release_docs/RELEASE.txt README.md
%{_bindir}/adf2hdf
%{_bindir}/cgconfig
%{_bindir}/cgnscalc
%{_bindir}/cgnscheck
%{_bindir}/cgnscompress
%{_bindir}/cgnsconvert
%{_bindir}/cgnsdiff
%{_bindir}/cgnslist
%{_bindir}/cgnsplot
%{_bindir}/cgnsnodes
%{_bindir}/cgnsnames
%{_bindir}/cgnstools/
%{_bindir}/cgnsupdate
%{_bindir}/cgnsview
%{_bindir}/hdf2adf
%{_bindir}/unitconv
%{_datadir}/cgnstools/
%{_libdir}/libcgns.so.4.1

%files devel
%{_includedir}/cgnsBuild.defs
%{_includedir}/cgns_io.h
%{_includedir}/cgnslib.h
%{_includedir}/cgnstypes.h
%{_includedir}/cgnstypes_f.h
%{_includedir}/cgnstypes_f03.h
%{_includedir}/cgnswin_f.h
%{_includedir}/cgnsconfig.h
%{_libdir}/libcgns.so
%{_fmoddir}/cgns.mod

%changelog
* Wed Aug 26 2020 Sandro Mani <manisandro@gmail.com> - 4.1.2-1
- Update to 4.1.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 4.1.1-2
- Rebuild for hdf5 1.10.6

* Thu May 07 2020 Sandro Mani <manisandro@gmail.com> - 4.1.1-1
- Update to 4.1.1

* Thu Mar 05 2020 Sandro Mani <manisandro@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Fri Feb 21 2020 Sandro Mani <manisandro@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Mon Feb 17 2020 Sandro Mani <manisandro@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.4.0-2
- Rebuild for hdf5 1.10.5

* Tue Mar 12 2019 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 3.3.1-9
- Append curdir to CMake invokation. (#1668512)

* Sun Sep 02 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.3.1-8
- Disable wl,--as-needed on fedora 30+
- Use CMake3 on epel

* Thu Aug 30 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.3.1-7
- Fix Fortran linker flags for epel7

* Wed Aug 29 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.3.1-6
- Fix undefined references to HDF5 (bz#1623439)
- Add shebang to cgconfig
- Remove spurious executable bit
- Add Requires gcc-gfortran to the devel sub-package

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 3.3.1-4
- Rebuild (hdf5)
- Add missing BR: gcc, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Sandro Mani <manisandro@gmail.com> - 3.3.1-2
- Add patch to drop matherr hack.

* Sat Aug 05 2017 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.3.0-3
- Rebuild (gfortran)

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-2
- Rebuild for hdf5 1.8.18

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-1
- Update to 3.3.0
- Add patch to change Fortran module install location

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-6
- Rebuild for hdf5 1.8.16

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Rebuild for hdf5 1.8.15

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-3
- Rebuild for hdf5 1.8.4

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Christopher Meng <rpm@cicku.me> - 3.2.1-1
- Update to 3.2.1
- Enable hdf5 support
- Enable fortran support
- Build cgnstools(included in main package)

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 3.2-6
- Rebuild for hdf 1.8.13

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 3.2-4
- Rebuild for hdf5 1.8.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 3.2-2
- Rebuild for hdf5 1.8.11

* Mon Mar 18 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 3.2-1
- new upstream version 3.2
- userguide not provided any more

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5.r4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Orion Poplawski <orion@cora.nwra.com> - 3.1-4.r4
- Rebuild for hdf5 1.8.10

* Wed Aug 15 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> 3.1-3.r4
- Updated to 3.1.3-4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 2.5-7.rc2
- Rebuild for hdf5
- Explicitly require version of hdf5 built with

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 01 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> 2.5-5.r2
- Added hdf5 to Requires, and hdf5-devel to devel Requires.

* Thu Feb 17 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> 2.5-5.r1
- Updated to 2.5-5 release.

* Sun Jul 18 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> 2.5-3.r4
- Use zlib license that supercedes LGPLv2.

* Fri Jul 16 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> 2.5-2.r4
- Expanded CFD abbreviation.
- Added -devel sub-package.
- Added global debug_package nil.
- Added patch for creating shared library with soname.
- Added patch to fix library returning exit.
- Added usersguide.pdf to -devel sub-package.
- hdf5 atleast 1.8 is required.
- Added if condition for matching LINUX64 when copying library.

* Sat Aug 15 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.5-1.r4
- New Package
