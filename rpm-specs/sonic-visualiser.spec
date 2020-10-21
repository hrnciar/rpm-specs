Name:           sonic-visualiser
Version:        4.2
Release:        1%{?dist}
Summary:        A program for viewing and exploring audio data

License:        GPLv2+
URL:            https://sonicvisualiser.org/
Source0:        https://code.soundsoftware.ac.uk/attachments/download/2755/sonic-visualiser-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  bzip2-devel
BuildRequires:  capnproto
BuildRequires:  dataquay-devel
BuildRequires:  desktop-file-utils
BuildRequires:  liblo-devel
BuildRequires:  pkgconfig(capnp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fishsound)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  vamp-plugin-sdk-devel >= 2.5
Requires:       hicolor-icon-theme

%description
Sonic Visualiser is an application for viewing and analyzing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to
it.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the Vamp
analysis plugin format – as well as applying standard audio effects.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT
# fix permissions
chmod +x %{buildroot}%{_bindir}/*vamp*


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sonic-visualiser.desktop


%files
%license COPYING
%doc CHANGELOG CITATION README.*
%{_bindir}/piper-vamp-simple-server
%{_bindir}/sonic-visualiser
%{_bindir}/vamp-plugin-load-checker
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
* Tue Aug 18 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.2-1
- Update to 4.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Neal Gompa <ngompa13@gmail.com> - 4.1-1
- Update to 4.1

* Sat Jul 18 2020 Neal Gompa <ngompa13@gmail.com> - 4.0.1-2
- Rebuilt for capnproto 0.8.0

* Sun Feb  2 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.3-1
- Update to 3.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.1-11
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.4.1-8
- Enable MP3 audio support

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov  7 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.4.1-2
- Fix tests on s390 and ppc64 (bug #1161119)

* Sun Nov  2 2014 Michel Salim <salimma@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Rex Dieter <rdieter@fedoraproject.org> 2.1-3
- rebuild (qt5 qreal/arm)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Michel Salim <salimma@fedoraproject.org> - 2.1-1
- Update to 2.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep  9 2012 Michel Salim <salimma@fedoraproject.org> - 2.0-1
- Update to 2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.9-1
- Update to 1.9

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug  9 2011 Michel Salim <salimma@fedoraproject.org> - 1.8-3
- Fix for Qt 4.8 disallowing virtual inheritance of QObject (Radek Novacek)

* Sun Jul 31 2011 Rex Dieter <rdieter@fedoraproject.org> 1.8-2
- rebuild (rasqal/redland)
- patch for raptor2 support

* Tue Jun 21 2011 Michel Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.7.2-2
- Rebuild against new liblo-0.26

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.7.2-1
- Updated to 1.7.2
- Release Notes:
- (reference: https://sourceforge.net/projects/sv1/files/sonic-visualiser/1.7.2/CHANGELOG/download)
-   The time-value layer now has an origin line and an option to
 show derivatives (change from one point to the next) rather than
 raw values
-   A crash when pressing Play straight after New Session has been
 fixed
-   Builds with latest liboggz

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.7.1-2
- Bump for new liboggz lib

* Wed Jan 13 2010 Michel Salim <salimma@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6-6
- rebuild (redland)

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6-5
- rebuild (rasqal/redland)

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.6-4
- Update desktop file according to F-12 FedoraStudio feature

* Sun Sep 13 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-3
- No longer conflict with RPM Fusion packaging
- Updated icon cache scriptlet

* Sun Aug 23 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-2
- Package now conflicts with RPM Fusion packaging

* Fri Aug 21 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-1
- Update to 1.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Michel Salim <salimma@fedoraproject.org> - 1.5-1
- Update to 1.5

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Michel Salim <salimma@fedoraproject.org> - 1.4-3
- Fix compilation problem with GCC 4.4

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 1.4-2
- Fix qmake profiles to properly detect 64-bit Linux

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 1.4-1
- Update to 1.4
- Replace PortAudio dependency with PulseAudio

* Thu Jul 17 2008 Michel Salim <salimma@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sun Mar 30 2008 Michel Salim <michel.sylvan@gmail.com> - 1.2-1
- Update to 1.2

* Fri Feb 15 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-5
- Use correct optflags

* Wed Feb 13 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-4
- Exclude ppc for now. On it, qmake uses wrong (x86) optflags (#432733).
- Add missing BR on libfishsound-devel

* Sun Feb  3 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-3
- Add some #includes, needed due to GCC 4.3's header dependency cleanup

* Sun Jan 27 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-2
- Fix icon placement and license

* Wed Jan 16 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-1
- Initial Fedora package
