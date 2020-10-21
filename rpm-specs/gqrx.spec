Name:           gqrx
Version:        2.12.1
Release:        5%{?dist}
Summary:        Software defined radio receiver powered by GNU Radio and Qt

License:        GPLv3+ and GPLv2+ and BSD
URL:            http://gqrx.dk/
Source0:        https://github.com/csete/gqrx/archive/v%{version}.tar.gz

Patch0:         0001-Update-FSF-Adres-for-afsk1200.patch
Patch1:         gqrx-boost173.patch

BuildRequires:  gcc-c++
BuildRequires:  gnuradio-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  git
BuildRequires:  gr-osmosdr-devel
BuildRequires:  pkgconfig(gnuradio-analog)
BuildRequires:  pkgconfig(gnuradio-blocks)
BuildRequires:  pkgconfig(gnuradio-digital)
BuildRequires:  pkgconfig(gnuradio-filter)
BuildRequires:  pkgconfig(gnuradio-fft)
BuildRequires:  pkgconfig(gnuradio-runtime)
BuildRequires:  pkgconfig(gnuradio-osmosdr)
BuildRequires:  boost-devel
BuildRequires:  log4cpp-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Needed by gnuradio-devel, not gqrx.
BuildRequires:  CGAL-devel

%description
Gqrx is a software defined radio receiver powered by the GNU Radio SDR
framework and the Qt graphical toolkit.

%prep
%autosetup -S git -p1

%build
%qmake_qt5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}

# icon
install -Dpm 644 resources/icons/%{name}.svg \
                 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# appdata
install -Dpm 644 %{name}.appdata.xml \
                 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
# desktop-file
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications %{name}.desktop

%check
appstream-util validate-relax --nonet \
               %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%{_bindir}/gqrx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc COPYING README.md

%changelog
* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.12.1-5
- Rebuilt for new gnuradio

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Jonathan Wakely <jwakely@redhat.com> - 2.12.1-3
- Rebuilt and patched for Boost 1.73.0

* Wed Apr 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.12.1-2
- Rebuilt for new gnuradio

* Fri Mar 20 2020 Richard Shaw <hobbes1069@gmail.com> - 2.12.1-1
- Update to 2.12.1 for compatibility with gnuradio 3.8.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.11.5-6
- Rebuilt for new gnuradio

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.11.5-4
- Rebuilt for new gnuradio

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.11.5-2
- Rebuilt for new gnuradio

* Tue Jun 05 2018 Dave Olsthoorn <dave@bewaar.me> - 2.11.5-1
- new version, changelog: https://github.com/csete/gqrx/releases/tag/v2.11.5

* Tue Apr 17 2018 Dave Olsthoorn <dave@bewaar.me> - 2.11.4-1
- new upstream version

* Thu Mar 29 2018 Dave Olsthoorn <dave@bewaar.me> - 2.11.2-1
- new version upstream: https://github.com/csete/gqrx/releases/tag/v2.11.2

* Wed Mar 21 2018 Dave Olsthoorn <dave@bewaar.me> - 2.11.1-1
- new upstream version

* Sun Feb 18 2018 Dave Olsthoorn <dave@bewaar.me> - 2.10-1
- new version
- add BuildRequire for gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Dave Olsthoorn <dave@bewaar.me> - 2.9-1
- new version

* Sun Sep 17 2017 Dave Olsthoorn <dave@bewaar.me> - 2.8-1
- New version

* Thu Aug 24 2017 Dave Olsthoorn <dave@bewaar.me> - 2.7-1
- New version, also fix broken dependencies

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 2.6.1-5
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6.1-4
- Rebuilt for new gnuradio

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6.1-2
- Rebuilt for new gr-osmosdr

* Mon Feb 20 2017 Dave Olsthoorn <dave@bewaar.me> - 2.6.1-1
- new version

* Tue Feb 07 2017 Dave Olsthoorn <dave@bewaar.me> - 2.6-2
- Rebuild for Boost 1.63

* Tue Oct 04 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 2.6-1
- new version
- build with qt5 instead of qt4

* Sun Sep 18 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 2.5.3-6
- Rebuild for new gnuradio

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.3-5
- Rebuilt for new gnuradio

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.3-4
- Rebuilt for new gnuradio

* Tue May 03 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 2.5.3-3
- add appdata

* Thu Mar 24 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 2.5.3-2
- rebuilt with pulseaudio and gr-osmosdr

* Sat Feb 27 2016 Dave Olsthoorn <dave.olsthoorn@gmail.com> - 2.5.3-1
- new version 2.5.3
- remove desktop file patch
- remove nonexistent news.txt from %%doc

* Thu Feb 11 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-19
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 2.3.2-17
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-16
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-15
- Rebuilt for new gnuradio

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-14
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.3.2-13
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-12
- Rebuilt for new gnuradio

* Tue Aug  4 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-11
- Rebuilt for new boost

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-9
- Rebuilt for new gnuradio

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.3.2-8
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-6
- Rebuilt for new gnuradio

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-4
- Rebuild for new gnuradio

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 2.3.2-3
- Rebuild for boost 1.57.0

* Mon Jan 12 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-2
- Fixed categories in desktop file
  Resolves: rhbz#1181130

* Mon Dec  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.3.2-1
- New version
- Fixed download URL
- Packaged desktop file and icon according to guidelines

* Thu Oct 23 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.0-13
- Rebuilt for new gr-osmosdr and gnuradio

* Tue Sep  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.0-12
- Rebuilt for new gnuradio

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.0-10
- Rebuilt for new gnuradio

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 2.2.0-8
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2.2.0-7
- rebuild for boost 1.55.0

* Thu Mar 13 2014 Josh Bressers <bressers@redhat.com> 2.2.0-6
- Rebuild to fix broken rawhide dependency

* Sat Mar 8 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.2.0-5
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Thu Feb 20 2014 Josh Bressers <bressers@redhat.com> 2.2.0-4
- Fix the License field

* Sat Feb 08 2014 Josh Bressers <bressers@redhat.com> 2.2.0-3
- Fix some issues noted in bug 1006104

* Fri Feb 07 2014 Josh Bressers <bressers@redhat.com> 2.2.0-2
- Package version 2.2.0

* Mon Sep 9 2013 Josh Bressers <bressers@redhat.com> 2.1_git_298_g0e78-1
- Initial RPM
