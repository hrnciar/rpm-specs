Name:           kmetronome
Version:        1.0.1
Release:        2%{?dist}
License:        GPLv2+
Summary:        A MIDI metronome using the Drumstick library
URL:            http://kmetronome.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-devel >= 5.1
BuildRequires:  qt5-qtsvg-devel >= 5.1
BuildRequires:  qt5-qttools-devel >= 5.1
BuildRequires:  qt5-qtx11extras-devel >= 5.1
BuildRequires:  drumstick-devel >= 1.0
BuildRequires:  alsa-lib-devel >= 1.0
BuildRequires:  desktop-file-utils

%description
KMetronome is a MIDI metronome with Qt5 interface, based on the Drumstick
library. The intended audience is musicians and music students. Like
solid, real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA sequencer.

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}
# check the .desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc README ChangeLog AUTHORS TODO COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/*/*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 (#1768953)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-10
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-5
- BR: alsa-lib-devel

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Oct 19 2014 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun  4 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.10.0-3
- Fix a typo
- Add scriptlets to update the icon cache

* Sun Jun 26 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.10.0-2
- Add kde4-macros(api) requirement
- BR: gettext and desktop-file-utils added, alsa-lib-devel removed
- Check the desktop entry file
- Drop explicit %%doc tag from the manpage

* Thu Jun  9 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.10.0-1
- Initial specfile
