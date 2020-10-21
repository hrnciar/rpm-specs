Name:           ocaml-ppx-tools-versioned
Version:        5.4.0
Release:        7%{?dist}
Summary:        Tools for authors of ppx rewriters

License:        MIT
URL:            https://github.com/ocaml-ppx/ppx_tools_versioned
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-migrate-parsetree-devel >= 1.7.0
BuildRequires:  ocaml-dune >= 2.6.2-2

%description
A variant of ppx_tools based on ocaml-migrate-parsetree.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-migrate-parsetree-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n ppx_tools_versioned-%{version}


%build
dune build @install --profile=release --verbose


%install
dune install --destdir="%{buildroot}" --verbose

# These files will be installed using doc and license directives.
rm -r %{buildroot}%{_prefix}/doc/ppx_tools_versioned/{LICENSE,README.md}

# Makes *.cmxs and ppx_metaquot_* executable such that they will be stripped.
find $OCAMLFIND_DESTDIR -name '*.cmxs' -exec chmod 0755 {} \;
find $OCAMLFIND_DESTDIR -regextype sed -regex '.*/ppx_metaquot_[0-9]*' -exec chmod 0755 {} \;

%files
%doc README.md
%license LICENSE
%{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif


%files devel
%doc README.md
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 5.4.0-7
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.4.0-6
- OCaml 4.11.0 rebuild

* Tue Aug 04 2020 Richard W.M. Jones <rjones@redhat.com> - 5.4.0-5
- Enable debuginfo generation now dune is fixed.

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 5.4.0-4
- Bump and rebuild to fix Location/Longident dependency.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 5.4.0-1
- New upstream release 5.4.0

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 5.3.0-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.3.0-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr  9 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 5.3.0-1
- New upstream release 5.3.0

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.3-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.3-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.3-3
- OCaml 4.10.0+beta1 rebuild.

* Sat Dec 28 2019 Andy Li <andy@onthewings.net> - 5.2.3-2
- Rebuilt for the latest OCaml.
- Remove unneeded BuildRequires on opam-installer.

* Wed Aug 21 2019 Richard W.M. Jones <rjones@redhat.com> - 5.2.3-1
- New upstream version 5.2.3.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 5.2.2-4
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 5.2.2-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Andy Li <andy@onthewings.net> - 5.2.2-1
- New upstream release.
- Update BuildRequires and build commands for dune.

* Wed Feb 06 2019 Richard W.M. Jones <rjones@redhat.com> - 5.2-3
- Bump release and rebuild against latest ocaml-migrate-parsetree.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Andy Li <andy@onthewings.net> - 5.2-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Andy Li <andy@onthewings.net> - 5.1-1
- New upstream release.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Andy Li <andy@onthewings.net> - 5.0.1-1
- Initial RPM release.
