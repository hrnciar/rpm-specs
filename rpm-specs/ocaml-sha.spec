Name:           ocaml-sha
Version:        1.13
Release:        4%{?dist}
Summary:        Binding to the SHA cryptographic functions

License:        ISC
URL:            https://github.com/djs55/ocaml-sha/
Source0:        https://github.com/djs55/ocaml-sha/archive/v%{version}/%{name}-%{version}.tar.gz

# Move to ounit2.
Patch1:         ocaml-sha-1.12-ounit2.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  opam-installer
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit-devel

%description
A binding for SHA interface code in OCaml. Offering the same interface than
the MD5 digest included in the OCaml standard library.
It's currently providing SHA1, SHA256 and SHA512 hash functions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
dune build @install --profile release


%install
mkdir -p %{buildroot}%{_libdir}/ocaml
dune install --destdir=%{buildroot}

# These files will be installed using doc and license directives.
rm -r %{buildroot}%{_prefix}/doc

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest --profile release


%files
%doc README.md CHANGES.md
%license LICENSE.md
%{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli


%files devel
%doc README.md CHANGES.md
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.13-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.13-3
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Andy Li <andy@onthewings.net> - 1.13-1
- New upstream version. (RHBZ#1818607) (RHBZ#1799819)
- Remove patches integrated in 1.13.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-13
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-12
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-10
- OCaml 4.10.0 final.
- Include all upstream patches since 1.12 was released.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 1.12-7
- Rebuild against latest ocaml package.

* Fri Nov 01 2019 Andy Li <andy@onthewings.net> - 1.12-6
- Rebuild against latest ocaml package.

* Sat Jul 27 2019 Andy Li <andy@onthewings.net> - 1.12-5
- Update build system and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Andy Li <andy@onthewings.net> - 1.12-1
- Initial RPM release.
