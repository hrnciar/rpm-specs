%global appname io.elementary.wingpanel

%global common_description %{expand:
Stylish top panel that holds indicators and spawns an application
launcher.}

Name:           wingpanel
Summary:        Stylish top panel
Version:        2.3.2
Release:        4%{?dist}
License:        GPLv2+

URL:            https://github.com/elementary/wingpanel
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-initial-support-for-libmutter-7-mutter-3.38.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.24.0

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(gala)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# wingpanel ayatana appindicator support was abandoned by upstream
# wingpanel-indicator-ayatana-2.0.3-10.fc32 retired for fedora 33+
Obsoletes:      wingpanel-indicator-ayatana < 2.0.3-11

%description %{common_description}


%package        libs
Summary:        Stylish top panel (shared library)
%description    libs %{common_description}

This package contains the shared library.


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains the files required for developing for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang wingpanel

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f wingpanel.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/wingpanel

%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%files libs
%license COPYING
%doc README.md

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_libdir}/libwingpanel-2.0.so.0
%{_libdir}/libwingpanel-2.0.so.0.2.0


%files devel
%license COPYING
%doc README.md

%{_includedir}/wingpanel-2.0/

%{_libdir}/libwingpanel-2.0.so
%{_libdir}/pkgconfig/wingpanel-2.0.pc

%{_datadir}/vala/vapi/wingpanel-2.0.deps
%{_datadir}/vala/vapi/wingpanel-2.0.vapi


%changelog
* Sat Aug 29 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-4
- Add patch for initial mutter 3.38 support.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-1
- Update to version 2.3.2.

* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-3
- Obsolete the retired wingpanel-indicator-ayatana package.

* Mon Apr 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-2
- Rebuild for gala 3.3.0 and mutter 3.36.

* Mon Apr 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-2.20200313.git88305e0
- Bump to commit 88305e0.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.6-1
- Update to version 2.2.6.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.5-1
- Update to version 2.2.5.

* Wed Apr 24 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.4-1
- Update to version 2.2.4.

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.2.3-2
- Rebuild with Meson fix for #1699099

* Mon Mar 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.3-1
- Update to version 2.2.3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.2-1
- Update to version 2.2.2.

* Thu Dec 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Sun Sep 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-4
- Rebuild for gala mutter328 support.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-2
- Add missing BR: gcc, gcc-c++.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.1-1
- Update to version 2.1.1.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Rebuild for granite5 soname bump.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-6
- Add patch to support and bump release for mutter 3.28.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-4
- Include upstream patch to fix undefined symbols.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-3
- Remove icon cache scriptlets, replaced by file triggers.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-2
- Rebuild for granite soname bump.

* Wed Sep 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.4-1
- Update to version 2.0.4.

* Mon Sep 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-5.20170902.git434f674
- Bump to commit 434f674, which includes fixes for the latest mutter.

* Sat Sep 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-4.20170901.git7a1a583
- Bump to commit 7a1a583, which includes support for the latest mutter.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Update to version 2.0.3.

* Sat Apr 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-2
- Create and own missing settings directory.

* Fri Mar 17 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1
- Update to version 2.0.2.
- Remove upstreamed patches.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-12
- Rebuild for new gala snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-10
- Add patch to fix pkgconfig file.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-9
- Create and own plugin directory.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-8
- Split off -libs subpackage.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-7
- Don't let COPYING be executable.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-6
- Clean up spec file.

* Thu Nov 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-5
- Add rpath workaround for f25.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-2
- Spec file cosmetics.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Fri Aug 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.4-1
- Update to version 0.4.

