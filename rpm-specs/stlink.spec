# %global gitcommit_full f82700623127538c8cf5cddbbeba6afc12d3adbf
# %global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
# %global date 20200420

%global optflags %{optflags} -flto=auto
%global build_ldflags %{build_ldflags} -flto

Name:           stlink
Version:        1.6.1
# Release:        0.1.%{date}git%{gitcommit}%{?dist}
Release:        1%{?dist}
Summary:        STM32 discovery line Linux programmer
License:        BSD

Url:            https://github.com/stlink-org/stlink
# Source0:        %{url}/tarball/%{gitcommit_full}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  desktop-file-utils
# BuildRequires:  pandoc
Requires:       pkgconfig(udev)

%description
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        gui
Summary:        GUI for STM32 discovery line linux programmer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    gui
STLINK v1/v2 JTAG/SWD debugging/flashing tool for STM32 microcontrollers.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development.

%prep
%autosetup
sed -i 's|/${PROJECT_NAME}||g' src/stlink-gui/CMakeLists.txt
sed -i 's|/${PROJECT_NAME}||g' doc/man/CMakeLists.txt
sed -i 's|#add_subdirectory(cmake/pkgconfig)|add_subdirectory(cmake/pkgconfig)|' CMakeLists.txt
sed -i 's|find_package(libusb REQUIRED)|find_package(libusb REQUIRED)\nset(STLINK_LIBRARY_PATH ${CMAKE_INSTALL_LIBDIR} CACHE PATH "Main library install directory")|' CMakeLists.txt


%build
mkdir build
pushd build
    %cmake3 \
        -DCMAKE_AR=/usr/bin/gcc-ar \
        -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
        -DCMAKE_NM=/usr/bin/gcc-nm \
        -DSTLINK_UDEV_RULES_DIR="%{_udevrulesdir}" \
        -DSTLINK_STATIC_LIB=OFF \
        -DSTLINK_GENERATE_MANPAGES=ON \
        ..
    %make_build
popd

%install
pushd build
    %make_install
popd
# Remove static library
rm %{buildroot}%{_libdir}/lib%{name}.a

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop


%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%config(noreplace) %{_sysconfdir}/modprobe.d/%{name}*
%{_bindir}/st-*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/st-*.1*
%{_udevrulesdir}/49-%{name}*

%files gui
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-gui.ui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-gui.svg

%files devel
%{_includedir}/%{name}*
%{_includedir}/stm32.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Jun 01 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.0-1
- Update to 1.6.1

* Mon Apr 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.1-0.1.20200420gita7568d3
- Update to latest git

* Thu Feb 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-0.5.20190606git84f63d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-0.4.20190606git84f63d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.1-0.3.20190606git84f63d2
- Update to latest git

* Mon May 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.1-0.3.20190513gitd040db5
- Update to latest git

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 1.5.1-0.3.20190216git1165cf7
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.1-0.2.20190216git1165cf7
- Update to latest git

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-0.2.20190103git7651d21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.1-0.1.20190103git7651d21
- Update to latest git

* Tue Aug 07 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.1-0.1.20180802gitae717b9
- Update to latest git

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.0-2
- Corrected Source0 url
- Added desktop file
- Removed static library

* Fri Sep 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Mon Jun 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.0-1
- Update to 1.2.0

* Tue Aug 18 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.1.0-1
- Correct spec for Fedora

* Fri Apr  3 2015 dmitry_r@opensuse.org
- Update to version 1.1.0
  * New devices support, see included README file
  * Bugfixes
* Wed Jun 11 2014 dmitry_r@opensuse.org
- Add COPYING and README to package documentation
* Fri Jun  6 2014 dmitry_r@opensuse.org
- Initial package, version 1.0.0
