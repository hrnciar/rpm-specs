%global commit  6abef18306271aafe0e9834bced8aa637063b8cb
%global oldname %{name}-updater
%global uuid    org.gnome.Firmware

Name:           gnome-firmware
Version:        3.36.0
Release:        4%{?dist}
Summary:        Install firmware on devices

License:        GPLv2
URL:            https://gitlab.gnome.org/hughsie/gnome-firmware-updater
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.0
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(fwupd) >= 1.2.10
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.51.92
BuildRequires:  pkgconfig(xmlb) >= 0.1.7
Requires:       hicolor-icon-theme
# Temporary added
Obsoletes:      %{oldname} < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{oldname} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This application can:

- Upgrade, Downgrade, & Reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson -Dman=true
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md MAINTAINERS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1.*
%{_metainfodir}/*.xml

%changelog
* Wed Aug 19 2020 Mohan Boddu <mboddu@bhujji.com> - 3.36.0-4
- Rebuild for the libxmlb API bump.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Richard Hughes <rhughes@redhat.com> - 3.36.0-1
- New upstream release
- Dynamically show verify and releases buttons
- Show device and progress when doing updates
- Show the release issues if supplied in the metadata

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.0-4
- Update to 3.34.0

* Wed Sep 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20190911git9d823d8
- Update to latest git snapshot

* Wed Aug 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20190827gitd5014ed
- Initial package

