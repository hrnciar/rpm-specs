%global prerel m1
%global prerel_d dev-m1

Name:  phasex
Version: 0.12.0
Release: 16.12.%{prerel}%{?dist}
Summary: PHASEX -- Phase Harmonic Advanced Synthesis EXperiment
License: GPLv2
URL:  https://github.com/disabled/phasex-dev

Source0: https://github.com/downloads/disabled/phasex-dev/%{name}-%{prerel_d}.tar.gz
Patch0: %{name}-cflags.patch
Patch1: %{name}-format.patch
Patch2: %{name}-asoundlib.patch
Patch3: %{name}-gcc10.patch

BuildRequires: gcc
BuildRequires: glibc-devel >= 2.3.0
BuildRequires: alsa-lib-devel >= 0.9.0
BuildRequires: jack-audio-connection-kit-devel >= 0.99.0
BuildRequires: libICE-devel
BuildRequires: lash-devel
BuildRequires: libsamplerate-devel >= 0.1.2
BuildRequires: gtk2-devel >= 2.4.0
BuildRequires: perl-interpreter
BuildRequires: desktop-file-utils

%description
PHASEX is an experimental JACK audio / ALSA MIDI softsynth for Linux
with a synth engine built around flexible phase modulation and
flexible oscillator/LFO sourcing.  Modulations include AM, FM, offset
PM, and wave select.  PHASEX comes equipped with a 12db/octave filter
with two distortion curves, a stereo crossover delay and chorus with
phaser, ADSR envelopes for amplifier and filter, realtime audio input
processing capabilities, and more.

%prep
%autosetup -p1 -n %{name}-%{prerel_d}

# Fix DSO linking
sed -i -e 's|\(-lpthread\)|\1 -lX11 -lgmodule-2.0|' configure

%build
%configure

%make_build

%install
%make_install

for s in 16 22 32 48 ; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp %{buildroot}%{_datadir}/phasex/pixmaps/phasex-icon-${s}x${s}.png \
            %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/phasex-icon.png
done

BASE="AudioVideo Audio"
XTRA="X-MIDI X-Digital_Processing X-Jack X-Synthesis Midi"

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{buildroot}%{_datadir}/phasex/%{name}.desktop

rm %{buildroot}%{_datadir}/phasex/phasex.desktop

%files
%doc README
%license COPYING
%{_bindir}/phasex
%{_datadir}/phasex/
%{_datadir}/themes/*
%{_datadir}/applications/phasex.desktop
%{_datadir}/icons/hicolor/*/apps/phasex-icon.png

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-16.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.12.0-15.12.m1
- Fix FTBFS with GCC 10
- Some spec cleanup

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-14.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.12.0-13.12.m1
- Fix FTBFS due to wrong include path
- Some spec cleanup

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-12.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-11.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-8.12.m1
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.12.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.0-0.11.m1
- Fix to use distro optflags. Also fixed FTBFS on ARM

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.10.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.12.0-0.9.
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.8.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.7.m1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.12.0-0.6.m1
- Update to 0.12.0.dev-m1
- Workaround DSO linking error

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.5.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.12.0-0.4.pre1
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.3.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.12.0-0.2.pre1
- Update to 0.12.0pre1
- Fix DSO linking error RHBZ#564951

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.12.0-0.1.beta4
- Fix optflags (RHBZ#499914)
- Update to 0.12.0beta4 (fixes segfault)
- Update desktop file according to F-12 FedoraStudio feature
- Update scriptlets

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  9 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.11.1-7
- Build with $RPM_OPT_FLAGS (#499914).
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11.1-5
- Autorebuild for GCC 4.3

* Mon Oct 22 2007 Anthony Green <green@redhat.com> - 0.11.1-4
- Fix tagging problem.

* Thu Oct 18 2007 Parag AN <panemade@gmail.com> - 0.11.1-3
- Really delete extra .desktop file after installation.

* Tue Oct 16 2007 Anthony Green <green@redhat.com> - 0.11.1-2
- Delete extra .desktop file after installation.
- Clean up .desktop file categories.

* Tue Oct 16 2007 Anthony Green <green@redhat.com> - 0.11.1-1
- First Fedora build.

* Tue Aug  7 2007 William Weston <weston@sysex.net> - 0.11.0-0
- Updated for 0.11.0.

* Thu May 24 2007 William Weston <weston@sysex.net> - 0.10.3-0
- Updated for 0.10.3.

* Tue May 15 2007 William Weston <weston@sysex.net> - 0.10.2-0
- Updated for 0.10.2.

* Thu May  3 2007 William Weston <weston@sysex.net> - 0.10.1-0
- Added README and COPYING to doc install.
- Updated for 0.10.1.

* Tue May  1 2007 William Weston <weston@sysex.net> - 0.10.0-0
- Initial RPM spec file.
