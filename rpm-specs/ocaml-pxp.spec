%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-pxp
Version:        1.2.9
Release:        1%{?dist}
Summary:        Validating XML parser
License:        BSD

URL:            http://projects.camlcity.org/projects/pxp.html
Source0:        http://download.camlcity.org/download/pxp-%{version}.tar.gz

BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-pcre-devel, pcre-devel

%global __ocaml_requires_opts -i Asttypes -i Outcometree -i Parsetree -i Pxp_rea


%description
PXP is a validating XML parser for O'Caml. It represents the parsed
document either as tree or as stream of events. In tree mode, it is
possible to validate the XML document against a DTD.

The acronym PXP means Polymorphic XML Parser. This name reflects the
ability to create XML trees with polymorphic type parameters.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pxp-%{version}


%build
./configure \
  -without-pp \
  -without-ulex \
  -without-wlex \
  -without-wlex-compat \
  -lexlist all


# Parallel builds don't work:
unset MAKEFLAGS

make all
%if %{opt}
make opt
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%doc LICENSE
%{_libdir}/ocaml/pxp-engine/*.cma
%{_libdir}/ocaml/pxp-engine/*.cmi
%{_libdir}/ocaml/pxp-engine/*.cmo
%{_libdir}/ocaml/pxp-lex-*/*.cma
%{_libdir}/ocaml/pxp-lex-*/*.cmi
%{_libdir}/ocaml/pxp-lex-*/*.cmo


%files devel
%doc LICENSE
%{_libdir}/ocaml/pxp-engine/META
%if %{opt}
%{_libdir}/ocaml/pxp-engine/*.a
%{_libdir}/ocaml/pxp-engine/*.cmxa
%endif
%{_libdir}/ocaml/pxp-engine/*.mli
%{_libdir}/ocaml/pxp-lex-*/META
%if %{opt}
%{_libdir}/ocaml/pxp-lex-*/*.a
%{_libdir}/ocaml/pxp-lex-*/*.cmxa
%{_libdir}/ocaml/pxp-lex-*/*.cmx
%{_libdir}/ocaml/pxp-lex-*/*.o
%endif
%{_libdir}/ocaml/pxp/META


%changelog
* Thu Feb 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.9-1
- New upstream version 1.2.9.
- Remove camlp4 and ulex extensions.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-16
- OCaml 4.10.0+beta1 rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-9
- Rebuild against new ocamlnet.

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-8
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-7
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-4
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.2.8-1
- New upstream version 1.2.8.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.7-5
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.7-4
- Enable bytecode builds.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.7-3
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.7-2
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.7-1
- New upstream version 1.2.7.
- ocaml-4.02.1 rebuild.

* Fri Sep 26 2014 Jerry James <loganjerry@gmail.com> - 1.2.4-8
- Drop obsolete ExcludeArch
- Fix changelog timestamp

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-7
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-3
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-1
- New upstream version 1.2.4.
- OCaml 4.01.0 rebuild.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-5
- Rebuild for OCaml 4.00.1.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-4
- Rebuild for OCaml 4.00.0 official.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-2
- Ignore Pxp_rea symbol when generating requires.

* Mon Jul  2 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-1
- New upstream version 1.2.3.
- Includes fixes upstream for OCaml 4.00.0 so remove patch.

* Sat Jun  9 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-3
- Rebuild for OCaml 4.00.0.
- Patch for new ocamldoc library.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-2
- Rebuild for OCaml 3.12.1.

* Wed Sep 21 2011 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-1
- New upstream version 1.2.2.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-4
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-3
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-1
- New upstream version 1.2.1.
- Rebuild for OCaml 3.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0test2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test2-5
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test2-4
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test2-3
- ExcludeArch ppc64 (bz #443899).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test2-2
- Rebuild for OCaml 3.10.2

* Wed Apr  2 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test2-1
- New upstream version 1.2.0test2.
- New upstream URL.
- Re-enabled camlp4 extension.

* Sun Mar  2 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-6
- Rebuild for ppc64.

* Fri Feb 15 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-5
- Added BR ocaml-camlp4-devel

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-4
- Added BR ocaml-pcre-devel, pcre-devel

* Thu Sep 13 2007 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-3
- ExcludeArch ppc64

* Thu Sep 13 2007 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-2
- Build on OCaml 3.10
- Disable building the preprocessor (requires old camlp4 or camlp5).
- License is BSD.
- Ignore Parsetree.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 1.2.0test1-1
- Initial RPM release.
