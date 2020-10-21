%undefine __cmake_in_source_build

Name: ksnip
Version: 1.7.3
Release: 1%{?dist}

License: GPLv2+
Summary: Qt based cross-platform screenshot tool
URL: https://github.com/%{name}/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(kImageAnnotator)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(kColorPicker)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Xml)

BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

Requires: hicolor-icon-theme

%description
Ksnip is a Qt based cross-platform screenshot tool that provides
many annotation features for your screenshots.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/*.appdata.xml

%changelog
* Fri Jul 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-1
- Initial SPEC release.
