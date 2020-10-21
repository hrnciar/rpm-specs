Name:       libkindrv
Version:    0.1.2
Release:    25%{?dist}
Summary:    Driver for controlling robotic arms by Kinova
License:    LGPLv3+
URL:        http://fawkesrobotics.org/projects/libkindrv/
Source0:    https://github.com/fawkesrobotics/libkindrv/archive/%{version}/%{name}-%{version}.tar.gz
# merged in upstream master, will be removed once a new version has been tagged
Patch0: libkindrv.printf.patch
# merged in upstream master, will be removed once a new version has been tagged
Patch1: libkindrv.configurable-udev-rules-dir.patch

BuildRequires:  boost-devel
BuildRequires:  boost-system
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig(udev)

%description
This driver allows to navigate robotic arms by Kinova.
It supports different modes for arm navigation and finger control.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%build
# we build the doc separately because we only want it in libkindrv-devel
# and 'make install' would install it in the wrong directory
%cmake \
  -DBUILD_DOC=OFF \
  -DUDEV_INSTALL_DIR=%{_udevrulesdir}

%cmake_build

%cmake_build --target apidoc


%install
%cmake_install


%files
%license LICENSE.GPL LICENSE.LGPL
%{_libdir}/libkindrv.so.*
%{_udevrulesdir}/10-libkindrv.rules


%files devel
%doc %{_vpath_builddir}/doc/html
%{_includedir}/*
%{_libdir}/libkindrv.so
%{_libdir}/pkgconfig/libkindrv.pc


%changelog
* Sat Sep 05 2020 Till Hofmann <thofmann@fedoraproject.org> - 0.1.2-25
- Adapt to cmake out-of-source builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-19
- Rebuilt for Boost 1.69

* Fri Nov 16 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.1.2-18
- Switch to GitHub source

* Wed Jul 18 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.1.2-17
- Install udev rules in udevrulesdir

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-14
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-11
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-10
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-8
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.1.2-3
- Rebuild for boost 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 06 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.1.2-1
- Update to 0.1.2
* Wed Jul 02 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.1.0-1.20140702
- Update to 0.1.0
* Tue Jun 03 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.1.0-1.20140617
- Initial package
