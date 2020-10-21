%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname tyxml

# This package is needed to build ocaml-odoc, but ocaml-odoc is needed to build
# documentation for this package.  Skip building documentation for now until we
# develop a strategy for handling dependency loops.

Name:           ocaml-%{srcname}
Version:        4.4.0
Release:        3%{?dist}
Summary:        Build valid HTML and SVG documents

License:        LGPLv2 with exceptions
URL:            https://ocsigen.org/tyxml/
Source0:        https://github.com/ocsigen/tyxml/releases/download/%{version}/%{srcname}-%{version}.tbz

# Temporary workaround for
# https://github.com/ocsigen/tyxml/issues/266
Patch1:         tyxml-4.3.0-ocaml-4.11-ignore-deprecated.patch

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-markup-devel >= 0.7.2
BuildRequires:  ocaml-ppx-tools-versioned-devel
BuildRequires:  ocaml-re-devel >= 1.5.0
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-uutf-devel >= 1.0.0

# See comment above about dependency loops.  If the issue is not resolved by
# Fedora 36, this can be removed.
Obsoletes:      %{name}-doc < 4.4.0-1
Provides:       %{name}-doc = %{version}-%{release}

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

%package        syntax
Summary:        Common layer for the JSX and PPX syntaxes for TyXML

%description    syntax
This package contains common code used by both the JSX and the PPX
syntaxes for TyXML.

%package        syntax-devel
Summary:        Development files for %{name}-syntax
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-tools-versioned-devel%{?_isa}

%description    syntax-devel
The %{name}-syntax-devel package contains libraries and signature files
for developing applications that use %{name}-syntax.

%package        jsx
Summary:        JSX syntax for writing TyXML documents
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}

%description    jsx
This package enables writing TyXML documents with reasons's JSX syntax,
from textual trees to reactive virtual DOM trees.

  open Tyxml
  let to_ocaml = <a href="ocaml.org"> "OCaml!" </a>;

%package        jsx-devel
Summary:        Development files for %{name}-jsx
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jsx%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-tools-versioned-devel%{?_isa}

%description    jsx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-jsx.

%package        ppx
Summary:        PPX for writing TyXML documents with HTML syntax
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}

%description    ppx
This package contains PPX for writing TyXML documents with HTML syntax.

  open Tyxml
  let%%html to_ocaml = "<a href='ocaml.org'>OCaml!</a>"

The TyXML PPX is compatible with all TyXML instance, from textual trees
to reactive virtual DOM trees.

%package        ppx-devel
Summary:        Development files for %{name}-ppx
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ppx%{?_isa} = %{version}-%{release}
Requires:       ocaml-markup-devel%{?_isa}
Requires:       ocaml-ppx-tools-versioned-devel%{?_isa}

%description    ppx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-ppx.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
dune build %{?_smp_mflags}

%install
dune install --destdir=%{buildroot}

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod 0755 {} \+
%endif

# As of version 4.4.0, the tests fail due to lack of the reason package in
# Fedora.  Tests are disabled until we can figure out how to work around that.

#%%check
#dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/functor/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cma
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmi
%{_libdir}/ocaml/%{srcname}/functor/*.cma
%{_libdir}/ocaml/%{srcname}/functor/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmxs
%{_libdir}/ocaml/%{srcname}/functor/*.cmxs
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
%endif
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmt
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmti
%{_libdir}/ocaml/%{srcname}/%{srcname}*.mli
%{_libdir}/ocaml/%{srcname}/functor/*.cmt
%{_libdir}/ocaml/%{srcname}/functor/*.cmti
%{_libdir}/ocaml/%{srcname}/functor/*.mli

%files syntax
%dir %{_libdir}/ocaml/%{srcname}-syntax/
%{_libdir}/ocaml/%{srcname}-syntax/META
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cma
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmxs
%endif

%files syntax-devel
%{_libdir}/ocaml/%{srcname}-syntax/dune-package
%{_libdir}/ocaml/%{srcname}-syntax/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.a
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmx
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmt
%{_libdir}/ocaml/%{srcname}-syntax/%{srcname}*.cmti
%{_libdir}/ocaml/%{srcname}-syntax/*.mli

%files jsx
%dir %{_libdir}/ocaml/%{srcname}-jsx/
%{_libdir}/ocaml/%{srcname}-jsx/META
%{_libdir}/ocaml/%{srcname}-jsx/ppx.exe
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cma
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cmxs
%endif

%files jsx-devel
%{_libdir}/ocaml/%{srcname}-jsx/dune-package
%{_libdir}/ocaml/%{srcname}-jsx/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.a
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cmx
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}-jsx/%{srcname}*.cmt

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
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmt
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.cmti
%{_libdir}/ocaml/%{srcname}-ppx/internal/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-2
- OCaml 4.11.0 rebuild

* Tue Aug  4 2020 Jerry James <loganjerry@gmail.com> - 4.4.0-1
- Version 4.4.0
- Drop documentation subpackage until dependency loop can be handled
- Disable tests since no reason package is available

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
