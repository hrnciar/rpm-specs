# Git submodules
# * wf-utils
%global commit1 f9b5eba437a04a0d1fb9f00a0fdb88c12b9f6b27
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           wayfire
Version:        0.5.0
Release:        1%{?dist}
Summary:        3D wayland compositor

License:        MIT
URL:            https://github.com/WayfireWM/wayfire
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/WayfireWM/wf-utils/archive/%{commit1}/wf-utils-%{shortcommit1}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wf-config) >= 0.5.0
BuildRequires:  pkgconfig(wlroots) >= 0.11.0
BuildRequires:  pkgconfig(xkbcommon)

Recommends:     wayfire-config-manager%{?_isa}
Recommends:     wf-shell%{?_isa}

Suggests:       lavalauncher%{?_isa}

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1
%autosetup -D -T -a1
mv wf-utils-%{commit1}/* subprojects/wf-utils/


%build
%meson \
    -Duse_system_wfconfig=enabled \
    -Duse_system_wlroots=enabled
%meson_build


%install
%meson_install
install -Dp -m0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop


%files
%license LICENSE
%doc README.md %{name}.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{name}/
%{_libdir}/libwf-utils.so.0*

%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/


%changelog
* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Sat Aug 01 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.0-5
- Add patch for wlroots 0.11.0 compatibility

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-2
- Add very weak dep: 'lavalauncher'
- Disable LTO

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20191001gitcec3540
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2-8.20191001gitcec3540
- Update to latest git snapshot

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2-6.20190510git5b91b87
- Unbundle 'wf-config'

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2-2.20190510git5b91b87
- Initial package
