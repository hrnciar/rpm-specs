%{?mingw_package_header}

Name:           mingw-libxslt
Version:        1.1.34
Release:        1%{?dist}
Summary:        MinGW Windows Library providing the Gnome XSLT engine

License:        MIT
URL:            http://xmlsoft.org/XSLT/
Source0:        ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-libxml2 >= 2.7.2-3

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-libxml2 >= 2.7.2-3

BuildRequires:  pkgconfig

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine


# Win32
%package -n mingw32-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw32-libxml2 >= 2.7.2-3
Requires:       pkgconfig

%description -n mingw32-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw32-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw32-libxslt = %{version}-%{release}

%description -n mingw32-libxslt-static
Static version of the MinGW Windows LibXSLT library.

# Win64
%package -n mingw64-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw64-libxml2 >= 2.7.2-3
Requires:       pkgconfig

%description -n mingw64-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw64-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw64-libxslt = %{version}-%{release}

%description -n mingw64-libxslt-static
Static version of the MinGW Windows LibXSLT library.


%{?mingw_debug_package}


%prep
%autosetup -n libxslt-%{version} -p1


%build
%mingw_configure --without-python --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Remove doc and man which duplicate stuff already in Fedora native package.
rm -r %{buildroot}%{mingw32_docdir}
rm -r %{buildroot}%{mingw32_mandir}
rm -r %{buildroot}%{mingw64_docdir}
rm -r %{buildroot}%{mingw64_mandir}

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-libxslt
%doc COPYING Copyright
%{mingw32_bindir}/xslt-config
%{mingw32_bindir}/xsltproc.exe
%{mingw32_includedir}/libexslt
%{mingw32_includedir}/libxslt
%{mingw32_bindir}/libexslt-0.dll
%{mingw32_libdir}/libexslt.dll.a
%{mingw32_bindir}/libxslt-1.dll
%{mingw32_libdir}/libxslt.dll.a
%{mingw32_libdir}/pkgconfig/libexslt.pc
%{mingw32_libdir}/pkgconfig/libxslt.pc
%{mingw32_libdir}/xsltConf.sh
%{mingw32_datadir}/aclocal/libxslt.m4

%files -n mingw32-libxslt-static
%{mingw32_libdir}/libexslt.a
%{mingw32_libdir}/libxslt.a

# Win64
%files -n mingw64-libxslt
%doc COPYING Copyright
%{mingw64_bindir}/xslt-config
%{mingw64_bindir}/xsltproc.exe
%{mingw64_includedir}/libexslt
%{mingw64_includedir}/libxslt
%{mingw64_bindir}/libexslt-0.dll
%{mingw64_libdir}/libexslt.dll.a
%{mingw64_bindir}/libxslt-1.dll
%{mingw64_libdir}/libxslt.dll.a
%{mingw64_libdir}/pkgconfig/libexslt.pc
%{mingw64_libdir}/pkgconfig/libxslt.pc
%{mingw64_libdir}/xsltConf.sh
%{mingw64_datadir}/aclocal/libxslt.m4

%files -n mingw64-libxslt-static
%{mingw64_libdir}/libexslt.a
%{mingw64_libdir}/libxslt.a


%changelog
* Tue Mar 10 2020 Sandro Mani <manisandro@gmail.com> - 1.1.34-1
- Update to 1.1.34

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 David King <amigadave@amigadave.com> - 1.1.33-1
- Update to 1.1.33
- Fix CVE-2019-11068 (#1709699)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.28-1
- Update to 1.1.28

* Sat Oct 13 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.27-2
- Fix a regression in default namespace handling (GNOME BZ #684564)

* Sat Sep 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.27-1
- Update to 1.1.27

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.26-9
- Added win64 support (contributed by Mikkel Kruse Johnsen)

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.26-8
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.1.26-7
- Renamed the source package to mingw-libxslt (#800931)
- Modernize the spec file
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.26-6
- Rebuild against the mingw-w64 toolchain
- Fix compatibility with mingw-w64

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.1.26-4
- Rebuilt against win-iconv

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.1.26-3
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org. - 1.1.26-1
- Update to 1.1.26

* Mon Sep 21 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.25-2
- Fix a locking bug in 1.1.25 (patch from native libxslt package)

* Thu Sep 17 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.25-1
- Update to 1.1.25
- Dropped upstreamed CVE patch
- Dropped upstreamed mingw32 patches
- Added a patch to never use pthreads even if it's available
- Automatically generate debuginfo subpackages

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.24-8
- Resolve FTBFS

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.24-7
- Use %%global instead of %%define
- Dropped the reference to the multilib patch as it isn't used for MinGW
- Fixed dangling-relative-symlink rpmlint warning

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.24-6
- Added some more comments in the .spec file
- Added -static subpackage
- Dropped the 'gzip ChangeLog' line as the ChangeLog isn't bundled anyway
- Fixed %%defattr line

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1.24-5
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1.24-4
- Include license file.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1.24-3
- Use _smp_mflags.
- Rebuild libtool.
- +BRs dlfcn and iconv.

* Sat Oct 25 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.24-2
- Initial RPM release.
