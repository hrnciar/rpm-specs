%global appname         com.github.tkashkin.%{name}
%global short_version   0.16.0
%global dev_version     %{short_version}-1-master

# Upstream recommendation disabling all optimizations due to known bugs
# * https://github.com/tkashkin/GameHub/pull/169
%global optflags %{optflags} -O0

Name:           gamehub
Version:        %{short_version}.1
Release:        1%{?dist}
Summary:        All your games in one place

License:        GPLv3+
URL:            https://github.com/tkashkin/GameHub
Source0:        %{url}/archive/%{dev_version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(unity)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
%if 0%{?fedora} >= 30
BuildRequires:  pkgconfig(manette-0.2)
%endif
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}

Recommends:     dosbox%{?_isa}
Recommends:     file-roller%{?_isa}
Recommends:     innoextract%{?_isa}
Recommends:     wine%{?_isa}

# Requires for GOG DOSBox games
Suggests:       libcaca%{?_isa}

# Interpreter for several adventure games
Suggests:       scummvm%{?_isa}

%description
Unified library for all your games, written in Vala using GTK+3, designed for
elementary OS.
GameHub allows to view, download, install, run and uninstall games from
supported sources.
GameHub supports non-native games as well as native games for Linux.
It supports multiple compatibility layers for non-native games:

• Wine/Proton
• DOSBox
• RetroArch
• ScummVM

It also allows to add custom emulators.
GameHub supports WineWrap — a set of preconfigured wrappers for supported games.
GameHub supports multiple game sources and services:

• Steam
• GOG
• Humble Bundle
• Humble Trove

Locally installed games can also be added to GameHub.
GameHub makes storing and managing your DRM-free game collection easier.
Download installers, DLCs and bonus content and GameHub will save your downloads
according to settings.


%prep
%autosetup -p1 -n GameHub-%{dev_version}


%build
branch=master
commit=8a88b0796857fa6c30bca4eabd7da44e192cf1ad
commit_short="$(c=${commit}; echo ${c:0:7})"
%meson                                      \
    --buildtype=debug                       \
    -Dgit_branch="${branch}"                \
    -Dgit_commit="${commit}"                \
    -Dgit_commit_short="${commit_short}"
%meson_build


%install
%meson_install
%find_lang %{appname}

# No HiDPI icons version yet
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/%{appname}-overlayfs-helper
%{_bindir}/%{name}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/*.policy
%{_metainfodir}/*.appdata.xml


%changelog
* Thu Apr 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0.1-1
- Update to 0.16.0-1-master

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0.1-1
- Update to 0.15.0-1-master

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.2.1-3
- Disable all compiler optimizations due to bugs
- Enable debug build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.2.1-1
- Update to 0.14.2-1-master

* Sat Jun 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1.4-1
- Update to 0.14.1-4-dev
- Remove 'granite' dependency

* Sun Jun 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.0.19-1
- Update to 0.14.0.19-dev

* Mon Jun 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1.107-1
- Update to 0.13.1-107-dev

* Fri May 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1.96-1
- Update to 0.13.1-96-dev
- Add more description
- Suggests libcaca package

* Sat Apr 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1.80-3
- Update to latest snapshot
- Add recommended packages as weak dependencies
- Add libmanette-devel as BR for gamepad support
- Enable symbolic icons by default

* Tue Apr 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1.77-1
- Initial Package
