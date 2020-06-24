# Debuginfo could be made to work if you could fix ocamlbuild to
# pass -g everywhere, but life is too short.
%global debug_package %{nil}

Name:           ocaml-ulex
Version:        1.1
Release:        47%{?dist}
Summary:        OCaml lexer generator for Unicode
License:        MIT

URL:            http://www.cduce.org/download.html#side
Source0:        http://www.cduce.org/download/ulex-%{version}.tar.gz

# ulex is essentially unmaintained.  This downstream patch fixes
# a string immutability issue.
Patch1:         ulex-1.1-fix-bytes.patch

BuildRequires:  ocaml >= 3.10.0-7
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel

%global __ocaml_requires_opts -i Asttypes -i Parsetree

%description
Ulex is an OCaml lexer generator for Unicode

- ulex is a lexer generator.

- it is implemented as an OCaml syntax extension:
  lexer specifications are embedded in regular OCaml code.

- the lexers work with a new kind of "lexbuf" that supports Unicode;
  a single lexer can work with arbitrary encodings of the input stream.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ulex-%{version}
%autopatch -p1

# Generate debuginfo
sed -i 's/^OCAMLBUILD=.*-byte-plugin/& -cflag -g/' Makefile


%build
make all
%ifarch %{ocaml_native_compiler}
make all.opt
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install


%files
%doc CHANGES README
%license LICENSE
%{_libdir}/ocaml/ulex
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/ulex/*.a
%exclude %{_libdir}/ocaml/ulex/*.cmxa
%endif
%exclude %{_libdir}/ocaml/ulex/*.mli


%files devel
%doc CHANGES README
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ulex/*.a
%{_libdir}/ocaml/ulex/*.cmxa
%endif
%{_libdir}/ocaml/ulex/*.mli


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-46
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-45
- OCaml 4.09.0 for riscv64

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-41
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-40
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-38
- OCaml 4.06.0 rebuild.
- Fix string immutability problem.
- Remove opt, use ocaml_native_compiler instead.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-37
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-34
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-33
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1-31
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-29
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-28
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-27
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1-26
- ocaml-4.02.1 rebuild.

* Wed Sep 24 2014 Jerry James <loganjerry@gmail.com> - 1.1.25
- Drop obsolete ExcludeArch
- Fix license handling
- Do not BR gawk; it is on the list of exceptions

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-24
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-23
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-21
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1-20
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1-18
- OCaml 4.01.0 rebuild.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1-15
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1-13
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1-12
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 1.1-10
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-9
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-7
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-5
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-4
- Rebuild for OCaml 3.11.0

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1-3
- fix license tag

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-2
- Rebuild for OCaml 3.10.2

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1-1
- New upstream version 1.1.
- Fixed upstream URL.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0-8
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0-7
- Rebuild for OCaml 3.10.1

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-6
- Ignore Parsetree module.

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-5
- Force rebuild because of updated requires/provides scripts in OCaml.

* Thu Aug 30 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-4
- Force rebuild because of changed BRs in base OCaml.

* Wed Jul 25 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-3
- ExcludeArch ppc64

* Wed Jul 25 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-2
- BuildRequires ocaml-camlp4

* Mon Jun 11 2007 Richard W.M. Jones <rjones@redhat.com> - 1.0-1
- Upstream release to match OCaml 3.10.
- Updated to latest packaging guidelines.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 0.8-1
- Initial RPM release.
