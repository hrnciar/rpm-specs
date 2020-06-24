%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if ! %opt
%global debug_package %{nil}
%endif

Name:           ocaml-base64
Version:        2.1.2
Release:        28%{?dist}
Summary:        Base64 library for OCaml

License:        ISC
URL:            https://github.com/mirage/ocaml-base64
Source0:        https://github.com/mirage/ocaml-base64/archive/v%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib


%description
Base64 is a group of similar binary-to-text encoding schemes that
represent binary data in an ASCII string format by translating it into
a radix-64 representation. It is specified in RFC 4648.


%package devel
Summary:        Development files for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for %{name}.


%prep
%setup -q


%build
# Bizarro build system, so build and install it by hand.
ocamlbuild -use-ocamlfind -classic-display -tag debug src/b64.cma
ocamlbuild -use-ocamlfind -classic-display -tag debug src/b64.cmxa
ocamlbuild -use-ocamlfind -classic-display -tag debug src/b64.cmxs


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
sed 's/^version.*/version = "%{version}"/' < pkg/META > META
ocamlfind install base64 _build/src/* META

# Delete a few files we don't really want.
pushd $OCAMLFIND_DESTDIR/base64
rm b64.annot b64.cmt b64.cmti
popd


%files
%doc README.md
%{_libdir}/ocaml/base64
%if %opt
%exclude %{_libdir}/ocaml/base64/*.a
%exclude %{_libdir}/ocaml/base64/*.cmx
%exclude %{_libdir}/ocaml/base64/*.cmxa
%exclude %{_libdir}/ocaml/base64/*.cmxs
%endif
%exclude %{_libdir}/ocaml/base64/*.mli


%files devel
%doc CHANGES.md
%if %opt
%{_libdir}/ocaml/base64/*.a
%{_libdir}/ocaml/base64/*.cmx
%{_libdir}/ocaml/base64/*.cmxa
%{_libdir}/ocaml/base64/*.cmxs
%endif
%{_libdir}/ocaml/base64/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-28
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-27
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-26
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-25
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-24
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-22
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-21
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-20
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-19
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-18
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-16
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-15
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-9
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-5
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 2.1.2-2
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-1
- New upstream version 2.1.2.

* Wed Oct 19 2016 Dan Horák <dan[at]danny.cz> - 2.0.0-5
- disable debuginfo subpackage on interpreted builds

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- OCaml 4.02.3 rebuild.

* Sat Jul 25 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-2
- Make -devel package depend on fully versioned base package.
- Remove duplicate META file.

* Fri Jul 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-1
- New package required by js-of-ocaml.
