%undefine __cmake_in_source_build

%global kf5_version_min 5.42

Name:           plasma-pass
Version:        1.1.0
Release:        3%{?dist}
Summary:        Plasma applet to access passwords from the Pass password manager

License:        LGPLv2+
URL:            https://cgit.kde.org/%{name}.git
Source0:        https://download.kde.org/stable/plasma-pass/plasma-pass-%{version}.tar.xz

# Exclude QML plugins from provides()
%global __provides_exclude_from ^(%{_kf5_qmldir}/.*\\.so)$

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version_min}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version_min}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version_min}

BuildRequires:  desktop-file-utils

Requires:       plasmashell(desktop)
# Invokes the gpg2 executable to decrypt passwords
Requires:       gnupg2

# Does not use pass directly, but is a GUI for its store, also using
# the command line is currently the only way how to add new passwords.
Recommends:     pass

%description
Plasma Pass is a Plasma systray applet to easily access passwords from the Pass
password manager.

%prep
%autosetup


%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pass.desktop

%find_lang plasma_applet_org.kde.plasma.pass

%files -f plasma_applet_org.kde.plasma.pass.lang
%license COPYING
%doc README.md
%{_kf5_sysconfdir}/xdg/plasma-pass.categories
%dir %{_kf5_qmldir}/org/kde/plasma/private/plasmapass/
%{_kf5_qmldir}/org/kde/plasma/private/plasmapass/*
%dir %{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pass/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pass/*
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_metainfodir}/*.xml


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Daniel Vrátil <dvratil@fedoraproject.org> - 1.1.0-1
- Plasma Pass 1.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Daniel Vrátil <dvratil@fedoraproject.org> - 1.0.0-1
- Initial version
