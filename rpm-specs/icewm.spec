# Note: there is always trade off between build IceWM more like full DE or
# vanilla build.  One group of people ask for first one and pre-configured out
# of box another one for for second.

# https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds
%undefine __cmake_in_source_build

# Autotools/CMake
%bcond_with fallback_build_tool

%global awe_commit 91c9d4ba4374a309d4c0a527ea1e0c8b1e509a43
%global awe_shortcommit %(c=%{awe_commit}; echo ${c:0:7})

Name:           icewm
Version:        1.8.3
Release:        2%{?dist}
Summary:        Window manager designed for speed, usability, and consistency

License:        LGPLv2+
URL:            https://ice-wm.org/
Source0:        https://github.com/ice-wm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/tim77/awesome-%{name}/archive/%{awe_commit}/awesome-%{name}.git%{awe_shortcommit}.tar.gz

# For better font rendering on non HiDPI screens (very weak dep)
Source20:       local.conf
Source21:       gtkrc-2.0
Source22:       gkt3-settings.ini

Source30:       %{name}-startup

Patch0:         %{name}-keys.patch
Patch1:         %{name}-toolbar.patch
Patch2:         %{name}-menu.patch

%if %{with fallback_build_tool}
BuildRequires:  automake
BuildRequires:  autoconf
%else
BuildRequires:  cmake3
%endif

BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  perl-Pod-Html
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

Requires:       adwaita-icon-theme
Requires:       alsa-utils%{?_isa}
Requires:       %{name}-data = %{version}-%{release}
Requires:       xdg-utils

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-themes = %{version}-%{release}
Recommends:     abattis-cantarell-fonts
Recommends:     gnome-backgrounds

# Various additional useful tools
# * Display resolution control
Recommends:     lxrandr%{?_isa}

# * Launcher
Recommends:     rofi%{?_isa}

# * Volume control
Recommends:     volumeicon%{?_isa}

# * Screenshot
Recommends:     gnome-screenshot%{?_isa}

Recommends:     gnome-terminal%{?_isa}
Recommends:     network-manager-applet%{?_isa}

Suggests:       %{name}-fonts-settings = %{version}-%{release}
Suggests:       %{name}-minimal-session = %{version}-%{release}

# * https://github.com/bbidulock/icewm/issues/379
Suggests:       xterm%{?_isa}

# * Night mode
Suggests:       redshift-gtk%{?_isa}

# * Notification daemon
Suggests:       dunst%{?_isa}

# * For antiX like IceWM
Suggests:       conky%{?_isa}

# * Compositor for X11
Suggests:       picom%{?_isa}
%endif

%if 0%{?fedora}
# * Screen brightness control (not available in EPEL8 yet)
Recommends:     xbacklight%{?_isa}
%endif

%description
IceWM is a window manager for the X Window System (freedesktop, XFree86). The
goal of IceWM is speed, simplicity, and not getting in the user's way.

You can install minimal version of IceWM without all optional dependencies:

  sudo dnf install %{name}-minimal-session --setopt=install_weak_deps=False


# Data package
%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


# Themes package
%package        themes
Summary:        Extra themes for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    themes
Extra themes for %{name}.


# Minimal-session package
%package        minimal-session
Summary:        Minimal session for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    minimal-session
Minimal, lightweight session for %{name}.


# Fonts-settings package
%package        fonts-settings
Summary:        Font settings and tweaks for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    fonts-settings
Font settings and tweaks for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%setup -q -D -T -a1


%build
%if %{with fallback_build_tool}
#./autogen.sh
autoreconf -fiv
%configure \
    --with-xterm=%{_bindir}/gnome-terminal \
    --sysconfdir=%{_sysconfdir}/%{name}
%else
%cmake \
    -DCFGDIR=%{_sysconfdir}/%{name} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCONFIG_GDK_PIXBUF_XLIB=on \
    -DCONFIG_LIBPNG=on \
    -DCONFIG_LIBRSVG=on \
    -DCONFIG_XPM=on \
    -DXTERMCMD=%{_bindir}/gnome-terminal
%endif

%if %{with fallback_build_tool}
%make_build
%else
%cmake_build
%endif


%install
%if %{with fallback_build_tool}
%make_install
%else
%cmake_install
%endif

# Themes
cp -a awesome-%{name}-%{awe_commit}/themes/AntiX-collection/* %{buildroot}%{_datadir}/%{name}/themes/
cp -a awesome-%{name}-%{awe_commit}/themes/IceAdwaita-* %{buildroot}%{_datadir}/%{name}/themes/
install -m0644 -p awesome-%{name}-%{awe_commit}/distro-logos/fedora/icewm.xpm %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Small/taskbar/icewm.xpm
install -m0644 -p awesome-%{name}-%{awe_commit}/distro-logos/fedora/icewm-24.xpm %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Medium/taskbar/icewm.xpm
install -m0644 -p awesome-%{name}-%{awe_commit}/distro-logos/fedora/icewm-24.xpm %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Dark-Medium-alpha/taskbar/icewm.xpm
install -m0644 -p awesome-%{name}-%{awe_commit}/distro-logos/fedora/icewm-32.xpm %{buildroot}%{_datadir}/%{name}/themes/IceAdwaita-Large/taskbar/icewm.xpm

echo "Theme=\"IceAdwaita-Medium/default.theme\"" > %{buildroot}%{_datadir}/%{name}/theme

# Font settings
install -Dp -m0644 %{SOURCE20} %{buildroot}%{_sysconfdir}/fonts/local.conf
install -Dp -m0644 %{SOURCE21} %{buildroot}%{_sysconfdir}/gtk-2.0/gtkrc
install -Dp -m0644 %{SOURCE22} %{buildroot}%{_sysconfdir}/gtk-3.0/settings.ini

install -Dp -m0755 %{SOURCE30} %{buildroot}%{_datadir}/%{name}/startup

%find_lang %{name}

# Tweak default settings
sed -i 's!# TaskBarShowMailboxStatus=1 # 0/1!TaskBarShowMailboxStatus=0 # 0/1!' %{buildroot}%{_datadir}/%{name}/preferences
sed -i 's!# TaskBarShowCPUStatus=1 # 0/1!TaskBarShowCPUStatus=0 # 0/1!' %{buildroot}%{_datadir}/%{name}/preferences
sed -i 's!# TaskBarShowMEMStatus=1 # 0/1!TaskBarShowMEMStatus=0 # 0/1!' %{buildroot}%{_datadir}/%{name}/preferences
sed -i 's!# TaskBarShowNetStatus=1 # 0/1!TaskBarShowNetStatus=0 # 0/1!' %{buildroot}%{_datadir}/%{name}/preferences


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-menu-fdo
%{_bindir}/%{name}-menu-xrandr
%{_bindir}/%{name}-session
%{_bindir}/%{name}-set-gnomewm
%{_bindir}/icehelp
%{_bindir}/icesh
%{_bindir}/icesound
%{_bindir}/icewmbg
%{_bindir}/icewmhint
%{_datadir}/doc/%{name}
%{_datadir}/xsessions/%{name}-session.desktop
%{_mandir}/man*/*

%files data
%{_datadir}/%{name}/IceWM.jpg
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/keys
%{_datadir}/%{name}/ledclock/
%{_datadir}/%{name}/mailbox/
%{_datadir}/%{name}/menu
%{_datadir}/%{name}/preferences
%{_datadir}/%{name}/programs
%{_datadir}/%{name}/startup
%{_datadir}/%{name}/taskbar/
%{_datadir}/%{name}/theme
%{_datadir}/%{name}/themes/default
%{_datadir}/%{name}/themes/IceAdwaita-*
%{_datadir}/%{name}/toolbar
%{_datadir}/%{name}/winoptions
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes/

%files themes
%{_datadir}/%{name}/themes/CrystalBlue/
%{_datadir}/%{name}/themes/Helix/
%{_datadir}/%{name}/themes/icedesert/
%{_datadir}/%{name}/themes/Infadel2/
%{_datadir}/%{name}/themes/metal2/
%{_datadir}/%{name}/themes/motif/
%{_datadir}/%{name}/themes/NanoBlue/
%{_datadir}/%{name}/themes/win95/

# AntiX-collection
%{_datadir}/%{name}/themes/Antix-*
%{_datadir}/%{name}/themes/AntiX-*
%{_datadir}/%{name}/themes/blue-crystal-*
%{_datadir}/%{name}/themes/BlueDay-*/
%{_datadir}/%{name}/themes/Breathe*/
%{_datadir}/%{name}/themes/Clearview*
%{_datadir}/%{name}/themes/eco-green-*
%{_datadir}/%{name}/themes/FauxGlass-*
%{_datadir}/%{name}/themes/Groove-*
%{_datadir}/%{name}/themes/IceClearlooks-*
%{_datadir}/%{name}/themes/icegil-remix-*
%{_datadir}/%{name}/themes/IceGilDust-*
%{_datadir}/%{name}/themes/icenoir-3.3-*
%{_datadir}/%{name}/themes/Korstro-*
%{_datadir}/%{name}/themes/KorstroDark-*
%{_datadir}/%{name}/themes/PrettyPink-*/
%{_datadir}/%{name}/themes/quiescent-*
%{_datadir}/%{name}/themes/Simplest_black-*
%{_datadir}/%{name}/themes/SunnyDay-*/
%{_datadir}/%{name}/themes/Truth*
%{_datadir}/%{name}/themes/UltraBlack-*

%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/themes/

%files minimal-session
%{_datadir}/xsessions/%{name}.desktop

%files fonts-settings
%{_sysconfdir}/fonts/local.conf
%{_sysconfdir}/gtk-2.0/gtkrc
%{_sysconfdir}/gtk-3.0/settings.ini


%changelog
* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.3-2
- build: update antiX theme collections and awe stuff to commit 91c9d4b
- build: make 'picom' as very weak dep

* Thu Sep 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.3-1
- Update to 1.8.3

* Tue Sep  8 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Wed Sep  2 07:05:42 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.1-2
- Simplify SPEC file and build radically
- Drop few themes, tweaks, deps

* Mon Aug 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Tue Aug 25 03:56:58 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Wed Aug 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.0-4
- Add '%undefine __cmake_in_source_build' macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.0-2
- Rebuild with out-of-source builds new CMake macros

* Wed Jul 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.6-1
- Update to 1.6.6

* Wed May 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.5-2
- Drop more weak deps and simpilfy SPEC file
- Disable LTO

* Tue Mar 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.5-1
- Update to 1.6.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.4-1
- Update to 1.6.4
- Switch source URL to 'github.com/ice-wm/icewm' due to release lags
  https://github.com/bbidulock/icewm/issues/405
- Preserve timestamps during copying

* Mon Nov 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Sat Nov 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-6
- Add patch fix: Anti-aliasing icon edges
  https://github.com/bbidulock/icewm/issues/392

* Wed Oct 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-5
- Theme polishing and new themes

* Sun Oct 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-4
- Update default theme, more Adwaita-like

* Sat Oct 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-3
- Theming improving and better defaults (work still in progress)

* Thu Oct 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-2
- Fixes and new features

* Tue Sep 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-12
- Replace 'pasystray' with 'volumeicon'

* Thu Sep 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-10
- Minor theming fixes

* Wed Sep 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-9
- Add Araita theme
- Add SVG support
- Replace 'xterm' with 'gnome-terminal'
- Spec file and packaging fixes
- Switch to CMake

* Thu Aug 22 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-4
- Update to 1.6.1
- Thanks to Sergio Cipolla <andorinha.sergio@gmail.com> for help

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan  3 2017 Tom Callaway <spot@fedoraproject.org> - 1.3.8-11
- move fedora logos out

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.8-9
- Require agnostic system-logos

* Mon Dec  7 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.8-8
- Add Fedora conditionals to enable single Fedora/EPEL spec

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.8-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 20 2015 Richard Hughes <richard@hughsie.com> - 1.3.8-5
- Rebuilt for gdk-pixbuf2-xlib split

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.8-3
- Fix FTBFS on new architectures (aarch64/ppc64le)
- Cleanup and modernise spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Gilboa Davara <gilboad [AT] gmail.com> - 1.3.8-1
- 1.3.38.
- Clearlooks_v3: clearlooks_2px added. Should solve #981758 and #960663.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Gilboa Davara <gilboad [AT] gmail.com> - 1.3.7-9
- Fix #925574 by calling autoconf. (Temporary solution, pending upsteam fix).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 6 2012 Gilboa Davara <gilboad[AT]gmail.com> - 1.3.7-7
- Updated clearlooks package (#811331).
- (Blunder alert) Finally pushes gnome-icon-theme change to stable.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Gilboa Davara <gilboad[AT]gmail.com> - 1.3.7-5
- Bluecurve is still used for menu generation.
- "Rebuild program menu" menu entry added.

* Sun Jun 10 2012 Gilboa Davara <gilboad[AT]gmail.com> - 1.3.7-4
- Emacs replaced fixes (BZ #805939, Ported Debian fix).
- Use gnome-icon-theme instead of bluecurve (BZ #811335).
- Gcc 4.7 compile fix.
- spec cleanup.

* Sun Mar 4 2012 Gilboa Davara <gilboad[AT]gmail.com> - 1.3.7-3
- Fix missing bluecurve-icon-theme in EL-6.
- Start menu icon should now be generated correctly on both Fedora and EPEL.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Gilboa Davara <gilboad[AT]gmail.com> - 1.3.7-1
- Switch to 1.3.7 tree.
- Fixes bugs: #694532, #689804, #696291, #694622, #716218, #754124.
- Add Marcus Moeller's menu icon size and wmclient patches.
- Missing license information for icewm-xdg-menu.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 22 2010 Gilboa Davara <gilboad[AT]gmail.com> - 1.2.37-7
- Fix missing backspace.
- Fix duplicate clearlooks theme. (#545268)

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.37-6
- Rebuild for libgnome-desktop soname bump
- Fix mixed use of tabs and spaces

* Thu Sep 24 2009 Gilboa Davara <gilboad[AT]gmail.com> - 1.2.37-5
- Patch in missing fribidi support. (#515134)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Gilboa Davara <gilboad[AT]gmail.com> - 1.2.37-1
- 1.2.37.
- Fix missing directory ownership. (#483346)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 6 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.36-3
- pkg-config --cflags gnome-desktop-2.0 doesn't implicitly include
  libgnomeui-2.0 anymore, so add it in explicitly

* Mon Jan 5 2009 Gilboa Davara <gilboad[AT]gmail.com> - 1.2.36-2
- Missing BR libgnomeui-devel. (devel)
- Missing BR gnome-vfs2-devel. (devel)

* Thu Jan 24 2008 <gilboad[AT]gmail.com> - 1.2.35-3
- Fix broken -devel BR (truetype).

* Sat Jan 19 2008 <gilboad[AT]gmail.com> - 1.2.35-2
- Disable xorg-x11-fonts-truetype in -devel.

* Mon Jan 14 2008 <gilboad[AT]gmail.com> - 1.2.35-1
- 1.2.35.
- Missing BR: xorg-x11-fonts-truetype. (#351811)

* Tue Oct 09 2007 <gilboad[AT]gmail.com> - 1.2.32-5
- EL-5 support.
- Missing BR - libgif-devel.
- Devel: Replace redhat-artwork with bluecurve-icon-theme.

* Sun Sep 02 2007 <gilboad[AT]gmail.com> - 1.2.32-4
- Fix mangled if/else. (Again...)

* Sat Sep 01 2007 <gilboad[AT]gmail.com> - 1.2.32-3
- Fix missing BR: libXinerama-devel.
- Fix broken source file.

* Mon Aug 27 2007 <gilboad[AT]gmail.com> - 1.2.32-2
- Fix bad %%{_fedora} if/else.

* Sun Aug 26 2007 <gilboad[AT]gmail.com> - 1.2.32-1
- Fixed license tag.
- Fixed F8 BR - popt-devel.
- Remove APMstatus fix.
- 1.2.32

* Mon Apr 09 2007 <gilboad[AT]gmail.com> - 1.2.30-13
- APMStatus crash fix. (Icewm #1696182)

* Sat Feb 10 2007 <gilboad[AT]gmail.com> - 1.2.30-12
- Add missing dot in the -gnome sub-package description.
- Replace REQ icewm (in both -gnome and -xdgmenu) with icewm-x.x.x.
- Fix -xdgmenu file list and %%install section.
- Preserve the source time-stamp.

* Sun Feb 04 2007 <gilboad[AT]gmail.com> - 1.2.30-11
- Remove .Xdefaults fix from startup. (reported upstream).
- Replace buildroot with RPM_BUILD_ROOT.

* Sun Jan 28 2007 <gilboad[AT]gmail.com> - 1.2.30-10
- Missing REQ: icewm (both -gnome and -xdgmenu)
- Updated menu.in patch.
- Updated startup script. (-xdgmenu)
- Updated icewm-xdg-menu script. (-xdgmenu)

* Thu Jan 25 2007 <gilboad[AT]gmail.com> - 1.2.30-9
- Remove redundant icewm-xdg-menu* %%file entry.
- Change sub-package name to xdgmenu.
- Move icewm-xdg-menu to xdgmenu sub-package.
- Removed the icewm-generate-menu script.

* Sat Jan 20 2007 <gilboad[AT]gmail.com> - 1.2.30-8
- Fix source1 URL. (2nd is a winner)
- Fix -gnome summery.
- New sub-package: icewm-xdg-menu
- ALPHA: icewm-generate-menu script added to use icewm-xdg-menu to generate static menus.

* Sat Jan 20 2007 <gilboad[AT]gmail.com> - 1.2.30-7
- Fix source1 URL.
- Fix xdg-menu* owner.
- Replace default terminal icon to reduce dep-chain.
- Fix icewm-gnome description.
- Replace install with %%{_install}
- Push -gnome's BR to main package.
- Change hard-coded sysconf path.

* Thu Jan 18 2007 <gilboad[AT]gmail.com> - 1.2.30-6
- Change license back to LGPL.
- Change summery.
- New sub-package: -gnome. (GNOME menu support.)
- Missing REQ: xterm.
- Missing REQ: htmlview.
- Remove redundant %%_sysconf section.
- Remove redundant redhat-xxx icons.
- New REQ: redhat-artwork. (icons)
- Better man pages handling.
- Customize keys to better match fedora.
- New REQ: eject. (keys)
- New REQ: alsautils. (keys)

* Wed Jan 17 2007 <gilboad[AT]gmail.com> - 1.2.30-5
- Fix Source0 URL.
- Replace cp with install.
- Do not gzip the man page, just copy it.
- Use htmlview instead of firefox.
- Use BlueCurve icons instead of the mozilla ones.
- Re-fix lang support.
- Return the default configuration files to %%_datadir
- Add gdm session support.
- Remove gnome-menus from default menu - replace it with pyxdg/icewm-xdg-menu.

* Tue Jan 16 2007 <gilboad[AT]gmail.com> - 1.2.30-4
- Fix man page name.
- Remove missing menu items.
- Convert GNOME-menu patch to configure.in patch.
- Push default configuration into /etc/icewm
- Remove the default KDE support. (At least for now)
- Require firefox (default browser in Fedora).
- Add missing firefox icon. (No source - manual convert)
- Add missing gnome-menus. (required for GNOME2 menus)
- Fix missing gettext BR.
- Fix missing lang support.

* Sat Jan 13 2007 <gilboad[AT]gmail.com> - 1.2.30-3
- Fix wrong license. (Was LGPL, should be GPL.)

* Thu Jan 11 2007 <gilboad[AT]gmail.com> - 1.2.30-2
- Manually add missing man page.

* Thu Jan 11 2007 <gilboad[AT]gmail.com> - 1.2.30-1
- Initial release.

