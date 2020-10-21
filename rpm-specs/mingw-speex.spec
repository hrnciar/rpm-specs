%{?mingw_package_header}

Name:           mingw-speex
Version:        1.2.0
Release:        6%{?dist}
Summary:        Voice compression format (codec)

License:        BSD
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/speex-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).


%package -n mingw32-speex
Summary:    Voice compression format (codec)

%description -n mingw32-speex
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the MinGW version, built for the win32 target.


%package -n mingw32-speex-tools
Summary:    The tools package for mingw32-speex
Requires:   mingw32-speex = %{version}-%{release}

%description -n mingw32-speex-tools
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This package contains tools files for the MinGW version of speex, built
for the win32 target.


%package -n mingw64-speex
Summary:    Voice compression format (codec)

%description -n mingw64-speex
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the MinGW version, built for the win64 target.


%package -n mingw64-speex-tools
Summary:    The tools package for mingw64-speex
Requires:   mingw64-speex = %{version}-%{release}

%description -n mingw64-speex-tools
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This package contains tools files for the MinGW version of speex, built
for the win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n speex-%{version}


%build
%{mingw_configure} --disable-static --enable-binaries

# Remove rpath from speexenc and speexdec
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win32/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win32/libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win64/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win64/libtool

# Fix libtool to recognize win64 archives
sed -i 's|file format pe-i386(\.\*architecture: i386)?|file format pe-x86-64|g' build_win64/libtool

%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libspeex*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libspeex*.la
rm -f $RPM_BUILD_ROOT%{mingw32_docdir}/speex/manual.pdf
rm -f $RPM_BUILD_ROOT%{mingw64_docdir}/speex/manual.pdf
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}


%files -n mingw32-speex
%license COPYING
%doc AUTHORS TODO ChangeLog README
%{mingw32_bindir}/libspeex-1.dll
%{mingw32_includedir}/speex
%{mingw32_datadir}/aclocal/speex.m4
%{mingw32_libdir}/pkgconfig/speex*.pc
%{mingw32_libdir}/libspeex.dll.a

%files -n mingw32-speex-tools
%{mingw32_bindir}/speexenc.exe
%{mingw32_bindir}/speexdec.exe

%files -n mingw64-speex
%license COPYING
%doc AUTHORS TODO ChangeLog README
%{mingw64_bindir}/libspeex-1.dll
%{mingw64_includedir}/speex
%{mingw64_datadir}/aclocal/speex.m4
%{mingw64_libdir}/pkgconfig/speex*.pc
%{mingw64_libdir}/libspeex.dll.a

%files -n mingw64-speex-tools
%{mingw64_bindir}/speexenc.exe
%{mingw64_bindir}/speexdec.exe


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 1.2.0-1
- Update to 1.2.0
- Use license macro for COPYING

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.23.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.22.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.21.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.20.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.19.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.18.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.17.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 6 2014 František Dvořák <valtri@civ.zcu.cz> - 1.2-0.16.rc1
- Update (review #970405)

* Mon Jun 3 2013 Steven Boswell <ulatekh@yahoo.com> - 1.2-0.15.rc1
- Ported existing Fedora package to MinGW
