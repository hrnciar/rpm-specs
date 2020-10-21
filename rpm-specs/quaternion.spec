%global appid com.github.quaternion

Name:       quaternion
Version:    0.0.9.4e
Release:    4%{?dist}

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

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_INTREE_LIBQMC=NO
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
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
* Thu Aug 06 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-4
- Fix build failure

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.4e-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.4e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4e-1
- Version 0.0.9.4e

* Thu Mar 05 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4c-1
- Version 0.0.9.4c


