%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname tyxml

Name:           ocaml-%{srcname}
Version:        4.3.0
Release:        7%{?dist}
Summary:        Build valid HTML and SVG documents

License:        LGPLv2 with exceptions
URL:            https://ocsigen.org/tyxml/
Source0:        https://github.com/ocsigen/tyxml/releases/download/%{version}/%{srcname}-%{version}.tbz

# Temporary workaround for
# https://github.com/ocsigen/tyxml/issues/266
Patch1:         tyxml-4.3.0-ocaml-4.11-ignore-deprecated.patch

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-markup-devel >= 0.7.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ppx-derivers-devel
BuildRequires:  ocaml-ppx-tools-versioned-devel
BuildRequires:  ocaml-re-devel >= 1.5.0
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-uuidm-devel
BuildRequires:  ocaml-uutf-devel >= 1.0.0

%description
TyXML provides a set of convenient combinators that uses the OCaml type
system to ensure the validity of the generated documents.  TyXML can be
used with any representation of HTML and SVG: the textual one, provided
directly by this package, or DOM trees (`js_of_ocaml-tyxml`), virtual DOM
(`virtual-dom`) and reactive or replicated trees (`eliom`).  You can also
create your own representation and use it to instantiate a new set of
combinators.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-seq-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.

%package        ppx
Summary:        PPX for writing TyXML documents with HTML syntax
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ppx
This package contains PPX for writing TyXML documents with HTML syntax.

  open Tyxml
  let%%html to_ocaml = "<a href='ocaml.org'>OCaml!</a>"

The TyXML PPX is compatible with all TyXML instance, from textual trees
to reactive virtual DOM trees.

%package        ppx-devel
Summary:        Development files for %{name}-ppx
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ppx%{?_isa} = %{version}-%{release}
Requires:       ocaml-markup-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-ppx-tools-versioned-devel%{?_isa}

%description    ppx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-ppx.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Fix typo in 4.3.0; fixed upstream, so remove this when updating
sed -i 's/onmousdown/onmousedown/' lib/svg_f.ml

# Fix deprecation warning treated as an error by dune.
# Fixed upstream after the 4.3.0 release; remove this when updating
sed -i 's/Re\.get/Re.Group.get/' ppx/tyxml_ppx.ml

%build
dune build %{?_smp_mflags}

# Build the documentation.
mkdir html
ocamldoc -html -d html \
  -colorize-code -short-functors -charset utf-8 -intro docs/indexdoc \
  -I _build/install/default/lib/tyxml \
  -I _build/install/default/lib/tyxml/functor \
  -I _build/install/default/lib/tyxml/tools \
  _build/install/default/lib/tyxml/*.mli \
  _build/install/default/lib/tyxml/functor/*.mli \
  _build/install/default/lib/tyxml/tools/*.mli

%install
dune install --destdir=%{buildroot}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod 0755 {} \+
%endif

%check
dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/functor/
%dir %{_libdir}/ocaml/%{srcname}/tools/
%dir %{_libdir}/ocaml/%{srcname}/top/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cma
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmi
%{_libdir}/ocaml/%{srcname}/functor/*.cma
%{_libdir}/ocaml/%{srcname}/functor/*.cmi
%{_libdir}/ocaml/%{srcname}/tools/*.cma
%{_libdir}/ocaml/%{srcname}/tools/*.cmi
%{_libdir}/ocaml/%{srcname}/top/*.cma
%{_libdir}/ocaml/%{srcname}/top/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmxs
%{_libdir}/ocaml/%{srcname}/functor/*.cmxs
%{_libdir}/ocaml/%{srcname}/tools/*.cmxs
%{_libdir}/ocaml/%{srcname}/top/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}*.a
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmx
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmxa
%{_libdir}/ocaml/%{srcname}/functor/*.a
%{_libdir}/ocaml/%{srcname}/functor/*.cmx
%{_libdir}/ocaml/%{srcname}/functor/*.cmxa
%{_libdir}/ocaml/%{srcname}/tools/*.a
%{_libdir}/ocaml/%{srcname}/tools/*.cmx
%{_libdir}/ocaml/%{srcname}/tools/*.cmxa
%{_libdir}/ocaml/%{srcname}/top/*.a
%{_libdir}/ocaml/%{srcname}/top/*.cmx
%{_libdir}/ocaml/%{srcname}/top/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmt
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmti
%{_libdir}/ocaml/%{srcname}/%{srcname}*.ml
%{_libdir}/ocaml/%{srcname}/%{srcname}*.mli
%{_libdir}/ocaml/%{srcname}/functor/*.cmt
%{_libdir}/ocaml/%{srcname}/functor/*.cmti
%{_libdir}/ocaml/%{srcname}/functor/*.ml
%{_libdir}/ocaml/%{srcname}/functor/*.mli
%{_libdir}/ocaml/%{srcname}/tools/*.cmt
%{_libdir}/ocaml/%{srcname}/tools/*.cmti
%{_libdir}/ocaml/%{srcname}/tools/*.ml
%{_libdir}/ocaml/%{srcname}/tools/*.mli
%{_libdir}/ocaml/%{srcname}/top/*.cmt
%{_libdir}/ocaml/%{srcname}/top/*.ml

%files ppx
%dir %{_libdir}/ocaml/%{srcname}-ppx/
%dir %{_libdir}/ocaml/%{srcname}-ppx/internal/
%{_libdir}/ocaml/%{srcname}-ppx/META
%{_libdir}/ocaml/%{srcname}-ppx/ppx.exe
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cma
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cmi
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cma
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cmxs
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmxs
%endif

%files ppx-devel
%{_libdir}/ocaml/%{srcname}-ppx/dune-package
%{_libdir}/ocaml/%{srcname}-ppx/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.a
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cmx
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cmxa
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.a
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmx
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.cmt
%{_libdir}/ocaml/%{srcname}-ppx/%{srcname}*.ml
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmt
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmti
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.ml
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.mli

%files doc
%doc html/*
%license LICENSE

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-6
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-5
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-4
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 4.3.0-2
- Add ocaml-re-dvel and ocaml-uutf-devel Rs to -devel
- Add ocaml-ppx-derivers-devel and ocaml-ppx-tools-versioned-devel Rs to
  -ppx-devel
- Build in parallel

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- Initial RPM
