%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-lablgtk
Version:        2.18.10
Release:        7%{?dist}

Summary:        Objective Caml interface to gtk+

License:        LGPLv2 with exceptions

URL:            http://lablgtk.forge.ocamlcore.org/
Source:         https://github.com/garrigue/lablgtk/archive/%{version}/lablgtk-%{version}.tar.gz
# Fix the build with -fno-common
# https://github.com/garrigue/lablgtk/pull/105
Patch0:         %{name}-fno-common.patch

BuildRequires:  help2man
BuildRequires:  ocaml >= 3.12.1-3
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  pkgconfig(libgnomeui-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib)

%global __ocaml_requires_opts -i GtkSourceView2_types


%description
LablGTK is is an Objective Caml interface to gtk+.

It uses the rich type system of Objective Caml 3 to provide a strongly
typed, yet very comfortable, object-oriented interface to gtk+. This
is not that easy if you know the dynamic typing approach taken by
gtk+.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n lablgtk-%{version} -p1

# Remove spurious executable bits
chmod a-x README*

%build
# Parallel builds don't work.
unset MAKEFLAGS
%configure --enable-debug
sed -e "s|-O|$RPM_OPT_FLAGS|" \
    -e "s|-shared|& -ccopt \"$RPM_LD_FLAGS\"|" \
    -e "s|(CAMLMKLIB)|& -ldopt \"$RPM_LD_FLAGS\"|" \
    -i src/Makefile
%if %{opt}
make world CAMLOPT="ocamlopt.opt -g"
make opt CAMLOPT="ocamlopt.opt -g"
%else
make world CAMLC="ocamlc -g"
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
make install \
     RANLIB=true \
     BINDIR=$RPM_BUILD_ROOT%{_bindir} \
     LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
     INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2 \
     DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
cp -p META $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2

# Remove ld.conf (part of main OCaml dist).
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/ld.conf

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk2
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd

# Remove .cvsignore files from examples directory.
find examples -name .cvsignore -exec rm {} \;

# Generate man pages
export LD_LIBRARY_PATH=$PWD/src
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p src/lablgladecc src/lablgladecc2
for bin in gdk_pixbuf_mlsource lablgladecc2 lablgtk2; do
  help2man -N --version-string=%{version} src/$bin > \
    $RPM_BUILD_ROOT%{_mandir}/man1/$bin.1
done


%files
%doc README CHANGES
%license COPYING LGPL
%dir %{_libdir}/ocaml/lablgtk2
%{_libdir}/ocaml/lablgtk2/*.cmi
%{_libdir}/ocaml/lablgtk2/*.cma
%if %{opt}
%{_libdir}/ocaml/lablgtk2/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/*.so*
%{_bindir}/gdk_pixbuf_mlsource
%{_bindir}/lablgladecc2
%{_bindir}/lablgtk2
%{_mandir}/man1/gdk_pixbuf_mlsource.1*
%{_mandir}/man1/lablgladecc2.1*
%{_mandir}/man1/lablgtk2.1*


%files devel
%doc CHANGES.API
%dir %{_libdir}/ocaml/lablgtk2
%{_libdir}/ocaml/lablgtk2/META
%{_libdir}/ocaml/lablgtk2/*.a
%if %{opt}
%{_libdir}/ocaml/lablgtk2/*.cmxa
%{_libdir}/ocaml/lablgtk2/*.cmx
%endif
%{_libdir}/ocaml/lablgtk2/*.mli
%{_libdir}/ocaml/lablgtk2/*.ml
%{_libdir}/ocaml/lablgtk2/*.h
%{_libdir}/ocaml/lablgtk2/gtkInit.cmo
%if %{opt}
%{_libdir}/ocaml/lablgtk2/gtkInit.o
%endif
%{_libdir}/ocaml/lablgtk2/gtkThInit.cmo
%{_libdir}/ocaml/lablgtk2/gtkThread.cmo
%if %{opt}
%{_libdir}/ocaml/lablgtk2/gtkThread.o
%endif
%{_libdir}/ocaml/lablgtk2/propcc
%{_libdir}/ocaml/lablgtk2/varcc


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.10-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.10-6
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.10-5
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.10-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.10-3
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 2.18.10-1
- New upstream version 2.18.10
- Add -fno-common patch to fix build with gcc 10
- Link shared objects with RPM_OPT_FLAGS
- Use %%license macro
- Drop ancient Obsoletes/Provides; package was obsoleting itself
- Add man pages

* Mon Jan 20 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.9-1
- New upstream version 2.18.9.
- Remove patch which has equivalent fix upstream.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-8
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-7
- OCaml 4.09.0 for riscv64

* Thu Dec 05 2019 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-6
- OCaml 4.09.0 (final) rebuild.

* Thu Aug 29 2019 Jerry James <loganjerry@gmail.com> - 2.18.8-5
- Bring the gtksourceview2 dependency back.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-4
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-3
- Drop dependency on gtksourceview2.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-2
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 2.18.8-1
- New version 2.18.8.
- Remove BRs on camlp4 and lablgl.
- Drop HTML documentation.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.18.6-7
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 2.18.6-6
- OCaml 4.07.0-rc1 rebuild.

* Tue Feb 13 2018 Richard W.M. Jones <rjones@redhat.com> - 2.18.6-5
- Remove support for GL.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.18.6-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.6-2
- OCaml 4.06.0 rebuild.

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.6-1
- New upstream version 2.18.6.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.5-9
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.5-6
- Bump release and rebuild.

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.5-5
- OCaml 4.04.2 rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 2.18.5-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 2.18.5-2
- rebuild for s390x codegen bug

* Fri Nov 04 2016 Richard W.M. Jones <rjones@redhat.com> - 2.18.5-1
- New version 2.18.5.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-7
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-6
- Enable bytecode builds (patch supplied by Rafael Fonseca).

* Tue Jul 07 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-5
- Drop dependency on gtksourceview-devel.  See:
  https://lists.fedoraproject.org/pipermail/devel/2015-July/thread.html#212049

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-3
- ocaml-4.02.2 rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-2
- ocaml-4.02.1 rebuild.

* Wed Oct 29 2014 Richard W.M. Jones <rjones@redhat.com> - 2.18.3-1
- New upstream version 2.18.3, which corrects a bindings problem
  with OCaml 4.02.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-8
- ocaml-4.02.0 final rebuild.

* Fri Aug 22 2014 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-7
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Tue Jul 22 2014 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-4
- OCaml 4.02.0 beta rebuild.

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 2.18.0-3
- Rebuild for OCaml 4.02

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  1 2013 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-1
- New upstream version 2.18.0.

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 2.16.0-5
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Remove bogus (and not accepted upstream) patch.

* Sun Aug  4 2013 Richard W.M. Jones <rjones@redhat.com> - 2.16.0-4
- gnome-panel is dead, apparently.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Richard W.M. Jones <rjones@redhat.com> - 2.16.0-2
- Clean up the spec file.
- Set OCAMLFIND_DESTDIR so the ocamlfind install works.

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 2.16.0-1
- Update to 2.16.0
- Rebase avoid-queue-empty-in-gtkThread patch
- Drop ocaml 4.00 patch fixed upstream, and drop autoconf rebuild
- Drop META version fix no longer needed
- Add BR ocaml-findlib

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-11
- Patch for changes in ocamldoc in OCaml 4.00.0.

* Fri Jun 8 2012 Orion Poplawski <orion@cora.nwra.com> - 2.14.2-10
- Rebuild for OCaml 4.00.0.
- Updated URL.

* Sat Apr 28 2012 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-9
- Bump and rebuild against new OCaml compiler in ARM.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-8
- Rebuild for OCaml 3.12.1.

* Mon Nov  7 2011 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-7
- Bump and rebuild for updated libpng 1.5.

* Wed Jul 27 2011 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-6
- Add patch (sent upstream) to fix gtkThread async callbacks throwing
  Queue.Empty.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-3
- Rebuild against rpm-4.9.0-0.beta1.6.fc15.  See discussion:
  http://lists.fedoraproject.org/pipermail/devel/2011-February/148398.html

* Fri Feb  4 2011 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-2
- Rebuild for libpanel-applet soname bump.

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 2.14.2-1
- New upstream version 2.14.2.
- Remove get/set patch, fixed upstream.

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 2.14.0-6
- fix building against new glib (#626765)

* Tue Jul 27 2010 David A. Wheeler <dwheeler@dwheeler.com> - 2.14.0-5
- Add support for gtksourceview2 (in addition to gtksourceview 1.0).

* Tue Jan  5 2010 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-4
- Use upstream RPM 4.8 dependency generator.
- -devel package should depend on gtk2-devel, otherwise lablgtk programs
  cannot find libgtk-x11-2.0.so.0 when they are being built.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-3
- Rebuild for OCaml 3.11.2.

* Mon Sep 28 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-2
- Ignore GtkSourceView2_types dependency (pure type-only *.cmi file).

* Mon Sep 28 2009 Richard W.M. Jones <rjones@redhat.com> - 2.14.0-1
- New upstream version 2.14.0.
- Patch to fix ml_panel.c is now upstream, so removed.
- New *.cmxs files (dynamically linked OCaml native code) added to
  the base package.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.12.0-3
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.12.0-1
- New upstream version 2.12.0.
- Patch to include gnome-ui-init.h.
- gdk-pixbuf-mlsource was renamed gdk_pixbuf_mlsource (this will
  probably break things).

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-7
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-6
- Rebuild for OCaml 3.11.0

* Mon Sep 22 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-5
- Ignore bogus requires GtkSourceView_types.

* Thu Sep 18 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-4
- Add missing BR for gtksourceview-devel (rhbz#462651).

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.10.1-3
- fix license tag

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-2
- Rebuild for OCaml 3.10.2

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-0
- New upstream release 2.10.1.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.0-3
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 2.10.0-2
- Rebuild for OCaml 3.10.1.

* Wed Nov  7 2007 Richard W.M. Jones <rjones@redhat.com> - 2.10.0-1
- New upstream release 2.10.0.
- Fix path to Camlp4Parsers in 'make doc' rule.

* Fri Sep  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-10.20060908cvs
- rebuild

* Thu Aug 30 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-9.20060908cvs
- rebuild

* Sat Jul  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-8.20060908cvs
- update to cvs version
- renamed package from lablgtk to ocaml-lablgtk

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-7
- Rebuild for ocaml 3.09.3

* Tue Aug 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-6
- added BR: ncurses-devel

* Tue Aug 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-5
- Rebuild for FE6

* Wed May 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-4
- rebuilt for ocaml 3.09.2
- removed unnecessary ldconfig

* Sun Feb 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-3
- Rebuild for Fedora Extras 5

* Sun Jan  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.0-1
- new version 2.6.0

* Sat Sep 10 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.4.0-6
- include META file

* Sun May 22 2005 Toshio Kuratomi <toshio-iki-lounge.com> - 2.4.0-5
- Removed gnome-1.x BuildRequires
- Removed BuildRequires not explicitly mentioned in the configure script
  (These are dragged in through dependencies.)
- Fix a gcc4 error about lvalue casting.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.4.0-4
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.4.0-2
- Remove %%{_smp_mflags} as it breaks the build

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.4.0-1
- New Version 2.4.0

* Sat Nov 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:2.2.0-5
- BR gnome-panel-devel instead of gnome-panel (since FC2!)

* Wed Apr 28 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.4
- Compile with debug

* Tue Dec  2 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.3
- Make GL support optional using --with gl switch

* Fri Nov 28 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.2.0-0.fdr.2
- Added dependency on libcroco
- Honor RPM_OPT_FLAGS

* Fri Oct 31 2003 Gerard Milmeister <milmei@ifi.unizh.ch> - 0:2.2.0-0.fdr.1
- First Fedora release

* Mon Oct 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Update to 2.2.0.

* Sun Aug 17 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Provide ocaml-lablgtk (reported by bishop@platypus.bc.ca).

* Wed Apr  9 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Rebuilt for Red Hat 9.

* Tue Nov 26 2002 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Initial build
