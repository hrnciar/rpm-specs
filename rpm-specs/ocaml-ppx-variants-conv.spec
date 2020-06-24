%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-variants-conv
%global upname  ppx_variants_conv

Name:           ocaml-%{srcname}
Version:        0.13.0
Release:        2%{?dist}
Summary:        Generate accessor & iteration functions for OCaml variant types

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  (ocaml-base-devel >= 0.13 and ocaml-base-devel < 0.14)
BuildRequires:  ocaml-dune >= 1.5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.9.0
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-odoc
BuildRequires:  (ocaml-variantslib-devel >= 0.13 and ocaml-variantslib-devel < 0.14)

%description
Ppx_variants_conv is a ppx rewriter that can be used to define
first-class values representing variant constructors, and additional
routines to fold, iterate and map over all constructors of a variant
type.  It provides corresponding functionality for variant types as
ppx_fields_conv provides for record types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-variantslib-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{version}

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
dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%endif

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli

%changelog
* Sun Jun  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop CONTRIBUTING.md
- Use boolean dependencies to more fully reflect upstream version dependencies

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
