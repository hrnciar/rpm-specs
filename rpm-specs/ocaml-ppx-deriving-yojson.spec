%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-deriving-yojson
%global upname  ppx_deriving_yojson

Name:           ocaml-%{srcname}
Version:        3.5.2
Release:        4%{?dist}
Summary:        JSON codec generator for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

# Fix for OCaml 4.11.  Sent upstream 2020-04-22.
Patch1:         ocaml-411.patch

BuildRequires:  ocaml >= 4.04.0
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-ppx-deriving-devel >= 4.0
BuildRequires:  ocaml-ppxfind
BuildRequires:  ocaml-ppx-tools-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-yojson-devel >= 1.6.0

%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers
and deserializers that use the Yojson library from an OCaml type
definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

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
%autosetup -n %{upname}-%{version} -p1

# Work around name change for ounit
sed -i 's/oUnit/ounit2/g' src_test/dune

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
ln -s ../../src/ppx_deriving_yojson.cppo.ml _build/default

%check
dune runtest

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE.txt
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/runtime/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/%{upname}.cma
%{_libdir}/ocaml/%{upname}/%{upname}.cmi
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cma
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.cmxs
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.a
%{_libdir}/ocaml/%{upname}/%{upname}.cmx
%{_libdir}/ocaml/%{upname}/%{upname}.cmxa
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.a
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmx
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmxa
%endif
%{_libdir}/ocaml/%{upname}/%{upname}.cmt
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmt
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.cmti
%{_libdir}/ocaml/%{upname}/runtime/%{upname}_runtime.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-2
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 10 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-1
- Initial RPM
