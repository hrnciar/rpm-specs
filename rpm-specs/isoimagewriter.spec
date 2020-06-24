Name:           isoimagewriter
Version:        0.8
Release:        2%{?dist}
Summary:        KDE ISO Image Writer, a tool to write a .iso file to a USB disk

License:        GPLv3+
URL:            https://community.kde.org/ISOImageWriter
Source0:        https://download.kde.org/unstable/%{name}/%{version}/%{name}-%{version}.tar.xz

# General build time stuff
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

# Libs
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libudev)

# KF5
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5WidgetsAddons)


%description
The KDE ISO Image Writer is a tool to write a .iso file to a USB disk.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml

desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/dbus-1/system.d/org.kde.isoimagewriter.conf
%{_kf5_datadir}/dbus-1/system-services/org.kde.isoimagewriter.service
%{_kf5_datadir}/polkit-1/actions/org.kde.isoimagewriter.policy
%{_kf5_datadir}/%{name}
%{_kf5_libexecdir}/kauth/%{name}_helper
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.8-1
- new version
- removed isoimagewriter-link-libudev-dynamically.patch (fixed upstream)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.2-3
- fixed location of org.kde.kstars.appdata.xml

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Christian Dersch <lupinix@fedoraproject.org> - 0.2-1
- initial package (review RHBZ #1505209)

