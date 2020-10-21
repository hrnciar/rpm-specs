%global commit0 bbe8386499621c8e60eebb06d80e966f13a69a95
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20200307

Name:           non-daw
Version:        1.2.0
Release:        20.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        A digital audio workstation for JACK

License:        GPLv2+ and ISC
URL:            https://non.tuxfamily.org/
Source0:        https://git.tuxfamily.org/non/non.git/snapshot/non-%{commit0}.tar.gz
# notified upstream of the following along with incorrect FSF address headers
Patch0:         add-lib64-in-ladspa-search-path.patch
Patch1:         fix-fsf-address.patch
# build optimization should be avoided in Fedora as Fedora has its own optimizations
Patch2:         remove-optimization-flags.patch

BuildRequires:  desktop-file-utils
BuildRequires:  imake
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  liblo-devel
BuildRequires:  liblrdf-devel
BuildRequires:  libsigc++20-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libXpm-devel
BuildRequires:  non-ntk-devel
BuildRequires:  non-ntk-fluid
BuildRequires:  python3
BuildRequires:  gcc-c++
BuildRequires:  %{_bindir}/pathfix.py
BuildRequires:  %{_bindir}/find
Requires:       jack-audio-connection-kit
Requires:       hicolor-icon-theme

%description
Non-daw is a digital audio workstation for JACK

%package -n non-mixer
Summary:        A digital audio mixer for JACK
Requires:       jack-audio-connection-kit
Requires:       hicolor-icon-theme

%description -n non-mixer
non-mixer is a powerful, reliable and fast modular Digital Audio Mixer

%package -n non-mixer-doc
Summary:        A digital audio mixer for JACK - Documentation

%description -n non-mixer-doc
non-mixer is a powerful, reliable and fast modular Digital Audio Mixer
This package contains the documentation.

%package -n non-session-manager
Summary:        A session manager for JACK
Requires:       jack-audio-connection-kit
Requires:       hicolor-icon-theme

%description -n non-session-manager
non-session-manager is an audio project session manager. It preserves
application state including JACK and MIDI connections between audio sessions.

%package -n non-session-manager-doc
Summary:        A session manager for JACK - Documentation

%description -n non-session-manager-doc
non-session-manager is an audio project session manager. It preserves
application state including JACK and MIDI connections between audio sessions.
This package contains the documentation.

%package -n non-sequencer
Summary:        A MIDI sequencer for JACK
Requires:       jack-audio-connection-kit
Requires:       hicolor-icon-theme

%description -n non-sequencer
non-sequencer is a powerful, lightweight, real-time, pattern-based MIDI 
sequencer

%package -n non-sequencer-doc
Summary:        A MIDI sequencer for JACK - Documentation

%description -n non-sequencer-doc
non-sequencer is a powerful, lightweight, real-time, pattern-based MIDI 
sequencer

%prep
%setup -q -n non-%{commit0}
%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -rf lib
pathfix.py -pni %{_bindir}/python3 waf $(find -name wscript)

%build
%set_build_flags
CXXFLAGS+=" -std=c++11"
./waf configure --prefix=%{_prefix} --libdir=%{_libdir} \
%ifarch %{ix86} x86_64

%else
--disable-sse
%endif
./waf build -v %{?_smp_mflags}

%install 
./waf install --destdir=%{buildroot} --docdir=%{buildroot}/%{_docdir}/
for i in %{buildroot}%{_datadir}/applications/*.desktop; do
    sed -i -e 's|\/usr\/bin\/||' $i
    desktop-file-validate $i;
done;
# correct locations
mv %{buildroot}%{_bindir}/bin/* %{buildrootdir}{_bindir}
# correct permissions
chmod 755 %{buildroot}%{_bindir}/*

#NOTE: No manpages, all documentation is at http://non.tuxfamily.org/wiki/Documentation

%files
%license COPYING
%{_bindir}/import*
%{_bindir}/%{name}
%{_bindir}/non-timeline
%{_docdir}/non-timeline
%{_datadir}/applications/non-timeline.desktop
%{_datadir}/icons/hicolor/*/apps/non-timeline*
%{_datadir}/pixmaps/non-timeline

%files -n non-mixer
%license COPYING
%{_bindir}/non-mixer
%{_bindir}/non-mixer-noui
%{_bindir}/non-midi-mapper
%{_datadir}/applications/non-mixer.desktop
%{_datadir}/icons/hicolor/*/apps/non-mixer*
%{_datadir}/pixmaps/non-mixer

%files -n non-mixer-doc
%license COPYING
%{_docdir}/non-mixer

%files -n non-session-manager
%license COPYING
%{_bindir}/nsm*
%{_bindir}/jackpatch
%{_bindir}/non-session-manager
%{_datadir}/applications/non-session-manager.desktop
%{_datadir}/icons/hicolor/*/apps/non-session-manager*
%{_datadir}/pixmaps/non-session-manager

%files -n non-session-manager-doc
%license COPYING
%{_docdir}/non-session-manager

%files -n non-sequencer
%license COPYING
%{_bindir}/non-sequencer
%{_datadir}/non-sequencer
%{_datadir}/applications/non-sequencer.desktop
%{_datadir}/icons/hicolor/*/apps/non-sequencer*
%{_datadir}/pixmaps/non-sequencer

%files -n non-sequencer-doc
%license COPYING
%{_docdir}/non-sequencer

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20.20200307gitbbe8386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.2.0-19.20200307gitbbe8386
- New git sync, built with waf built with python3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15.git16885e69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-14.git16885e69
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13.git16885e69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12.git16885e69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.2.0-11.git16885e69
- Added BR: python2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10.git16885e69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-9.git16885e69
- Disable SSE on non x86 arches (fixes FTBFS on ARMv7 and others)
- Enable vorbis support
- Put jackpatch in right sub package (rhbz 1336224)
- Fix ladspa plugins search path (rhbz 1317283)

* Thu Aug 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-8.git16885e69
- Fix up Release so upgrade path works correctly

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-5.git13c3ca8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-4.git13c3ca8
- rebuild (fltk)
- non-session-manager: omit non-sensical Obsoletes
- fix Release: tag

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3.1.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2.1.git13c3ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.5.git9fba8a8
- New source, adding additional sub packages, non-mixer
- obsoletes non-session-manager, non-sequencer

* Mon Aug 12 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.4.gitae6b78cf
- Unversioned doc dir changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.3.gitae6b78cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.gitae6b78cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.1.0-0.1.gitae6b78cf
- Initial build
