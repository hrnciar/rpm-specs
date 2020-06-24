%global uuid    org.%{name}.%{name}

Name:           corectrl
Version:        1.1.0
Release:        1%{?dist}
Summary:        Friendly hardware control

# The entire source code is GPLv3+ except bundled libs:
# * Boost:          tests/3rdparty/catch
#                   tests/3rdparty/trompeloeil
# * BSD:            3rdparty/fmt
# * MIT:            3rdparty/easyloggingpp
#                   3rdparty/pugixml
#                   3rdparty/units
# * Public Domain   FindBotan.cmake
License:        GPLv3+ and Boost and BSD and MIT and Public Domain
URL:            https://gitlab.com/corectrl/corectrl
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        README.fedora.md

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libdrm-devel
BuildRequires:  ninja-build
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(x11)

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}
Requires:       qca-qt5-ossl%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}

# Used to gather more information
# * For glxinfo
Recommends:     mesa-demos%{?_isa}

# * For lscpu
Recommends:     util-linux%{?_isa}

# * For vulkaninfo
Recommends:     vulkan-tools%{?_isa}

# https://gitlab.com/corectrl/corectrl/issues/13
Provides:       bundled(easyloggingpp) = 9.96.7
Provides:       bundled(fmt) = 5.2.1
Provides:       bundled(pugixml) = 1.9
Provides:       bundled(units)

%description
CoreCtrl is a Free and Open Source GNU/Linux application that allows you to
control with ease your computer hardware using application profiles. It aims to
be flexible, comfortable and accessible to regular users.

- For setup instructions run:

  xdg-open %{_docdir}/%{name}/README.fedora.md

- or go to the project wiki:

  https://gitlab.com/corectrl/corectrl/wikis


%prep
%autosetup -n %{name}-v%{version} -p1

# 'lib64' path fix
sed -e 's@DESTINATION lib@DESTINATION %{_lib}@g' -i src/CMakeLists.txt

# lib soversion fix
echo "set_property(TARGET corectrl_lib PROPERTY SOVERSION 0)" >> src/CMakeLists.txt

mkdir -p %{_target_platform}


%build
pushd %{_target_platform}
    %cmake -G Ninja                     \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo   \
    -DBUILD_TESTING=ON                  \
    ..
popd
%ninja_build -C %{_target_platform}


%install
%ninja_install -C %{_target_platform}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.fedora.md
find README.md -type f -perm /111 -exec chmod 644 {} \;
find %{buildroot}/%{_datadir}/. -type f -executable -exec chmod -x "{}" \;

# Useless symlink without headers
rm %{buildroot}/%{_libdir}/libcorectrl.so


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING LICENSE
%doc README.md README.fedora.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/polkit-1/actions/*.policy
%{_libdir}/libcorectrl.so.0*
%{_libexecdir}/kf5/kauth/*
%{_metainfodir}/*.xml

%if 0%{?fedora} < 30
%{_sysconfdir}/dbus-1/system.d/*.conf
%endif


%changelog
* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Disable LTO

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.9-1
- Update to 1.0.9 (basically the same as previous build but now patch upstreamed)

* Mon Mar 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.7-2
- Add new missed BR dep: libdrm-devel

* Sat Nov 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.6-2
- Remove '$(nproc)' from '-flto' for reproducible builds
- Tiny cosmetic spec file fixes

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.5-1
- Update to 1.0.5
- App summary more descriptive now (upstream suggestion)

* Wed Jul 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.4-4
- Update to 1.0.4

* Mon Jul 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-15
- Initial package
- Thanks to Dead_Mozay <dead_mozay@opensuse.org> for initial spec file
- Thanks to Vitaly Zaitsev <vitaly@easycoding.org> for significant help with packaging and review
