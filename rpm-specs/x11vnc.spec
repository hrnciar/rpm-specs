Name:           x11vnc
Version:        0.9.16
Release:        2%{?dist}
Summary:        VNC server for the current X11 session
Summary(ru):    VNC-сервер для текущей сессии X11
# COPYING:                  GPLv2 text
# misc/Xdummy.in:           GPLv2+
# src/cleanup.c:            GPLv2+ with OpenSSL exception
# src/help.c:               GPLv2+ with OpenSSL exception and GPLv2 text
# src/help.h:               GPLv2+ with OpenSSL exception
# src/tkx11vnc.h:           GPLv2+
# src/win_utils.c:          GPLv2+ with OpenSSL exception
# src/xi2_devices.c:        GPLv2+
# src/xi2_devices.h:        GPLv2+
# src/xkb_bell.h:           GPLv2+ with OpenSSL exception
## Not in any binary package
# m4/ax_type_socklen_t.m4:  GPLv2+ with Autoconf exception
## Not used at all
# misc/blockdpy.c:          GPLv2+
# misc/connect_switch:      GPLv2+
# misc/desktop.cgi:         GPLv2+
# misc/deskshot:            GPLv2+
# misc/enhanced_tightvnc_viewer/bin/util/ss_vncviewer:  GPLv2+
# misc/enhanced_tightvnc_viewer/COPYING:    GPLv2 text
# misc/enhanced_tightvnc_viewer/man/man1/ssvnc.1:       GPL+
# misc/enhanced_tightvnc_viewer/man/man1/ssvncviewer.1: GPL+
# misc/enhanced_tightvnc_viewer/README:     GPL+
# misc/enhanced_tightvnc_viewer/src/patches/tight-vncviewer-full.patch:
#                           GPLv2+ and and GPL+ and
#                           wxWindows version 3.1 or later and BSD
# misc/inet6to4:            GPLv2+
# misc/LICENSE:             GPLv2+
# misc/qt_tslib_inject.pl:  GPLv2+
# misc/turbovnc/apply_turbovnc:     Public Domain
# misc/turbovnc/convert:            Public Domain
# misc/turbovnc/convert_rfbserver:  Public Domain
# misc/turbovnc/Makefile.am:        Public Domain
# misc/turbovnc/README:             Public Domain
# misc/turbovnc/tight.c:            GPLv2+
# misc/turbovnc/turbojpeg.h:        wxWindows version 3 or later
# misc/turbovnc/undo_turbovnc:      Public Domain
# misc/uinput.pl:           GPLv2+
# misc/ultravnc_repeater.pl:    GPLv2+
# misc/Xdummy.c:            GPLv2+ with OpenSSL exception
# src/nox11.h:              MIT
# tkx11vnc:     GPLv2
License:        GPLv2+
URL:            https://github.com/LibVNC/x11vnc
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Enforce system crypto policy
# <https://fedoraproject.org/wiki/Packaging:CryptoPolicies#C.2FC.2B.2B_applications>
Patch0:         x11vnc-0.9.16-Respect-a-system-crypto-policy.patch
# Normalize changlog encoding
Patch1:         x11vnc-0.9.16-Convert-a-changelog-to-UTF-8.patch
# Fix building with GCC 10 properly, in upstream after 0.9.16
Patch2:         x11vnc-0.9.16-Fix-build-with-fno-common.patch
# Fix a NULL pointer dereference in a cursor handler, upstream bug #123, in
# upstream after 0.9.16
Patch3:         x11vnc-0.9.16-src-cursor-fix-xfc-NULL-pointer-dereference.patch
BuildRequires:  autoconf
BuildRequires:  automake
# for autogen.sh script
BuildRequires:  bash
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(avahi-client) >= 0.6.4
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(inputproto) >= 1.9.99.9
BuildRequires:  pkgconfig(libvncclient) >= 0.9.8
BuildRequires:  pkgconfig(libvncserver) >= 0.9.8
BuildRequires:  pkgconfig(xi) >= 1.2.99
BuildRequires:  sed
# Tests:
BuildRequires:  desktop-file-utils
# /usr/bin/wish is executed in do_gui() in src/gui.c.
Requires:       tk
# Default X11 server for "x11vnc --create" is Xvfb
Requires:       Xvfb
# Java viewers now are available on
# https://github.com/LibVNC/libvncserver/tree/master/webclients/java-applet
Obsoletes:      x11vnc-javaviewers < 0.9.14-14

%description
What WinVNC is to Windows x11vnc is to X Window System, i.e. a server which
serves the current X Window System desktop via RFB (VNC) protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer it has evolved into
a versatile and productive while still easy to use program.

%description -l ru
Это подобно VNC-серверу под Windows - VNC-сервер, который предоставляет доступ
к текущей X-сессии пользователя по протоколу (VNC).  Таким образом, Вы всегда
можете вернуться к работе удаленно, даже если сессия была стандартно запущена
локально. Более того, доступ к Логин- менеджеру также может быть осуществлен
(GDM, KDM, XDM и т.п.)

Базируется на идее x0rfbserver и LibVNCServer x11vnc эволюционировал в гибкий
и производительный инструмент, который, однако, остаётся прост
в использовании.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure \
    --with-avahi \
    --with-colormultipointer \
    --with-crypto \
    --with-dpms \
    --with-fbdev \
    --without-fbpm \
    --without-macosx-native \
    --with-ssl \
    --with-uinput \
    --without-v4l \
    --with-x \
    --without-xcomposite \
    --with-xdamage \
    --with-xfixes \
    --with-xinerama \
    --with-xkeyboard \
    --with-xrandr \
    --with-xrecord \
    --without-xtrap
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/x11vnc.desktop

%files
%license COPYING
%doc ChangeLog NEWS README
%{_bindir}/x11vnc
%{_bindir}/Xdummy
%{_datadir}/applications/x11vnc.desktop
%{_mandir}/man1/x11vnc.1*

%changelog
* Mon Apr 06 2020 Petr Pisar <ppisar@redhat.com> - 0.9.16-2
- Modernize a spec file
- License corrected from GPLv2 to GPLv2+
- Enforce system crypto policy
- Normalize ChangeLog encoding
- Fix building with GCC 10 properly
- Fix a NULL pointer dereference in a cursor handler (upstream bug #123)

* Tue Feb 11 2020 Sérgio Basto <sergio@serjux.com> - 0.9.16-1
- Update to 0.9.16
- Java viewers moved to
  https://github.com/LibVNC/libvncserver/tree/master/webclients/java-applet
- classes and jars have been removed from upstream sources.
- Remove support to EL5
- Encoding and permissions of files seems that are correct, no need to fix.
- rpmlint doesn't find any hardcoded rpath

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.14-10
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.14-7
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.14-4
- rebuild (libvncserver)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.14-1
- New upstream version 0.9.19.
- bz#1118353 should be fixed.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 28 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.13-11
- enable avahi support and xfixes/xinerama/xrandr extensions... for real (#864947)

* Sat Dec 21 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.13-10
- add support for Xrandr extension (#864947)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.13-8
- Add requires to tk (bz#920554).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.13-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.9.13-5
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Deepak Bhole <dbhole@redhat.com> 0.9.13-3
- Resolves rhbz#794475
- Patch from Omair Majid <omajid@redhat.com> to remove explicit Java 6 req.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.13-1
- Update to 0.9.13 version (asked in bz#669780)
- Drop x11vnc-0.9.8-XShm-explicit-include.patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.12-17
- Update to last version 0.9.12 with hope it fix BZ#646694 and by request BZ#666612
- Change java related exclusion to El6 too.

* Sun Nov 1 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-16
- Noarch subpackage became only on Fedora
    ( https://fedorahosted.org/fedora-infrastructure/ticket/1772#comment:4 )
- Also -javaviewers subpackage compleatly disabled on PPC arch on EL-5 because
    there no java-devel >= 1:1.6.0 and java-1.6.0-openjdk-devel.
    ( https://fedorahosted.org/fedora-infrastructure/ticket/1772#comment:4 )

* Tue Oct 6 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-14
- Make -javaviewers subpackage noarch.

* Sun Oct 4 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-13
- Small fis requires release.
- Rename README file to avoid name bump

* Fri Sep 25 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-12
- Own %%{_datadir}/%%{name} instead of %%{_datadir}/%%{name}/classes
- Add Requires: %%{name} = %%{version}-%%{release} in subpackage.
- Change summary and description for javaviewers subpackage.
- Remove %%doc marker from man-page.
- %%defattr(-,root,root,0755) -> %%defattr(-,root,root,-)
- Add classes/ssl/src/tight/README classes/ssl/src/ultra/README files into
    javaviewers subpackage %%doc (thank you Orcan Ogetbil)
- ln -s replaced by %%{__ln_s}
- Set License: GPLv2+ for javaviewers subpackage (Thanks Spot)

* Mon Aug 31 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-11
- Remove all prebuilt *.jar-files in %%prep section and try build it from source.
- Add BR java-1.6.0-openjdk-devel
- Introduce new subpackage x11vnc-javaviewers.
- Add separate build java-viewers.
- Add Russian localized versions of Summary and descrioptions.

* Wed Aug 26 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-10
- Fix some spelling, change some cosmetic things.
- Delete Patch0 and hacks to link with system lzo package - it is not needed
    anymore as we link it with systel libvncserver instead.
- Delete BR lzo-devel
- Remiove empty directory %%{_datadir}/%%{name}/

* Sun Aug 9 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-9
- Add Requires: Xvfb

* Fri Aug 7 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-8
- Link to shared lzo instead of minilzo for all (not only EL-5).
- Add BuildRequires: /usr/include/X11/extensions/XShm.h
- Patch2: x11vnc-0.9.8-XShm-explicit-include.patch
- Step to conditional BR for Fedora 12, add
    Patch2: x11vnc-0.9.8-XShm-explicit-include.patch to build on it.

* Tue Aug 4 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-7
- Change license to GPLv2 without plus according to x11vnc.c
    source (thanks to Christian Krause).
- For consistency macros usage replace "ln -s" by %%{__ln_s},
    mv by %%{__mv} and similar (chmod, sed).
- Change find call to avoid using xargs in chmod sources command.

* Wed Jul 29 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-6
- Build with openssl unconditionally.
- Add Patch1: x11vnc-0.9.8-disableRpath.patch
- fix source perms for the -debuginfo package rpmlint warnings

* Tue Jul 21 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-5
- Try use lzo instead of minilzo in EL-5 (minilzo is not bundled in it).
- Try use system libvncserver library (--with-system-libvncserver
    configure option) instead of bundled one.
- System libvncserver built without tightvnc-filetransfer support.
    Now disable it there (--without-filetransfer)
    And according to it change License to only GPLv2+
    ./configure --help misleading, using --without-tightvnc-filetransfer

* Tue Jul 21 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-4
- All changes inspired by started Fedora Review (thank you to Christian Krause).
- README and AUTHORS files converted into UTF-8.
- Explicit mention previous author in changelog and delet old entries of it.
- Source renamed to Source0.
- Source0 URL changed to long (correct) variant:
    http://downloads.sourceforge.net/libvncserver/%%{name}-%%{version}.tar.gz
    was http://dl.sf.net/libvncserver/x11vnc-%%{version}.tar.gz
- Add BR: /usr/include/X11/extensions/XInput.h; In F12 it is located in
    libXi-devel but in previous versions in xorg-x11-proto-devel
    so, to do not make conditional requires, require explicit file.
- Remove prebuild binaries clients.
- Remove Requires: minilzo it will be automatically propogated.
- Add BR: libvncserver-devel

* Fri Jul 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-3
- Add BR openssl-devel to provide SSL capability (thanks Manuel Wolfshant).
- Requires: minilzo, BR lzo-devel and Patch0:
    11vnc-0.9.8-use-system-minilzo.patch to use system version of library.
- Add "and GPLv2" to License. See comment above why.
- Add BuildRequires: libXfixes-devel

* Fri Jul 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.8-2
- Import http://packages.sw.be/x11vnc/x11vnc-0.9.7-1.rf.src.rpm to maintain it in fedora:
    Packager: Dag Wieers <dag@wieers.com>
    Vendor: Dag Apt Repository, http://dag.wieers.com/apt/
- Step to version 0.9.8
- Reformat spec with tabs.
- Comment out (leave for history) Packager and Vendor tags
- Remove defines of several macros like dtag, conditional _without_modxorg
- Remove all stuff around conditional build _without_modxorg
- Add -%%(%%{__id_u} -n) part into buildroot.
- Make setup quiet.
- Remove "rf" Release suffix and replace it by %%{?dist}
- License from GPL changed to GPLv2+
