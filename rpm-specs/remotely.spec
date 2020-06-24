%global commit      10d00345a6824a250e93a20c974f9493281d69b4
%global file_name   de.haeckerfelix.Remotely

Name:           remotely
Version:        1.0
Release:        3%{?dist}
Summary:        Simple VNC viewer for the GNOME desktop environment

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/Remotely
Source0:        %{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.10
BuildRequires:  pkgconfig(gtk-vnc-2.0)

Requires:       hicolor-icon-theme

%description
Remotely is a simple VNC viewer for the GNOME desktop environment. It supports
common authentication methods. The display can be adjusted with three different
modes so that the most optimal presentation is always possible, regardless of
the remote display size.

%prep
%autosetup -n Remotely-v%{version}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{file_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{file_name}.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{file_name}.desktop
%{_datadir}/glib-2.0/schemas/%{file_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{file_name}.appdata.xml

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-1
- Initial package
