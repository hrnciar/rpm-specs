Name:           xmonad-log-applet
Version:        2.1.0
Release:        21%{?dist}
Summary:        Panel applet to display Xmonad log information
License:        BSD
URL:            https://github.com/alexkay/xmonad-log-applet
Source0:        http://xmonad-log-applet.googlecode.com/files/%{name}-%{version}.tar.gz
# Trivial patch to configure.ac only -- there was no API breakage, apparently
Patch1:         0001-update-to-libmatepanelapplet-4.0.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0)

%description
xmonad-log-applet is for Xmonad users who find the XFCE or MATE panel useful.
The applet will show the active workspaces, the title of the selected window,
or any other information you send it from your xmonad.hs.

%package xfce
Summary:        XFCE panel plugin to display Xmonad log information
Conflicts:      %{name}-mate < %{version}-%{release}
# for directory ownership:
Requires:       xfce4-panel

%description xfce
xmonad-log-applet is for Xmonad users who find the XFCE panel useful.
The applet will show the active workspaces, the title of the selected window,
or any other information you send it from your xmonad.hs.

%package mate
Summary:        MATE panel applet to display Xmonad log information
Conflicts:      %{name}-xfce < %{version}-%{release}
# for directory ownership:
Requires:       mate-panel

%description mate
xmonad-log-applet is for Xmonad users who find the MATE panel useful.
The applet will show the active workspaces, the title of the selected window,
or any other information you send it from your xmonad.hs.

%prep
%autosetup -p1
mkdir build-{xfce4,mate}

%build
# The upstream build only allows selecting one desktop environment, but 
# we would like to package both. So we run the build two times.
%global _configure ../configure

(
  cd build-xfce4
  %configure --cache-file=../config.cache --with-panel=xfce4
)

(
  cd build-mate
  %configure --cache-file=../config.cache --with-panel=mate
)

%make_build -C build-xfce4
%make_build -C build-mate

%install
%make_install -C build-xfce4
%make_install -C build-mate

%files xfce
%doc README.md LICENSE AUTHORS.md
%{_libdir}/xfce4/panel/plugins/%{name}
%{_datadir}/xfce4/panel-plugins/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files mate
%doc README.md LICENSE AUTHORS.md
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.mate.panel.applet.XmonadLogAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.panel.XmonadLogApplet.mate-panel-applet
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-15
- Remove obsolete scriptlets

* Wed Aug 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-14
- Do not go outside of build directory created by RPM

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Kevin Fenzi <kevin@scrye.com> 2.1.0-8
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Dan Callaghan <dcallagh@redhat.com> 2.1.0-5
- avoid using autotools during RPM build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-3
- Drop gnome-panel support as no longer supported

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Dan Callaghan <dcallagh@redhat.com> 2.1.0-1
- new upstream release 2.1.0: adds MATE support, no other changes

* Mon Sep 03 2012 Dan Callaghan <dcallagh@redhat.com> 2.0.0-3
- added explicit Requires for directory ownership

* Mon Aug 27 2012 Dan Callaghan <dcallagh@redhat.com> 2.0.0-2
- build both GNOME and XFCE versions

* Sat Apr 21 2012 Dan Callaghan <dcallagh@redhat.com> 2.0.0-1
- initial version
