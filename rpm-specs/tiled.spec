Name:           tiled
Version:        1.3.4
Release:        1%{?dist}
Summary:        Tiled Map Editor
# tiled itself is GPLv2+, libtiled and tmxviewer are BSD
License:        GPLv2+ and BSD
URL:            http://www.mapeditor.org
Source0:        https://github.com/bjorn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  python3-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  zlib-devel

%description
Tiled is a general purpose tile map editor. It is built to be easy to use,
yet flexible enough to work with varying game engines, whether your game
is an RPG, platformer or Breakout clone. Tiled is free software and written
in C++, using the Qt application framework.

This package contains the tiled application and tmxviewer, a simple application
to view Tiled maps.

%package plugin-python
Summary:        Python plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-python
A plugin for tiled which allows to write Python plugins.

%define pluginwarning Warning: This plugin does not offer full compatibility with Tileds features.

%package plugin-tbin
Summary:        tBIN plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-tbin
A plugin for tiled which allows support for the tBIN map format.

%{pluginwarning}

%package plugin-droidcraft
Summary:        Droidcraft plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-droidcraft
A plugin for tiled which allows to save maps as .dat droidcraft maps.

%{pluginwarning}

%package plugin-flare
Summary:        Flare plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-flare
A plugin for tiled which allows to save maps as .txt flare maps.

%{pluginwarning}

%package plugin-replica-island
Summary:        Replica Island plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-replica-island
A plugin for tiled which allows to save maps as .bin Replica Island maps.

%{pluginwarning}

%package plugin-t-engine4
Summary:        T-Engine4 plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-t-engine4
A plugin for tiled which allows to export maps as .lua T-Engine4 maps.

%{pluginwarning}

%package plugin-defold
Summary:        Defold plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-defold
A plugin for tiled which allows to export maps as .tilemap Defold maps.

%{pluginwarning}

%package plugin-gmx
Summary:        GameMaker Studio plugin for Tiled
License:        GPLv2+
URL:            http://www.mapeditor.org
Requires:       %{name} = %{version}-%{release}
%description plugin-gmx
A plugin for tiled which allows to export maps as GameMaker Studio room files.

%{pluginwarning}

%prep
%setup -q
# Remove copy of zlib
rm -rf src/zlib

%build
%qmake_qt5 -r PREFIX=%{_prefix} LIBDIR=%{_libdir} RPATH=no USE_FHS_PLUGIN_PATH=yes
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

# Clean build artefacts
find -name ".uic" -or -name ".moc" -or -name ".rcc" | xargs rm -rf

# Validate desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.mapeditor.Tiled.desktop

# Appdata
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml

# locale files
%find_lang %{name} --with-qt

# Removed development file (this version does not install headers anyway)
rm %{buildroot}/%{_libdir}/lib%{name}.so

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS.md README.md COPYING LICENSE.GPL LICENSE.BSD
%{_bindir}/%{name}
%{_bindir}/terraingenerator
%{_bindir}/tmxrasterizer
%{_bindir}/tmxviewer
%{_datadir}/icons/hicolor/*/apps/*%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/*%{name}*
%{_datadir}/applications/org.mapeditor.Tiled.desktop
%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml
%{_datadir}/mime/packages/org.mapeditor.Tiled.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations
%{_libdir}/lib%{name}.so.*

%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/

# Core plugins
%{_libdir}/%{name}/plugins/libcsv.so
%{_libdir}/%{name}/plugins/libgmx.so
%{_libdir}/%{name}/plugins/libjson.so
%{_libdir}/%{name}/plugins/liblua.so
%{_libdir}/%{name}/plugins/libjson1.so
%{_libdir}/%{name}/plugins/libdefoldcollection.so

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/tmxrasterizer.1*
%{_mandir}/man1/tmxviewer.1*
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer

%files plugin-python
%{_libdir}/%{name}/plugins/libpython.so

%files plugin-tbin
%{_libdir}/%{name}/plugins/libtbin.so

%files plugin-droidcraft
%{_libdir}/%{name}/plugins/libdroidcraft.so

%files plugin-flare
%{_libdir}/%{name}/plugins/libflare.so

%files plugin-replica-island
%{_libdir}/%{name}/plugins/libreplicaisland.so

%files plugin-t-engine4
%{_libdir}/%{name}/plugins/libtengine.so

%files plugin-defold
%{_libdir}/%{name}/plugins/libdefold.so

%files plugin-gmx
%{_libdir}/%{name}/plugins/libgmx.so

%changelog
* Mon May 18 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.4-1
- Update to 1.3.4 fixes rhbz#1809805 + fix spec file changelog

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.2-1
- update to 1.3.2 fixes rhbz#1669013

* Mon Dec 16 2019 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.1-1
- Update to upstream

* Mon Aug 19 2019 Miro Hroncok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-1
- Rebuilt for new upstream release 1.2.0, fixes rhbz #1552361
- Added Python3 support

* Fri Sep 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.6-1
- Rebuilt for new upstream release 1.1.6, fixes rhbz #1552361
- Remove upstreamed patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.2-1
- Rebuilt for new upstream release 1.1.2, fixes rhbz #1531028
- TMW plugin: Removed since it is no longer needed
- tBIN plugin: Added read/write support for the tBIN map format

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-2
- Remove obsolete scriptlets

* Thu Sep 21 2017 Erik Schilling <ablu.erikschilling@googlemail.com> - 1.0.3-1
- New release 1.0.3
- Added subpackage for gmx plugin

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.18.2-1
- Rebuilt for new upstream release 0.18.2, fixes rhbz #1406593 #1435926

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.17.2-1
- Rebuilt for new upstream release 0.17.2, fixes rhbz #1392732

* Thu Sep 01 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.17.0-1
- New release 0.17.0
- Added subpackage for defold plugin

* Tue Apr 19 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.16.0-1
- New upstream release 0.16.0

* Sun Mar 06 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.15.2-1
- New bugfix release 0.15.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.15.0-2
- use %%qmake_qt5 to ensure proper build flags

* Sat Jan 09 2016 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.15.0-1
- New upstream release 0.15.0

* Fri Nov 27 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.14.2-1
- New upstream release 0.14.2

* Mon Sep 21 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.14.0-1
- New upstream release

* Tue Sep 08 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.13.1-1
- New upstream release

* Sat Aug 15 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.13.0-1
- New upstream release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 2 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.3-1
- New upstream release

* Fri May 22 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.2-1
- New upstream release

* Wed May 20 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.1-1
- New upstream release

* Fri May 15 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.12.0-1
- New upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.11.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 11 2015 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.11.0-1
- New upstream release

* Mon Oct 27 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.2-1
- New bugfix release

* Mon Sep 22 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.1-1
- New bugfix release

* Sun Sep 14 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.10.0-1
- New upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Erik Schilling <ablu.erikschilling@googlemail.com> - 0.9.1-2
- Fixed detection of plugins on 64bit
- Splitted plugins into subpackages

* Sat Jul 27 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.9.1-1
- New upstream release 0.9.1

* Sat Jan 12 2013 Erik Schilling <ablu.erikschilling@googlemail.com> 0.9.0-1
- New upstream release 0.9.0
- Dropped now obsolete patches and files

* Mon Sep 3 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-3
- Fixed preserving of timestamps in install command.
- Fixed typo in permission setting.
- Talked with upstream about license mismatch in headers.
- Those headers were outdated.

* Mon Sep 3 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-2
- Added note about which parts are licensed with which license.
- Made sure that the copy of zlib inside of the source is removed.
- Fixed handling of locales (using %%find_lang).
- Avoided plain asterisks in %%files.
- Made description clear about containing the tmxviewer.

* Sun Sep 2 2012 Erik Schilling <ablu.erikschilling@googlemail.com> 0.8.1-1
- First version for official fedora repos.
