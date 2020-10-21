%global __cmake_in_source_build 1

%bcond_without check
%bcond_without python

Name:           libCombine
Summary:        C++ library for working with the COMBINE Archive format
Version:        0.2.7
Release:        5%{?dist}
URL:            https://github.com/sbmlteam/libCombine
Source0:        %{url}/archive/%{version}/libCombine-%{version}.tar.gz

# Header files and part of source code is released under LGPLv2+ license
License:        BSD and LGPLv2+

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libsbml-devel
BuildRequires: libnuml-devel
BuildRequires: expat-devel
BuildRequires: libxml2-devel
BuildRequires: bzip2-devel
BuildRequires: xerces-c-devel
BuildRequires: zlib-devel
BuildRequires: zipper-devel
BuildRequires: minizip-devel >= 2.5.0

%description
LibCombine implements a C++ API library providing support for the
Combine Archive. The library is written after the likeness of
libSBML (and in fact some classes have been generated using DEVISER).
Thus even thought he core is written in C++, the classes can be
accessed via SWIG from .NET, Java and Python.

%package devel
Summary: Development files of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libsbml-devel%{?_isa}

%description devel
This package provides header, shared and static library files
of %{name}.

%package static
Summary: Static library of %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of %{name}.

%if %{with python}
%package -n python3-%{name}
BuildRequires:  python3-devel, swig
BuildRequires:  python3-setuptools
Summary:  Python 3 bindings for libCombine
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: swig

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains %{summary}.
%endif

%prep
%autosetup -n libCombine-%{version}

# Fix library destination
sed -e 's|CMAKE_INSTALL_LIBDIR lib|CMAKE_INSTALL_LIBDIR %{_lib}|g' -i CMakeLists.txt
sed -e 's|PACKAGE_CONFIG_DIR lib/cmake|PACKAGE_CONFIG_DIR %{_lib}/cmake|g' -i CMakeLists.txt

%build
mkdir -p build && cd build
%cmake -Wno-dev -Wno-cpp -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBCOMBINE_SHARED_VERSION:BOOL=ON -DLIBCOMBINE_SKIP_SHARED_LIBRARY:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON -DWITH_CHECK:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES -Dsbml-static_DIR:PATH=%{_libdir}/cmake \
 -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so -DLIBSBML_SHARED:BOOL=ON \
 -DZIPPER_LIBRARY:FILEPATH=%{_libdir}/libZipper.so \
 -DZIPPER_INCLUDE_DIR:PATH=%{_includedir}/zipper -DEXTRA_LIBS:STRING="numl;sbml;xml2;bz2;z;m;dl;expat" \
%if %{with python}
 -DWITH_PYTHON:BOOL=ON \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}$(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}$(python3-config --abiflags).so \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
%endif
..
%make_build

%install
%make_install -C build

%ldconfig_scriptlets

%if %{with check}
%check
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
ctest --force-new-ctest-process -V
%endif

%files
%doc README.md VERSION.txt
%license LICENSE.md
%{_libdir}/libCombine.so.*

%files devel
%{_libdir}/libCombine.so
%{_libdir}/cmake/Combine-config-*.cmake
%{_libdir}/cmake/Combine-config.cmake
%{_includedir}/combine/
%{_includedir}/omex/

%files static
%{_libdir}/libCombine-static.a
%{_libdir}/cmake/Combine-static-*.cmake

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/libcombine.pth
%{python3_sitearch}/libcombine/
%endif

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable cmake_in_source_build

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-3
- BuildRequires python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.2.7-1
- Release 0.2.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.6.20190327gitd7c11a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-0.5.20190327gitd7c11a9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-0.4.20190327gitd7c11a9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.3.20190327gitd7c11a9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Charalampos Stratakis <cstratak@redhat.com> - 0.2.3-0.2.20190327gitd7c11a9
- Don't hard-code python's abi flags

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.3-0.1.20190327gitd7c11a9
- Bump version

* Sun May 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-10.20190327gitd7c11a9
- Build commit #d7c11a90

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9.20180426git8902b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-8.20180426git8902b68
- Bundle minizip on fedora 30+ (rhbz#1632180) (upstream bug #466)

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 0.2.2-7.20180426git8902b68
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6.20180426git8902b68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-5.20180426git8902b68
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-4.20180426git8902b68
- Rebuild for libsbml-5.17.0

* Mon Apr 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-3.20180426git8902b68
- Specify source code's licenses

* Sun Apr 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-2.20180426git8902b68
- Build Python3 binding

* Thu Apr 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-1.20180426git8902b68
- First package
