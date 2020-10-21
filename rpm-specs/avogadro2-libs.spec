## This release does not compile because of current unsupported GCC version (4.8.5) on rhel7
## during compilation of bundled 'jsoncpp'.
## Error "unsupported GCC version - see https://github.com/nlohmann/json#supported-compilers"

%global __cmake_in_source_build 1

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:           avogadro2-libs
Version:        1.93.0
Release:        7%{?dist}
Summary:        Avogadro2 libraries

# BSD is main license
# BSD is the license of avogenerators scripts
License: BSD and MIT
URL:     http://avogadro.openmolecules.net/
Source0: https://github.com/OpenChemistry/avogadrolibs/archive/%{version}/avogadrolibs-%{version}.tar.gz

# External source code for avogadrolibs >= 1.91.0
# See https://github.com/OpenChemistry/avogadrolibs/issues/362
%global commit 84443126ba5529fc134068047c206f0b3b7b823b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source1: https://github.com/OpenChemistry/avogenerators/archive/%{commit}/avogenerators-%{commit}.tar.gz

# Fix reported path
Patch0: %{name}-fix_AvogadroLibsConfig.patch

# Set installation path of Python files
Patch2: %{name}-set_pythonpath.patch

# Fix libgwavi name and link
Patch3: %{name}-fix_libgwavi.patch

BuildRequires:  boost-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?fedora}
BuildRequires:  boost-python3-devel
%endif
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath
BuildRequires:  %{?dts}gcc, %{?dts}gcc-c++
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(openbabel-2.0)
BuildRequires:  mesa-libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  mmtf-cpp-devel, jsoncpp-devel
BuildRequires:  spglib-devel, molequeue-devel
BuildRequires:  qt5-qtbase-devel, qt5-qttools-devel
BuildRequires:  libarchive-devel >= 3.4.0

Obsoletes: %{name} < %{version}-%{release}
Provides: %{name}%{?_isa} = 0:%{version}-%{release}
Provides: %{name}-static = 0:%{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular modeling,
bioinformatics, materials science, and related areas.

%package  devel
Summary:  Development files of %{name}
Requires: qt5-qtbase-devel%{?_isa}
Requires: glew-devel%{?_isa}
Requires: libGL-devel%{?_isa}
Requires: mesa-libGLU-devel%{?_isa}
Requires: spglib-devel%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: libgwavi-static

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
BuildRequires: doxygen, graphviz
%description doc
HTML documentation of %{name}.

%prep
%autosetup -a 1 -N -n avogadrolibs-%{version}
%autopatch -p0

# Make avogadro generators source code available for CMake
mv avogenerators-%{commit} avogadrogenerators
mv avogadrogenerators/README.md avogadrogenerators/README-avogenerators.md
sed -e 's|../avogadrogenerators|avogadrogenerators|g' -i avogadro/qtplugins/quantuminput/CMakeLists.txt
#

mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md

%build
mkdir build && pushd build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
%cmake3 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 -DINSTALL_LIBRARY_DIR:PATH=%{_lib} \
 -Wno-dev \
 -DENABLE_GLSL:BOOL=ON \
 -DENABLE_PYTHON:BOOL=ON  \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_VERSION:STRING=%{python3_version} \
%if 0%{?fedora}
 -DUSE_BOOST_PYTHON:BOOL=ON \
%else
 -DUSE_BOOST_PYTHON:BOOL=OFF \
%endif
 -DENABLE_RPATH:BOOL=OFF \
 -DENABLE_TESTING:BOOL=OFF \
 -DUSE_MMTF:BOOL=ON \
 -DUSE_QT:BOOL=ON \
 -DUSE_MOLEQUEUE:BOOL=ON \
 -DUSE_VTK:BOOL=OFF \
 -DUSE_HDF5:BOOL=ON \
 -DUSE_SPGLIB:BOOL=ON \
 -DSPGLIB_LIBRARY:FILEPATH=%{_libdir}/libsymspg.so \
 -DBUILD_GPL_PLUGINS:BOOL=ON \
 -DBUILD_STATIC_PLUGINS:BOOL=ON \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DUSE_LIBMSYM:BOOL=OFF \
 -DUSE_SYSTEM_LIBARCHIVE:BOOL=ON ..
%make_build

pushd docs
doxygen
popd

%install
%make_install -C build

# Move scale.py* files into %%{python3_sitearch}/avogadro2
cp -a %{buildroot}%{_libdir}/avogadro2/scripts %{buildroot}%{python3_sitearch}/avogadro2/
pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/avogadro2/scripts/*/*.py
ln -sf %{python3_sitearch}/avogadro2/scripts %{buildroot}%{_libdir}/avogadro2/scripts

chrpath -d %{buildroot}%{_libdir}/lib*.so
rm -rf %{buildroot}%{_datadir}/doc

%ldconfig_scriptlets

%files
%doc README.md thirdparty/libgwavi/README-libgwavi.md avogadrogenerators/README-avogenerators.md
%license LICENSE
%{_libdir}/lib*.so.*
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/scripts
%exclude %{_libdir}/avogadro2/libgwavi.a
%exclude %{_libdir}/avogadro2/staticplugins
%{python3_sitearch}/avogadro2/

%files devel
%{_includedir}/avogadro2/
%{_libdir}/lib*.so
%{_libdir}/avogadro2/libgwavi.a
%{_libdir}/avogadro2/staticplugins/
%{_libdir}/cmake/avogadrolibs/

%files doc
%doc README.md build/docs/html
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Orion Poplawski <orion@nwra.com> - 1.93.0-5
- Rebuild for hdf5 1.10.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.93.0-4
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-3
- Reorganize scripts directory

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-2
- Set USE_SYSTEM_LIBARCHIVE CMake option
- Set libarchive's minimal version for building
- Explicit Obsoletes tag

* Thu Feb 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-1
- Release 1.93.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.92.1-1
- Release 1.92.1
- Rebuild for spglib-1.14.1
- Use devtools-8 on EPEL7
- Use CMake3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.91.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.91.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.91.0-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-1
- Release 1.91.0
- Include 'avogenerators' source code

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.91.0-0.3.20180612gitda6ebb9
- Rebuilt for glew-2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-0.2.20180612gitda6ebb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-0.1.20180612gitda6ebb9
- Update to commit #da6ebb9 (1.91.0 pre-release)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.90.0-16
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-15
- Add explicit dependencies to -devel sub-package (bz#1544510)

* Tue Feb 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-14
- Fix AvogadroLibsConfig.cmake relative paths (bz#1544510)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-12
- Rebuild for moloqueue-0.9.0
- Use %%ldconfig_scriptlets

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-11
- Rebuild for spglib-1.10.2

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.90.0-10
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-7
- Modified for epel builds

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Mar 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-5
- Add ld scriptlets

* Sun Mar 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-4
- Set python3 installation directory

* Sun Mar 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-3
- Move jsoncpp.a into the private lib directory

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-2
- Use default paths

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-1
- Initial package
