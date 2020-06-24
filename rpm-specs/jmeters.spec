Summary:       Multichannel audio level meter
Name:          jmeters
Version:       0.4.1
Release:       18%{?dist}
License:       GPLv2
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: gcc-c++
#BuildRequires: clalsadrv-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: libsndfile-devel
BuildRequires: libpng-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: cairo-devel

%description
Jmeters is a Jack multichannel audio level meter app.
It looks very similar to meterbridge since it uses the
same pixmaps.

%prep
%setup -q

sed -i -e 's|-O3|%{optflags}|' \
  -e 's|-march=native||' \
  -e 's|-m64||' source/Makefile


%build
cd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS -lpthread " CFLAGS="%{optflags}"

%install
cd source
mkdir -p %{buildroot}%{_bindir}
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-14
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.4.1-2
- Remove arch specific build flags, add cairo-devel

* Wed Nov 07 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.4.1-1
- Update to version 0.4.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.2.0-3
- Patch for libpng15 and FSF address

* Fri Feb 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.2.0-2 
- modified to Fedora packaging guidelines

* Wed May 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- add patch to link with -lpthread for fc13/gcc4.4.4

* Wed Mar 16 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.2.0-1
- initial build
