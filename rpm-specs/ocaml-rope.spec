Name:           ocaml-rope
Version:        0.6.2
Release:        14%{?dist}
Summary:        Ropes ("heavyweight strings") for OCaml

License:        LGPLv2+ with exceptions
URL:            http://rope.forge.ocamlcore.org/
Source0:        https://github.com/Chris00/ocaml-rope/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-benchmark-devel
BuildRequires:  ocaml-dune
BuildRequires:  opam-installer

%description
Ropes ("heavyweight strings") are a scalable string implementation:
they are designed for efficient operation that involve the string as
a whole. Operations such as concatenation, and substring take time
that is nearly independent of the length of the string. Unlike
strings, ropes are a reasonable representation for very long strings
such as edit buffers or mail messages.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
dune build @install --profile release


%install
mkdir -p %{buildroot}%{_libdir}/ocaml
dune install --destdir=%{buildroot} --verbose

# These files will be installed using the doc and license directives
rm %{buildroot}%{_prefix}/doc/rope/{CHANGES.md,LICENSE.md,README.md}

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

%check
dune runtest --profile=release


%files
%doc README.md CHANGES.md
%license LICENSE.md
%{_libdir}/ocaml/rope
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/rope/*.a
%exclude %{_libdir}/ocaml/rope/*.cmxa
%exclude %{_libdir}/ocaml/rope/*.cmx
%endif
%exclude %{_libdir}/ocaml/rope/*.mli
%exclude %{_libdir}/ocaml/rope/top/*.ml


%files devel
%doc README.md CHANGES.md
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/rope/*.a
%{_libdir}/ocaml/rope/*.cmxa
%{_libdir}/ocaml/rope/*.cmx
%endif
%{_libdir}/ocaml/rope/*.mli
%{_libdir}/ocaml/rope/top/*.ml


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-14
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-13
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-9
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-8
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-7
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-5
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.2-4
- OCaml 4.10.0+beta1 rebuild.

* Tue Aug 06 2019 Andy Li <andy@onthewings.net> - 0.6.2-3
- Use "--profile release" to build.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Andy Li <andy@onthewings.net> - 0.6.2-1
- New upstream version. (RHBZ#1690671)
- Use ocaml-dune instead of jbuilder.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Andy Li <andy@onthewings.net> - 0.6.1-1
- New upstream version.
- Enable debug package.

* Fri Dec 22 2017 Andy Li <andy@onthewings.net> - 0.6-1
- Initial RPM release.
