%{?mingw_package_header}

Name:           mingw-libxml2
Version:        2.9.10
Release:        1%{?dist}
Summary:        MinGW Windows libxml2 XML processing library

License:        MIT
URL:            http://xmlsoft.org/
Source0:        ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch0:         libxml2-multilib.patch
# Patch from openSUSE.
# See:  https://bugzilla.gnome.org/show_bug.cgi?id=789714
Patch1:         libxml2-2.9.8-python3-unicode-errors.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1780573
Patch2:         mingw-libxml2-2.9.10-fix-relaxed-approach-to-nested-documents.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1799738
Patch3:         mingw-libxml2-2.9.10-CVE-2019-20388.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1799788
Patch4:         mingw-libxml2-2.9.10-CVE-2020-7595.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib


%description
MinGW Windows libxml2 XML processing library.


# Win32
%package -n mingw32-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig

%description -n mingw32-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw32-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw32-libxml2 = %{version}-%{release}

%description -n mingw32-libxml2-static
Static version of the MinGW Windows XML processing library.

# Win64
%package -n mingw64-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig

%description -n mingw64-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw64-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw64-libxml2 = %{version}-%{release}

%description -n mingw64-libxml2-static
Static version of the MinGW Windows XML processing library.


%?mingw_debug_package


%prep
%autosetup -p1 -n libxml2-%{version}


%build
# LibXML2 can't build static and shared libraries in one go, so we
# build LibXML2 twice here
MINGW32_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL"
MINGW64_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL"
MINGW_BUILDDIR_SUFFIX=static %mingw_configure --without-python --with-modules --enable-static --disable-shared --with-threads=win32
MINGW32_CPPFLAGS=
MINGW64_CPPFLAGS=
MINGW_BUILDDIR_SUFFIX=shared %mingw_configure --without-python --with-modules --disable-static --enable-shared --with-threads=win32

MINGW_BUILDDIR_SUFFIX=static %mingw_make %{?_smp_mflags}
MINGW_BUILDDIR_SUFFIX=shared %mingw_make %{?_smp_mflags}


%install
# First install all the files belonging to the shared build
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Then manually install the static libraries to the right location
install -m 0644 build_win32static/.libs/libxml2.a $RPM_BUILD_ROOT%{mingw32_libdir}/
install -m 0644 build_win64static/.libs/libxml2.a $RPM_BUILD_ROOT%{mingw64_libdir}/

# Remove documentation which duplicates Fedora native.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc/

rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc/

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-libxml2
%doc AUTHORS ChangeLog COPYING Copyright NEWS README README.tests TODO TODO_SCHEMAS
%{mingw32_bindir}/libxml2-2.dll
%{mingw32_bindir}/xml2-config
%{mingw32_bindir}/xmlcatalog.exe
%{mingw32_bindir}/xmllint.exe
%{mingw32_libdir}/libxml2.dll.a
%{mingw32_libdir}/cmake/libxml2/
%{mingw32_libdir}/pkgconfig/libxml-2.0.pc
%{mingw32_libdir}/xml2Conf.sh
%{mingw32_includedir}/libxml2
%{mingw32_datadir}/aclocal/*

%files -n mingw32-libxml2-static
%{mingw32_libdir}/libxml2.a

# Win64
%files -n mingw64-libxml2
%doc AUTHORS ChangeLog COPYING Copyright NEWS README README.tests TODO TODO_SCHEMAS
%{mingw64_bindir}/libxml2-2.dll
%{mingw64_bindir}/xml2-config
%{mingw64_bindir}/xmlcatalog.exe
%{mingw64_bindir}/xmllint.exe
%{mingw64_libdir}/libxml2.dll.a
%{mingw64_libdir}/cmake/libxml2/
%{mingw64_libdir}/pkgconfig/libxml-2.0.pc
%{mingw64_libdir}/xml2Conf.sh
%{mingw64_includedir}/libxml2
%{mingw64_datadir}/aclocal/*

%files -n mingw64-libxml2-static
%{mingw64_libdir}/libxml2.a


%changelog
* Thu Apr 23 2020 David King <amigadave@amigadave.com> - 2.9.10-1
- Update to 2.9.10
- Fix CVE-2019-19956 (#1788858)
- Fix CVE-2019-20388 (#1799738)
- Fix CVE-2020-7595 (#1799788)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Richard W.M. Jones <rjones@redhat.com> - 2.9.9-2
- Resync with Fedora Rawhide libxml2 2.9.9-2.
- Use autosetup.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.3-1
- Update to 2.9.3
- Fixes various CVE's:
  RHBZ #1213960, #1262853, #1262854, #1274225, #1274226, #1276299
  RHBZ #1276300, #1277149, #1277150, #1281952, #1281953

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2
- Avoid corrupting the xml catalogs
- Fix CVE-2014-0191 (RHBZ #1107557)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.1-3
- Added the license and other %%doc files (RHBZ #980288)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1

* Fri Apr 12 2013 Nicola Fontana <ntd@entidi.it> - 2.9.0-3
- Throw off LDFLAGS and CFLAGS settings (#951472)
- Simplified static libraries installation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-7
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-6
- Dropped .la files

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 2.7.8-5
- Renamed the source package to mingw-libxml2 (#800440)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-4
- Rebuild against the mingw-w64 toolchain

* Fri Jan  6 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.8-3
- Re-added patch which was dropped in 2.7.8-1 as it is still needed
  to get DTD validation working (GNOME BZ #561340, #663588)

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.7.8-2
- Rebuilt against win-iconv

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.7.8-1
- Update to 2.7.8
- Dropped upstreamed patches
- Use the CVE-2010-4494 patch from Fedora native libxml2 (#665965)

* Mon May 23 2011 Kalev Lember <kalev@smartlink.ee> - 2.7.6-3
- Don't install html documentation which duplicates what is in Fedora native

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 20 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.6-1
- Update to 2.7.6
- Updated the configure arguments so that the native Win32 thread API
  will be used instead of pthreads

* Fri Sep 25 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.5-2
- Added a patch to fix GNOME bug #561340

* Thu Sep 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-3
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sat Sep 12 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-2
- Always use the native win32 thread API even when pthreads is available
- Dropped a patch which isn't necessary anymore

* Fri Sep 11 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.4-1
- Update to 2.7.4
- Drop upstreamed libxml2-2.7.3-ficora-parse.patch patch
- Added a new patch to fix compatibility with the w32 port of pthreads
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Mon Aug 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-3
- two patches for parsing problems CVE-2009-2414 and CVE-2009-2416

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May  4 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.3-1
- Update to 2.7.3

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.7.2-9
- Fixed %%defattr line
- Added -static subpackage. Applications which want to link
  against this static library needs to add -DLIBXML_STATIC to the CFLAGS
- This package shouldn't own %%{mingw32_libdir}/pkgconfig

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-7
- Rebuild for mingw32-gcc 4.4

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-6
- Rerun autoreconf after patching configure.in (Erik van Pienbroek).
- Rebuild libtool for Rawhide / libtool 2.
- Add BRs dlfcn and iconv.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-5
- Use _smp_mflags.
- Disable static libraries.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-4
- Requires pkgconfig.

* Sat Oct 25 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-3
- Enable modules support for libxslt.

* Fri Oct 17 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.2-1
- Resynch to native Fedora package + patch.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.7.1-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.7.1-1
- Update to 2.7.1 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-5
- Remove manpages which duplicate Fedora native.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-4
- Remove static libraries.
- List libdir files explicitly.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-3
- Use RPM macros from mingw-filesystem.
- BuildArch is noarch.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 2.6.32-1
- Initial RPM release, largely based on earlier work from several sources.
