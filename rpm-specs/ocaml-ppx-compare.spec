%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-compare
%global upname  ppx_compare

Name:           ocaml-%{srcname}
Version:        0.13.0
Release:        2%{?dist}
Summary:        Generate comparison functions from types

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.13.0
BuildRequires:  ocaml-dune >= 1.5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.9.0
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-odoc

%description
Ppx_compare is a ppx rewriter that derives comparison and equality
functions from type representations.  The scaffolded functions are
usually much faster than OCaml's `Pervasives.compare` and
`Pervasives.(=)`.  Scaffolding functions also give more flexibility by
allowing them to be overridden for a specific type, and more safety by
making sure that only comparable values are compared.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{version} -p1

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

# The tests require a native build.
%ifnarch %{ocaml_native_compiler}
%check
dune runtest
%endif

%files
%doc CHANGES.md CONTRIBUTING.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/expander/
%dir %{_libdir}/ocaml/%{upname}/runtime-lib/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%{_libdir}/ocaml/%{upname}/*/*.cma
%{_libdir}/ocaml/%{upname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%{_libdir}/ocaml/%{upname}/*/*.cmxs
%endif

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%{_libdir}/ocaml/%{upname}/*/*.a
%{_libdir}/ocaml/%{upname}/*/*.cmx
%{_libdir}/ocaml/%{upname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli
%{_libdir}/ocaml/%{upname}/*/*.cmt
%{_libdir}/ocaml/%{upname}/*/*.cmti
%{_libdir}/ocaml/%{upname}/*/*.mli

%changelog
* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop unnecessary patch

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
