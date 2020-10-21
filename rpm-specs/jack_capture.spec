Name:		jack_capture
Version:	0.9.73
Release:	8%{?dist}
Summary:	Record sound files with JACK
# As explained in the COPYING file,
# jack_capture.c and atomicity/* are GPLv2+,
# jack_capture_gui2.cpp is BSD,
# atomic/* are LGPLv2+.
License:	GPLv2+ and BSD and LGPLv2+
URL:		https://github.com/kmatheussen/jack_capture
Source0:	http://archive.notam02.no/arkiv/src/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	lame-devel
BuildRequires:	libsndfile-devel

Requires:	meterbridge
Requires:	vorbis-tools


%description
Jack_capture is a program for recording sound files with JACK. It's default
operation is to capture whatever sound is going out to your speakers into a
file, but it can do a number of other operations as well.

%prep
%setup -q

# No need to look for the c++ compiler
sed -i '/CPP/d' Makefile

%build
make %{?_smp_mflags} OPTIMIZE="%{optflags}" LDFLAGS="$RPM_LD_FLAGS"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license COPYING
%doc README
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.73-4
- Replaced BR: gcc-c++ with BR: gcc
- Enabled liblo and lame support

* Fri Jul 20 2018 Adam Huffman <bloch@verdurin.com> - 0.9.73-3
- Add BR for gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.73-1
- Update to 0.9.73
- Specfile cleanup. Removing the GUI parts as it is no longer built or maintained
  upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.69-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.69-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Adam Huffman <bloch@verdurin.com> - 0.9.69-1
- Update to latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.9.61-1
- update to 0.9.61

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.56-4
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.9.56-2
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.56-1
- Update to 0.9.56 (drops /usr/bin/jack_capture_gui which depended on gtk1)

* Mon Jul 19 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.53-1
- Update to 0.9.53

* Sat Jul 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.52-1
- Update to 0.9.52

* Sat Jun 26 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.49-1
- Update to 0.9.49

* Tue Jun 15 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.48-1
- Update to 0.9.48

* Fri Jun 04 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.47-1
- Update to 0.9.47

* Wed Jun 02 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.44-1
- Update to 0.9.44
- Drop upstreamed patches

* Wed Feb 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.40-2
- Fix DSO-linking failure

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.40-1
- Update to 0.9.40

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.35-1
- Update to 0.9.35

* Tue May 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.34-1
- Update to 0.9.34
- Drop upstreamed ppc64 patch

* Fri May 08 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.33-1
- Update to 0.9.33
- Drop upstreamed patches
- Fix the build failure on ppc64

* Wed May 06 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.32-1
- Initial build
