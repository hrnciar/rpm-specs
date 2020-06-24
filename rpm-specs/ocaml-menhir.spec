%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%bcond_without coq

Name:           ocaml-menhir
Version:        20200612
Release:        1%{?dist}
Summary:        LR(1) parser generator for OCaml

# The generator is GPLv2
License:        GPLv2
URL:            http://gallium.inria.fr/~fpottier/menhir/
Source0:        https://gitlab.inria.fr/fpottier/menhir/-/archive/%{version}/menhir-%{version}.tar.bz2

%if %{with coq}
BuildRequires:  coq
%endif
BuildRequires:  hevea
BuildRequires:  ImageMagick
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-odoc
BuildRequires:  tex(latex)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(moreverb.sty)

Requires:       ocaml-menhirlib-devel%{?_isa} = %{version}-%{release}

# This can be removed when F32 reaches EOL
Obsoletes:      %{name}-devel < 20200211-1
Provides:       %{name}-devel = %{version}-%{release}

%description
Menhir is a LR(1) parser generator for the Objective Caml programming
language.  That is, Menhir compiles LR(1) grammar specifications down to
OCaml code.  Menhir was designed and implemented by François Pottier and
Yann Régis-Gianas.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%package     -n ocaml-menhirlib
Summary:        Runtime library for parsers produced by Menhir
# The library is LGPLv2 with a linking exception.
License:        LGPLv2 with exceptions

%description -n ocaml-menhirlib
This package contains the runtime library for parsers produced by Menhir.

%package     -n ocaml-menhirlib-devel
Summary:        Development files for ocaml-menhirlib
# The library is LGPLv2 with a linking exception.
License:        LGPLv2 with exceptions
Requires:       ocaml-menhirlib%{?_isa} = %{version}-%{release}

%description -n ocaml-menhirlib-devel
This ocaml-menhirlib-devel package contains libraries and signature
files for building applications with a parser produced by Menhir.

%if %{with coq}
%package     -n coq-menhirlib
Summary:        Support library for verified Coq parsers produced by Menhir
License:        LGPLv3+
Requires:       coq%{?_isa}

%description -n coq-menhirlib
The Menhir parser generator, in --coq mode, can produce Coq parsers.
These parsers must be linked against this library, which provides both an
interpreter (which allows running the generated parser) and a validator
(which allows verifying, at parser construction time, that the generated
parser is correct and complete with respect to the grammar).
%endif

%prep
%setup -q -n menhir-%{version}

# Enable debuginfo
sed -i 's/-j 0/-cflag -g -lflag -g &/' src/Makefile

# Do not ship the obsolete demos
rm -fr demos/obsolete

%build
dune build %{?_smp_mflags}
%if %{with coq}
make -C coq-menhirlib
%endif
dune build %{?_smp_mflags} @doc

%install
dune install --destdir=%{buildroot}

%if %{with coq}
make -C coq-menhirlib install DESTDIR=%{buildroot}
%else
# Even if coq is disabled, dune will put a META file and dune-package
# here.
rm -rf %{buildroot}%{_libdir}/ocaml/coq-menhirlib/
%endif

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

%files
%doc doc/manual.pdf
%license LICENSE
%{_bindir}/menhir
%{_mandir}/man1/menhir.1*
%{_libdir}/ocaml/menhir/
%{_libdir}/ocaml/menhirSdk/

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE

%files -n ocaml-menhirlib
%dir %{_libdir}/ocaml/menhirLib/
%license LICENSE
%{_libdir}/ocaml/menhirLib/META
%{_libdir}/ocaml/menhirLib/menhirLib.cma
%{_libdir}/ocaml/menhirLib/menhirLib.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/menhirLib/menhirLib.cmxs
%endif

%files -n ocaml-menhirlib-devel
%{_libdir}/ocaml/menhirLib/dune-package
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/menhirLib/menhirLib.a
%{_libdir}/ocaml/menhirLib/menhirLib.cmx
%{_libdir}/ocaml/menhirLib/menhirLib.cmxa
%endif
%{_libdir}/ocaml/menhirLib/menhirLib.cmt
%{_libdir}/ocaml/menhirLib/menhirLib.cmti
%{_libdir}/ocaml/menhirLib/menhirLib.mli

%if %{with coq}
%files -n coq-menhirlib
%doc coq-menhirlib/CHANGES.md coq-menhirlib/README.md
%license coq-menhirlib/LICENSE
%{_libdir}/coq/user-contrib/MenhirLib/
%{_libdir}/ocaml/coq-menhirlib/
%endif

%changelog
* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 20200612-1
- Version 20200612

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 20200211-6
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 20200211-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 20200211-4
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 20200211-3
- Re-enable Coq bindings after OCaml bootstrap.

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 20200211-2
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 20200211-1
- Version 20200211
- Dune is now used to build the package
- Split the build-time and runtime parts into separate packages

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 20190924-9
- OCaml 4.10.0 final.
- Disable Coq for 4.10.0 build.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190924-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 20190924-7
- Reenable coq support
- Add coq-menhirlib subpackage, without which coq support is rather pointless

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 20190924-6
- OCaml 4.10.0+beta1 rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 20190924-5
- Disable coq for now.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 20190924-4
- Bump release and rebuild.

* Thu Dec 05 2019 Richard W.M. Jones <rjones@redhat.com> - 20190924-3
- Bump release and rebuild.

* Thu Dec 05 2019 Richard W.M. Jones <rjones@redhat.com> - 20190924-2
- OCaml 4.09.0 (final) rebuild.

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 20190924-1
- New upstream version
- BR coq to get coq_makefile

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 20190626-4
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 20190626-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190626-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Jerry James <loganjerry@gmail.com> - 20190626-1
- New upstream version

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 20190620-2
- OCaml 4.08.0 (final) rebuild.

* Wed Jun 26 2019 Jerry James <loganjerry@gmail.com> - 20190620-1
- New upstream version

* Tue Jun 18 2019 Jerry James <loganjerry@gmail.com> - 20190613-1
- New upstream version

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 20181113-4
- OCaml 4.08.0 (beta 3) rebuild.

* Tue Mar 26 2019 Jerry James <loganjerry@gmail.com> - 20181113-3
- Add missing R on ocamlfind (bz 1692434)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Jerry James <loganjerry@gmail.com> - 20181113-1
- New upstream version
- New source URL

* Mon Oct 22 2018 Jerry James <loganjerry@gmail.com> - 20181006-1
- New upstream version
- Ship libraries in the main package

* Thu Sep 27 2018 Jerry James <loganjerry@gmail.com> - 20180905-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180530-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 20180530-3
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 20180530-2
- OCaml 4.07.0-rc1 rebuild.

* Wed Jun  6 2018 Jerry James <loganjerry@gmail.com> - 20180530-1
- New upstream version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Jerry James <loganjerry@gmail.com> - 20171222-1
- New upstream version

* Sat Dec  9 2017 Jerry James <loganjerry@gmail.com> - 20171206-1
- New upstream version

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 20170712-5
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 20170712-4
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170712-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170712-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Jerry James <loganjerry@gmail.com> - 20170712-1
- New upstream version
- Build the manual from LaTeX sources

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 20170607-2
- OCaml 4.04.2 rebuild.

* Sat Jun 10 2017 Jerry James <loganjerry@gmail.com> - 20170607-1
- New upstream version

* Fri May 19 2017 Jerry James <loganjerry@gmail.com> - 20170509-1
- New upstream version
- License change: QPL with exceptions to GPLv2

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 20170101-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  2 2017 Jerry James <loganjerry@gmail.com> - 20170101-1
- New upstream version

* Tue Nov 15 2016 Jerry James <loganjerry@gmail.com> - 20161115-1
- New upstream version

* Mon Nov 14 2016 Jerry James <loganjerry@gmail.com> - 20161114-1
- New upstream version

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 20160825-2
- Rebuild for OCaml 4.04.0.
- Add explicit dep on ocamlbuild.

* Sat Aug 27 2016 Jerry James <loganjerry@gmail.com> - 20160825-1
- New upstream version

* Mon Jul  4 2016 Jerry James <loganjerry@gmail.com> - 20160526-1
- New upstream version

* Thu May 12 2016 Jerry James <loganjerry@gmail.com> - 20160504-1
- New upstream version

* Thu Mar  3 2016 Jerry James <loganjerry@gmail.com> - 20160303-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Jerry James <loganjerry@gmail.com> - 20151112-1
- New upstream version

* Mon Oct 26 2015 Jerry James <loganjerry@gmail.com> - 20151026-1
- New upstream version

* Sat Oct 24 2015 Jerry James <loganjerry@gmail.com> - 20151023-1
- New upstream version

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 20151012-1
- New upstream version

* Fri Oct  9 2015 Jerry James <loganjerry@gmail.com> - 20151005-1
- New upstream version

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 20150914-1
- New upstream version

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-5
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-3
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-2
- ocaml-4.02.1 rebuild.

* Mon Jan  5 2015 Jerry James <loganjerry@gmail.com> - 20141215-1
- New upstream version

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 20140422-7
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 20140422-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140422-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 20140422-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.
- Fix license handling

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 20140422-3
- OCaml 4.02.0 beta rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140422-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jerry James <loganjerry@gmail.com> - 20140422-1
- New upstream version
- Fix standard.mly character encoding

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 20130911-3
- Remove ocaml_arches macro (bz 1087794)

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 20130911-2
- Rebuild for OCaml 4.01.0

* Thu Sep 12 2013 Jerry James <loganjerry@gmail.com> - 20130911-1
- New upstream version
- Allow debuginfo generation since ocaml 4 supports it

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Jerry James <loganjerry@gmail.com> - 20130116-1
- New upstream version

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 20120123-5
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 20120123-3
- Rebuild for OCaml 4.00.0.

* Fri Jun  8 2012 Jerry James <loganjerry@gmail.com> - 20120123-2
- Rebuild for OCaml 4.00.0

* Mon Jan 23 2012 Jerry James <loganjerry@gmail.com> - 20120123-1
- New upstream version

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 20111019-3
- Rebuild for ocaml 3.12.1

* Mon Dec 19 2011 Jerry James <loganjerry@gmail.com> - 20111019-2
- Change the subpackages to match Debian
- Add patch to allow building demos outside of the menhir source tree

* Wed Nov  9 2011 Jerry James <loganjerry@gmail.com> - 20111019-1
- Initial RPM
