# Set to 1 to enable testsuite. Fails everywhere with GCC 8+.
%global with_tests 0

Name:           openvdb
Version:        7.0.0
Release:        7%{?dist}
Summary:        C++ library for sparse volumetric data discretized on three-dimensional grids
License:        MPLv2.0
URL:            http://www.openvdb.org/

Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel >= 1.61
# boost-python3-devel merged in boost-devel for Fedora 33+
# https://src.fedoraproject.org/rpms/boost/c/1f2e448e099a867f9da62b9da009d3dec5e1ad64?branch=master
%if 0%{?fedora} < 33
BuildRequires:  boost-python3-devel
%endif
BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen >= 1.8.11
#BuildRequires:  epydoc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript >= 8.70
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(blosc) >= 1.5.0
BuildRequires:  pkgconfig(cppunit) >= 1.10
# RHEL and CentOS only has that build requirement for x86_64
%if 0%{?rhel}
%ifarch x86_64
BuildRequires:  glfw-devel >= 2.7
%endif
%else
BuildRequires:  pkgconfig(glfw3) >= 2.7
%endif
BuildRequires:  pkgconfig(IlmBase)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(log4cplus) >= 1.0
BuildRequires:  pkgconfig(OpenEXR) >= 2.2
BuildRequires:  pkgconfig(tbb) >= 3.0
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib) > 1.2.7

%description
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.

This package contains some graphical tools.

%package        libs
Summary:        Core OpenVDB libraries

%description    libs
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-doc < 6.1.0-1
Provides:       %{name}-doc = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%if 0%{?fedora}
%package        -n python3-%{name}
Summary:        OpenVDB Python module
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-numpy
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-python3 < 6.2.0
Obsoletes:      %{name}-python2 < 5.1.0-1
Provides:       %{name}-python2 = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description    -n python3-%{name}
%{description}

This package contains the Python module.
%endif


%prep
%autosetup

# Hardcoded values
sed -i \
    -e 's|lib$|%{_lib}|g' \
    %{name}/CMakeLists.txt %{name}/python/CMakeLists.txt

mkdir build

%build
pushd build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
# Ignore versions (python 3, etc.)
%cmake \
    -DCMAKE_NO_SYSTEM_FROM_IMPORTED=TRUE \
    -DDISABLE_DEPENDENCY_VERSION_CHECKS=ON \
    -DOPENVDB_BUILD_DOCS=ON \
%if 0%{?fedora}
    -DOPENVDB_BUILD_PYTHON_MODULE=ON \
%endif
%if 0%{?rhel}
    -DCONCURRENT_MALLOC=None \
%endif
    -DOPENVDB_BUILD_UNITTESTS=OFF \
    -DOPENVDB_ENABLE_RPATH=OFF \
    -DOPENVDB_INSTALL_CMAKE_MODULES=OFF \
    -DPYOPENVDB_INSTALL_DIRECTORY=%{python3_sitearch} \
    ..
%make_build
popd

%if 0%{?with_tests}
%check
%make test
%endif

%install
pushd build
%make_install
popd

# Let RPM pick up HTML documents in the files section
mv %{buildroot}%{_prefix}/doc/html .
rm -fr %{buildroot}%{_datadir}/doc

find %{buildroot} -name '*.a' -delete

%files
%{_bindir}/vdb_print

%files libs
%license %{name}/LICENSE %{name}/COPYRIGHT
%doc README.md CHANGES
%{_libdir}/*.so.*

%if 0%{?fedora}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}.so
%endif

%files devel
%doc html
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sun Jun 21 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-7
- Disable jemalloc build for RHEL and its derivative

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 7.0.0-6
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-5
- Rebuilt for Python 3.9

* Sat May 23 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-4
- Drop boost-python3-devel build requirement for Fedora 33+ 

* Sat May 23 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-3
- Disable python3 binding for CentOS and Red Hat Enterprise
- On RHEL and CentOS, glfw is exclusive for x86_64
- Switch to pkgconfig build requirements as possible

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0
- Set python3 module installation path via cmake
- Drop epydoc dependency

* Thu Sep 19 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.2.0-1
- Update to 6.2.0
- Drop no longer needed upstream patch
- Rename subpackge module to python3-*
- Fix correct python module installation path

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Simone Caronni <negativo17@gmail.com> - 6.1.0-2
- Fix build with latest options.
- Update SPEC file.
- rpmlint fixes.

* Thu Aug 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0
- Fix cmake build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 6.0.0-2
- Rebuild for Ilmbase 2.3.0.

* Sat Feb 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0
- Update source url and description
- Apply patch for boost 1.6.9 borrowed from Arch Linux

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 5.1.0-4
- Rebuild for tbb 2019_U1

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-3
- Require libs subpackage for python3/devel.

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-2
- Fix Python 3 Boost link.

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-1
- Update to 5.1.0.
- Switch to Python 3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 5.0.0-3
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Sun Mar 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 5.0.0-2
- Added gcc-c++ dependency
- Upstream patch for Boost compability

* Mon Feb 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0
- Use new upstream macro for abi compatibility
- Rebuild for Boost 1.66

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-5
- Rename python subpackage (module) to python2.

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-3
- Rebuilt for Boost 1.64

* Sat May 06 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-2
- Review fixes.

* Sat Apr 22 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-1
- Update to 4.0.1.
- Perform tests, build HTML documentation.
- Require main OpenVDB library for Python module.

* Wed Nov 23 2016 Simone Caronni <negativo17@gmail.com> - 4.0.0-2
- Update to 4.0.0.

* Sun Oct 16 2016 Simone Caronni <negativo17@gmail.com> - 4.0.0-1.20161015git40271e7
- First build.
