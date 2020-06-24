%ifnarch ppc64
# Enable LTO on non-ppc64 (c.f. rhbz#1515934)
%bcond_without lto
%endif

# Disable ctest run by default
# They take a long time and are generally broken in the build environment
%bcond_with run_tests

Name:           mir
Version:        1.7.1
Release:        3%{?dist}
Summary:        Next generation display server

# mirclient is LGPLv2/LGPLv3, everything else is GPLv2/GPLv3
License:        (GPLv2 or GPLv3) and (LGPLv2 or LGPLv3)
URL:            https://mir-server.io/
Source0:        https://github.com/MirServer/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
## From: https://github.com/MirServer/mir/commit/eecb7af2ebbdf915344f4d0b6b5dc31cce73b9f9
Patch0001:      0001-If-there-s-a-gmock-pkg-config-then-use-it.-With-a-bi.patch
## From: https://github.com/MirServer/mir/commit/4ad1a9b5d22241046bc62288ffe933c55883b8af
Patch0002:      0001-Add-a-font-location-for-the-wallpaper-that-works-on-.patch
## From: https://github.com/MirServer/mir/commit/f1d3d28583b945b07307e39c08652b6b15c85885
Patch003:       0001-Don-t-launch-Mir-shells-in-separate-dbus-sessions.patch
## From: https://github.com/MirServer/mir/pull/1388
Patch004:       PR1388-Almost-universal-terminal-launcher.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake, ninja-build, doxygen, graphviz, lcov, gcovr
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  boost-devel, protobuf-compiler, capnproto
BuildRequires:  python3-devel
BuildRequires:  glm-devel
BuildRequires:  protobuf-devel, protobuf-lite-devel, capnproto-devel
BuildRequires:  glog-devel, lttng-ust-devel, systemtap-sdt-devel
BuildRequires:  gflags-devel
BuildRequires:  python3-pillow

# Everything detected via pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm) >= 9.0.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock) >= 1.8.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtest) >= 1.8.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(umockdev-1.0) >= 0.6
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(wlcs)

# pkgconfig(egl) is now from glvnd, so we need to manually pull this in for the Mesa specific bits...
BuildRequires:  mesa-libEGL-devel

# For some reason, this doesn't get pulled in automatically into the buildroot
BuildRequires:  libatomic

# For detecting the font for CMake
BuildRequires:  gnu-free-sans-fonts

# For validating the desktop file for mir-demos
BuildRequires:  %{_bindir}/desktop-file-validate

# Add architectures as verified to work
%ifarch %{ix86} x86_64 %{arm} aarch64
BuildRequires:  valgrind
%endif


%description
Mir is a display server running on linux systems,
with a focus on efficiency, robust operation,
and a well-defined driver model.

%package utils
Summary:       Utilities for Mir
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description utils
Utilities for Mir.

%package devel
Summary:       Development files for Mir
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-test-libs-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package provides the development files to create
applications that can run on Mir.

%package common-libs
Summary:       Common libraries for Mir
License:       LGPLv2 or LGPLv3

%description common-libs
This package provides the libraries common to be used
by Mir clients or Mir servers.

%package server-libs
Summary:       Server libraries for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description server-libs
This package provides the libraries for applications
that use the Mir server.

%package client-libs
Summary:       Client libraries for Mir
License:       LGPLv2 or LGPLv3
Requires:      %{name}-common-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# debug extension for mirclient is gone...
Obsoletes:     %{name}-client-libs-debugext < 1.6.0

%description client-libs
This package provides the libraries for applications
that connect to a Mir server.

%package test-tools
Summary:       Testing tools for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:    %{name}-demos
Recommends:    glmark2
Recommends:    xorg-x11-server-Xwayland
Requires:      wlcs

%description test-tools
This package provides tools for testing Mir.

%package demos
Summary:       Demonstration applications using Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-server-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      %{name}-client-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:      hicolor-icon-theme
Recommends:    xorg-x11-server-Xwayland
# For some of the demos
Requires:      gnu-free-sans-fonts

%description demos
This package provides applications for demonstrating
the capabilities of the Mir display server.

%package doc
Summary:       Documentation for developing Mir based applications
BuildArch:     noarch

%description doc
This package provides documentation for developing Mir based
applications.

%package -n python3-mir-perf-framework
Summary:       Performance benchmark framework for Mir
License:       GPLv2 or GPLv3
BuildArch:     noarch
%{?python_provide:%python_provide python3-mir-perf-framework}

%description -n python3-mir-perf-framework
This package provides a benchmark framework for Mir
and Mir based applications.

%package test-libs-static
Summary:       Testing framework library for Mir
License:       GPLv2 or GPLv3
Requires:      %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description test-libs-static
This package provides the static library for building
Mir unit and integration tests.


%prep
%autosetup -p1

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake .. -GNinja %{?with_lto:-DMIR_LINK_TIME_OPTIMIZATION=ON} \
	  -DMIR_USE_PRECOMPILED_HEADERS=OFF \
	  -DCMAKE_INSTALL_LIBEXECDIR="usr/libexec/mir" \
	  -DMIR_PLATFORM="mesa-kms;mesa-x11;wayland;eglstream-kms"
popd
%ninja_build -C %{_target_platform}

# Build documentation
%ninja_build -C %{_target_platform} doc

%install
%ninja_install -C %{_target_platform}

# Install documentation
pushd %{_target_platform}
mkdir -p %{buildroot}%{_datadir}/doc/mir-doc
cp -a doc/html %{buildroot}%{_datadir}/doc/mir-doc
popd

# Nothing outside Mir should link to libmirprotobuf directly.
rm -fv %{buildroot}%{_libdir}/libmirprotobuf.so


%check
%if %{with run_tests}
pushd %{_target_platform}
# The tests are somewhat fiddly, so let's just run them but not block on them...
ctest -V .. || :
popd
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/miral-shell.desktop


%files utils
%license COPYING.GPL*
%doc README.md
%{_bindir}/mirin
%{_bindir}/mirout
%{_bindir}/mirscreencast

%files devel
%license COPYING.*
%{_bindir}/mir_wayland_generator
%{_libdir}/libmir*.so
%{_libdir}/pkgconfig/mir*.pc
%{_includedir}/mir*

%files common-libs
%license COPYING.LGPL*
%doc README.md
%{_libdir}/libmircore.so.*
%{_libdir}/libmircommon.so.*
%{_libdir}/libmircookie.so.*
%{_libdir}/libmirplatform.so.*
%{_libdir}/libmirprotobuf.so.*
%dir %{_libdir}/mir

%files server-libs
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmiral.so.*
%{_libdir}/libmirserver.so.*
%{_libdir}/libmirwayland.so.*
%dir %{_libdir}/mir/server-platform
%{_libdir}/mir/server-platform/graphics-mesa-kms.so.*
%{_libdir}/mir/server-platform/input-evdev.so.*
%{_libdir}/mir/server-platform/server-mesa-x11.so.*
%{_libdir}/mir/server-platform/graphics-eglstream-kms.so.*
%{_libdir}/mir/server-platform/graphics-wayland.so.*

%files client-libs
%license COPYING.LGPL*
%doc README.md
%{_libdir}/libmirclient.so.*
%dir %{_libdir}/mir/client-platform
%{_libdir}/mir/client-platform/mesa.so.*

%files test-tools
%license COPYING.GPL*
%{_bindir}/mir-*test*
%{_bindir}/mir_*test*
%{_bindir}/mir_stress
%dir %{_libdir}/mir/tools
%{_libdir}/mir/tools/libmirserverlttng.so
%{_libdir}/mir/tools/libmirclientlttng.so
%dir %{_libdir}/mir
%{_libdir}/mir/miral_wlcs_integration.so
%dir %{_libdir}/mir/server-platform
%{_libdir}/mir/server-platform/graphics-dummy.so
%{_libdir}/mir/server-platform/input-stub.so
%dir %{_libdir}/mir/client-platform
%{_libdir}/mir/client-platform/dummy.so

%files demos
%license COPYING.GPL*
%doc README.md
%{_bindir}/mir_demo_*
%{_bindir}/miral-*
%{_datadir}/applications/miral-shell.desktop
%{_datadir}/wayland-sessions/miral-shell.desktop
%{_datadir}/icons/hicolor/scalable/apps/ubuntu-logo.svg

%files doc
%license COPYING.*
%doc README.md
%{_datadir}/doc/mir-doc/html

%files -n python3-mir-perf-framework
%license COPYING.GPL*
%doc README.md
%{python3_sitelib}/mir_perf_framework
%{python3_sitelib}/mir_perf_framework*.egg-info
%{_datadir}/mir-perf-framework

%files test-libs-static
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmir-test-assist.a


%changelog
* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 1.7.1-3
- Rebuilt for protobuf 3.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-2
- Rebuilt for Python 3.9

* Wed Apr 01 2020 Neal Gompa <ngompa13@gmail.com> - 1.7.1-1
- Update to 1.7.1 (RH#1806678)
- Backport fixes from upstream to improve Mir functionality

* Mon Feb 17 2020 Neal Gompa <ngompa13@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Backport fix from upstream to fix build with GCC 10 (RH#1799655)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Neal Gompa <ngompa13@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.5.0-2
- Rebuild for yaml-cpp 0.6.3.

* Fri Oct 11 2019 Neal Gompa <ngompa13@gmail.com> - 1.5.0-1
- Update to 1.5.0 (RH#1760820)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Neal Gompa <ngompa13@gmail.com> - 1.4.0-1
- Update to 1.4.0 (RH#1742690)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Neal Gompa <ngompa13@gmail.com> - 1.3.0-1
- Update to 1.3.0 (RH#1678585)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-2
- Rebuilt for Boost 1.69

* Sat Dec 22 2018 Neal Gompa <ngompa13@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Tue Dec 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-3
- Rebuild for new protobuf

* Fri Sep 28 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.0-2
- Add patch to correctly detect gtest using pkg-config

* Sun Sep 23 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Tue Sep 11 2018 Neal Gompa <ngompa13@gmail.com> - 0.32.1-2
- Rebuild for gtest 1.8.1

* Sun Aug 26 2018 Neal Gompa <ngompa13@gmail.com> - 0.32.1-1
- Update to 0.32.1 (RH#1570223)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.31.1-2
- Rebuilt for Python 3.7

* Sat Mar 31 2018 Neal Gompa <ngompa13@gmail.com> - 0.31.1-1
- Update to 0.31.1 (RH#1562271)
- Drop upstreamed patch to fix disabling LTO for ppc64 builds

* Wed Mar 21 2018 Neal Gompa <ngompa13@gmail.com> - 0.31.0.1-1
- Update to 0.31.0.1 (RH#1558534)
- Drop conditionals and scriptlets for Fedora < 28
- Add patch to fix disabling LTO for ppc64 builds
- Drop upstreamed patch for mir-perf-framework

* Mon Feb 19 2018 Neal Gompa <ngompa13@gmail.com> - 0.30.0.1-1
- Update to 0.30.0.1 (RH#1546741)

* Sat Feb 17 2018 Neal Gompa <ngompa13@gmail.com> - 0.30.0-1
- Update to 0.30.0 (RH#1545646)
- Switch to build with ninja
- Add patch to fix versioning of mir-perf-framework
- Switch to macroized ldconfig scriptlets

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.0-2
- Remove obsolete scriptlets

* Sun Dec 17 2017 Neal Gompa <ngompa13@gmail.com> - 0.29.0-1
- Update to 0.29.0 (RH#1526660)
- Enable building and shipping tests for Fedora 27+

* Mon Nov 20 2017 Neal Gompa <ngompa13@gmail.com> - 0.28.1-1
- Initial import into Fedora (RH#1513512)

* Sat Nov 18 2017 Neal Gompa <ngompa13@gmail.com> - 0.28.1-0.3
- Add scriptlets for updating icon cache to mir-demos
- Add hicolor-icon-theme dependency to mir-demos
- Validate the desktop file shipped in mir-demos
- Declare which subpackages own Mir library subdirectories

* Fri Nov 17 2017 Neal Gompa <ngompa13@gmail.com> - 0.28.1-0.2
- Add patch to fix building with libprotobuf 3.4.1

* Wed Nov 15 2017 Neal Gompa <ngompa13@gmail.com> - 0.28.1-0.1
- Rebase to 0.28.1
- Add patch to fix installing the perf framework
- Add patch to fix locating Google Mock for building Mir

* Sat Apr 15 2017 Neal Gompa <ngompa13@gmail.com> - 0.26.2-0.1
- Rebase to 0.26.2

* Wed Nov  9 2016 Neal Gompa <ngompa13@gmail.com> - 0.24.1-0.2
- Add patch to add missing xkbcommon Requires to mirclient.pc

* Mon Oct 31 2016 Neal Gompa <ngompa13@gmail.com> - 0.24.1-0.1
- Initial packaging
