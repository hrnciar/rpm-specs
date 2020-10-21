%global forgeurl https://github.com/fcitx/fcitx5
%global commit dd9dc94c42ee98ea04782bdb4d4aa3f7822e56f0
%forgemeta
%global dictver 20121020
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           fcitx5
Version:        0
Release:        0.9%{?dist}
Summary:        Next generation of fcitx
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}
Source1:        https://download.fcitx-im.org/data/en_dict-%{dictver}.tar.gz
Source2:        fcitx5-xinput


BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
Requires:       dbus-x11
Requires:       %{name}-data = %{version}-%{release}
# Requires:       imsettings
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package data
Summary:        Data files of Fcitx5
BuildArch:      noarch
# require with isa will lead to problem on koji build
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       dbus

%description data
The %{name}-data package provides shared data for Fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx5 libraries.

%prep
%forgesetup
cp %{S:1} src/modules/spell/dict/

%build
%cmake
%cmake_build 

%install
%cmake_install
install -pm 644 -D %{S:2} %{buildroot}%{_xinputconf}
install -d                %{buildroot}%{_datadir}/%{name}/inputmethod
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
 
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
%ctest

%post
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%config %{_xinputconf}
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-diagnose
%{_libdir}/%{name}/
%{_libdir}/libFcitx5*.so.*.*
%{_libdir}/libFcitx5Config.so.6
%{_libdir}/libFcitx5Core.so.7
%{_libdir}/libFcitx5Utils.so.2

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc


%files data
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.9.20201016gitdd9dc94
- update to dd9dc94c42ee98ea04782bdb4d4aa3f7822e56f0 upstream commit

* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.8
- upstream commit 5415db391c1b84ea9964b0d508c053ae5c25e4aa

* Sat Sep 12 2020 Karuboniru <yanqiyu01@gmail.com> - 0-0.7
- Drop imsetting
- Update to commit d0383bc4a8e65e71189c18e31f7b832e543144c1
- sobump from libFcitx5Core.so.6 to libFcitx5Core.so.7

* Wed Sep  2 08:44:37 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.6
- Fix a typo

* Tue Sep  1 09:07:22 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5.20200830git4706f37
- Own /usr/share/fcitx5/inputmethod

* Sun Aug 30 23:39:20 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4.20200830git4706f37
- rebuild to push to f32

* Sun Aug 30 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200830git4706f37
- update to commit 4706f37e60686d391a7f9a45ca1be6df6052ec4d
- fix a wrong xinputrc file

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200813git87fb655
- change according to review suggestions

* Thu Aug 13 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200813git87fb655
- new version

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitc87ea48
- initial package
