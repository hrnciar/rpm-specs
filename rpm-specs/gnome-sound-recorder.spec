Name:           gnome-sound-recorder
Version:        3.34.0
Release:        2%{?dist}
Summary:        Make simple recordings from your desktop

License:        GPLv2+
URL:            https://wiki.gnome.org/Design/Apps/SoundRecorder
Source0:        https://download.gnome.org/sources/%{name}/3.34/%{name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

# Version requirement is for the first release with package.js.
Requires:       gjs >= 1.41.4
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description
Make simple recordings from your desktop.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.SoundRecorder.desktop

%files -f %{name}.lang
%doc AUTHORS README.md NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.SoundRecorder.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundRecorder.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.SoundRecorder-symbolic.svg
%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml
%{_datadir}/org.gnome.SoundRecorder/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 05 2019 David King <amigadave@amigadave.com> - 3.31.90-1
- Update to 3.31.90 (#1672566)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 David King <amigadave@amigadave.com> - 3.28.2-2
- Add patch to fix crash when selecting (#1667681)

* Fri Jan 11 2019 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Thu Nov 29 2018 David King <amigadave@amigadave.com> - 3.28.1-4
- Fix missing launcher icon (#1654687)

* Wed Oct  3 2018 Hans de Goede <hdegoede@redhat.com> - 3.28.1-3
- Fix gnome-sound-recorder not starting under Fedora 29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Feb 12 2018 David King <amigadave@amigadave.com> - 3.27.90-1
- Update to 3.27.90

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.24.0.1-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Kalev Lember <klember@redhat.com> - 3.24.0.1-1
- Update to 3.24.0.1

* Tue Mar 21 2017 David King <amigadave@amigadave.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92
- Don't set group tags

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Thu Apr 28 2016 David King <amigadave@amigadave.com> - 3.19.92-1
- Update to 3.19.92 (#1331379)

* Sun Feb 28 2016 David King <amigadave@amigadave.com> - 3.19.91-1
- Update to 3.19.91 (#1312642)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Wed Nov 11 2015 David King <amigadave@amigadave.com> - 3.18.2-1
- Update to 3.18.2 (#1279839)

* Fri Oct 30 2015 David King <amigadave@amigadave.com> - 3.18.1-2
- Add upstream patch to fix waveforms

* Tue Oct 13 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Mon Aug 17 2015 David King <amigadave@amigadave.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Thu Apr 30 2015 David King <amigadave@amigadave.com> - 3.17.1-1
- Update to 3.17.1

* Tue Mar 24 2015 David King <amigadave@amigadave.com> - 3.16.0-1
- Update to 3.16.0

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING
- Validate AppData in check

* Tue Dec 16 2014 David King <amigadave@amigadave.com> - 3.15.3-1
- Update to 3.15.3

* Sun Nov 09 2014 David King <amigadave@amigadave.com> - 3.14.2-1
- Update to 3.14.2

* Mon Sep 15 2014 David King <amigadave@amigadave.com> - 3.14.0.1-1
- Update to 3.14.01

* Mon Sep 15 2014 David King <amigadave@amigadave.com> - 3.14-1
- Update to 3.14

* Tue Sep 02 2014 David King <amigadave@amigadave.com> - 3.13.91-1
- Update to 3.13.91

* Tue Jul 22 2014 David King <amigadave@amigadave.com> - 3.13.4-1
- Update to 3.13.4
- Switch to noarch

* Wed Jul 16 2014 David King <amigadave@amigadave.com> - 3.12.2-3
- Add Audio to desktop file categories

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 David King <amigadave@amigadave.com> - 3.12.2-1
- Update to 3.12.2

* Mon Apr 14 2014 David King <amigadave@amigadave.com> - 3.12.1-1
- Update to 3.12.1

* Wed Mar 26 2014 David King <amigadave@amigadave.com> - 3.12.0-1
- Initial import (#1077810)
