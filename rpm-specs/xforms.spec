%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    xforms
Summary: XForms toolkit library
Version: 1.2.4
Release: 16%{?dist}

License: LGPLv2+
URL:     http://xforms-toolkit.org/
Source0:  http://download.savannah.gnu.org/releases-noredirect/xforms/xforms-%{version}%{?pre}.tar.gz
Source1:  http://download.savannah.gnu.org/releases-noredirect/xforms/xforms-%{version}%{?pre}.tar.gz.sig
Patch0:   xforms-1.2.4-gcc10.patch

BuildRequires:  gcc
BuildRequires: libjpeg-devel
%define x_deps xorg-x11-devel libGL-devel
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires: libXpm-devel
# skip xorg-x11-proto-devel, for now, pulled in indirectly via libX11-devel
%define x_deps libGL-devel libX11-devel
%endif
BuildRequires: %{x_deps}

# import/export: png, sgi (optional?)
Requires: netpbm-progs
# import eps,ps (optional?)
#Requires: ghostscript
# eww, http://lists.nongnu.org/archive/html/xforms-development/2010-05/msg00000.html
Requires: xorg-x11-fonts-ISO8859-1-75dpi xorg-x11-fonts-ISO8859-1-100dpi

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It features a
rich set of objects, such as buttons, sliders, browsers, and menus etc.
integrated into an easy and efficient object/event callback execution model
that allows fast and easy construction of X-applications. In addition, the
library is extensible and new objects can easily be created and added to
the library.

%package devel
Summary: Development files for the XForms toolkit library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{?x_deps}
%description devel
%{summary}.

%package doc
Summary: XForms documentation
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
%endif
BuildRequires:   texi2html
BuildRequires:   texinfo
BuildRequires:   texinfo-tex
BuildRequires:   ImageMagick
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildArch:       noarch
%endif
%description doc
%{summary}.


%prep
%setup -q -n %{name}-%{version}%{?pre}
%patch0 -p1 -b .gcc10

# rpath hack
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure


%build
%configure \
  --disable-demos \
  --enable-docs --htmldir=%{_pkgdocdir}/html --pdfdir=%{_pkgdocdir} \
  --disable-static \
  --enable-optimization="$RPM_OPT_FLAGS"

make %{?_smp_mflags} X_PRE_LIBS=""


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' install

rm -rfv demos/.deps
cp -r demos/ $RPM_BUILD_ROOT%{_pkgdocdir}/


## Unpackaged files
rm -fv  $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rfv $RPM_BUILD_ROOT%{_infodir}/{dir,xforms_images}



%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB Copyright
%doc ChangeLog README
%{_libdir}/libflimage.so.2*
%{_libdir}/libformsGL.so.2*
%{_libdir}/libforms.so.2*
%exclude %{_pkgdocdir}/demos/
%exclude %{_pkgdocdir}/html/
%exclude %{_pkgdocdir}/xforms.pdf

%files devel
%{_bindir}/fd2ps
%{_bindir}/fdesign
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_mandir}/man1/*
%{_mandir}/man5/*

%if 0%{?rhel} && 0%{?rhel} <= 7
%post doc
/sbin/install-info %{_infodir}/xforms.info %{_infodir}/dir ||:

%preun doc
if [ $1 -eq 0 ]; then
/sbin/install-info --delete %{_infodir}/xforms.info %{_infodir}/dir ||:
fi
%endif

%files doc
%{_infodir}/xforms.info*
%{_pkgdocdir}/demos/
%{_pkgdocdir}/html/
%{_pkgdocdir}/xforms.pdf


%changelog
* Mon Feb 10 2020 Robert Scheck <robert@fedoraproject.org> - 1.2.4-16
- Declare curobj as static (#1800271, thanks to Jens Thoms Toerring)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.4-5
- tweak pkgdocdir to work on el6 too, fix %%preun doc scriptlet

* Thu May 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.4-4
- -doc: include demos/ too

* Tue May 26 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.4-3
- -doc subpkg
- trim %%changelog

* Wed Apr 08 2015 Robert Scheck <robert@fedoraproject.org> - 1.2.4-2
- Some minor spec file tweaks

* Wed Apr 08 2015 Robert Scheck <robert@fedoraproject.org> - 1.2.4-1
- Upgrade to 1.2.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.3-1
- 1.2.3

* Tue Jan 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-1
- 1.2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-0.10.pre17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-0.9.pre17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.0.94-0.8.pre17
- rebuild due to "jpeg8-ABI" feature drop

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.94-0.7.pre17
- 1.9.94pre17

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.94-0.6.pre12
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-0.5.pre12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.94-0.4.pre12
- xforms-1.9.94pre12

* Tue May 15 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.94-0.3.pre11
- xforms-1.9.94pre11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.94-0.2.pre5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 15 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.94-0.1.pre5
- 1.0.94pre5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.93-1
- xforms-1.0.93

* Tue May 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.93-0.1.pre7
- xforms-1.0.93pre7
- Requires: xorg-x11-fonts-ISO8859-1-75dpi

* Thu Nov 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-2.sp2
- xforms-1.9.92sp2

* Mon Sep 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-1.sp1
- xforms-1.0.92sp1

* Tue Sep 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-0.4.pre13
- xforms-1.0.92pre13

* Mon Sep 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-0.3.pre12
- xforms-1.0.92pre12

* Wed Sep 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-0.2.pre8
- xforms-1.0.92pre8

* Mon Aug 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.92-0.1.pre7
- xforms-1.0.92pre7

* Mon Aug 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.91-2
- %%files: fix %%defattr typo
- drop libXpm-devel from x_deps

* Mon Jul 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.91-1
- xforms-1.0.91
- nuke rpaths
- rebase prelink/no_undefined patch

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0.90-11
- respin (gcc43)

* Tue Aug 21 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.90-10
- respin (BuildID)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0.90-9
- License: LGPLv2+

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-8
- fc6 respin

* Tue Aug 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-7
- cleanup

* Wed Mar 01 2006 Rex Dieter <rexdieter[AT]users.sf.net> 
- fc5: gcc/glibc respin

* Fri Jan 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-6
- -devel: Req: libjpeg-devel(flimage), libXpm-devel

* Mon Jan 02 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-5
- prelink.patch: fix undefined symbols in (shared) lib(s)

* Mon Dec 19 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-4
- BR: libXpm-devel
- -devel: Req: libX11-devel 

* Mon Oct 17 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-3
- BR: libGL-devel
- #BR: libXpm-devel (coming soon)

* Mon Oct 17 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-2
- BR: libGL.so.1 -> BR: %%x_pkg-Mesa-libGL 
- remove legacy crud

* Mon Oct 17 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.0.90-1
- 1.0.90
- new version removes use-of/references-to xmkmf,/usr/X11R6 (#170942)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Nov 23 2003 Rex Dieter <rexdieter at sf.net> 0:1.0-0.fdr.2
- update for Fedora Core support
- remove extraneous macros

* Fri May 30 2003 Rex Dieter <rexdieter at sf.net> 0:1.0-0.fdr.1
- BuildRequires: libtiff-devel
- add few more %%doc files.

* Fri Apr 02 2003 Rex Dieter <rexdieter at sf.net> 0:1.0-0.fdr.0
- fedora-ize package.

* Mon Jan 20 2003 Rex Dieter <rexdieter at sf.net> 1.0-0
- 1.0-release
- redhat-ize specfile
