%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-deriving
%global upname  ppx_deriving

Name:           ocaml-%{srcname}
Version:        4.5
Release:        3%{?dist}
Summary:        Type-driven code generation for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.2
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune >= 1.6.3
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-migrate-parsetree-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppxfind
BuildRequires:  ocaml-ppx-tools-devel >= 4.02.3

%description
Deriving is a library simplifying type-driven code generation on OCaml.
It includes a set of useful plugins: show, eq, ord (eq), enum, iter,
map (iter), fold (iter), make, yojson, and protobuf.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-migrate-parsetree-devel%{?_isa}
Requires:       ocaml-ppx-tools-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{upname}-%{version} -p1

# Work around name change for ounit
sed -i 's/oUnit/ounit2/g' src_test/*/dune

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

# Help the debuginfo generator find the source files
cd _build/default
ln -s ../../src/ppx_deriving_main.cppo.ml
ln -s ../../src/api/ppx_deriving.cppo.ml .
ln -s ../../src/runtime/ppx_deriving_runtime.cppo.ml .
ln -s ../../src_plugins/create/ppx_deriving_create.cppo.ml .
ln -s ../../src_plugins/enum/ppx_deriving_enum.cppo.ml .
ln -s ../../src_plugins/eq/ppx_deriving_eq.cppo.ml .
ln -s ../../src_plugins/fold/ppx_deriving_fold.cppo.ml .
ln -s ../../src_plugins/iter/ppx_deriving_iter.cppo.ml .
ln -s ../../src_plugins/make/ppx_deriving_make.cppo.ml .
ln -s ../../src_plugins/map/ppx_deriving_map.cppo.ml .
ln -s ../../src_plugins/ord/ppx_deriving_ord.cppo.ml
ln -s ../../src_plugins/show/ppx_deriving_show.cppo.ml
cd -

%check
dune runtest

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/api/
%dir %{_libdir}/ocaml/%{upname}/create/
%dir %{_libdir}/ocaml/%{upname}/enum/
%dir %{_libdir}/ocaml/%{upname}/eq/
%dir %{_libdir}/ocaml/%{upname}/fold/
%dir %{_libdir}/ocaml/%{upname}/iter/
%dir %{_libdir}/ocaml/%{upname}/make/
%dir %{_libdir}/ocaml/%{upname}/map/
%dir %{_libdir}/ocaml/%{upname}/ord/
%dir %{_libdir}/ocaml/%{upname}/runtime/
%dir %{_libdir}/ocaml/%{upname}/show/
%dir %{_libdir}/ocaml/%{upname}/std/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/ppx_deriving
%{_libdir}/ocaml/%{upname}/*/*.cma
%{_libdir}/ocaml/%{upname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*/*.a
%{_libdir}/ocaml/%{upname}/*/*.cmx
%{_libdir}/ocaml/%{upname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*/*.cmt
%{_libdir}/ocaml/%{upname}/*/*.cmti
%{_libdir}/ocaml/%{upname}/*/*.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE.txt

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.5-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.5-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 4.5-1
- Version 4.5
- Drop upstreamed ppx_deriving-4.4.1-ocaml-4.11.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.1-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.1-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.1-2
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 10 2020 Jerry James <loganjerry@gmail.com> - 4.4.1-1
- Initial RPM
