Name:       clingo
Version:    5.4.0
Release:    4%{?dist}
Summary:    A grounder and solver for logic programs

License:    MIT
URL:        https://potassco.org/clingo/
Source0:    https://github.com/potassco/clingo/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable gcc warning no-class-memaccess, which is intended use in this case
Patch0:     clingo.clasp-disable-class-memaccess-warning.patch
# https://github.com/potassco/clingo/pull/167
Patch1:     clingo.python38.patch

BuildRequires: bison
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: re2c

%description
Clingo is part of the Potassco project for Answer Set Programming
(ASP). ASP offers a simple and powerful modeling language to describe
combinatorial problems as logic programs. The clingo system then takes
such a logic program and computes answer sets representing solutions
to the given problem.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n lua-%{name}
Summary:        Lua bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  lua-devel

%description -n lua-%{name}
Lua bindings for Clingo, a grounder and solver for logic programs.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%package -n python3-%{name}
Summary:        Python 3 bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3, python3-devel
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This module provides functions and classes to work with ground terms and to
control the instantiation process. In clingo builts, additional functions to
control and inspect the solving process are available.
 
Functions defined in a python script block are callable during the
instantiation process using @-syntax. The default grounding/solving process can
be customized if a main function is provided.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/


%prep
%autosetup -p1


%build
%cmake \
  -H. \
  -Brelease \
  -DCLINGO_MANAGE_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DCLINGO_BUILD_APPS:BOOL=ON \
  -DCLINGO_BUILD_LUA_SHARED:BOOL=ON \
  -DPYTHON_EXECUTABLE=%{__python3} \
  -DCLINGO_BUILD_PY_SHARED:BOOL=ON \
  -DCLINGO_BUILD_SHARED:BOOL=ON \
  -DCLINGO_REQUIRE_PYTHON:BOOL=ON \
  -DPYCLINGO_USER_INSTALL:BOOL=OFF \
  -DLUACLINGO_INSTALL_DIR:PATH=%{lua_libdir}

cmake --build release -- %{?_smp_mflags}


%install
%make_install -C release

%files
%doc README.md INSTALL.md 
%license LICENSE.md
%{_libdir}/libclingo.so.3*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Clingo

%files -n lua-%{name}
%{_libdir}/libluaclingo.so.1*
%{lua_libdir}/%{name}.so

%files -n python3-%{name}
%{_libdir}/libpyclingo.so.1*
%{python3_sitearch}/%{name}.*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Till Hofmann <thofmann@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0
- Add patch to fix compatibility with Python 3.8
- Remove upstreamed patch
- Rebase patches to allow usage of %%autosetup

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Till Hofmann <thofmann@fedoraproject.org> - 5.3.0-5
- Do not glob library sonames to avoid unintentional soname bumps

* Thu Jul 25 2019 Till Hofmann <thofmann@fedoraproject.org> - 5.3.0-4
- Do not build python2 bindings

* Tue Nov 13 2018 Tim Niemueller <tim@niemueller.de> - 5.3.0-3
- build python2 and python3 bindings

* Tue Nov 13 2018 Tim Niemueller <tim@niemueller.de> - 5.3.0-2
- update clasp patch

* Mon Nov 12 2018 Tim Niemueller <tim@niemueller.de> - 5.3.0-1
- Initial package
