Name:           ocaml-gen
Version:        0.5.3
Release:        5%{?dist}
Summary:        Simple, efficient iterators for OCaml

License:        BSD
URL:            https://github.com/c-cube/gen
Source0:        https://github.com/c-cube/gen/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-qtest-devel

%description
Iterators for OCaml, both restartable and consumable.
The implementation keeps a good balance between simplicity and performance.


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
%setup -q -n gen-%{version}
%autopatch -p1


%build
dune build %{?_smp_mflags} -p gen @install
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
# disable test for armhf https://github.com/ocaml/dune/issues/2527
%ifnarch armv7hl
dune runtest -p gen --no-buffer
%endif

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/ocaml/gen
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/gen/*.a
%exclude %{_libdir}/ocaml/gen/*.cmxa
%exclude %{_libdir}/ocaml/gen/*.cmx
%endif
%exclude %{_libdir}/ocaml/gen/*.ml
%exclude %{_libdir}/ocaml/gen/*.mli


%files devel
%doc README.md CHANGELOG.md
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/gen/*.a
%{_libdir}/ocaml/gen/*.cmxa
%{_libdir}/ocaml/gen/*.cmx
%endif
%{_libdir}/ocaml/gen/*.ml
%{_libdir}/ocaml/gen/*.mli


%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Jerry James <loganjerry@gmail.com> - 0.5.3-1
- New upstream version 0.5.3 (bz 1834874)

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-10
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-8
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 0.5.2-7
- Rebuild for ocaml-qcheck 0.13.
- Build documentation with odoc, and ship it in a new doc subpackage.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-5
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-4
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.5.2-3
- OCaml 4.10.0+beta1 rebuild.

* Sat Dec 28 2019 Andy Li <andy@onthewings.net> - 0.5.2-2
- Disable test for armhf.

* Sat Dec 28 2019 Andy Li <andy@onthewings.net> - 0.5.2-1
- New upstream version 0.5.2. (RHBZ#1706435)
- Use dune (instead of jbuilder) to build.
- Remove unneeded BuildRequires on opam-installer.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-10
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-9
- Miscellaneous build system updates.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-8
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Andy Li <andy@onthewings.net> - 0.5.1-1
- New upstream version 0.5.1. (RHBZ#1541679)
- Enable debug package.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 0.5-2
- OCaml 4.06.0 rebuild.

* Fri Nov 17 2017 Andy Li <andy@onthewings.net> - 0.5-1
- New upstream version 0.5.

* Fri Jul 07 2017 Andy Li <andy@onthewings.net> - 0.4.0.1-1
- Initial RPM release.
