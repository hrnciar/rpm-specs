Name:		demorse
Version:	1.2
Release:	13%{?dist}
Summary:	Command line tool for decoding Morse code signals

License:	GPLv2+
URL:		http://www.qsl.net/5b4az/pages/morse.html
Source0:	http://www.qsl.net/5b4az/pkg/morse/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:	alsa-lib-devel

%description
demorse is a non-interactive command line tool for decoding Morse code signals
into text. demorse detects the "dihs" and "dahs" that make a Morse code
character via the computer's sound card, which can be connected to a radio
receiver tuned to a CW Morse code transmission or to a tone generator.

The input signal is processed by a Goertzel tone detector which produces "mark"
or "space" (signal/no signal) outputs and the resulting stream of Morse code
"elements" is decoded into an ASCII character for printing to the screen.
Currently demorse is a non- interactive command line tool for the console and
decoded Morse signals are sent to stdout.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS README COPYING doc/demorse.html doc/Morsecode.txt
%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  2 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-1
- New version
  Resolves: rhbz#1044371
- Fixed whitespaces in the description
- Dropped format-security patch (upstreamed)

* Wed Dec  4 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1-3
- Fixed compilation with format-security
  Resolves: rhbz#1037032
- Updated URL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1-1
- New version
  Resolves: rhbz#909893
- RPM_BUILD_ROOT variables replaced by {buildroot} macros

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-1
- New version
  Resolves: rhbz#837243

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 29 2008 David Woodhouse <dwmw2@infradead.org> 0.9-2
- Fix CFLAGS

* Fri Feb 29 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9-1
- New Upstream Version 

* Sun Feb 17 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.8-3
- Initial SPEC

* Wed Nov 21 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.8-2
- Update License tag
- Copy of GPL is missing form upstream tarball, make note of this
- Rewrite makefile Patch
- include doc files

* Tue May 15 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.8-0
- Initial SPEC
