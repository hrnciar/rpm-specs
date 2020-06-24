%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppxlib

Name:           ocaml-%{srcname}
Version:        0.13.0
Release:        1%{?dist}
Summary:        Base library and tools for ppx rewriters

License:        MIT
URL:            https://github.com/ocaml-ppx/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# The invalid argument exception format differs across OCaml versions.  Patch
# the test to expect the format used by the OCaml version currently in Rawhide.
# See https://github.com/ocaml-ppx/ppxlib/pull/111.
Patch0:         %{name}-exception-format.patch
# Fix this error:
# Error (alert deprecated): Longident.parse
# this function may misparse its input,
# use "Parse.longident" or "Longident.unflatten"
# See https://github.com/ocaml-ppx/ppxlib/issues/127.
Patch1:         %{name}-longident-parse.patch

BuildRequires:  ocaml >= 4.04.1
BuildRequires:  ocaml-base-devel >= 0.11.0
BuildRequires:  ocaml-cinaps-devel >= 0.12.1
BuildRequires:  ocaml-compiler-libs-janestreet-devel >= 0.11.0
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-migrate-parsetree-devel >= 1.3.1
BuildRequires:  ocaml-ppx-derivers-devel >= 1.0
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-seq-devel
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
Requires:       %{name}%{?_isa} = %{version}-%{release}
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

%check
# Ordinarily, this script would contain only "dune runtest".  As of dune 2.0,
# if the OCaml version is 4.10 or greater, then bytecode executables are
# created with -output-complete-exe instead of -custom.  However, ppxlib wants
# to load debug symbols, but there are no debug symbols because of
# https://github.com/ocaml/ocaml/issues/9344.  Until that issue is fixed, or
# dune stops using -output-complete-exe, we are forced to build the tests
# manually with -custom.
#
# This fails, but builds all of the object files.
dune runtest || :

# Rebuild the test executable with -custom
cd _build/default
ocamlc -w "@1..3@5..28@30..39@43@46..47@49..57@61..62-40" \
  -strict-sequence -strict-formats -short-paths -keep-locs -w -66 -g \
  -o test/expect/expect_test.exe -custom -linkall \
  %{_libdir}/ocaml/unix.cma -I %{_libdir}/ocaml \
  %{_libdir}/ocaml/compiler-libs/ocamlcommon.cma \
  %{_libdir}/ocaml/compiler-libs/ocamlbytecomp.cma \
  %{_libdir}/ocaml/compiler-libs/ocamltoplevel.cma \
  %{_libdir}/ocaml/ocaml-compiler-libs/common/ocaml_common.cma \
  %{_libdir}/ocaml/ocaml-compiler-libs/shadow/ocaml_shadow.cma \
  %{_libdir}/ocaml/result/result.cma \
  %{_libdir}/ocaml/ppx_derivers/ppx_derivers.cma \
  %{_libdir}/ocaml/ocaml-migrate-parsetree/migrate_parsetree.cma \
  -I %{_libdir}/ocaml/base/base_internalhash_types \
  %{_libdir}/ocaml/base/base_internalhash_types/base_internalhash_types.cma \
  %{_libdir}/ocaml/base/caml/caml.cma \
  %{_libdir}/ocaml/sexplib0/sexplib0.cma \
  %{_libdir}/ocaml/base/shadow_stdlib/shadow_stdlib.cma \
  -I %{_libdir}/ocaml/base %{_libdir}/ocaml/base/base.cma \
  %{_libdir}/ocaml/stdio/stdio.cma ast/ppxlib_ast.cma \
  print-diff/ppxlib_print_diff.cma \
  traverse_builtins/ppxlib_traverse_builtins.cma src/ppxlib.cma \
  traverse/ppxlib_traverse.cma \
  test/expect/.expect_test.eobjs/byte/printers.cmo \
  test/expect/.expect_test.eobjs/byte/expect_test.cmo

# Run the tests manually.  Using "dune runtest" rebuilds expect_test.exe,
# thereby undoing the work we just did.
test/expect/expect_test.exe test/driver/attributes/test.ml &> /dev/null
test/expect/expect_test.exe test/code_path/test.ml &> /dev/null
test/expect/expect_test.exe test/driver/non-compressible-suffix/test.ml &> /dev/null
test/expect/expect_test.exe test/deriving/test.ml &> /dev/null
test/expect/expect_test.exe test/quoter/test.ml &> /dev/null
test/expect/expect_test.exe test/driver/transformations/test.ml &> /dev/null
test/expect/expect_test.exe test/traverse/test.ml &> /dev/null
test/expect/expect_test.exe test/base/test.ml &> /dev/null

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
* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
