Name:           gcompris-qt
Version:        0.97
Release:        3%{?dist}
Summary:        Educational software suite for children aged 2 to 10

License:        GPLv3+
URL:            http://gcompris.net
Source0:        http://gcompris.net/download/qt/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  openssl-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       qt5-qtmultimedia
Requires:       qt5-qtquickcontrols 
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtsvg
Requires:       hicolor-icon-theme
Requires:       %{name}-activities = %{version}-%{release}

Obsoletes:      gcompris <= 15.10-16

%description
GCompris-Qt is an educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently, GCompris offers in excess of 100 activities. New
activities can be added, and an activity can implement its own game
scheme.

This version is a rewrite of GCompris using the QtQuick
technology.


%package activities
Summary:        Activity files for %{name}
License:        GPLv3 and MPLv2.0 and Public Domain and CC0 and CC-BY and CC-BY-SA and GFDL and OFL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description activities
This package contains the bundle of activities for %{name}.
More than 100 activities are available.


%prep
%autosetup


%build
mkdir build
pushd build
# qml-box2d in not available in Fedora
%cmake_kf5 \
  -DQML_BOX2D_MODULE=disabled \
  ..
%make_build
popd


%install
pushd build
%make_install
popd

# Validate desktop file
desktop-file-validate \
   %{buildroot}%{_datadir}/applications/org.kde.gcompris.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.gcompris.appdata.xml

%find_lang %{name} --all-name --with-qt --with-html


%files -f %{name}.lang
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/%{name}
%exclude %{_kf5_datadir}/%{name}/rcc
%{_kf5_metainfodir}/org.kde.gcompris.appdata.xml
%{_kf5_datadir}/applications/org.kde.gcompris.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
%license COPYING
%doc README 

%files activities
%{_kf5_datadir}/%{name}/rcc
%license COPYING


%changelog
* Sat May 09 2020 Andrea Musuruane <musuruan@gmail.com> - 0.97-3
- Added missing qt5-qtsvg dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Andrea Musuruane <musuruan@gmail.com> - 0.97-1
- Updated to new upstream release

* Sat Aug 17 2019 Andrea Musuruane <musuruan@gmail.com> - 0.96-3
- Obsoletes gcompris package (BZ #1740801)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 14 2019 Andrea Musuruane <musuruan@gmail.com> - 0.96-1
- Updated to new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Andrea Musuruane <musuruan@gmail.com> - 0.95-1
- Updated to new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Andrea Musuruane <musuruan@gmail.com> - 0.91-1
- Updated to new upstream release

* Sun Mar 18 2018 Andrea Musuruane <musuruan@gmail.com> - 0.90-1
- Updated to new upstream release
- Made a separate package for activities
- Added gcc-c++ dependency
- Added kf5-kdoctools-devel to BR to enable the documentation

* Sun Feb 04 2018 Andrea Musuruane <musuruan@gmail.com> - 0.81-2
- Removed obsolete scriptlets

* Sun Dec 17 2017 Andrea Musuruane <musuruan@gmail.com> - 0.81-1
- First release

