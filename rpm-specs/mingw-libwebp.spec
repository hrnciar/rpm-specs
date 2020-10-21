%{?mingw_package_header}

Name:           mingw-libwebp
Version:        1.1.0
Release:        3%{?dist}
Summary:        MinGW compilation of Library and tools for the WebP format

License:        BSD
URL:            http://webmproject.org
Source0:        http://downloads.webmproject.org/releases/webp/libwebp-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg


%description

WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

# Win32
%package -n mingw32-libwebp
Summary:        MinGW compilation of Library and tools for the WebP format


%description -n mingw32-libwebp
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.


# Win64
%package -n mingw64-libwebp
Summary:        MinGW compilation of Library and tools for the WebP format

%description -n mingw64-libwebp
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%?mingw_debug_package


%prep
%autosetup -p1 -n libwebp-%{version}


%build
%mingw_configure \
        --enable-shared --disable-static \
        --enable-libwebpmux --enable-libwebpdemux \
        --enable-libwebpdecoder

%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

#drop unneeded files
rm -f %{buildroot}%{mingw32_libdir}/libwebp*.la
rm -f %{buildroot}%{mingw64_libdir}/libwebp*.la
rm -fr %{buildroot}%{mingw32_mandir}
rm -fr %{buildroot}%{mingw64_mandir}


# Win32
%files -n mingw32-libwebp
%license PATENTS COPYING

%{mingw32_bindir}/cwebp.exe
%{mingw32_bindir}/dwebp.exe
%{mingw32_bindir}/img2webp.exe
%{mingw32_bindir}/webpinfo.exe
%{mingw32_bindir}/webpmux.exe
%{mingw32_bindir}/libwebp-7.dll
%{mingw32_bindir}/libwebpdecoder-3.dll
%{mingw32_bindir}/libwebpdemux-2.dll
%{mingw32_bindir}/libwebpmux-3.dll
%{mingw32_includedir}/webp
%{mingw32_libdir}/pkgconfig/libwebp.pc
%{mingw32_libdir}/pkgconfig/libwebpdecoder.pc
%{mingw32_libdir}/pkgconfig/libwebpdemux.pc
%{mingw32_libdir}/pkgconfig/libwebpmux.pc
%{mingw32_libdir}/libwebp.dll.a
%{mingw32_libdir}/libwebpdecoder.dll.a
%{mingw32_libdir}/libwebpdemux.dll.a
%{mingw32_libdir}/libwebpmux.dll.a

# Win64
%files -n mingw64-libwebp
%license PATENTS COPYING

%{mingw64_bindir}/cwebp.exe
%{mingw64_bindir}/dwebp.exe
%{mingw64_bindir}/img2webp.exe
%{mingw64_bindir}/webpinfo.exe
%{mingw64_bindir}/webpmux.exe
%{mingw64_bindir}/libwebp-7.dll
%{mingw64_bindir}/libwebpdecoder-3.dll
%{mingw64_bindir}/libwebpdemux-2.dll
%{mingw64_bindir}/libwebpmux-3.dll
%{mingw64_includedir}/webp
%{mingw64_libdir}/pkgconfig/libwebp.pc
%{mingw64_libdir}/pkgconfig/libwebpdecoder.pc
%{mingw64_libdir}/pkgconfig/libwebpdemux.pc
%{mingw64_libdir}/pkgconfig/libwebpmux.pc
%{mingw64_libdir}/libwebp.dll.a
%{mingw64_libdir}/libwebpdecoder.dll.a
%{mingw64_libdir}/libwebpdemux.dll.a
%{mingw64_libdir}/libwebpmux.dll.a

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.0.3-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Sandro Mani <manisandro@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Sandro Mani <manisandro@gmail.com> - 0.6.1-1
- Update to 0.6.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Thu Dec 22 2016 Sandro Mani <manisandro@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Sat Oct 29 2016 Sandro Mani <manisandro@gmail.com> - 0.5.1-2
- Backport e2affacc35f1df6cc3b1a9fa0ceff5ce2d0cce83 (CVE-2016-9085, rhbz#1389338)

* Fri Aug 12 2016 Sandro Mani <manisandro@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Sandro Mani <manisandro@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Fri Oct 30 2015 Sandro Mani <manisandro@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Thu Mar 27 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 0.2.1-4
- Fix mingw64 BRs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Paweł Forysiuk <tuxator@o2.pl> - 0.2.1-2
- Fix Buildrequires
- Add COPYING files

* Sun Dec 30 2012 Paweł Forysiuk <tuxator@o2.pl> - 0.2.1-1
- Initial packaging

