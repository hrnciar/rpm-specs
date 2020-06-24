%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ocaml-compiler-libs

Name:           %{srcname}-janestreet
Version:        0.12.1
Release:        1%{?dist}
Summary:        OCaml compiler libraries repackaged

License:        MIT
URL:            https://github.com/janestreet/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.1
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-odoc

%description
This package exposes the OCaml compiler libraries repackaged under
the toplevel names Ocaml_common, Ocaml_bytecomp, Ocaml_optcomp, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

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
%autosetup -n %{srcname}-%{version}

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

%files
%doc README.org
%license LICENSE.md
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/bytecomp/
%dir %{_libdir}/ocaml/%{srcname}/common/
%dir %{_libdir}/ocaml/%{srcname}/optcomp/
%dir %{_libdir}/ocaml/%{srcname}/shadow/
%dir %{_libdir}/ocaml/%{srcname}/toplevel/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*/*.cma
%{_libdir}/ocaml/%{srcname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*/*.a
%{_libdir}/ocaml/%{srcname}/*/*.cmx
%{_libdir}/ocaml/%{srcname}/*/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*/*.cmt

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE.md

%changelog
* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.12.1-1
- Initial RPM
