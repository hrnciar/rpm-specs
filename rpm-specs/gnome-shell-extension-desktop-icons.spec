%global extid   %{extname}@csoriano
%global extname desktop-icons
%global uuid    org.gnome.shell.extensions.%{extname}

Name:           gnome-shell-extension-%{extname}
Version:        20.04.0
Release:        1%{?dist}
Summary:        GNOME Shell extension for providing desktop icons

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/ShellExtensions/desktop-icons
Source0:        %{url}/-/archive/%{version}/%{extname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  meson

Requires:       gnome-shell
Requires:       nautilus >= 3.30.4
Requires:       xdg-desktop-portal-gtk

%description
This package provides a GNOME Shell extension for showing the contents of
~/Desktop on the desktop of the Shell. Common file management operations such as
launching, copy/paste, rename and deleting are supported.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %{extid}


%prep
%autosetup -n %{extname}-%{version}
sed -e "/meson_post_install/d" -i meson.build


%build
%meson --localedir=%{_datadir}/locale
%meson_build


%install
%meson_install
%find_lang %{extname}


%files -f %{extname}.lang
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/gnome-shell/extensions/%{extid}/


%changelog
* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.0-1
- Update to 20.04.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.2-1
- Update to 19.10.2

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.1-1
- Update to 19.10.1

* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.01.4-4
- Initial package

