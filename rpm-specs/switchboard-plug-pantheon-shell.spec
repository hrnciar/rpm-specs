%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name pantheon-desktop
%global plug_rdnn io.elementary.switchboard.pantheon-shell

Name:           switchboard-plug-pantheon-shell
Summary:        Switchboard Pantheon Shell plug
Version:        2.8.4
Release:        2%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       contractor
Requires:       gala
Requires:       tumbler
Requires:       wingpanel

Requires:       switchboard%{?_isa}
Supplements:    (switchboard%{?_isa} and gala and wingpanel)


%description
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other
desktop settings such as the panel, app launcher, and window manager.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.contract.set-wallpaper

%{_datadir}/contractor/set-wallpaper.contract
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.8.4-1
- Update to version 2.8.4.

* Wed Apr 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.8.3-1
- Update t oversion 2.8.3.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 2.8.2-2
- Rebuilt for libgnome-desktop soname bump

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.2-1
- Update to version 2.8.2.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 2.8.1-3
- Rebuilt for libgnome-desktop soname bump

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.8.1-2
- Rebuild with Meson fix for #1699099

* Sat Mar 30 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.1-1
- Update to version 2.8.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.8.0-1
- Update to version 2.8.0.

* Wed Nov 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.2-1
- Update to version 2.7.2.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.7.1-1
- Update to version 2.7.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.7-3
- Add missing tumbler dependency.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.7-2
- Rebuild for granite5 soname bump.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.7-1
- Update to version 0.2.7.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-7
- Rebuild for gnome-desktop3 soname bump.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-5
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-4
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.6-1
- Update to version 0.2.6.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1.20170519.git8f0b853
- Bump to commit 8f0b853, fixing compilation with CMake 3.8 and vala 0.35+.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Update to version 0.2.5.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-3
- Mass rebuild.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-2
- Spec file cosmetics.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.

