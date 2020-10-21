%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppx-tools
%global upname  ppx_tools

Name:           ocaml-%{srcname}
Version:        6.2
Release:        4%{?dist}
Summary:        Tools for authors of ppx rewriters

License:        MIT
URL:            https://github.com/ocaml-ppx/%{upname}
Source0:        %{url}/archive/%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 1.6
BuildRequires:  ocaml-odoc

%description
Tools for authors of syntactic tools (such as ppx rewriters).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

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
%doc README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/ast_lifter/
%dir %{_libdir}/ocaml/%{upname}/metaquot/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/dumpast
%{_libdir}/ocaml/%{upname}/genlifter
%{_libdir}/ocaml/%{upname}/ppx_metaquot
%{_libdir}/ocaml/%{upname}/rewriter
%{_libdir}/ocaml/%{upname}/metaquot/ppx.exe
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%{_libdir}/ocaml/%{upname}/*/*.cma
%{_libdir}/ocaml/%{upname}/*/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%{_libdir}/ocaml/%{upname}/*/*.cmxs
%endif

%files devel
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

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 6.2-4
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 6.2-3
- Bump and rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 6.2-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 6.2-1
- Version 6.2
- Drop upstreamed ppx_tools-6.1-ocaml-4.11.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 6.1-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 6.1-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 6.1-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 6.1-2
- OCaml 4.10.0 final

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 6.1-1
- Version 6.1

* Wed Feb  5 2020 Jerry James <loganjerry@gmail.com> - 5.3-1
- Initial RPM
