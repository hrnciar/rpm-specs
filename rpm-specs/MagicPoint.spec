%define _legacy_common_support 1
Name:           MagicPoint
Version:        1.13a
Release:        27%{?dist}
Summary:        X based presentation software
License:        BSD
URL:            http://member.wide.ad.jp/wg/mgp/
Source0:        ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/magicpoint-%{version}.tar.gz
Patch0:         magicpoint-1.11b-debian.patch
Patch1:         magicpoint-1.11b-64bit.patch
Patch2:         magicpoint-1.11b-embed.patch
Patch3:         magicpoint-1.13a-gcc-warnings.patch
Patch4:         magicpoint-1.13a-xwintoppm.patch
Patch5:         magicpoint-1.13a-m17n.patch
Patch6:         magicpoint-1.13a-mng.patch
Patch7:         magicpoint-1.13a-honor-cflags-for-unimap.patch
# giflib-5.x compatibility
Patch8:         magicpoint-1.13a-giflib5.patch
# libpng > 1.5.0 compatibility
Patch9:         magicpoint-1.13a-libpng.patch
BuildRequires:  gcc
BuildRequires:  giflib-devel libpng-devel libmng-devel fontconfig-devel 
BuildRequires:  imlib2-devel libXmu-devel libXft-devel m17n-lib-devel
BuildRequires:  imake bison flex perl-interpreter perl-generators sharutils
Requires:       sharutils
Obsoletes:      mgp < %{version}-%{release}, magicpoint < %{version}-%{release}
Provides:       mgp = %{version}-%{release}, magicpoint = %{version}-%{release}

%description
MagicPoint is an X11 based presentation tool. MagicPoint's
presentation files (typically .mgp files) are plain text so you can
create presentation files quickly with your favorite editor.


%prep
%setup -q -n magicpoint-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1


%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-function -D_DEFAULT_SOURCE"
export CFLAGS="$RPM_OPT_FLAGS"
%configure --enable-locale --enable-xft2 --enable-gif --enable-imlib --with-m17n-lib
xmkmf -a
# LIBDIR is used by the makefile to determine where to install data files
make CDEBUGFLAGS="$RPM_OPT_FLAGS" LIBDIR=%{_datadir}


%install
make install install.man DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_datadir}
install -m 755 contrib/mgp2html.pl $RPM_BUILD_ROOT%{_bindir}/mgp2html
install -m 755 contrib/mgp2latex.pl $RPM_BUILD_ROOT%{_bindir}/mgp2latex
# stop these from ending up in %%doc
rm sample/.cvsignore sample/*akefile*


%files
%doc COPYRIGHT README SYNTAX USAGE sample
%{_bindir}/*
%{_datadir}/mgp
%{_mandir}/*/*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Jeff Law <law@redhat.com> - 1.13a-26
- Enable legacy common support

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.13a-21
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.13a-20
- Rebuild (giflib)
- Switch to imlib2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Hans de Goede <hdegoede@redhat.com> - 1.13a-15
- Honor CFLAGS when building unimap.o, fix FTBFS (rhbz#1307283)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Hans de Goede <hdegoede@redhat.com> - 1.13a-10
- Fix FTBFS (rhbz#1001694)

* Tue Aug 27 2013 Jon Ciesla <limburgher@gmail.com> - 1.13a-9
- libmng rebuild.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.13a-7
- Perl 5.18 rebuild

* Mon Mar 11 2013 Hans de Goede <hdegoede@redhat.com> - 1.13a-6
- Enable m17n-lib support (rhbz#920308)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.13a-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.13a-3
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Hans de Goede <hdegoede@redhat.com> 1.13a-1
- New upstream release 1.13a (rhbz#819168)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.11b-12
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Adam Jackson <ajax@redhat.com> 1.11b-9
- Use freetype, not freetype1, which is old and broken.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 1.11b-7
- Fix patch fuzz build failure

* Sun Mar 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.11b-6
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.11b-5
- Autorebuild for GCC 4.3

* Sat Oct 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.11b-4
- Unorphan
- Take some patches from Debian
- Actually make ./configure detect and use freetype1, it was testing for it
  but the test failed
- Package mgp2html and mgp2latex from the contrib dir 

* Fri Aug 5 2005 Colin Charles <colin@fedoraproject.org> - 1.11b-3
- Re-enable debuginfo builds
- Ralf Corsepius watchful eyes fixes - cleaning up the spec

* Thu Aug 4 2005 Colin Charles <colin@fedoraproject.org> - 1.11b-2
- Removed Patch12 to fix undefined operation
- Bump spec to somewhat match work from Rui Miguel Silva Seabra <rms@1407.org>
- Remove requirement on VFlib2, seeing that we disable it in configure

* Mon Sep 27 2004 Akira TAGOH <tagoh@redhat.com> - 1.11b-1
- New upstream release.

* Wed Sep 15 2004 Akira TAGOH <tagoh@redhat.com> - 1.11a-1
- New upstream release.
- magicpoint-1.11a-fix-gcc-warnings.patch: updated from 1.10a.
- magicpoint-1.10a-fixtypo-opaque.patch: removed, it's no lnger needed.
- magicpoint-1.10a-fix-ft2build.patch: removed, it's no longer needed.
- magicpoint-1.10a-png.patch: removed, it's no longer needed.
- XFree4.0-freetype.patch: removed, freetype1 is no longer available.

* Mon Jun 21 2004 Akira TAGOH <tagoh@redhat.com> 1.10a-10
- magicpoint-1.10a-fix-gcc34.patch: applied to build with gcc 3.4.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Akira TAGOH <tagoh@redhat.com> 1.10a-8
- fix wrong license description. (#115947: Miloslav Trmac)
- included COPYRIGHT file.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 09 2004 Akira TAGOH <tagoh@redhat.com> 1.10a-6
- magicpoint-1.10a-fix-gcc-warnings2.patch: applied to fix gcc warnings (#115161)
- magicpoint-1.10a-fix-ft2build.patch: applied to fix build error for freetype.
- magicpoint-1.10a-fix-usleep.patch: applied to fix missing compile options.

* Fri Nov 28 2003 Akira TAGOH <tagoh@redhat.com> 1.10a-5
- magicpoint-1.10a-fix-gcc-warnings.patch: updated for more gcc3 compliant. (#110773)

* Fri Sep 19 2003 Akira TAGOH <tagoh@redhat.com> 1.10a-4
- added some missing BuildRequires.

* Tue Sep 02 2003 Akira TAGOH <tagoh@redhat.com> 1.10a-3
- magicpoint-1.10a-fixtypo-opaque.patch: applied a patch to work the opaque.

* Wed Aug 20 2003 Akira TAGOH <tagoh@redhat.com> 1.10a-2
- magicpoint-1.10a-longline.patch: fixed the freeze if the line is too long. (#100736)

* Wed Jun 25 2003 Akira TAGOH <tagoh@redhat.com> 1.10a-1
- New upstream release.
- removed the dependency of watanabe-vf due to the copyright issue.
- add fontconfig-devel and XFree86-devel to BuildReqruies.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.09a-12
- gcc 3.3 doesn't implement varargs.h, include stdarg.h instead

* Fri Apr 18 2003 Akira TAGOH <tagoh@redhat.com> 1.09a-11
- rebuild.

* Fri Apr 18 2003 Akira TAGOH <tagoh@redhat.com> 1.09a-10
- magicpoint-1.09a-rpath.patch: don't specify -rpath. (#65966)
- magicpoint-1.09a-fix-gcc-warnings.patch: applied to fix gcc warnings. (#79642)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.09a-8
- add VFlib2-conf-ja >=2.25.6-8 as a requirement to fix bug 74105

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Remove extraneous ttfonts dependency; VFlib already has that dependency

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 27 2002 Yukihiro Nakai <ynakai@redhat.com>
- Remove .cvsignore file(#65241)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar 26 2002 Yukihiro Nakai <ynakai@redhat.com>
- Update to 1.09a

* Tue Mar  5 2002 Jeremy Katz <katzj@redhat.com>
- Add ttfonts to Requires (#24868)
- rebuild in new environment

* Thu Jan 31 2002 Bill Nottingham <notting@redhat.com>
- rebuild in new environment

* Wed Sep 05 2001 Yukihiro Nakai <ynakai@redhat.com>
- Add magicpoint to Obsoletes.

* Tue Sep 04 2001 Yukihiro Nakai <ynakai@redhat.com>
- Add --enable-gif
- Add watanabe-vf to Requires.

* Wed Jul 18 2001 Yukihiro Nakai <ynakai@redhat.com>
- Delete require ttfont-ja

* Mon Jul  9 2001 Yukihiro Nakai <ynakai@redhat.com>
- Rebuild against RHL7.2
- Rename to MagicPoint
- Update to 1.08a
- Enable vflib

* Wed Jan 24 2001 Tim Powers <timp@redhat.com>
- fixed bug 24868

* Mon Aug 7 2000 Tim Powers <timp@redhat.com>
- disable vflib to fix bug #15607

* Wed Aug 2 2000 Tim Powers <timp@redhat.com>
- rebuilt against libpng-1.0.8

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Thu Jul 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- stop disabling freetype support

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed May 24 2000 Tim Powers <timp@redhat.com>
- updated to 1.07a
- cleaned up files list
- using %%configure
- fixed to use XFree86 4.0

* Mon Jul 19 1999 Tim Powers <timp@redhat.com>
- updated source to 1.05a 
- built for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Oct 08 1998 Michael Maher <mike@redhat.com> 
- updated source to 1.04a
- built for 5.2

* Fri May 22 1998 Cristian Gafton <gafton@redhat.com>
- built for PowerTools
