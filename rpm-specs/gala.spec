%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Summary:        Gala window manager
Version:        3.3.2
Release:        4%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Include a patch to set some default settings to better match fedora
Patch1:         0001-fedora-default-settings.patch

# initial port to mutter 3.38 with some ugly hacks to make it compile
Patch2:         0002-meson-initial-support-for-libmutter-7-mutter-3.38.patch
Patch3:         0003-adapt-to-mutter-3.38-API-changes.patch
Patch4:         0004-BackgroundSource-use-map-values-not-map-entries.patch
Patch5:         0005-ugly-hack-for-removed-Clutter.Stage.capture-method.patch
Patch6:         0006-fix-for-new-Clutter.Actor.allocate_preferred_size-me.patch
Patch7:         0007-ugly-hack-for-removed-Cogl.Path.patch
Patch8:         0008-ugly-hack-for-removed-Meta.BackgroundManager-members.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.0
BuildRequires:  vala >= 0.28.0

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.15.2
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(mutter-clutter-7)
BuildRequires:  pkgconfig(mutter-cogl-7)
BuildRequires:  pkgconfig(mutter-cogl-pango-7)
BuildRequires:  pkgconfig(plank) >= 0.11.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# gala provides a generic icon (apps/multitasking-view)
Requires:       hicolor-icon-theme

# gala's multitasking view is activated via dbus
Requires:       dbus-tools

# gala relies on the new notification server
Requires:       elementary-notifications


%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        libs
Summary:        Gala window manager libraries

%description    libs
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the shared libraries.


%package        devel
Summary:        Gala window manager development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang gala


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/gala-daemon.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f gala.lang
%doc AUTHORS README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/gala-daemon.desktop

%{_bindir}/gala
%{_bindir}/gala-daemon

%{_libdir}/gala/plugins/*

%{_datadir}/applications/gala*.desktop
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg
%{_datadir}/metainfo/%{name}.appdata.xml


%files libs
%doc AUTHORS README.md
%license COPYING

%dir %{_libdir}/gala
%dir %{_libdir}/gala/plugins

%{_libdir}/libgala.so.0*


%files devel
%doc AUTHORS README.md
%license COPYING

%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Sat Aug 29 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.2-4
- Initial port to mutter 3.38 (uglyyy hacks inside).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.2-1
- Update to version 3.3.2.

* Sat Apr 25 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.1-1
- Update to version 3.3.1.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-1
- Update to version 3.3.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.2.0-2
- Rebuilt for libgnome-desktop soname bump

* Wed Jan 08 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.31.20190712.gita790d2d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 0.3.1-0.30.20190712.gita790d2d
- Rebuilt for libgnome-desktop soname bump

* Tue Jul 16 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.29.20190712.gita790d2d
- Bump to commit a790d2d.

* Wed Jul 03 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.28.20190701.git5f1dbf1
- Bump to commit 5f1dbf1.

* Sat Jun 01 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.27.20190531.git1024813
- Bump to commit 1024813.

* Mon May 20 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.26.20190514.git3ae100d
- Bump to commit 3ae100d.

* Sat May 11 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.25.20190511.git4459c59
- Bump to commit 4459c59.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.3.1-0.24.20190307.git2c610b3
- Rebuild with Meson fix for #1699099

* Wed Mar 13 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.23.20190307.git2c610b3
- Bump to commit 2c610b3.

* Sun Mar 03 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.22.20190302.git395670e
- Bump to commit 395670e.

* Tue Feb 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.21.20190128.git1a96644
- Bump to commit 1a96644.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.20.20190128.git6654145
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.19.20190128.git6654145
- Bump to commit 6654145.

* Sun Dec 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.18.20181216.git7f1e392
- Bump to commit 7f1e392.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.17.20181205.git66a95e0
- Bump to commit 66a95e0.

* Mon Nov 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.16.20181122.gitcf8d455
- Bump to commit cf8d455.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.15.20181020.gita1bad26
- Bump to commit a1bad26.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.14.20181003.gitfeffbf8
- Make sure the right version of mutter is pulled in for builds.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.13.20181003.gitfeffbf8
- Bump to commit feffbf8.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.12.20180918.git9747bd6
- Bump to commit 9747bd6.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.11.20180910.git1970bac
- Bump to commit 1970bac.

* Wed Sep 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.10.20180910.git2995cd6
- Bump to commit 2995cd6.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.9.20180729.git15f722a
- Use mutter328 compat package for now.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.8.20180729.git15f722a
- Bump to commit 15f722a.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.7.20180710.git9502677
- Bump to commit 9502677.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-0.6.20180607.git985baa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.5.20180607.git985baa0
- Rebuild for granite5 soname bump.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.4.20180607.git985baa0
- Bump to commit 985baa0 and update default settings overrides.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.3.20180603.git3661cbd
- Bump to commit 3661cbd.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.2.20180430.gitf02b776
- Bump to commit f02b776.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-0.1.20180318.gita71e8c1
- Bump to version 0.3.1 snapshots, commit a71e8c1.
- Remove obsolete ldconfig scriptlets.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-2.20180314.git22f0d95
- Update to commit 22f0d95.

* Mon Mar 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-1.20180311.git6d3253a
- Update to commit 6d3253a and switch to meson.

* Thu Feb 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git146.22e1.1
- Update to latest snapshot (git 146-22e1).

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git141.f90f.2
- Rebuild for libgnome-desktop soname bump.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.git141.f90f.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git141.f90f.1
- Update to latest snapshot (git 141-f90f).

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git140.d76c.1
- Update to latest snapshot (git 140-d76c).

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git139.439f.3
- Remove icon cache scriptlets, replaced by file triggers.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git139.439f.2
- Add patch so window buttons match fedora's default layout.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git139.439f.1
- Update to latest snapshot (git 139-439f).

* Tue Nov 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git138.a82b.1
- Update to latest snapshot (git 138-a82b).

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git136.60ee.2
- Rebuild for granite soname bump.

* Fri Oct 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git136.60ee.1
- Update to latest snapshot (git 136-60ee).

* Thu Sep 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git126.4fe5.1
- Update to latest snapshot (git 126-4fe5).

* Wed Aug 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git124.cd28.1
- Update to latest snapshot (git 124-cd28).

* Sat Aug 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git120.87f5a.1
- Update to latest snapshot (git 120-87f5a).

* Mon Jul 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.git119.c7d5.1
- Update to latest snapshot (git 119-c7d5).

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.bzr567.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr567.1
- Update to latest snapshot (rev 567).
- De-remove other configurations, now the .desktop files are valid again.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr562.1
- Update to latest snapshot (rev 562).
- Filter provides to exclude internal plugins.
- Remove explicit pkgconfig BR.
- Remove unsupported / broken configurations.
- Fix build with mutter-3.24.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.bzr552.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.4
- Make BR on /usr/bin/pkg-config explicit.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.3
- Put plugins and the plugin directory into the right respective subpackages.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.2
- Make sure no *.la files are in the packages.

* Thu Jan 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-0.bzr552.1
- Initial package.

