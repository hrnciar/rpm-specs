# Smoldyn provides the SFMT-1.3.3 (SIMD-oriented Fast Mersenne Twister) source code;
# currently unavailable on Fedora.
# http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/SFMT/index.html

%global with_libs 0

# VTK support?
# See https://github.com/ssandrews/Smoldyn-official/issues/3
%global with_vtk 0

%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:  smoldyn
Summary: A particle-based spatial stochastic simulator
Version: 2.61
Release: 3%{?dist}

# The rxnparam.c and SurfaceParam.c source code files are in the public domain.
#
# The Next Subvolume module is Copyright 2012 by Martin Robinson and is distributed
# under the Gnu LGPL license.
#
# The rest of the code is Copyright 2003-2018 by Steven Andrews and also
# distributed under the Gnu LGPL.
#
# source/lib/SFMT is licensed under the 'BSD 3-clause "New" or "Revised" License'
License: LGPLv3+ and Public Domain and BSD
URL:   http://www.smoldyn.org
Source0: %{url}/%{name}-%{version}.zip

# Fix library paths according to the Fedora Project guidelines
Patch0: %{name}-fix_libpaths.patch
Patch1: %{name}-freeglut.patch

Patch2: %{name}-use_boost169.patch

BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: %{?dts}gcc-c++
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires: %{?dts}toolchain, %{?dts}libatomic-devel
BuildRequires: boost169-devel
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: boost-devel
%endif
BuildRequires: freeglut-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: libtiff-devel
BuildRequires: libglvnd-devel
BuildRequires: perl-macros
%if %{?with_vtk}
BuildRequires: vtk-devel
%endif
BuildRequires: zlib-devel

Requires: bionetgen-perl

Provides: bundled(SFMT) = 1.3.3 

%description
Smoldyn is a computer program for cell-scale biochemical simulations.
It simulates each molecule of interest individually to capture natural
stochasticity and to yield nanometer-scale spatial resolution.
It treats other molecules implicitly, enabling it to simulate hundreds
of thousands of molecules over several minutes of real time.

Simulated molecules diffuse, react, are confined by surfaces,
and bind to membranes much as they would in a real biological system.

It is more accurate and faster than other particle-based simulators.
Smoldyn's unique features include: a "virtual experimenter" who can
manipulate or measure the simulated system, support for spatial compartments,
molecules with excluded volume, and simulations in 1, 2, or 3 dimensions. 

%if %{?with_libs}
%package devel
Summary: %{name} devel files 
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
%description devel
This package provides the %{name} examples, header files and private libraries.
%endif

%package doc
Summary: %{name} PDF documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{name} PDF documentation.

%prep
%autosetup -n %{name}-%{version} -N
%patch0 -p0 -b .fix_libpaths
%if 0%{?fedora}
%patch1 -p0 -b .freeglut
%endif
%if 0%{?rhel} && 0%{?rhel} == 7
%patch2 -p0 -b .use_boost169
%endif

# Copy license file
mv source/lib/SFMT/LICENSE.txt source/lib/SFMT/SFMT-LICENSE.txt
mv source/lib/SFMT/README.txt source/lib/SFMT/SFMT-README.txt

# Remove pre-built archives
rm -rf Linux

# Remove bundled libraries
rm -rf source/BioNetGen source/MinGWlibs Toolchain-mingw32.cmake
rm -rf source/vcell/* source/NextSubVolume/Eigen
rm -rf source/NextSubVolume/boost_include
%if !%{?with_vtk}
rm -f source/vtk/*
%endif

#Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;
find . -type f -name "*.pdf" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec sed -i 's/\r$//' '{}' \;

# Set system path to BNG2.pl
sed -e 's|../../../source/BioNetGen/BNG2.pl|%{perl_vendorlib}/BioNetGen/BNG2.pl|g' -i examples/S95_regression/lrmsim.txt \
 examples/S12_bionetgen/lrm/lrmsim.txt \
 examples/S12_bionetgen/abba/abbasim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/lrm/lrmsim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/abba/abbasim.txt

%build
mkdir -p build && pushd build
%if 0%{?rhel} && 0%{?rhel} == 7
. /opt/rh/devtoolset-8/enable
%endif
%cmake3 -Wno-dev \
 -DCPACK_BINARY_STGZ:BOOL=OFF \
 -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_BINARY_TZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF \
 -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TXZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF \
 -DOPTION_VCELL:BOOL=OFF \
%if %{?with_vtk}
 -DOPTION_VTK:BOOL=ON \
%else
 -DOPTION_VTK:BOOL=OFF \
%endif
%if %{?with_libs}
 -DOPTION_TARGET_LIBSMOLDYN:BOOL=ON \
%else
 -DOPTION_TARGET_LIBSMOLDYN:BOOL=OFF \
%endif
 -DOPTION_USE_ZLIB:BOOL=ON \
 -DOPTION_PDE:BOOL=ON \
 -DPERL_VENDORLIB:PATH=%{perl_vendorlib} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DHAVE_GL_FREEGLUT_H=TRUE ..
%make_build V=1
popd

%install
%make_install -C build

%files
%doc source/lib/SFMT/SFMT-README.txt
%license License.txt source/lib/SFMT/SFMT-LICENSE.txt
%{_bindir}/%{name}

%if %{?with_libs}
%files devel
%doc examples
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%endif

%files doc
%doc documentation/*

%changelog
* Mon May 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-3
- Fix patch for EPEL7

* Mon May 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-2
- Patched for using Boost169 on EPEL7

* Sun May 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.61-1
- Release 2.61

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.58-3
- Rebuilt for new freeglut

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.58-1
- Release 2.58

* Sun Feb 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.56-1
- First package
- Unbundle zlib, boost and BioNetGen
- Remove unused header files
- Fix file permissions
- Add License file provided by upstream
