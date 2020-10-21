Name:           vmpk
Version:        0.7.2
Release:        3%{?dist}
Summary:        Virtual MIDI Piano Keyboard
License:        GPLv3+
URL:            http://vmpk.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel >= 5.1
BuildRequires:  qt5-qtsvg-devel >= 5.1
BuildRequires:  qt5-qttools-devel >= 5.1
BuildRequires:  qt5-qtx11extras-devel >= 5.1
BuildRequires:  drumstick-devel >= 1.1.3
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  desktop-file-utils
Requires:       fluid-soundfont-gm

%description
VMPK is a MIDI event generator/receiver. It doesn't produce any sound by
itself, but can be used to drive a MIDI synthesizer (either hardware or
software, internal or external). You can use the computer's keyboard to play
MIDI notes, and also the mouse. You can use the Virtual MIDI Piano Keyboard to
display the played MIDI notes from another instrument or MIDI file player.


%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%doc NEWS README ChangeLog AUTHORS TODO COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.7.2-1
- Release 0.7.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7.0-2
- Remove description of JACK driver

* Sat Apr 21 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 (BZ#1563239)

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2a-7
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2a-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2a-1
- Update to 0.6.2a (BZ#1296770)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Oct 17 2014 Robin Lee <cheeselee@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  9 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.0-4
- Use the RtMidi shared object
- License revised to "GPLv3+ and (LGPLv2 with exceptions or GPLv3)"

* Sat Jul 30 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.0-3
- License specified to "GPLv3+ and MIT and (LGPLv2 with exceptions or GPLv3)"

* Wed Jun 22 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.0-2
- Use JACK driver instead of ALSA

* Mon Jun  6 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.0-1
- Initial specfile
