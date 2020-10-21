%undefine __cmake_in_source_build

%if 0%{?fedora} >= 30
# asan doesn't work with gcc9 on s390x...
%ifarch s390 s390x
%bcond_with asan
%else
%bcond_without asan
%endif
%endif

%bcond_without ubsan

%ifarch %{ix86} %{arm} s390 s390x
%bcond_with tsan
%else
%bcond_without tsan
%endif

Name:           wlcs
Version:        1.1.0
Release:        5%{?dist}
Summary:        Wayland Conformance Test Suite

License:        GPLv2 or GPLv3
URL:            https://github.com/MirServer/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Backports from upstream
Patch0001:      0001-Fix-project-version-in-CMake-134.patch
Patch0002:      %{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  %{_bindir}/wayland-scanner
# Because for some reason they're not pulled in normally?
BuildRequires:  libatomic
%if %{with asan}
BuildRequires:  libasan
%endif
%if %{with ubsan}
BuildRequires:  libubsan
%endif
%if %{with tsan}
BuildRequires:  libtsan
%endif

%description
wlcs aspires to be a protocol-conformance-verifying test suite
usable by Wayland compositor implementors.

It is growing out of porting the existing Weston test suite to
be run in Mir's test suite, but it is designed to be usable by
any compositor.

wlcs relies on compositors providing an integration module,
providing wlcs with API hooks to start a compositor, connect a
client, move a window, and so on.

This makes both writing aid debugging tests easier - the tests
are (generally) in the same address space as the compositor, so
there is a consistent global clock available, it's easier to poke
around in compositor internals, and standard debugging tools can
follow control flow from the test client to the compositor and
back again.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{name} aspires to be a protocol-conformance-verifying test suite
usable by Wayland compositor implementors.

The %{name}-devel package contains libraries and header files for
developing Wayland compositor tests that use %{name}.


%prep
# Version wasn't bumped before releasing...
%autosetup -n %{name}-1.0.0 -p1


%build
%cmake -GNinja %{!?with_asan:-DWLCS_BUILD_ASAN=OFF} %{!?with_ubsan:-DWLCS_BUILD_UBSAN=OFF} %{!?with_tsan:-DWLCS_BUILD_TSAN=OFF}
%cmake_build

%install
%cmake_install

%files
%license COPYING.*
%doc README.rst
%{_libexecdir}/%{name}/

%files devel
%license COPYING.*
%doc README.rst
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat Oct 17 2020 Jeff Law <law@redhat.com> - 1.1.0-5
- Use reference for loop variable to avoid range-loop-construct warning

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Neal Gompa <ngompa13@gmail.com> - 1.1.0-3
- Rebuild for gtest 1.10.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Update to 1.1.0 (RH#1742232)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Neal Gompa <ngompa13@gmail.com> - 1.0.0-2
- Fix pkgconfig file to point to runner binaries

* Sat Jul 13 2019 Neal Gompa <ngompa13@gmail.com> - 1.0.0-1
- Initial packaging for Fedora
