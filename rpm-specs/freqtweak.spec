
Summary:       Realtime audio frequency spectral manipulation
Name:          freqtweak
Version:       0.7.2
Release:       24%{?dist}
URL:           http://%{name}.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}.png
Source2:       %{name}.desktop
Patch0:        %{name}-%{version}-gcc44.patch
Patch1:        %{name}-%{version}-long.patch
# correct macro in error
Patch2:        %{name}-%{version}-man-page.patch  
# correct fsf address
Patch3:        %{name}-%{version}-fsf-address.patch  
# gcc7 fix
Patch4:        %{name}-gcc7.patch
Patch5:        %{name}-%{version}-wx3.0.patch

License:       GPLv2+
Requires:      hicolor-icon-theme

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: pkgconfig 
BuildRequires: libsigc++-devel 
BuildRequires: desktop-file-utils 
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel 
BuildRequires: libxml2-devel
BuildRequires: wxGTK3-devel

%description
FreqTweak is a tool for FFT-based realtime audio spectral manipulation
and display. It provides several algorithms for processing audio data
in the frequency domain and a highly interactive GUI to manipulate the
associated filters for each. It also provides high-resolution spectral
displays in the form of scrolling-raster spectragrams and energy vs
frequency plots displaying both pre- and post-processed spectra.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e 's|-O2 -fexpensive-optimizations -funroll-loops -finline-functions -ffast-math|%{optflags}|'\
    Makefile.in

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install

# install icon in the proper freedesktop location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE2}

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Scott Talbert <swt@techie.net> - 0.7.2-21
- Rebuild with wxWidgets 3.0 and fix FTBFS (#1604007)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-18
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.7.2-15
- gcc7 fix

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 02 2012 Brendan Jones <brendan.s.jones@gmail.com> 0.7.2-5
- Patch the FSF address for upstream (but not the COPYING file) 

* Fri Apr 27 2012 Brendan Jones <brendan.s.jones@gmail.com> 0.7.2-4
- Man page patch and further correction of macros

* Wed Apr 25 2012 Brendan Jones <brendan.s.jones@gmail.com> 0.7.2-3
- Corrected desktop file categories and macros

* Thu Feb 09 2012 Brendan Jones <brendan.s.jones@gmail.com> 0.7.2-2
- Imported from CCRMA, packaged according to Fedora guidelines

* Tue Oct 13 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.7.2-1
- updated to 0.7.2, added patch for gcc44/fc11 and unsigned long
  precision loss on x86_64
- sync with latest post scripts (borrowed from Fedora's ardour spec)
- add Fedora's DigitalProcessing menu category

* Wed Feb  6 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- rebuilt on CentOS 5

* Mon Nov 19 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- changed build requirements for modified wxGKT24-2 package on f8
  (because f8 wxGTK obsoletes all older compat packages)

* Wed Nov 14 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- updated desktop categories

* Wed Dec  6 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-5
- added long int patch for x86_64

* Wed May  3 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-4
- added home brewed icon

* Wed May  3 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-3
- added Planet CCRMA menu categories

* Wed Apr  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-2
- pull in the pangox libraries, otherwise there is an unknown symbol
  in the link stage

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-1
- proper build dependency for fc5

* Mon May 30 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-1
- add patch to remove jack_set_server_dir function (patch2), did this
  for test fc4 build, no change in release for now
- build dependency now is wxGTK2 (from fedora extras)
- tweaked configure patch to recognize wxgtk2-2.4-config

* Tue Feb  8 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-1
- add patch to inject very low level noise at the inputs to try to
  avoid denormals
- erased old jack_set_server_dir library call
- arghh, reverted patch, for some reason the cpu load goes up a lot

* Tue Jul 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.1-1
- updated to 0.6.1

* Sat Apr 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.6.0-1
- updated to 0.6.0

* Mon Sep 22 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.3-1
- updated to 0.5.3
- added help to file list (/usr/share/freqtweak/help/usagehelp.html)

* Wed Aug 20 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.2-1
- updated to 0.5.2, added release tags

* Sat Jul 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.5.1-1
- updated to 0.5.1

* Tue Apr  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.8-2
- rebuilt for newer version of fftw

* Fri Apr  4 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.8-1
- update to 0.4.8

* Wed Apr  2 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.7-3
- rebuild for jack 0.66.3, added explicit requires for it

* Sun Mar 23 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.7-2
- rebuild due to update of wxGTK, patch configure to recognize the config
  script of wxGTK 2.4.0 (wxgtk-2.4-config instead of wx-config)

* Tue Mar  4 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.7-1
- update to 0.4.7

* Wed Feb 11 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.6-1
- update to 0.4.6

* Sun Nov 17 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.5-1
- update to 0.4.5

* Tue Nov 12 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.4-3
- menu in 7.2/7.3 was in wrong group

* Sun Nov 10 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.4-2
- added patch to rename jack alsa ports for jack >= 0.40
- added explicit dependency to jack
- added redhat menu entry

* Tue Oct 15 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.3-1
- Initial build. 
- Update to 0.4.3
