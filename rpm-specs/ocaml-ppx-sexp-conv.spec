%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is now a transitive dependency of ocaml-ppx-inline-test, so using
# it to test this package creates a circular dependency.
%bcond_with tests

%global srcname ppx-sexp-conv
%global upname  ppx_sexp_conv

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        4%{?dist}
Summary:        Generate S-expression conversion functions from type definitions
License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  (ocaml-base-devel >= 0.14 and ocaml-base-devel < 0.15)
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.11.0
BuildRequires:  ocaml-odoc
BuildRequires:  (ocaml-sexplib0-devel >= 0.14 and ocaml-sexplib0-devel < 0.15)

%if %{with tests}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_sexp_conv is a PPX syntax extension that generates code for
converting OCaml types to and from s-expressions, as defined in the
sexplib0 library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
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

%if %{with tests}
%check
dune runtest
%endif

%files
%doc CHANGES.md README.org
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
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- Bump and rebuild.

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop CONTRIBUTING.md
- Use boolean dependencies to more fully reflect upstream version dependencies

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
