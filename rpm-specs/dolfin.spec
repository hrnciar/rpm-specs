%global __cmake_in_source_build 1
Name:		dolfin
Version:	2019.1.0.post0
%global fenics_version 2019.1
Release:        11%{?dist}
Summary:        FEniCS computational backend and problem solving environment

License:        LGPLv3+
URL:            https://fenicsproject.org/
Source0:        https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-%{version}.tar.gz
Source1:        https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-%{version}.tar.gz.asc
Source2:        3083BE4C722232E28AD0828CBED06106DD22BAB3.gpg

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  petsc-devel
BuildRequires:  sundials-devel
BuildRequires:  scotch-devel
# ptscotch-mpich-devel?
BuildRequires:  %{blaslib}-devel
BuildRequires:  hdf5-devel
# hdf5-mpich-devel?
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pybind11-devel
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(fenics-ffc) >= %{fenics_version}
BuildRequires:  python3dist(fenics-ufl) >= %{fenics_version}
BuildRequires:  python3dist(fenics-dijitso) >= %{fenics_version}
# go cmake go
BuildRequires:  chrpath

# check-buildroot flags the python .so, but it should be fine after rpath removal.
# It seems that the original path to the library is stored in some comment.
%global __arch_install_post /usr/lib/rpm/check-buildroot || :

#BuildRequires:  mpich-devel
#BuildRequires:  openmpi-devel

%global _description %{expand:
DOLFIN is the computational backend of FEniCS and implements the
FEniCS Problem Solving Environment.}

%description %_description

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}%{?isa}

%description devel
%{summary}.

%package -n python3-dolfin
Summary:        Python wrapper for the FEniCS dolfin environment
# The jit compiles and links to the dolfin library
Requires:       %{name}-devel = %{version}-%{release}%{?isa}
%{?python_provide:%python_provide python3-dolfin}

%description -n python3-dolfin %_description

%package doc
Summary:        Documentation and demos for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%autosetup -n dolfin-%{version}

# Let's just specify an exact version of a dependency, yay!
sed -i -r 's|pybind11==|pybind11>=|' python/setup.py

cat >>python/CMakeLists.txt <<EOF
set(CMAKE_CXX_FLAGS "\${CMAKE_CXX_FLAGS} -I$PWD")
EOF

# https://bugzilla.redhat.com/show_bug.cgi?id=1843103
sed -r -i 's/#include </#include <algorithm>\n\0/' \
  dolfin/geometry/IntersectionConstruction.cpp \
  dolfin/mesh/MeshFunction.h

sed -r -i 's|boost/detail/endian.hpp|boost/endian/arithmetic.hpp|' \
  dolfin/io/VTKFile.cpp \
  dolfin/io/VTKWriter.cpp

%build
# %%_mpich_load
mkdir -p build && cd build
CFLAGS=-Wno-unused-variable %cmake .. \
  -DBLAS_LIBRARIES=-l%{blaslib} \
  -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=off
%make_build

# "temporary install" so the python build can find the stuff it needs
%make_install

cd ../python
VERBOSE=1 CMAKE_PREFIX_PATH=%{buildroot}/usr/share/dolfin/cmake CMAKE_SKIP_INSTALL_RPATH=yes CMAKE_SKIP_RPATH=yes %py3_build

%install
cd build
%make_install

cd ../python
VERBOSE=1 CMAKE_PREFIX_PATH=%{buildroot}/usr/share/dolfin/cmake CMAKE_SKIP_INSTALL_RPATH=yes CMAKE_SKIP_RPATH=yes %py3_install

sed -r -i '1 {s|#!/usr/bin/env python.*|#!%{__python3}|}' \
    %{buildroot}/usr/bin/dolfin-order \
    %{buildroot}/usr/bin/dolfin-plot \
    %{buildroot}/usr/bin/dolfin-convert

# this file is just pointless
rm %{buildroot}/usr/share/dolfin/dolfin.conf

# there's even an option for this, except it seems to have no effect
chrpath %{buildroot}%{python3_sitearch}/dolfin/*.so
chrpath --delete %{buildroot}%{python3_sitearch}/dolfin/*.so

%check
ctest -V %{?_smp_mflags}

%files
%license COPYING COPYING.LESSER AUTHORS
%doc README.rst
/usr/bin/dolfin-version
/usr/bin/fenics-version
%{_libdir}/libdolfin.so.%{fenics_version}
%{_libdir}/libdolfin.so.%{fenics_version}.*
%dir /usr/share/dolfin
%dir /usr/share/dolfin/data
/usr/share/dolfin/data/README

%files devel
/usr/include/dolfin.h
/usr/include/dolfin/
%{_libdir}/libdolfin.so
%{_libdir}/pkgconfig/dolfin.pc
/usr/share/dolfin/cmake/

%files doc
/usr/bin/dolfin-get-demos
/usr/share/dolfin/demo/

%files -n python3-dolfin
/usr/bin/dolfin-convert
/usr/bin/dolfin-order
/usr/bin/dolfin-plot
%{python3_sitearch}/dolfin/
%{python3_sitearch}/dolfin_utils/
%{python3_sitearch}/fenics/
%{python3_sitearch}/fenics_dolfin-%{fenics_version}*-py%{python3_version}.egg-info/

%changelog
* Mon Oct  5 07:22:07 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0.post0-11
- Rebuilt for sundials 5.4.0

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2019.1.0.post0-10
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 2019.1.0.post0-9
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0.post0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0.post0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2019.1.0.post0-6
- Rebuild for hdf5 1.10.6

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 2019.1.0.post0-5
- Directly BR python3-setuptools.

* Wed Jun  3 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0.post0-4
- Rebuilt for new boost (#1843103)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.0.post0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.0.post0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.1.0-1
- Initial packaging
