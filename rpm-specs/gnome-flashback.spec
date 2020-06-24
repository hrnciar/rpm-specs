# Build with Compiz session
# * Disable due minimum 'libcompizconfig' >= 0.9.14.0 version
%bcond_with compiz_session

Name:           gnome-flashback
Version:        3.36.3
Release:        5%{?dist}
Summary:        GNOME Flashback session

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        https://download.gnome.org/sources/%{name}/3.36/%{name}-%{version}.tar.xz
Source1:        gnome-flashback.pamd

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.2
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.31.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.13
BuildRequires:  pkgconfig(libgnome-panel) >= 3.35.2
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.97
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi) >= 1.6.0
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
BuildRequires:  pkgconfig(xxf86vm) >= 1.1.4
%if %{with compiz_session}
BuildRequires:  pkgconfig(compiz)
BuildRequires:  pkgconfig(libcompizconfig) >= 0.9.14.0
%endif

Requires:       gnome-applets%{?_isa}
Requires:       gnome-keyring%{?_isa}
Requires:       gnome-panel%{?_isa}
Requires:       gnome-session%{?_isa}
Requires:       gnome-settings-daemon%{?_isa}
Requires:       metacity%{?_isa}

Recommends:     alacarte
Recommends:     nautilus%{?_isa}
Recommends:     network-manager-applet%{?_isa}

%if %{with compiz_session}
Suggests:       compiz%{?_isa}
%endif

%description
GNOME Flashback is a session for GNOME 3 which was initially called "GNOME
Fallback", and shipped as a stand-alone session in Debian and Ubuntu. It
provides a similar user experience to the GNOME 2.x series sessions. The
differences to the MATE project is that GNOME Flashback uses GTK+ 3 and tries to
follow the current GNOME development by integrating recent changes of the GNOME
libraries. The development currently lags behind a little but a lot of progress
has been made and most importantly many open bugs have been fixed.


%prep
%autosetup -p1


%build
%if %{with compiz_session}
%configure --with-compiz-session
%else
%configure
%endif
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete;
%find_lang %{name}

install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/%{name}


%check
# Disable temporary
# * https://gitlab.freedesktop.org/xdg/desktop-file-utils/-/merge_requests/2
# * https://gitlab.freedesktop.org/xdg/xdg-specs/-/merge_requests/5
%dnl desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service


%files -f %{name}.lang
%license COPYING
%doc NEWS
%config %{_sysconfdir}/pam.d/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/glib-2.0/schemas/*.gschema.override
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.desktop.enums.xml
%{_datadir}/gnome-panel/layouts/%{name}.layout
%{_datadir}/gnome-session/sessions/%{name}-metacity.session
%{_datadir}/xsessions/%{name}-metacity.desktop
%{_libdir}/gnome-panel/modules/system_indicators.so
%{_libexecdir}/%{name}-clipboard
%{_libexecdir}/%{name}-metacity
%{_sysconfdir}/xdg/autostart/%{name}-clipboard.desktop
%{_sysconfdir}/xdg/autostart/%{name}-nm-applet.desktop
%{_sysconfdir}/xdg/menus/%{name}-applications.menu
%{_userunitdir}/*%{name}*

%if %{with compiz_session}
%{_datadir}/gnome-session/sessions/%{name}-compiz.session
%{_datadir}/xsessions/%{name}-compiz.desktop
%{_libexecdir}/%{name}-compiz
%endif


%changelog
* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.3-5
- Rebuilt | https://pagure.io/koji/issue/2286

* Wed May 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.3-4
- Add weak dep: alacarte

* Tue May 26 2020 Yaakov Selkowitz <yselkowi@redhat.com> - 3.36.3-3
- Add PAM file | Fix RH#1840146

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.3-2
- Disable LTO

* Sat May 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.3-1
- Update to 3.36.3

* Tue Apr 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.1-1
- Update to 3.36.1

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.0-2
- Backport upstream patch for memory leak fix | gnome-panel#21

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.36.0-1
- Update to 3.36.0

* Sun Feb 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.34.2-4
- Spec file improvements
- Drop obsolete macroses
- Enable LTO

* Thu Dec 26 2019 Yaakov Selkowitz <yselkowi@redhat.com> - 3.34.2-1
- new version

* Sun May 05 2019 Yaakov Selkowitz <yselkowi@redhat.com> - 3.32.0-1
- new version

* Mon Nov 12 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 3.30.0-1
- new version

* Mon Mar 26 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 3.28.0-1
- new version

* Mon Nov 13 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 3.26.0-1
- new version

* Tue Mar 28 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 3.24.0-1
- new version

* Sun Mar 26 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 3.22.1-1
- new version

* Thu Oct 06 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.22.0-1
- new version

* Mon Sep 12 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20.2-1
- new version

* Wed May 18 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20.1-1
- new version

* Thu Apr 14 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20.0-1
- new version for GNOME Flashback 3.20.

* Thu Oct 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Oct 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.0-1
- Update for GNOME Flashback 3.18.

* Mon Aug 24 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.17.2-2
- Fix crash in display-config (BGO#753927)

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.17.2-1
- Unstable version bump

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-3
- Add polkit-gnome autostart

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-2
- Add upstream fix for BGO#738562

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-1
- Update for GNOME 3.16.

* Fri Feb 27 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-4
- Fix for BGO#738562

* Mon Feb 23 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-3
- Requires: gnome-screensaver

* Tue Feb 10 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-2
- Fix deps

* Mon Feb 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-1
- Update for GNOME 3.14.

* Mon Jan 12 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.10.0-1
- Initial release.
