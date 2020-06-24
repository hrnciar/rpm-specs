
Name:           giada
Version:        0.16.3
Release:        1%{?dist}
Summary:        An audio looping machine

License:        GPLv3+
URL:            https://www.giadamusic.com
Source0:        https://github.com/monocasual/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
# submitted upstream https://github.com/monocasual/giada/issues/5
Source1:        giada.desktop

BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  fltk-fluid
BuildRequires:  fltk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  icoutils
BuildRequires:  jansson-devel
BuildRequires:  rtaudio-devel
BuildRequires:  rtmidi-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXext-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXinerama-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
giada is an audio looper for ALSA/JACK using the FLTK toolit.
Load or record up to 32 samples, choose to play them in single mode 
(drum machine) or loop mode (sequencer) and start the show with your computer 
keyboard as a controller. Giada aims to be a compact and portable virtual 
device for Linux for production use and live sets. 
%prep
%setup -q -n %{name}-%{version}

# convert icon
icotool -x src/ext/giada.ico

# fix build issue
sed -i 's|%f|%.3f|' src/gui/elems/mainWindow/mainTimer.cpp

%build
./autogen.sh
%configure --prefix=%{_prefix} --target=linux --enable-system-catch
%make_build

%install 
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %SOURCE1
install -D -m 644 giada_1_48x48x32.png %{buildroot}%{_datadir}/pixmaps/giada.png

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jun 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.3-1
- New upstream version

* Thu Mar 26 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.16.2.2-1
- New upstream version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.15.4-1
- Update to 0.15.4 fixes rhbz#1604101 rhbz#1674963 and rhbz#1703719

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot] com> - 0.14.4-1
- Update to 0.14.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-7
- Fix FTBFS (gcc5?), don't build with -Werror

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-6
- rebuild (fltk)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.7.0-2
- Add missing libsamplerate

* Wed Jun 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.7.0-1
- New upstream 0.7.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.5.6-1
- New upstream release

* Tue Dec 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.4-2
- Rebuild for new rtaudio

* Thu Nov 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.4-1
- New upstream, removing vst patch
- Apply desktop translation patch from Ismael Olea
- Remove unecessary scriptlets and add a more descriptive summary

* Mon Nov 26 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-4
- Missing BR libXext-devel

* Sun Nov 25 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-3
- Add missing BR rtaudio

* Sun Oct 21 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-2
- correct description and URL, add make flags

* Sun Oct 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.5.2-1
- Initial package
