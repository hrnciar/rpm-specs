%global modulename %{name}-c++

Name:           capnproto
Version:        0.7.0
Release:        6%{?dist}
Summary:        A data interchange format and capability-based RPC system

License:        MIT
URL:            https://capnproto.org
Source0:        https://capnproto.org/%{modulename}-%{version}.tar.gz

# Backports from upstream
## https://github.com/capnproto/capnproto/commit/a5b53be194073895e78fa130a5bb31489871401b
Patch0001:      0001-Fix-aliasing-violation.patch

# We need C++
BuildRequires:  gcc-c++

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  cmake >= 3.1
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  cmake3 >= 3.1
%endif

# Ensure that we use matching version of libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Cap’n Proto is an insanely fast data interchange format
and capability-based RPC system. Think JSON, except binary.
Or think Protocol Buffers, except faster. In fact, in benchmarks,
Cap’n Proto is INFINITY TIMES faster than Protocol Buffers.

This package contains the schema compiler and command-line
encoder/decoder tools.

%package        libs
Summary:        Libraries for %{name}

%description    libs
The %{name}-libs package contains the libraries for using %{name}
in applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{modulename}-%{version} -p2

%build
# The tests are randomly failing due to poor sparsing support in the build system
export CFLAGS="%{optflags} -DHOLES_NOT_SUPPORTED=1"
export CXXFLAGS="%{optflags} -DHOLES_NOT_SUPPORTED=1"

%{?cmake3:%cmake3}%{!?cmake3:%cmake} .

# Make runs a simple test, and that test needs to be able to find the
# just-built libraries.
LD_LIBRARY_PATH=$(pwd)/.libs:$(pwd)/gtest/lib/.libs %make_build

%check
# The make check builds bundled gtest (but doesn't install it!)
LD_LIBRARY_PATH=$(pwd)/.libs:$(pwd)/gtest/lib/.libs %make_build check


%install
%make_install
find %{buildroot} -name '*.la' -delete


%files
%{_bindir}/capnp
%{_bindir}/capnpc
%{_bindir}/capnpc-c++
%{_bindir}/capnpc-capnp

%files libs
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/CapnProto/

%changelog
* Thu Mar 12 2020 Neal Gompa <ngompa13@gmail.com> - 0.7.0-6
- Backport patch to fix aliasing violation breaking builds on GCC 10 on ARM (#1807872)
- Disable "DiskFile holes" test to stop build failures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 0.7.0-2
- Append curdir to CMake invokation. (#1668512)

* Sun Sep 23 2018 Neal Gompa <ngompa13@gmail.com> - 0.7.0-1
- Update to 0.7.0
- Drop upstreamed patches
- Drop obsolete ldconfig scriptlets

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 0.6.1-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Neal Gompa <ngompa13@gmail.com> - 0.6.1-3
- Update patch based on upstream feedback

* Fri Jun 09 2017 Neal Gompa <ngompa13@gmail.com> - 0.6.1-2
- Adjust soversion patch to maintain binary compat across patch versions

* Fri Jun 09 2017 Neal Gompa <ngompa13@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Mon Feb 27 2017 Neal Gompa <ngompa13@gmail.com> - 0.5.3-4
- Add patch to fix FTBFS with GCC 7 (#1423291)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 28 2016 Neal Gompa <ngompa13@gmail.com> - 0.5.3-2
- Add patches to fix ppc builds

* Tue Apr 26 2016 Neal Gompa <ngompa13@gmail.com> - 0.5.3-1
- Initial packaging
