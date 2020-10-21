%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppxlib

Name:           ocaml-%{srcname}
Epoch:          1
Version:        0.13.0
Release:        6%{?dist}
Summary:        Base library and tools for ppx rewriters

License:        MIT
URL:            https://github.com/ocaml-ppx/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Fix this error:
# Error (alert deprecated): Longident.parse
# this function may misparse its input,
# use "Parse.longident" or "Longident.unflatten"
# See https://github.com/ocaml-ppx/ppxlib/issues/127.
Patch0:         %{name}-longident-parse.patch
# The invalid argument exception format differs across OCaml versions.  Patch
# the test to expect the format used by the OCaml version currently in Rawhide.
# See https://github.com/ocaml-ppx/ppxlib/pull/111.
Patch1:         %{name}-exception-format.patch
# OCaml output varies in whitespace only across versions.  Patch a test to
# expect the whitespace produced by the OCaml version currently in Rawhide.
Patch2:         %{name}-whitespace.patch

BuildRequires:  ocaml >= 4.04.1
BuildRequires:  ocaml-base-devel >= 0.11.0
BuildRequires:  ocaml-cinaps-devel >= 0.12.1
BuildRequires:  ocaml-compiler-libs-janestreet-devel >= 0.11.0
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-migrate-parsetree-devel >= 1.3.1
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ppx-derivers-devel >= 1.0
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-stdio-devel >= 0.11.0

%description
The ppxlib project provides the basis for the ppx system, which is
currently the officially supported method for meta-programming in Ocaml.
It offers a principled way to generate code at compile time in OCaml
projects.  It features:
- an OCaml AST / parser/ pretty-printer snapshot, to create a full
  frontend independent of the version of OCaml;
- a library for ppx rewriters in general, and type-driven code generators
  in particular;
- a full-featured driver for OCaml AST transformers;
- a quotation mechanism for writing values representing OCaml AST in the
  OCaml syntax;
- a generator of open recursion classes from type definitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-compiler-libs-janestreet-devel%{?_isa}
Requires:       ocaml-migrate-parsetree-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
dune build %{?_smp_mflags}
dune build %{?_smp_mflags} @doc

%install
dune install --destdir=%{buildroot}

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

# FIXME: On arm only, building the tests fails:
# /usr/bin/ld: src/.cinaps/.cinaps.eobjs/native/dune__exe__Cinaps.o: relocation R_ARM_THM_MOVW_ABS_NC against `camlCinaps_runtime' can not be used when making a shared object; recompile with -fPIC
# src/.cinaps/.cinaps.eobjs/native/dune__exe__Cinaps.o: in function `.L297': :(.text+0xdec): dangerous relocation: unsupported relocation
# <many more such warnings>
#
# Disable the tests on arm until we can figure out what is going wrong.
%ifnarch %{arm}
%check
dune runtest
%endif

%files
%doc CHANGES.md HISTORY.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/ast/
%dir %{_libdir}/ocaml/%{srcname}/metaquot/
%dir %{_libdir}/ocaml/%{srcname}/metaquot_lifters/
%dir %{_libdir}/ocaml/%{srcname}/print_diff/
%dir %{_libdir}/ocaml/%{srcname}/runner/
%dir %{_libdir}/ocaml/%{srcname}/runner_as_ppx/
%dir %{_libdir}/ocaml/%{srcname}/traverse/
%dir %{_libdir}/ocaml/%{srcname}/traverse_builtins/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%{_libdir}/ocaml/%{srcname}/*/*.cma
%{_libdir}/ocaml/%{srcname}/*/*.cmi
%{_libdir}/ocaml/%{srcname}/*/*.exe
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%{_libdir}/ocaml/%{srcname}/*/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.a
%{_libdir}/ocaml/%{srcname}/*.cmx
%{_libdir}/ocaml/%{srcname}/*.cmxa
%{_libdir}/ocaml/%{srcname}/*/*.a
%{_libdir}/ocaml/%{srcname}/*/*.cmx
%{_libdir}/ocaml/%{srcname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*.cmt
%{_libdir}/ocaml/%{srcname}/*.cmti
%{_libdir}/ocaml/%{srcname}/*.mli
%{_libdir}/ocaml/%{srcname}/*/*.cmt
%{_libdir}/ocaml/%{srcname}/*/*.cmti
%{_libdir}/ocaml/%{srcname}/*/*.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE.md

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-5
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-4
- Add Epoch to Requires from -devel to main package

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-3
- Some ppx rewriters do not work with version 0.14.0 or 0.15.0, so revert to
  version 0.13.0 until they can be updated

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.14.0-1
- New upstream release 0.14.0

* Thu Jun 18 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Rebuild for ocaml-stdio 0.14.0

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
