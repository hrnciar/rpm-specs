%global framework kipi-plugins

Name:    kf5-%{framework}
Summary: Plugins to use with kf5-libkipi applications
Version: 20.04.2 
Release: 1%{?dist}

License: GPLv2+
URL:     http://www.digikam.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: gcc-c++

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5KIO)

BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5X11Extras)

BuildRequires: cmake(KF5Kipi)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme

# upgrade path for eol'd kde4-based kipi-plugins
Obsoletes: kipi-plugins < 5.0.0

%description
This package contains plugins to use with Kipi, the KDE Image Plugin
Interface.

%package libs
Summary: Runtime libraries for %{name}
# upgrade path
Obsoletes: kipi-plugins-libs < 5.0.0
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1 -n kipi-plugins-%{version}

# fix ChagngeLog encoding
mv ChangeLog ChangeLog.orig
iconv -f iso-8859-1 -t utf-8 ChangeLog.orig -o ChangeLog


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang all --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/kipiplugins.desktop


%files -n kf5-kipi-plugins -f all.lang
%doc AUTHORS ChangeLog
%doc README TODO NEWS
%license COPYING
%{_kf5_metainfodir}/org.kde.kipi_plugins.metainfo.xml
%{_kf5_datadir}/applications/kipiplugins.desktop
%{_kf5_datadir}/kxmlgui5/kipi/
%{_kf5_datadir}/icons/hicolor/*/apps/kipi-*
%{_kf5_datadir}/kservices5/kipiplugin_*.desktop
%{_kf5_datadir}/kipiplugin_*/

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libKF5kipiplugins.so*
%{_kf5_qtplugindir}/kipiplugin_*.so
%{_kf5_metainfodir}/org.kde.kipi_plugins.metainfo.xml

%changelog
* Sat Jun 13 2020 Marie Loise Nolden <loise@kde.org> - 20.04.2-1
- 20.04.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-2
- Requires: hicolor-icon-theme
- fix ChangeLog encoding
- validate kipiplugins.desktop
- add .spec comment clarifying purpose of Obsoletes: kipi-plugins (upgrade path only)

* Thu May 09 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-1
- kipi-plugis-5.9.1

