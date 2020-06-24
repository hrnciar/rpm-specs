%global appid com.github.quaternion

Name:       quaternion
Version:    0.0.9.4e
Release:    1%{?dist}

Summary:    A Qt5-based IM client for Matrix
License:    GPLv3
URL:        https://github.com/quotient-im/Quaternion
Source0:    https://github.com/quotient-im/Quaternion/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(QMatrixClient)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Keychain)

Requires:       hicolor-icon-theme

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep
%autosetup -n Quaternion-%{version}
mkdir -p %{_target_platform}

%build
%cmake \
    -DUSE_INTREE_LIBQMC=NO
%make_build

%install
%make_install
%find_lang %{name} --with-qt
cp -p linux/%{appid}.appdata.xml %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/QMatrixClient
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Thu Apr 02 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-1
- Version 0.0.9.4e

* Thu Mar 05 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4c-1
- Version 0.0.9.4c


