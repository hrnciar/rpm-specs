%global srcname mlmpfr

Name:           ocaml-%{srcname}
Version:        4.1.0
Release:        5%{?dist}
Summary:        OCaml bindings for MPFR

License:        LGPLv3
URL:            https://github.com/thvnx/%{srcname}
Source0:        %{url}/archive/%{srcname}.%{version}.tar.gz

BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-dune >= 1.11.0
BuildRequires:  ocaml-odoc
BuildRequires:  pkgconfig(mpfr)

%description
This library provides OCaml bindings for MPFR.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mpfr-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{srcname}.%{version}
# https://github.com/thvnx/mlmpfr/issues/11
mv examples/rndo-add.ml examples/rndo_add.ml
sed -i -e 's/rndo-add/rndo_add/' examples/dune

%build
dune build %{?_smp_mflags}
dune build %{?_smp_mflags} @doc

# Relink the stublibs with $RPM_LD_FLAGS.
cd _build/default/src
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" $(pkgconf --libs mpfr) \
  -o mlmpfr_stubs $(ar t libmlmpfr_stubs.a)
cd -

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
%doc Changes README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/mpfr.cmi
%{_libdir}/ocaml/%{srcname}/%{srcname}.cma
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxs
%endif
%{_libdir}/ocaml/stublibs/dll%{srcname}_stubs.so

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/lib%{srcname}_stubs.a
%{_libdir}/ocaml/%{srcname}/%{srcname}.a
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxa
%{_libdir}/ocaml/%{srcname}/mpfr.cmx
%endif
%{_libdir}/ocaml/%{srcname}/mpfr.cmt
%{_libdir}/ocaml/%{srcname}/mpfr.cmti
%{_libdir}/ocaml/%{srcname}/mpfr.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- Version 4.1.0
- Drop upstreamed -32bit patch

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-2
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 4.0.2-1
- Initial RPM
