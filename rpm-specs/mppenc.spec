Summary: Musepack SV7 audio file encoder
Name: mppenc
Version: 1.16
Release: 19%{?dist}

# Some source files by one of the authors lack a license header.
# Musepack website acknowledges the licensing as "LGPL".
# Shy Keidar from the Musepack project additionally has confirmed
# that "mppenc as a whole is licensed under the LGPL v2.1 (or later)".
# That also matches the license used for the much newer SV8 release.
License: LGPLv2+

URL: http://www.musepack.net/
Source0: http://files.musepack.net/source/mppenc-%{version}.tar.bz2
# prefer Fedora optflags
Patch0: mppenc-1.16-cflags.patch
# compile wave_in.c with -fno-strict-aliasing because of dereferencing
# pointer after cast-madness: short int* -> void* -> unsigned long*
Patch1: mppenc-1.16-strict-aliasing.patch

BuildRequires:  gcc
BuildRequires: cmake

%description
This is a Musepack StreamVersion7 encoder for audio.

Musepack is an audio compression format with a strong emphasis on high
quality. It's not lossless, but it is designed for transparency, so that
you won't be able to hear differences between the original wave file and
the much smaller MPC file. It is based on the MPEG-1 Layer-2 / MP2
algorithms, but has rapidly developed and vastly improved and is now at an
advanced stage in which it contains heavily optimized and patentless code.


%prep
%setup -q
%patch0 -p1 -b .cflags
%patch1 -p1 -b .strict-aliasing


%build
%cmake .
%make_build VERBOSE=1


%install
%make_install


%files
%doc Changelog
%{_bindir}/mppenc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Michael Schwendt <mschwendt@fedoraproject.org> - 1.16-17
- Cannot reproduce FTBFS in Rawhide, since mock build works, but
  update spec file with newer macros.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 24 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.16-1
- Compile wave_in.c with -fno-strict-aliasing because of dereferencing
  pointer after cast-madness: short int* -> void* -> unsigned long*

* Sat Nov 21 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.16-0.2
- Spec comments for package review.

* Sat Nov 21 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.16-0.1
- Initial packaging for Fedora.
