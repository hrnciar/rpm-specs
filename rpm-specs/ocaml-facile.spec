%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}
%global _default_patch_fuzz 2

Name:          ocaml-facile
Version:       1.1
Release:       67%{?dist}
Summary:       OCaml library for constraint programming
Summary(fr):   Librairie OCaml de programmation par contraintes
License:       LGPLv2+

URL:           http://www.recherche.enac.fr/log/facile/
Source0:       http://www.recherche.enac.fr/log/facile/distrib/facile-1.1.tar.gz

# makefile fixes by Steffen Joeris <white@debian.org>:
# * only build and install native binaries if ocamlopt is available
# * install .mli files
Patch0:        facile-1.1-makefile-fixes.patch

# Fix for OCaml 4.00.0.
Patch1:        ocaml-facile-ocaml-4.patch

BuildRequires: ocaml >= 3.02
BuildRequires: ocaml-findlib-devel

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml. It offers all usual facilities to create and
manipulate finite domain variables, arithmetic expressions and constraints
(possibly non-linear), built-in global constraints (difference, cardinality,
sorting etc.) and search and optimization goals. FaCiLe allows as well to build
easily user-defined constraints and goals (including recursive ones), making
pervasive use of OCaml higher-order functionals to provide a simple and flexible
interface for the user. As FaCiLe is an OCaml library and not "yet another
language", the user benefits from type inference and strong typing discipline,
high level of abstraction, modules and objects system, as well as native code
compilation efficiency, garbage collection and replay debugger, all features of
OCaml (among many others) that allow to prototype and experiment quickly:
modeling, data processing and interface are implemented with the same powerful
and efficient language.

%description -l fr
FaCiLe est une librairie de Programmation par Contraintes sur les domaines
finis (entiers et ensembles d'entiers) entièrement écrite avec OCaml. FaCiLe
intègre toutes les fonctionnalités standards de création et manipulation de
variables (logiques) à domaine fini, d'expressions et de contraintes
arithmétiques (éventuellement non-linéaires), de contraintes globales
(différence, cardinalité, tri etc.) et de buts de recherche et d'optimisation.
FaCiLe permet aussi de construire facilement de nouvelles contraintes et de
nouveaux buts (éventuellement récursifs) définis par l'utilisateur, à l'aide
d'interfaces simples et puissantes qui utilisent intensivement des fonctions
d'ordre supérieur. Comme FaCiLe est une librairie OCaml et pas "encore un
nouveau langage", l'utilisateur bénéficie de l'inférence de type et du typage
statique strict, d'un haut niveau d'abstraction, des systèmes de modules et
d'objets, ainsi que de l'efficacité du compilateur qui produit du code natif
optimisé (pour toutes les plates-formes courantes), de la gestion automatique de
la mémoire et du débogueur avec retour arrière, autant de caractéristiques
d'OCaml qui permettent de prototyper et expérimenter très rapidement: la
modélisation, le traitement des données et les interfaces sont implémentés à
l'aide du même langage puissant et efficace.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n facile-%{version}
%patch0 -p1 -b .makefile-fixes
%patch1 -p1 -b .ocaml4

%build
# This is not autoconf, but a simple custom configure script.
# The --faciledir directory is only used for "make install".
./configure --faciledir $RPM_BUILD_ROOT%{_libdir}/ocaml/facile
%if %opt
make
%else
make OCAMLC=ocamlc OCAMLMLI=ocamlc
%endif

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml
make install

%files
%doc LICENSE README
%{_libdir}/ocaml/facile/
%if %opt
%exclude %{_libdir}/ocaml/facile/*.a
%exclude %{_libdir}/ocaml/facile/*.cmxa
%endif
%exclude %{_libdir}/ocaml/facile/*.mli

%files devel
%if %opt
%{_libdir}/ocaml/facile/*.a
%{_libdir}/ocaml/facile/*.cmxa
%endif
%{_libdir}/ocaml/facile/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-67
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-66
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-64
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-63
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-62
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-61
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-60
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-58
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-57
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-56
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-55
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-54
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-52
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-51
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-48
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-47
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-45
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-44
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-41
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-40
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1-38
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-36
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-35
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-34
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-33
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-31
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-30
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-29
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-27
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-26
- OCaml 4.02.0 beta rebuild.

* Mon Jul 21 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1-25
- rebuild (ocaml 4.02.0, #1121640)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-23
- Remove ocaml_arches macro (RHBZ#1087794).

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1-22
- Rebuild for OCaml 4.01.0.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-19
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1-17
- Rebuild for OCaml 4.00.0.
- Add a patch for OCaml 4.00.0 (change in Hashtbl signature).
- Move configure into build section.

* Sat Jan 07 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-15
- Rebuild for OCaml 3.12.1
- Drop obsolete conditionals
- Use ocaml_arches macro instead of hardcoded ExcludeArch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 1.1-13
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-12
- Rebuild for OCaml 3.11.2.

* Thu Dec 17 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-11
- Use RPM's builtin OCaml dependency generator on F13+

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-9
- Rebuild for new OCaml (3.11.1 rc0)

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-7
- Rebuild for OCaml 3.11.0+rc1.

* Tue Nov 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-6
- rebuild for new ocaml (3.11.0 beta1)

* Thu Aug 28 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-5
- Rebuild with patch fuzz.
- No need to create $RPM_BUILD_ROOT.

* Wed Apr 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-3
- rebuild for new ocaml (3.10.2)

* Fri Mar 21 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-2.1
- ExcludeArch: ppc64 on Fedora < 9 (no ocaml, #438562)

* Wed Mar 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-2
- use correct syntax for French description

* Wed Mar 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1-1
- initial Fedora package
