%{?mingw_package_header}

Name:           mingw-flac
Version:        1.3.2
Release:        10%{?dist}
Summary:        Encoder/decoder for the Free Lossless Audio Codec

# BSD: libraries, GPLv2+: tools and examples
License:        BSD and GPLv2+
URL:            http://xiph.org/flac/
Source0:        http://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
# Copied from the native Fedora package.
Patch0:         flac-cflags.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-win-iconv

BuildRequires:  automake autoconf libtool gettext-devel
BuildRequires:  nasm

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.


%package -n mingw32-flac
Summary:        %{summary}

%description -n mingw32-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win32 target.


%package -n mingw32-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw32-flac = %{version}-%{release}

%description -n mingw32-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win32 target.


%package -n mingw64-flac
Summary:        %{summary}

%description -n mingw64-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win64 target.


%package -n mingw64-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw64-flac = %{version}-%{release}

%description -n mingw64-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n flac-%{version}
%patch0 -p1 -b .cflags


%build
# use our libtool to avoid problems with RPATH
./autogen.sh -V

# -funroll-loops makes encoding about 10% faster
export CFLAGS="%{optflags} -funroll-loops"
%mingw_configure \
    --disable-xmms-plugin \
    --disable-silent-rules \
    --disable-thorough-tests

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# documentation in native package
rm -rf %{buildroot}%{mingw32_docdir}/flac*
rm -rf %{buildroot}%{mingw64_docdir}/flac*
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la


%files -n mingw32-flac
%doc AUTHORS README
%license COPYING*
%{mingw32_bindir}/libFLAC-8.dll
%{mingw32_bindir}/libFLAC++-6.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libFLAC.dll.a
%{mingw32_libdir}/libFLAC++.dll.a
%{mingw32_libdir}/pkgconfig/flac.pc
%{mingw32_libdir}/pkgconfig/flac++.pc
%{mingw32_datadir}/aclocal/libFLAC.m4
%{mingw32_datadir}/aclocal/libFLAC++.m4

%files -n mingw32-flac-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-flac
%doc AUTHORS README
%license COPYING*
%{mingw64_bindir}/libFLAC-8.dll
%{mingw64_bindir}/libFLAC++-6.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libFLAC.dll.a
%{mingw64_libdir}/libFLAC++.dll.a
%{mingw64_libdir}/pkgconfig/flac.pc
%{mingw64_libdir}/pkgconfig/flac++.pc
%{mingw64_datadir}/aclocal/libFLAC.m4
%{mingw64_datadir}/aclocal/libFLAC++.m4

%files -n mingw64-flac-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3.2-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 David King <amigadave@amigadave.com> - 1.3.2-1
- Update to 1.3.2 (#1409574)
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 David King <amigadave@amigadave.com> - 1.3.1-1
- Update to 1.3.1 (#1168768)
- Fixes CVE-2014-8962 and CVE-2014-9028

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 16 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-2
- Added tools subpackage
- Comment licensing breakdown

* Sat Jan 11 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-1
- Initial package, based on the native flac
