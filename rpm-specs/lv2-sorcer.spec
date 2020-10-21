%global commit 18e68914f2ae19dff01d77ce263a42c31041d0cc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global prerelease 20131104

Name:           lv2-sorcer
Version:        1.1
Release:        26%{prerelease}git%{shortcommit}%{?dist}
Summary:        An audio compressor for JACK

License:        GPLv3+
URL:            http://openavproductions.com/sorcer/
Source0:        https://github.com/harryhaaren/openAV-Sorcer/archive/%{shortcommit}.zip
Patch0:         lv2-sorcer-lv2dir.patch
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  faust
BuildRequires:  gtkmm24-devel
BuildRequires:  cairo-devel
BuildRequires:  boost-devel
BuildRequires:  fltk-devel
BuildRequires:  non-ntk-devel
BuildRequires:  libsndfile-devel
Requires:       lv2

%global __provides_exclude_from ^%{_libdir}/lv2/.*$

%description
Sorcer is a polyphonic wavetable synth LV2 plugin. Its sonic fingerprint is 
one of harsh modulated sub-bass driven walls of sound. Two morphing wavetable
oscillators and one sine oscillator provide the generation routines. The LFO
can be mapped to wavetable modulation as well as filter cutoff. An ADSR allows
for shaping the resulting sound, while a master volume finishes the signal
chain. Easily creating a variety of dubstep basslines and harsh pad sounds.

Additional presets can be found here:
 https://github.com/harryhaaren/openAV-presets

%prep
%setup -q -n openAV-Sorcer-%{commit}
%patch0 -p1
sed -i -e "s|-O3 -Wall|%{optflags}|"\
       -e "s|main.cpp|%{optflags} main.cpp|"  \
  makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot}%{_libdir}/lv2 
chmod 644 %{buildroot}%{_libdir}/lv2/*/*.ttl

%files
%doc README
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2620131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Petr Viktorin <pviktori@redhat.com> - 1.1-2520131104git18e6891
- Remove BuildRequires on python2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2420131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2320131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2220131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2120131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2020131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-1920131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-1820131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1-1720131104git18e6891
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-1620131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1-1520131104git18e6891
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1-1420131104git18e6891
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-1320131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1-1220131104git18e6891
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1-1120131104git18e6891
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-1020131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1-920131104git18e6891
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-820131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-720131104git18e6891
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1-6.20131104git18e6891
- rebuild(fltk)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1-5.1.20131104git18e6891
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.1.20131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.1.20131104git18e6891
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.1-2.1.20131104git18e6891
- Rebuild for boost 1.55.0

* Mon Nov 04 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.1-1.1.20131104git18e6891
- Update version

* Mon Nov 04 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-1.0.20131104git18e6891
- New upstream release

* Tue Oct 29 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.3.20131013git4e35643
- Add missing BR's

* Sat Oct 26 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.2.20131013git4e35643
- Remove presets, add to description

* Sun Oct 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-0.1.20131013git4e35643
- Initial package

