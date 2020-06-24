# lib%%{name}core.so* is a private lib with no headers, so we should
# not provide that.
%global __provides_exclude ^lib%{name}.*\\.so$
%global __requires_exclude ^lib%{name}.*\\.so$

Name:       soundkonverter
Version:    3.0.1
Release:    4%{?dist}
Summary:    Audio file converter, CD ripper and Replay Gain tool

License:    GPLv2+
URL:        http://kde-apps.org/content/show.php?content=29024
Source0:    https://github.com/dfaust/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/dfaust/soundkonverter/commit/16fb09fcbd5712b7b75004229dbb74f85f213b53
Patch0:     https://github.com/dfaust/soundkonverter/commit/16fb09fcbd5712b7b75004229dbb74f85f213b53.patch#/0001-Fix-adding-directories-to-the-Replay-Gain-tool.patch
# https://github.com/dfaust/soundkonverter/pull/72
Patch1:     https://patch-diff.githubusercontent.com/raw/dfaust/soundkonverter/pull/72.patch#/0002-Install-appdata-in-usr_share_metainfo.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(phonon4qt5)
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  cdparanoia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       cdparanoia
Requires:       flac
Requires:       fluidsynth
Requires:       speex
Requires:       timidity++
Requires:       vorbis-tools
Requires:       wavpack
Recommends:     faac
Recommends:     faad2
Recommends:     ffmpeg
Recommends:     lame
Recommends:     mac
Recommends:     mp3gain
Recommends:     mppenc
Recommends:     sox
Recommends:     twolame
Recommends:     vorbisgain
Recommends:     opus-tools

%description
SoundKonverter is a front-end to various audio converters.

The key features are:
  * Audio conversion
  * Replay Gain calculation
  * CD ripping


%prep
%autosetup -p1


%build
mkdir -p build
cd build
%cmake_kf5 ../src "-DKF5_BUILD=ON"
%make_build


%install
cd build
%make_install
%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{name}.appdata.xml


%files -f build/%{name}.lang
%{_kf5_bindir}/%{name}
%{_kf5_libdir}/lib%{name}core.so
%{_kf5_libdir}/qt5/plugins/%{name}_*
%{_kf5_datadir}/%{name}
%dir %{_kf5_datadir}/solid
%dir %{_kf5_datadir}/solid/actions
%dir %{_kf5_datadir}/kxmlgui5/%{name}
%{_kf5_datadir}/kservices5/%{name}_*
%{_kf5_datadir}/kservicetypes5/%{name}_*
%{_kf5_datadir}/kxmlgui5/%{name}/%{name}ui.rc
%{_kf5_datadir}/solid/actions/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-replaygain.png
%{_kf5_metainfodir}/%{name}.appdata.xml


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Release 3.0.1
- Refresh SPEC

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.2.2-1
- Rebuilt for new upstream version 2.2.2 fixes rhbz #1315062
- Fixes FTBFS rhbz #1308143
- Fix GitHub URLs

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Björn Esser <bjoern.esser@gmail.com> - 2.1.1-2
- use %%{_kde4_appsdir}-macro as suggested by Rex Dieter (#1114547)
  see: https://bugzilla.redhat.com/show_bug.cgi?id=1114547#c7

* Sun Jun 29 2014 Björn Esser <bjoern.esser@gmail.com> - 2.1.1-1
- initial rpm release (#1114547)
