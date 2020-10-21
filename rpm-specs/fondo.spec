%global uuid    com.github.calo001.%{name}

Name:           fondo
Version:        1.3.10
Release:        1%{?dist}
Summary:        Find the most beautiful wallpapers

License:        AGPLv3+
URL:            https://github.com/calo001/fondo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(unity)

Requires:       hicolor-icon-theme

%description
Find a variety of the most beautiful wallpapers from Unsplash.com the world’s
most generous community of photographers.

Fondo allows you to see thousands of beautiful photographs from the most recent
to the one you are to looking for. Give a simple click on a picture to set as
wallpaper, wait until the download is complete and enjoy!

Have a simple and elegant interface, you can change from light mode to dark mode
as you prefer.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE.md
%doc README.md AUTHORS.md
%{_bindir}/%{uuid}
%{_datadir}/Fondo/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*.png
%{_metainfodir}/*.xml


%changelog
* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.10-1
- build(update): 1.3.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.9-1
- Update to 1.3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.8-1
- Update to 1.3.8

* Thu Sep 19 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3.20190622git5961af1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.2-2.20190622git5961af1
- Update to 1.3.2-20190622git5961af1

* Mon Jun 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1.20190617git581faa5
- Update to 1.3.0-20190617git581faa5

* Fri Jun 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.4-2.20190515gitdd012ec
- Update to 1.2.4-1.20190515gitdd012ec

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.2.2-4.20190324git71d97ee
- Rebuild with Meson fix for #1699099

* Fri Mar 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.2-3.20190324git71d97ee
- Initial Package
