Name:           ocaml-qcheck
Version:        0.15
Release:        1%{?dist}
Summary:        QuickCheck inspired property-based testing for OCaml

License:        BSD
URL:            https://github.com/c-cube/qcheck
Source0:        https://github.com/c-cube/qcheck/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-ounit-devel


%description
This module allows to check invariants (properties of some types) over
randomly generated instances of the type. It provides combinators for
generating instances and printing them.


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
%autosetup -n qcheck-%{version}


%build
dune build %{?_smp_mflags} @install --verbose
dune build %{?_smp_mflags} @doc


%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# These files will be installed using doc and license directives.
rm -r %{buildroot}%{_prefix}/doc

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest --no-buffer --profile release


%files
%doc README.adoc CHANGELOG.md
%license LICENSE
%dir %{_libdir}/ocaml/qcheck-alcotest/
%dir %{_libdir}/ocaml/qcheck-core/
%dir %{_libdir}/ocaml/qcheck-ounit/
%{_libdir}/ocaml/*/{,*/}*.cma
%{_libdir}/ocaml/*/{,*/}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/{,*/}*.cmxs
%endif


%files devel
%doc README.adoc CHANGELOG.md
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/{,*/}*.a
%{_libdir}/ocaml/*/{,*/}*.cmxa
%{_libdir}/ocaml/*/{,*/}*.cmx
%endif
%{_libdir}/ocaml/*/{,*/}*.ml
%{_libdir}/ocaml/*/{,*/}*.mli
%{_libdir}/ocaml/*/{,*/}*.cma
%{_libdir}/ocaml/*/{,*/}*.cmi
%{_libdir}/ocaml/*/{,*/}*.cmt
%{_libdir}/ocaml/*/{,*/}*.cmti
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam


%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE


%changelog
* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 0.15-1
- Version 0.15

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14-4
- OCaml 4.11.1 rebuild

* Fri Aug 28 2020 Jerry James <loganjerry@gmail.com> - 0.14-3
- Rebuild for alcotest 1.2.2

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 0.14-1
- Version 0.14

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-6
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-5
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-4
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-2
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 0.13-1
- New upstream release.
- Build with alcotest support.
- Build documentation with odoc, and ship it in a new doc subpackage.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.12-2
- OCaml 4.10.0+beta1 rebuild.

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 0.12-1
- New upstream release. (RHBZ#1757625)
- Remove unneeded BuildRequires on opam-installer.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10-3
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10-2
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Andy Li <andy@onthewings.net> - 0.10-1
- New upstream release.
- Update build system and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.8-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.8-4
- OCaml 4.07.0-rc1 rebuild.

* Mon May 14 2018 Andy Li <andy@onthewings.net> - 0.8-3
- Rebuilt against ounit.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Andy Li <andy@onthewings.net> - 0.8-1
- New upstream release. (RHBZ#1541681)
- Enable debug package.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7-2
- OCaml 4.06.0 rebuild.

* Mon Nov 20 2017 Andy Li <andy@onthewings.net> - 0.7-1
- Initial RPM release.
