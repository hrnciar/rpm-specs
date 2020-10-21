%undefine __cmake_in_source_build
%global appname Spectral

%global commit0 d6009479a5cea4a9b5abcfacaa205eb9c8bf851c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20200729

# Git revision of SortFilterProxyModel...
%global commit1 770789ee484abf69c230cbf1b64f39823e79a181
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name: spectral
Version: 0
Release: 12.%{date}git%{shortcommit0}%{?dist}

# Spectral - GPLv3+
# SortFilterProxyModel - MIT
License: GPLv3+ and MIT
URL: https://gitlab.com/spectral-im/%{name}
Summary: Glossy cross-platform Matrix client
Source0: %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/oKcerG/SortFilterProxyModel/archive/%{commit1}/SortFilterProxyModel-%{shortcommit1}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Quotient) >= 0.6.0
BuildRequires: pkgconfig(libcmark)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

# Require exact version of Qt due to compiled QML usage.
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

Provides: bundled(SortFilterProxyModel) = 0.1.1~git%{shortcommit1}
Requires: hicolor-icon-theme
Requires: qt5-qtquickcontrols2%{?_isa}

Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
Recommends: google-noto-sans-fonts
Recommends: google-roboto-fonts

%description
Spectral is a glossy cross-platform client for Matrix, the decentralized
communication protocol for instant messaging.

%prep
%autosetup -n %{name}-%{commit0} -p1

# Unpacking SortFilterProxyModel...
pushd include
    rm -rf SortFilterProxyModel
    tar -xf %{SOURCE1}
    mv SortFilterProxyModel-%{commit1} SortFilterProxyModel
popd

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGIT_SHA1=%{commit0}
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_metainfodir}/*.appdata.xml

%changelog
* Sat Oct 17 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20200729gitd600947
- Rebuilt due to Qt update.

* Wed Jul 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20200729gitd600947
- Updated to latest Git snapshot.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20200209git29e6933
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0-9.20200209git29e6933
- Add missing runtime dependency qt5-qtquickcontrols2 (rhbz#1842184)

* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-8.20200209git29e6933
- Updated to latest Git snapshot.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20200123git6af7bef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20200123git6af7bef
- Updated to latest Git snapshot.
