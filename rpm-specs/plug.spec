%global release_hash aaf782d8e6b4

Name:           plug
Version:        1.2.1
Release:        6%{?dist}
Summary:        Linux software for Fender Mustang amplifiers

License:        GPLv3+
Url:            http://piorekf.org/plug/
# The tarball has a rather unconventional name - v1.1.tar.gz
Source0:        https://bitbucket.org/piorekf/plug/get/v%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        plug-udev-rules

# Qt5 fixes
# https://bitbucket.org/piorekf/plug/commits/40057045db25b0d62aaac3b618da10b4d2c05c94
Patch0:         plug-1.2.1-qt5.patch

BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  desktop-file-utils


%description
Linux replacement for Fender FUSE software for Mustang amps.


%prep
# The way this tarball is packed up is rather unconventional!
%setup -q -n piorekf-plug-%{release_hash}/plug

%patch0 -p2 -b .qt5

%build
%{qmake_qt5}
make %{?_smp_mflags}

%install
install -D -m 755 %{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

# Install desktop file
desktop-file-install \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE1}

# Install udev rules
install -D -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_usr}/lib/udev/rules.d/50-mustang.rules

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_usr}/lib/udev/rules.d/50-mustang.rules

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Dan Horák <dan[at]danny.cz> - 1.2.1-1
- Updated to 1.2.1
- Switched to Qt5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1-19
- Better Qt dep, use %%license

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1-13
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-6
- Change udev rules to be systemd conformant (See BZ 856002 comment 6)
- No longer created the plugdev group
- Drop unneeded README.Fedora file

* Sun Sep 30 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-5
- Change Group to Applications/System
- Untabify spec file
- Fix Source URL

* Sun Sep 23 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-4
- Remove BuildRequires for gcc-c++
- Use pkgconfig style BuildRequires for qt-devel

* Mon Sep 10 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-3
- Add patch to allow updating of firmware for Mustang III, IV, V models

* Sun Sep  9 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-2
- Add udev rules
- Add creation of group "plugdev" on package install
- Add README.Fedora file

* Sun Sep  9 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-1
- Initial package

