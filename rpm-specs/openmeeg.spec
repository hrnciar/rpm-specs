%bcond_without vtk
%bcond_without python
%bcond_without hdf5
%bcond_without matio
%bcond_with cgal
%bcond_without doc
%bcond_without check

%bcond_with debug

## https://github.com/openmeeg/openmeeg/issues/346
ExcludeArch: s390x

#%%global relsuf rc4

Name:    openmeeg
Version: 2.4.2
Release: 0.3%{?dist}
Summary: Low-frequency bio-electromagnetism solving forward problems in the field of EEG and MEG
License: CeCILL-B
URL:     http://openmeeg.github.io/
Source0: https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Do not require lapacke library
Patch0: %{name}-openblas_libraries.patch

# Set private directory for Python files
Patch1: %{name}-python_install_destination.patch

Patch2: %{name}-bug385.patch

BuildRequires: cmake3
BuildRequires: gcc-c++, git, chrpath
BuildRequires: gnuplot, wget, graphviz
BuildRequires: expat-devel
BuildRequires: openblas-devel
%{?fedora:BuildRequires: gifticlib-devel}
%{?fedora:BuildRequires: nifticlib-devel}
BuildRequires: zlib-devel
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with matio}
BuildRequires: matio-devel
%endif
%if %{with vtk}
BuildRequires: vtk-devel
%endif
%if %{with cgal}
BuildRequires: CGAL-devel
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
%endif

# CGAL causes 'memory exhausted' error
%global openmeeg_cmake_options \\\
        -DCMAKE_BUILD_TYPE=Release \\\
        -DUSE_PROGRESSBAR=ON \\\
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_OpenMEEG:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_matio:BOOL=ON \\\
        -DBUILD_SHARED_LIBS_zlib:BOOL=ON \\\
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \\\
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \\\
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=include/%{name} \\\
        -DBLA_VENDOR=OpenBLAS \\\
        -DBLAS_openblas_LIBRARY:FILEPATH=%{_libdir}/libopenblas.so \\\
%if %{with python} \
        -DENABLE_PYTHON:BOOL=ON \\\
        -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \\\
%endif \
%if %{with doc} \
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
%endif \
%if %{with check} \
        -DBUILD_TESTING:BOOL=ON \\\
%endif \
        -DBUILD_TOOLS:BOOL=ON \\\
        -DENABLE_PACKAGING:BOOL=OFF \\\
        -DSKIP_GITHUB_TESTS:BOOL=ON \\\
%if %{with cgal} \
        -DUSE_CGAL:BOOL=ON \\\
%endif \
        %{?fedora:-DUSE_GIFTI:BOOL=ON} \\\
        -DUSE_OMP:BOOL=ON \\\
%if %{with hdf5} \
        -DUSE_SYSTEM_hdf5:BOOL=ON \\\
%endif \
%if %{with matio} \
        -DUSE_SYSTEM_matio:BOOL=ON \\\
%endif \
%if %{with vtk} \
        -DUSE_VTK:BOOL=ON \\\
%endif \
        -DUSE_SYSTEM_zlib:BOOL=ON \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON

%description
The OpenMEEG software is a C++ package for solving the forward
problems of electroencephalography (EEG) and magnetoencephalography (MEG).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use OpenMEEG.

%if %{with python}
%package        -n python%{python3_pkgversion}-openmeeg
Summary:        OpenMEEG binding for Python%{python3_pkgversion}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  swig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-numpy%{?_isa}
Requires:       swig
%description    -n python%{python3_pkgversion}-openmeeg
OpenMEEG binding for Python%{python3_pkgversion}.

%if 0%{?with_python3_other}
%package        -n python%{python3_other_pkgversion}-openmeeg
Summary:        OpenMEEG binding for Python%{python3_other_pkgversion}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{name}}

BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-numpy
BuildRequires:  swig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python%{python3_other_pkgversion}-numpy%{?_isa}
Requires:       swig
%description    -n python%{python3_other_pkgversion}-openmeeg
OpenMEEG binding for Python%{python3_other_pkgversion}.
%endif
%endif

%if %{with doc}
%package        doc
Summary:        Documentation files for OpenMEEG
BuildRequires:  doxygen
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep
%autosetup -n %{name}-%{version} -p1

%build
mkdir -p build && pushd build
%cmake3 %{openmeeg_cmake_options} ..

# If built including the documentation, Make's parallel jobs are damaging
%if %{with doc}
make -j1 VERBOSE=1
%else
%make_build VERBOSE=1
%endif

%install
%make_install -C build

%if %{with check}
%check
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/%{name}:%{_libdir}
%if %{with debug}
ctest3 -VV --force-new-ctest-process -j1 --output-on-failure --debug
%else
ctest3 --force-new-ctest-process --parallel %{?_smp_mflags}
%endif
%endif

%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%doc coding_guidelines.txt
#%%{_libdir}/cmake/%%{name}/
%{_libdir}/lib*.so
%{_includedir}/%{name}/

%if %{with python}
%files -n python%{python3_pkgversion}-openmeeg
%{python3_sitearch}/%{name}/

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-openmeeg
%{python3_other_sitearch}/%{name}/
%endif
%endif

%if %{with doc}
%files doc
%license LICENSE.txt
%{_docdir}/OpenMEEG/
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-0.3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.2-0.1
- Pre-release 2.4.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.4.1-4
- Rebuild for vtk 8.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-2
- Rebuild for VTK 8.1

* Sun Sep 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.1-1
- Release 2.4.1
- Exclude s390x build

* Sat Sep 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.5.rc4
- Switch to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-0.4.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.3.rc4
- Update to 2.4-rc4

* Fri Apr 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.2.rc1
- Update to 2.4-rc1
- Modified for epel7

* Fri Mar 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-0.1.20180323gitee565c4
- Initial rpm
