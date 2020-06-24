# rpmlint "no-binary" error is not really an error - see:
# https://www.redhat.com/archives/fedora-packaging/2008-August/msg00017.html
# and ocaml-ocamlgraph spec file for a discussion of this issue.

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:		alt-ergo
Version:	2.2.0
Release:	1%{?dist}
Summary:	Automated theorem prover including linear arithmetic
License:	ASL 2.0

URL:		https://alt-ergo.ocamlpro.com/
Source0:	https://alt-ergo.ocamlpro.com/http/%{name}-%{version}/%{name}-%{version}.tar.gz
# Created with gimp from official upstream icon
Source1:	%{name}-icons.tar.xz
Source2:	%{name}.desktop
Source3:	%{name}.appdata.xml

# Use the asmrun_pic variant when linking the binary.
Patch0:		%{name}-1.30-use-pic.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gtksourceview2-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgtk-devel
BuildRequires:	ocaml-menhir-devel
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-ocplib-simplex-devel
BuildRequires:	ocaml-psmt2-frontend-devel
BuildRequires:	ocaml-zarith-devel
BuildRequires:	ocaml-zip-devel

Requires:	ocaml-alt-ergo%{?_isa} = %{version}-%{release}

# Do not Require private ocaml interfaces that we don't Provide
%global __requires_exclude ocamlx?\\\((Commands|Ex(ception|planation)|Formula|Hstring|Inequalities|L(iteral|oc)|Matching_types|Numbers(Interface)?|Options|P(arsed|olynome)|S(atml_types|ig|ymbols)|T(erm|y(ped)?)|U(f|til)|Vec)\\\)

%global _desc %{expand:
Alt-Ergo is an automated theorem prover implemented in OCaml. It is
based on CC(X) - a congruence closure algorithm parameterized by an
equational theory X. This algorithm is reminiscent of the Shostak
algorithm. Currently CC(X) is instantiated by the theory of linear
arithmetics. Alt-Ergo also contains a home made SAT-solver and an
instantiation mechanism by which it fully supports quantifiers.}

%description %_desc

%package gui
Summary:	Graphical front end for Alt-Ergo
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gtksourceview2
Requires:	hicolor-icon-theme

%description gui %_desc

This package contains a graphical front end for the Alt-Ergo theorem
prover.

%package -n ocaml-alt-ergo
Summary:	Automated theorem prover library

%description -n ocaml-alt-ergo %_desc

This package is the core of Alt-Ergo as an OCaml library.

%package -n ocaml-alt-ergo-devel
Summary:	Development files for ocaml-altergolib
Requires:	ocaml-alt-ergo%{?_isa} = %{version}-%{release}

%description -n ocaml-alt-ergo-devel %_desc

This package contains development files needed to build applications
that use the Alt-Ergo library.

%prep
%autosetup -p1
%setup -q -T -D -a 1

cp -p %{SOURCE2} .

# Look for zip instead of camlzip
sed -i 's/camlzip/zip/g' configure opam

%ifarch %{arm}
# Work around for https://github.com/ocaml/ocaml/issues/7608
# Remove this once a released ocaml version fixes that issue.
sed -i "s|^LIGHT_OFLAGS =|& -fno-thumb|" Makefile.users
%endif

%build
%configure --libdir=%{_libdir}/ocaml

%ifnarch %{ocaml_native_compiler}
%global opt_option OCAMLBEST=byte OCAMLC=ocamlc OCAMLLEX=ocamllex
%else
%global opt_option OCAMLBEST=opt OCAMLOPT=ocamlopt.opt
%endif

make %{opt_option}
make %{opt_option} gui

%install
mkdir -p %{buildroot}%{_bindir}
make %{opt_option} DESTDIR=%{buildroot} install install-gui

# Move the gtksourceview file to the right place
mv %{buildroot}%{_datadir}/%{name}/gtksourceview-2.0 %{buildroot}%{_datadir}
rmdir %{buildroot}%{_datadir}/%{name}

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm 644 %{SOURCE3} %{buildroot}%{_datadir}/appdata

# Install the icons
mkdir -p %{buildroot}%{_datadir}/icons
cp -a icons %{buildroot}%{_datadir}/icons/hicolor

%check
# Test alt-ergo on the examples.
%define altergo %{buildroot}%{_bindir}/alt-ergo
cd examples/valid
for fil in *.why; do
  if ! %{altergo} $fil | grep -Fq Valid; then
    echo $fil was not found valid
    exit 1
  fi
done
cd ../invalid
for fil in *.why; do
  if %{altergo} $fil | grep -Fq Valid; then
    echo $fil was erroneously found valid
    exit 1
  fi
done

%files
%doc README.md CHANGES examples
%license COPYING.md LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/alt-ergo.1.*

%files gui
%{_bindir}/altgr-ergo
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gtksourceview-2.0/language-specs/%{name}.lang
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files -n ocaml-alt-ergo
%dir %{_libdir}/ocaml/%{name}/
%{_libdir}/ocaml/%{name}/plugins/
%{_libdir}/ocaml/%{name}/preludes/
%{_libdir}/ocaml/%{name}/altErgoLib.cma
%{_libdir}/ocaml/%{name}/altErgoLib.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{name}/altErgoLib.cmxs
%endif

%files -n ocaml-%{name}-devel
%{_libdir}/ocaml/%{name}/META
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{name}/altErgoLib.a
%{_libdir}/ocaml/%{name}/altErgoLib.cmx
%{_libdir}/ocaml/%{name}/altErgoLib.cmxa
%endif
%{_libdir}/ocaml/%{name}/altErgoLib.o
%{_libdir}/ocaml/%{name}/altErgoLib.cmo
%{_libdir}/ocaml/%{name}/altErgoLib.cmt

%changelog
* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0
- Drop upstreamed -newline patch

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-15
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-14
- OCaml 4.11.0 pre-release attempt 2

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-13
- Filter out Requires for private interfaces we do not Provide

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-12
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-11
- Rebuild for ocaml-zip 1.10

* Tue Mar 24 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-10
- Rebuild for ocaml-menhir 20200211

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-9
- OCaml 4.10.0 final.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-7
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-6
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-5
- Rebuild for ocaml-zarith 1.9

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-4
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Update to version 2.0.0
- Add -newline patch to fix FTBFS
- Add a 256x256 icon

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.30-14
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.30-13
- OCaml 4.07.0-rc1 rebuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.30-11
- Remove obsolete scriptlets

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-10
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-9
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-6
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-5
- Bump release and rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-4
- Bump release and rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-3
- OCaml 4.04.1 rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.30-1
- Update to version 1.30

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.01-3
- Rebuild for OCaml 4.04.0.

* Sat Apr 16 2016 Jerry James <loganjerry@gmail.com> - 1.01-2
- Rebuild for ocaml-ocamlgraph 1.8.7

* Wed Feb 17 2016 Jerry James <loganjerry@gmail.com> - 1.01-1
- Update to version 1.01

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-9
- Rebuild for zarith 1.4.1

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-8
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-7
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-6
- ocaml-4.02.2 rebuild.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-4
- Rebuild for ocaml-ocamlgraph 1.8.6

* Fri Mar 13 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-3
- Fix FTBFS (bz 1099153)

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-2
- ocaml-4.02.1 rebuild.

* Tue Jan  6 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-1
- Update to version 0.99.1

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-14
- Rebuild for new ocaml-lablgtk

* Tue Oct 14 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-13
- Rebuild for ocaml-zarith 1.3
- Fix license handling

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-12
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-11
- ocaml-4.02.0+rc1 rebuild.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-9
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-8
- Bump release and rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-7
- Rebuild for OCaml 4.02.0 beta.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-5
- Rebuild for ocamlgraph 1.8.5

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-4
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-3
- Add desktop icons
- Drop unnecessary gmp-devel BR (pulled in by ocaml-zarith-devel)
- Fix bytecode build
- Drop screenshot, now hosted externally

* Tue Mar  4 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-2
- Add an AppData file and screenshot
- Adapt to ocamlgraph 1.8.4

* Fri Sep 20 2013 Jerry James <loganjerry@gmail.com> - 0.95.2-1
- Update to version 0.95.2
- Web pages and downloads now hosted by ocamlpro.com
- Add ocaml-findlib, ocaml-zarith, and gmp-devel BRs
- Drop prelink BR; execstack is no longer set
- Fix bogus changelog dates

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.95.1-4
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Change some define -> global.
- Remove Group lines not needed by modern RPM.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.95.1-2
- Rebuild for ocaml-ocamlgraph 1.8.3
- Make the binaries full RELRO due to network use

* Tue Mar  5 2013 Jerry James <loganjerry@gmail.com> - 0.95.1-1
- Update to version 0.95.1
- Drop upstreamed -install patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Jerry James <loganjerry@gmail.com> - 0.95-1
- Update to version 0.95
- Add -install patch to fix installation failure

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 0.94-7
- Rebuild for OCaml 4.00.1

* Mon Jul 30 2012 Jerry James <loganjerry@gmail.com> - 0.94-6
- Rebuild for ocaml-ocamlgraph 1.8.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Jerry James <loganjerry@gmail.com> - 0.94-4
- Rebuild for OCaml 4.00.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 0.94-2
- Rebuild for OCaml 3.12.1

* Tue Dec  6 2011 Jerry James <loganjerry@gmail.com> - 0.94-1
- Add a desktop file for the gui.
- Update to version 0.94.  This means:
- The theory of records replaces the theory of pairs
- Bug fixes (intervals, term data-structure, stack-overflows, matching,
  existentials, distincts, CC, GUI)
- Improvements (SMT-Lib2 front-end, intervals, case-splits, triggers, lets)
- Multiset ordering for AC(X)
- Manual lemma instantiation in the GUI

* Mon Nov 14 2011 Jerry James <loganjerry@gmail.com> - 0.93-2
- Build on all arches with ocaml

* Thu May 12 2011 Jerry James <loganjerry@gmail.com> - 0.93-1
- Update to version 0.93.  This means:
- New command-line options -steps, -max-split, and -proof
- New polymorphic theory of arrays
- Built-in support for enumeration types
- Graphical front end
- New predicate distinct()
- New constructs: let x = <term> in <term>, let x = <term> in <formula>
- Partial support for the division operator
- Unspecified bug fixes

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 David A. Wheeler <dwheeler@dwheeler.com> 0.92.1-1
- Update to version 0.92.1. This means:
- New built-in syntax for the theory of arrays
- Fixes a bug in the arithmetic module
- Allows folding and unfolding of predicate definitions

* Tue Jun 08 2010 David A. Wheeler <dwheeler@dwheeler.com> 0.91-1
- Update to version 0.91. This means:
- partial support for non-linear arithmetics
- support case split on integer variables
- new support for Euclidean division and modulo operators


* Tue Aug 04 2009 Alan Dunn <amdunn@gmail.com> 0.9-2
- Added ExcludeArch sparc64 due to no OCaml

* Fri Jul 24 2009 Alan Dunn <amdunn@gmail.com> 0.9-1
- New upstream version
- Removed code for check for Fedora version (8) that is EOL
- Removed comments re: CeCILL-C license as it is ok to have (no
  rpmlint warnings to explain either).

* Wed Jun 17 2009 Karsten Hopp <karsten@redhat.com> 0.8-5.1
- ExcludeArch s390x as there's no ocaml available

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Alan Dunn <amdunn@gmail.com> 0.8-4
- Rebuild: Source upstream appears to have changed even with same version number
  (seems like bug fix from examination of changes)
- Changed hardcoded version number in source string
* Fri Sep 05 2008 Alan Dunn <amdunn@gmail.com> 0.8-3
- Fixed BuildRequires to add prelink (for execstack).
* Tue Aug 26 2008 Alan Dunn <amdunn@gmail.com> 0.8-2
- Fixed BuildRequires to add ocaml-ocamlgraph-devel instead of
  ocaml-ocamlgraph, made other minor changes.
* Mon Aug 25 2008 Alan Dunn <amdunn@gmail.com> 0.8-1
- Initial Fedora RPM version.
