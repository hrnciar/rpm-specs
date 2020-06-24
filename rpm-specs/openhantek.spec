%global optflags %{optflags} -flto
%global build_ldflags %{build_ldflags} -flto

Name:           openhantek
Version:        3.1.0
Release:        1%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope

License:        GPLv3+ and GPLv2+ and ASL 2.0
URL:            https://github.com/OpenHantek/OpenHantek6022
Source0:        %{url}/archive/%{version}/OpenHantek6022-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fftw-devel
BuildRequires:  libusbx-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(udev)
BuildRequires:  hicolor-icon-theme

Requires:       hicolor-icon-theme
Requires:       udev

%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: 6022BE/BL.

%prep
%autosetup -n OpenHantek6022-%{version}

%build
mkdir build
pushd build
    %cmake3 \
        -DCMAKE_AR=/usr/bin/gcc-ar \
        -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
        -DCMAKE_NM=/usr/bin/gcc-nm \
        ..
    %make_build
popd

%install
pushd build
    %make_install
popd
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/60-hantek.rules %{buildroot}%{_udevrulesdir}
rm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/OpenHantek.png
rm %{buildroot}%{_datadir}/doc/%{name}/*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/OpenHantek.desktop

%files
%license COPYING LICENSE
%doc readme.md CHANGELOG docs/OpenHantek6022_User_Manual.pdf
%{_bindir}/OpenHantek
%{_datadir}/applications/OpenHantek.desktop
%{_datadir}/icons/hicolor/scalable/apps/OpenHantek.svg
%{_udevrulesdir}/60-hantek.*


%changelog
* Fri May 08 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Tue Apr 14 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.4b-1
- Update to 3.0.4b

* Wed Mar 18 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Tue Mar 03 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.2-2
- Update to 3.0.2
- Fix BR

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Mon Nov 18 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Thu Oct 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.16-1
- Update to 2.16

* Mon Oct 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.15-1
- Update to 2.15

* Mon Sep 09 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.14-1
- Update to 2.14

* Sat Sep 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.13-1
- Update to 2.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.12-1
- Update to 2.12

* Tue Jun 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.10-1
- Update to 2.10
- Correct udev Require

* Mon May 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.09-1
- Update to 2.09
- Corrected license

* Thu May 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.07-1
- Update to 2.07

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.06-1
- Update to 2.06

* Sat May 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.05-1
- Update to 2.05

* Fri May 10 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.04-1
- Update to 2.04

* Mon May 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.03-1
- Update to 2.03
- Fix crashing in normal mode

* Sat Apr 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.01-1
- Update to 2.01

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0-4.20190110giteb33325
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20190110giteb33325
- Update to latest git

* Sat Dec 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 0-3.20180722git7862387
- Drop systemd-udev as it's installed by default.
  This avoid a dependency break in el7 as udev is provided by the systemd package

* Wed Aug 01 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20180722git7862387
- Update to latest git

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0-2.20180715git57e0beb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180715git57e0beb
- Update to latest git

* Wed Jul 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180710git9935f0a
- Update to latest git

* Thu Mar 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180320git0eff8d4
- Initial package for Fedora
