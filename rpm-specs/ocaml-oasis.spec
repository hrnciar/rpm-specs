%global debug_package %{nil}

Name:           ocaml-oasis
Version:        0.4.11
Release:        23%{?dist}
Summary:        Tooling for building OCaml libraries and applications

License:        LGPLv2+ with exceptions
URL:            http://oasis.forge.ocamlcore.org/
Source0:        https://forge.ocamlcore.org/frs/download.php/1757/oasis-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocamlify
BuildRequires:  ocamlmod
BuildRequires:  ocaml-ocamldoc
BuildRequires:  help2man

%description
OASIS generates a full configure, build and install system for your
application. It starts with a simple _oasis file at the toplevel of
your project and creates everything required.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n oasis-%{version}


%build
ocaml setup.ml -configure \
    --destdir $RPM_BUILD_ROOT \
    --prefix %{_prefix}
ocaml setup.ml -build


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

# generate manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
help2man $RPM_BUILD_ROOT%{_bindir}/oasis \
    --output $RPM_BUILD_ROOT%{_mandir}/man1/oasis.1 \
    --name "Tooling for building OCaml libraries and applications" \
    --version-string %{version} \
    --no-info

%check
ocaml setup.ml -test


%files
%doc README.md CHANGES.txt
%license COPYING.txt
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_mandir}/man1/*


%files devel
%doc README.md CHANGES.txt
%license COPYING.txt
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-23
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-22
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-20
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-19
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-18
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-17
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-15
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-14
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-13
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-12
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-11
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-9
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-8
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-4
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-3
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.4.11-2
- OCaml 4.07.0-rc1 rebuild.

* Thu Apr 05 2018 Andy Li <andy@onthewings.net> - 0.4.11-1
- New upstream release. (#1563675)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.4.10-3
- Rebuild against new ocamlbuild.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 0.4.10-2
- OCaml 4.06.0 rebuild.

* Wed Nov 15 2017 Andy Li <andy@onthewings.net> - 0.4.10-1
- Initial RPM release.
