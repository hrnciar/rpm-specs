%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

# Don't abort on compilation errors of the example python snippets
%global _python_bytecompile_errors_terminate_build 0

%if 0%{?el6}
	%ifarch ppc64
		%global build_mpich 0
	%else
		%global build_mpich 1
	%endif
%else
	%global build_mpich 1
%endif

%global build_openmpi 1

Name:           netgen-mesher
Version:        6.2.2006
Release:        1%{?dist}
Summary:        Automatic mesh generation tool

License:        LGPLv2
URL:            https://github.com/NGSolve/netgen
Source0:        https://github.com/NGSolve/netgen/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netgen-mesher.png
Source2:        netgen-mesher.desktop
Source99:       https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/pybind11Tools.cmake
Source100:      https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/FindPythonLibsNew.cmake

# Rename shared libaries (the original names are often way too generic), add library version
Patch1:         0002-Rename-libraries-add-library-versions.patch
# Make some includes relative (needed for when headers are in -private subpackage)
Patch2:         0004-Make-some-includes-relative.patch
# Only include immintrin.h on x86 arches
# Fall back to clock() instead of rdtsc on non x86 arches
Patch3:         0009-immintrin.patch
# Rename binary in cmake so that exported modules work correctly
Patch4:         0010-rename-netgen-binary.patch
# Allow using system pybind11
Patch5:         0011-system-pybind11.patch
# Workaround "CMake Error: install(EXPORT "netgen-targets" ...) includes target "gui" which requires target "togl" that is not in the export set."
Patch6:         netgen_install-togl.patch
# Project checks for ability to write to the install location which breaks DESTDIR
Patch7:         0012-cmake_fixes.patch
# Fix function redefinition due to sizet being equal to unsigned int on non 64bit arches
Patch8:         netgen_sizet.patch



BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tk-devel
BuildRequires:  opencascade-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  metis-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  pybind11-devel
BuildRequires:  git

# Bundles a modified version of togl-2.1
Provides: bundled(tcl-togl) = 2.1


Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input from
constructive solid geometry (CSG) or boundary representation (BRep) from STL
file format. The connection to a geometry kernel allows the handling of IGES
and STEP files. NETGEN contains modules for mesh optimization and hierarchical
mesh refinement.

%package        common
Summary:        Common files for netgen
Requires:       hicolor-icon-theme
Requires:       tix
BuildArch:      noarch

%description    common
Common files for netgen.

%package        libs
Summary:        Netgen libraries

%description    libs
Netgen libraries.

%package        devel
Summary:        Development files for netgen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for netgen.

%package        devel-private
Summary:        Private headers of netgen
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    devel-private
Private headers of netgen, needed to build certain netgen based software
packages.

%package -n     python3-%{name}
Summary:        Python3 interface for netgen
%{?python_provide:%python_provide python3-netgen}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python3 interface for netgen.

###############################################################################

%if %{build_openmpi}
%package        openmpi
Summary:        Netgen compiled against openmpi
BuildRequires:  openmpi-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description    openmpi
Netgen compiled against openmpi.

%package        openmpi-libs
Summary:        Netgen libraries compiled against openmpi

%description    openmpi-libs
Netgen libraries compiled against openmpi.

%package        openmpi-devel
Summary:        Development files for Netgen compiled against openmpi
# Require explicitly for dir ownership
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description    openmpi-devel
Development files for Netgen compiled against openmpi.

%package -n     python3-%{name}-openmpi
Summary:        Python3 interface for netgen compiled against openmpi
%{?python_provide:%python_provide python3-netgen-openmpi}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi
Python3 interface for netgen compiled against openmpi.

%endif

###############################################################################

%if %{build_mpich}
%package        mpich
Summary:        Netgen compiled against mpich
BuildRequires:  mpich-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}

%description    mpich
Netgen compiled against mpich.

%package        mpich-libs
Summary:        Netgen libraries compiled against mpich

%description    mpich-libs
Netgen libraries compiled against mpich.

%package        mpich-devel
Summary:        Development files for Netgen compiled against mpich
# Require explicitly for dir ownership
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description    mpich-devel
Development files for Netgen compiled against mpich.

%package -n     python3-%{name}-mpich
Summary:        Python3 interface for netgen compiled against mpich
%{?python_provide:%python_provide python3-netgen-mpich}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich
Python3 interface for netgen compiled against mpich.

%endif

###############################################################################

%prep
%autosetup -p1 -n netgen-%{version}

# Pull in minimal cmake files from NGSolv pybind11 project to make this one happy.
install -pm 0744 %{SOURCE99} cmake/
install -pm 0744 %{SOURCE100} cmake/cmake_modules/


%build
### serial version ###
mkdir serial
(cd serial
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=%{name} \
  -DUSE_NATIVE_ARCH=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/%{name} \
  -DNG_INSTALL_DIR_LIB=%{_libdir} \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{python3_sitearch}/%{name} \
  -DUSE_JPEG=1 -DUSE_OCC=1 \
  -DOpenGL_GL_PREFERENCE=GLVND \
  ..
%make_build
)

### openmpi version ###
%if %{build_openmpi}
%{_openmpi_load}
export CXX=mpicxx
mkdir openmpi
(cd openmpi
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=%{name} \
  -DUSE_NATIVE_ARCH=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/openmpi/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/openmpi/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/openmpi/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/openmpi/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/openmpi/python%{python3_version}/site-packages/%{name} \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1 \
  ..
%make_build
)
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%{_mpich_load}
export CXX=mpicxx
mkdir mpich
(cd mpich
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=%{name} \
  -DUSE_NATIVE_ARCH=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/mpich/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/mpich/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/mpich/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/mpich/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/mpich/python%{python3_version}/site-packages/%{name} \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1 \
   ..
%make_build
)
%{_mpich_unload}
%endif


%install
%define writepkgconfig() \
install -d -m 0755 %{buildroot}/$MPI_LIB/pkgconfig; \
cat > %{buildroot}/$MPI_LIB/pkgconfig/%{name}.pc << EOF\
prefix=%{_prefix}\
exec_prefix=${prefix}\
libdir=$MPI_LIB\
includedir=$MPI_INCLUDE/%{name}\
\
Name: %{name}\
Description:  %{summary}\
Version: %{version}\
Libs: -L\\\${libdir} -lnglib\
Libs.private: -lngcgs -lnggeom2d -lngmesh -lngocc -lngstl\
Cflags: -I\\\${includedir}\
EOF\
%{nil}

### openmpi version ###
%if %{build_openmpi}
%{_openmpi_load}
%make_install -C openmpi
%writepkgconfig
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%{_mpich_load}
%make_install -C mpich
%writepkgconfig
%{_mpich_unload}
%endif

### serial version ###
%make_install -C serial
export MPI_LIB=%{_libdir}
export MPI_INCLUDE=%{_includedir}
%writepkgconfig

# Install icon and desktop file
install -Dpm 0644 %SOURCE1 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %SOURCE2

# Delete the doc folder, the files are in %%doc below
rm -rf %{buildroot}/%{_prefix}/doc

# Install private headers
(
cd libsrc
find \( -name *.hpp -or -name *.hxx -or -name *.h -or -name *.ixx -or -name *.jxx \) -exec install -Dpm 0644 {} %{buildroot}%{_includedir}/%{name}/private/{} \;
)

# Install the nglib.h header
install -Dpm 0644 nglib/nglib.h %{buildroot}%{_includedir}/%{name}/nglib.h

%ldconfig_scriptlets libs


%ldconfig_scriptlets openmpi-libs


%if %{build_mpich}
%ldconfig_scriptlets mpich-libs
%endif


%files common
%doc AUTHORS doc/ng4.pdf
%license LICENSE
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*

%files libs
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}/private
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%files devel-private
%{_includedir}/%{name}/private

%files -n python3-%{name}
%{python3_sitearch}/%{name}/

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/*

%files openmpi-libs
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_includedir}/openmpi*/%{name}
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%{_libdir}/openmpi/lib/cmake/%{name}/*.cmake

%files -n python3-%{name}-openmpi
%{_libdir}/openmpi/python%{python3_version}/site-packages/%{name}/
%endif

%if %{build_mpich}
%files mpich
%{_libdir}/mpich/bin/*

%files mpich-libs
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_includedir}/mpich*/%{name}
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%{_libdir}/mpich/lib/cmake/%{name}/*.cmake

%files -n python3-%{name}-mpich
%{_libdir}/mpich/python%{python3_version}/site-packages/%{name}/
%endif


%changelog
* Fri Jun 19 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2006-1
- Update to 6.2.2006

* Sun Jun 14 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2005-1
- Update to 6.2.2005

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.2.2004-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Sandro Mani <manisandro@gmail.com> - 6.2.2004-1
- Update to 6.2.2004

* Mon Feb 03 2020 Sandro Mani <manisandro@gmail.com> - 6.2.1910-1
- Update to 6.2.1910

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1810-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild


* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.1810-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.2.1810-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1810-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 6.2.1810-1
- Update to 6.2.1810

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 6.2-0.9.git94fd571
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.8.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.7.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.2-0.6.git94fd571
- Rebuilt for Python 3.7

* Wed May 02 2018 Sandro Mani <manisandro@gmail.com> - 6.2-0.5.git94fd571
- Rename netgen binary at CMake level to prevent breaking cmake config module (#1573330)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.4.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-0.3.git94fd571
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.git94fd571
- Install the nglib.h header

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.git94fd571
- Update to 6.2.0 snapshot

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 5.3.1-12
- Rebuild for openmpi 2.0

* Thu Apr  7 2016 Richard Shaw <hobbes1069@gmail.com> - 5.3.1-11
- Rebuild for updated OCE.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 5.3.1-9
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.3.1-8
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 5.3.1-7
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Sandro Mani <manisandro@gmail.com> - 5.3.1-4
- Rebuild (GCC5 ABI change)

* Sat Dec 13 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-3
- Fix library in -devel package

* Tue Oct 07 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-2
- Fix soname, use -release instead of -version-info

* Mon Oct 06 2014 Sandro Mani <manisandro@gmail.com> - 5.3.1-1
- Update to 5.3.1

* Mon Sep 01 2014 Sandro Mani <manisandro@gmail.com> - 5.3.0-1
- Update to 5.3.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Sandro Mani <manisandro@gmail.com> - 5.1-10
- Rebuild (OCE)

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 5.1-9
- Add missing mpich-devel BR

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 5.1-8
- Fix escaping of pkg-config variables

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-7
- Rename subpackage private -> devel-private

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-6
- Add netgen-5.1_relative-includes.patch

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 5.1-5
- Add subpackage for private headers
- Add patches from salome
- Make common package noarch
- Add missing %%{?_isa}

* Fri Jun 13 2014 Sandro Mani <manisandro@gmail.com> - 5.1-4
- Update netgen-5.1_build.patch
- Add netgen-5.1_msc-ver.patch

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-3
- Fix libgnlib soname

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-2
- Split off libraries in libs subpackages
- Rename shared libraries to less generic names

* Thu Jun 12 2014 Sandro Mani <manisandro@gmail.com> - 5.1-1
- Initial package
