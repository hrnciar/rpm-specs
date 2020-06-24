%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}

Summary: Library of Optimized Inner Loops, CPU optimized functions
Name: mingw-liboil
Version: 0.3.16
Release: 21%{?dist}
# See COPYING which details everything, various BSD licenses apply
License: BSD
URL: http://liboil.freedesktop.org/
Source: http://liboil.freedesktop.org/download/liboil-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=435771
Patch4: liboil-0.3.13-disable-ppc64-opts.patch

BuildArch: noarch

BuildRequires: mingw32-filesystem >= 40
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-glib2
BuildRequires: pkgconfig


%description
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%package -n mingw32-liboil
Summary:        Library of Optimized Inner Loops, CPU optimized functions
Requires:       pkgconfig

%description -n mingw32-liboil
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%prep
%setup -q -n liboil-%{version}
%patch4 -p0 -b .disable-ppc64-opts


%build
%{mingw32_configure}
# Remove standard rpath from oil-bugreport
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# multi-jobbed make makes the build fail:
# ./build_prototypes_doc >liboilfuncs-doc.h
# /bin/sh: ./build_prototypes_doc: No such file or directory
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Remove static libraries but DON'T remove *.dll.a files.
rm $RPM_BUILD_ROOT%{mingw32_libdir}/liboil-0.3.a
rm $RPM_BUILD_ROOT%{mingw32_libdir}/liboil-0.3.la

# Remove manpages which duplicate Fedora native.
rm -rf $RPM_BUILD_ROOT%{_mingw_mandir} 

# Remove documentation too.
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc


%files -n mingw32-liboil
%doc AUTHORS COPYING BUG-REPORTING NEWS README
%{mingw32_bindir}/oil-bugreport.exe
%{mingw32_includedir}/*
%{mingw32_bindir}/liboil-0.3*.dll
%{mingw32_libdir}/liboil-0.3*.dll.a
%{mingw32_libdir}/pkgconfig/liboil-0.3*.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.3.16-20
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 0.3.16-12
- Use global instead of define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.3.16-6
- Renamed the source package to mingw-liboil (RHBZ #800919)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.3.16-5
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 26 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.3.16-1
- add mingw32 changes

* Thu Mar 26 2009 - Behdad Esfahbod <besfahbo@redhat.com> - 0.3.16-1
- Update to 0.3.16
- Remove upstreamed patches
- Resolves #489861

* Wed Mar 18 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.3.15-2
- Add new BRs

* Mon Mar 11 2009 Zoltan Seress <gatesofdarkness@gmail.com> - 0.3.15-1
- Windows cross compilation

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Caolán McNamara <caolanm@redhat.com> - 0.3.14-2
- rebuild to get provides pkgconfig(liboil-0.3)

* Mon Apr 07 2008 Colin Walters <walters@redhat.com> - 0.3.14-1
- New upstream version
- Drop upstreamed liboil-0.3.13-better-altivec-detect.patch
- Drop upstreamed clobber-ecx.patch

* Wed Mar 12 2008 - Bastien Nocera <bnocera@redhat.com> - 0.3.13-6
- Disable PPC64 optimisations as rgb2bgr_ppc() crashes on 64-bit

* Tue Mar 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.3.13-5
- Detect Altivec using /proc instead of causing a SIGILL fault

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 0.3.13-4
- Try disabling Altivec for now

* Tue Feb 26 2008 Matthias Clasen  <mclasen@redhat.com> - 0.3.13-3
- Use the upstream fix instead

* Mon Feb 25 2008 Matthias Clasen  <mclasen@redhat.com> - 0.3.13-2
- Work around a segfault by compiling the offending file with -O0 for now

* Fri Feb 22 2008 Matthias Clasen  <mclasen@redhat.com> - 0.3.13-1
- Update to 0.3.13

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.12-12
- Autorebuild for GCC 4.3

* Fri Sep 07 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-11
- Revert the previous commit, it's still broken, see:
  http://koji.fedoraproject.org/koji/taskinfo?taskID=151172

* Thu Aug 30 2007 - David Woodhouse <dwmw2@infradead.org> - 0.3.12-10
- Re-enable explicit Altivec but don't let the compiler use it automatically
- Start applying the ppc64-configure patch again

* Thu Aug 23 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-9
- Disable Altivec so we don't crash on non-Altivec PPCs, see
  https://bugzilla.redhat.com/bugzilla/process_bug.cgi#c16

* Thu Aug 16 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-8
- And another go at fixing #252179

* Wed Aug 15 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-7
- Add upstream patch to not crash on PPC machines without Altivec
  (hopefully this time the right one) (#252179)

* Tue Aug 14 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-6
- Revert previous change it's not the fix

* Tue Aug 14 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-5
- Add upstream patch to not crash on PPC machines without Altivec
  (#252179)

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 0.3.12-4
- Update License field.
- Remove standard gcc-c++ build requirement.
- Spec file cleanup, only consistency changes.
- Remove standard rpath from oil-bugreport.

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.3.12-3
- Add patch from David Woodhouse <dwmw2@redhat.com> to allow building
  on ppc64 systems (#242418)

* Mon Jun  4 2007 Christopher Aillon <caillon@redhat.com> - 0.3.12-2
- ExcludeArch: ppc64 for now as it fails to build (#242418)

* Mon Jun  4 2007 Christopher Aillon <caillon@redhat.com> - 0.3.12-1
- Update to 0.3.12

* Tue Nov 21 2006 Behdad Esfahbod <besfahbo@redhat.com> - 0.3.10-1
- Update to 0.3.10

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.3.9-1
- Update to 0.3.9

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.8-2.1
- rebuild

* Mon Mar 27 2006 Ray Strode <rstrode@redhat.com> 0.3.8-2
- Update to 0.3.8 (bug 186930)

* Tue Mar 21 2006 Matthias Saou <http://freshrpms.net/> 0.3.7.1-1
- Update to today's CVS code which should fix the PPC build issue.
- Include new oil-bugreport tool in the devel package.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.3.7-3
- FC5 rebuild (well, try at least since PPC fixes are required).

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.3.7-2
- Rebuild for new gcc/glibc.

* Fri Feb  3 2006 Matthias Saou <http://freshrpms.net/> 0.3.7-1
- Update to 0.3.7.

* Wed Dec 14 2005 Matthias Saou <http://freshrpms.net/> 0.3.6-1
- Update to 0.3.6.

* Mon Nov 14 2005 Matthias Saou <http://freshrpms.net/> 0.3.5-3
- Sync spec files across branches.
- Parallel make seems to have worked for 0.3.5 on devel, but just in case...

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.5-2
- Trigger rebuild.

* Sat Nov 12 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.5-1
- Update to 0.3.5.

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 0.3.3-3
- Add patch to disable unrecognized "-fasm-blocks" gcc option on PPC.

* Tue Oct  4 2005 Matthias Saou <http://freshrpms.net/> 0.3.3-2
- Update to 0.3.3.
- Update liboil-0.3.3-gccoptfixes.patch.

* Thu Jun 16 2005 Thomas Vander Stichele <thomas at apestaart dot org> 0.3.2-2
- Disable parallel make

* Wed May 25 2005 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3.2.
- Change ldconfig calls to be the program.
- Include new gtk-doc files in the devel package.
- add dist macro.

* Tue May 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-4
- fix compilation error in FC-4 (bz #158641)
- use buildtime exported CFLAGS instead of making up its own

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.3.0-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.

* Wed Nov 24 2004 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Update to 0.2.2.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Initial RPM release.

