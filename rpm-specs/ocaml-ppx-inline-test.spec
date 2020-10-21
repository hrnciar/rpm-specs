# TESTING NOTE: The ppx_jane module is needed to run the tests.  However,
# ppx_jane transitively requires this module.  Therefore, we cannot run the
# tests at all until we are able to add ppx_jane to Fedora, and even then we
# will only be able to run the tests in non-bootstrap mode.

%global srcname ppx-inline-test
%global upname  ppx_inline_test

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        3%{?dist}
Summary:        Syntax extension for writing inline tests in OCaml code

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.11.0
BuildRequires:  ocaml-time-now-devel >= 0.14
BuildRequires:  ocaml-odoc

%description
Ppx_inline_test is a syntax extension for writing inline tests in OCaml
code.

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

# Relink the stublib with $RPM_LD_FLAGS.
pushd _build/default/runner/lib
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -o %{upname}_runner_lib_stubs am_testing.o
popd

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

%files
%doc CHANGES.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/config/
%dir %{_libdir}/ocaml/%{upname}/drop/
%dir %{_libdir}/ocaml/%{upname}/libname/
%dir %{_libdir}/ocaml/%{upname}/runner/
%dir %{_libdir}/ocaml/%{upname}/runner/lib/
%dir %{_libdir}/ocaml/%{upname}/runtime-lib/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/ppx.exe
%{_libdir}/ocaml/%{upname}/drop/ppx.exe
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%{_libdir}/ocaml/%{upname}/*/*.cma
%{_libdir}/ocaml/%{upname}/*/*.cmi
%{_libdir}/ocaml/%{upname}/runner/lib/*.cma
%{_libdir}/ocaml/%{upname}/runner/lib/*.cmi
%{_libdir}/ocaml/%{upname}/runner/lib/*.js
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%{_libdir}/ocaml/%{upname}/*/*.cmxs
%{_libdir}/ocaml/%{upname}/runner/lib/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dll%{upname}_runner_lib_stubs.so

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
%{_libdir}/ocaml/%{upname}/runner/lib/*.a
%{_libdir}/ocaml/%{upname}/runner/lib/*.cmx
%{_libdir}/ocaml/%{upname}/runner/lib/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli
%{_libdir}/ocaml/%{upname}/*/*.cmt
%{_libdir}/ocaml/%{upname}/*/*.cmti
%{_libdir}/ocaml/%{upname}/*/*.mli
%{_libdir}/ocaml/%{upname}/runner/lib/*.cmt

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Wed Aug 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.1-1
- Initial RPM
