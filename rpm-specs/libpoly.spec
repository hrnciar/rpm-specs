Name:           libpoly
Version:        0.1.8
Release:        3%{?dist}
Summary:        C library for manipulating polynomials

License:        LGPLv3+
URL:            https://github.com/SRI-CSL/%{name}
Source0:        https://github.com/SRI-CSL/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(sympy)

%description
LibPoly is a C library for manipulating polynomials.  The target
applications are symbolic reasoning engines, such as SMT solvers, that
need to reason about polynomial constraints.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python3-%{name}
Summary:        Python 3 interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This package contains a python 3 interface to %{name}.

%prep
%autosetup

# Install in the right place
if [ "%{_lib}" != "lib" ]; then
  sed -i 's/\(DESTINATION \)lib/\1%{_lib}/' src/CMakeLists.txt
fi

# Clean up hidden files before they get installed
find . -name .gitignore -delete

%build
%cmake %{_cmake_skip_rpath} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLIBPOLY_BUILD_STATIC:BOOL=OFF \
  -DLIBPOLY_BUILD_STATIC_PIC:BOOL=OFF
%cmake_build

%install
%cmake_install

# Install the python interface by hand
mkdir -p %{buildroot}%{python3_sitearch}
cp -p %{__cmake_builddir}/python/polypy.so %{buildroot}%{python3_sitearch}

%ifnarch %{ix86} %{arm}
%check
export LD_LIBRARY_PATH=$PWD/%{__cmake_builddir}/src
%ctest
%endif

%files
%license LICENCE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/poly/
%{_libdir}/*.so

%files -n python3-%{name}
%{python3_sitearch}/polypy.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-2
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- Version 0.1.8
- Add sympy BR for the tests
- Add the python3 interface
- Bring back the check script for 64-bit platforms; 32-bit platforms cannot
  run all tests due to the limited size of a C integer

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 0.1.7-1
- New upstream version
- Drop python2-only interface; we'll bring it back when it is ported to python3
- Drop python-only check script

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 0.1.5-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  1 2018 Jerry James <loganjerry@gmail.com> - 0.1.4-1
- Initial RPM
