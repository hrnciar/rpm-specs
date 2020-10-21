# libgnome-volume-control
# * This project is only intended to be used as a subproject
%global gvc_commit      e2be83ee4a47da9c4c4fbf302a63f04b8d5683b9
%global gvc_shortcommit %(c=%{gvc_commit}; echo ${c:0:7})

Name:           wf-shell
Version:        0.5.0
Release:        1%{?dist}
Summary:        GTK3-based panel for wayfire

License:        MIT
URL:            https://github.com/WayfireWM/wf-shell
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/GNOME/libgnome-volume-control/tarball/%{gvc_commit}#/gvc-%{gvc_shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.1
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config) >= 0.5.0

Provides:       bundled(gvc) = 0.git%{gvc_shortcommit}

%description
wf-shell is a repository which contains the various components needed to built a
fully functional DE based around wayfire. Currently it has only a GTK-based
panel and background client.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1
%autosetup -D -T -a1
mv GNOME-libgnome-volume-control-%{gvc_shortcommit}/* \
    %{_builddir}/%{name}-%{version}/subprojects/gvc


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md %{name}.ini.example
%{_bindir}/wf-background
%{_bindir}/wf-dock
%{_bindir}/wf-panel
%{_datadir}/wayfire/

%files devel
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Update 0.5.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-2
- Add example configuration file
- Enable LTO

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update 0.4.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20190930gitb240566
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-4.20190930gitb240566
- Update to latest git snapshot

* Fri Sep 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1-3.20190916gitb26f5f3
- Tiny fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
