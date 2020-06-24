%bcond_without clang

%if %{with clang}
%global optflags %(echo %{optflags} | sed -e 's/-mcet//g' -e 's/-fcf-protection//g' -e 's/-fstack-clash-protection//g' -e 's/$/ -Qunused-arguments -Wno-unknown-warning-option -Wno-deprecated-declarations/')
%endif

Name: nheko
Version: 0.7.2
Release: 1%{?dist}

Summary: Desktop client for the Matrix protocol
License: GPLv3+
URL: https://github.com/Nheko-Reborn/nheko
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/Nheko-Reborn/nheko/pull/220
Patch100: %{name}-themes-fix.patch

BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5QuickCompiler)
BuildRequires: cmake(Qt5QuickControls2)

BuildRequires: mtxclient-devel >= 0.3.1
BuildRequires: spdlog-devel >= 0.16
BuildRequires: boost-devel >= 1.70
BuildRequires: json-devel >= 3.1.2
BuildRequires: mpark-variant-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libsodium-devel
BuildRequires: openssl-devel
BuildRequires: libolm-devel
BuildRequires: tweeny-devel
BuildRequires: lmdbxx-devel
BuildRequires: ninja-build
BuildRequires: cmark-devel
BuildRequires: lmdb-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%if %{with clang}
BuildRequires: compiler-rt
BuildRequires: clang
BuildRequires: llvm
%endif

Requires: hicolor-icon-theme

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app.

%prep
%autosetup -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
%if %{with clang}
    -DCMAKE_C_COMPILER=%{_bindir}/clang \
    -DCMAKE_CXX_COMPILER=%{_bindir}/clang++ \
    -DCMAKE_AR=%{_bindir}/llvm-ar \
    -DCMAKE_RANLIB=%{_bindir}/llvm-ranlib \
    -DCMAKE_LINKER=%{_bindir}/llvm-ld \
    -DCMAKE_OBJDUMP=%{_bindir}/llvm-objdump \
    -DCMAKE_NM=%{_bindir}/llvm-nm \
%else
    -DCMAKE_AR=%{_bindir}/gcc-ar \
    -DCMAKE_RANLIB=%{_bindir}/gcc-ranlib \
    -DCMAKE_NM=%{_bindir}/gcc-nm \
%endif
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DUSE_BUNDLED_BOOST:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_CMARK:BOOL=OFF \
    -DUSE_BUNDLED_MTXCLIENT:BOOL=OFF \
    -DUSE_BUNDLED_LMDB:BOOL=OFF \
    -DUSE_BUNDLED_LMDBXX:BOOL=OFF \
    -DUSE_BUNDLED_TWEENY:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_SODIUM:BOOL=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Sun Jun 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.2-1
- Updated to version 0.7.2.

* Wed Jun 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.1-1
- Updated to version 0.7.1.

* Sun May 31 2020 Jonathan Wakely <jwakely@redhat.com> - 0.6.4-5
- Rebuilt for Boost 1.73

* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.4-4
- Rebuit due to cmark update.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.4-1
- Updated to version 0.6.4.

* Sun Feb 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-1
- Switched upstream to a new maintained fork.
- Updated to version 0.6.3.

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0.6.2-4
- Rebuilt for Boost 1.69

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-3
- Rebuilt due to libolm update.

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-2
- Backported patch with localization update from maintained fork.

* Sun Oct 07 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-1
- Updated to version 0.6.2.

* Wed Sep 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-2
- Fixed bogus changelog entry.

* Wed Sep 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Sat Sep 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Sun Sep 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.5-1
- Updated to version 0.5.5.

* Wed Aug 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.4-1
- Updated to version 0.5.4.

* Wed Aug 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-2
- Backported patch with crash fix on logout.

* Sun Aug 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-1
- Updated to version 0.5.3.

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.2-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-1
- Updated to version 0.5.2.

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-2
- Rebuild for new binutils

* Thu Jul 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.3-2
- Fixed issue with system shutdown on KDE Plasma.

* Sun Jun 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.3-1
- Updated to version 0.4.3.

* Fri May 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.2-1
- Updated to version 0.4.2.

* Thu May 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Fri May 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Fri Apr 13 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.1-1
- Updated to version 0.3.1.

* Tue Apr 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Wed Mar 14 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.1-1
- Updated to version 0.2.1.

* Mon Mar 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Thu Dec 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Updated to version 0.1.0.

* Mon Sep 25 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170924git9def76a
- Initial SPEC release.
