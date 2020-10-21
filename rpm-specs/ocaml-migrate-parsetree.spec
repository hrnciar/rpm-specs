Name:           ocaml-migrate-parsetree
Version:        1.7.3
Release:        2%{?dist}
Summary:        Convert OCaml parsetrees between different major versions

License:        LGPLv2+ with exceptions
URL:            https://github.com/ocaml-ppx/ocaml-migrate-parsetree
Source0:        https://github.com/ocaml-ppx/ocaml-migrate-parsetree/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-ppx-derivers-devel

%description
This library converts between parsetrees of different OCaml versions.
For each version, there is a snapshot of the parsetree and conversion
functions to the next and/or previous version.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build
%make_build


%install
mkdir -p %{buildroot}%{_libdir}/ocaml
%make_install INSTALL_ARGS='--destdir=%{buildroot}'

# These files will be installed using doc and license directives.
rm -r %{buildroot}/usr/doc

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

%check
%make_build test


%files
%doc README.md MANUAL.md CHANGES.md
%license LICENSE.md
%{_libdir}/ocaml/*
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/{,*/}*.a
%exclude %{_libdir}/ocaml/*/{,*/}*.cmxa
%exclude %{_libdir}/ocaml/*/{,*/}*.cmx
%endif
%exclude %{_libdir}/ocaml/*/{,*/}*.ml
%exclude %{_libdir}/ocaml/*/{,*/}*.mli


%files devel
%doc README.md MANUAL.md CHANGES.md
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/{,*/}*.a
%{_libdir}/ocaml/*/{,*/}*.cmxa
%{_libdir}/ocaml/*/{,*/}*.cmx
%endif
%{_libdir}/ocaml/*/{,*/}*.ml
%{_libdir}/ocaml/*/{,*/}*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-2
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-1
- Upgrade to 1.7.3 (but not 2.0.0) because of:
  https://github.com/ocaml-ppx/ocaml-migrate-parsetree/pull/96
- OCaml 4.11.0 rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-7
- Bump and rebuild to fix dependencies.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-4
- Rebuild to resolve build order symbol problems.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 1.7.1-1
- Version 1.7.1

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-3
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-2
- OCaml 4.10.0+beta1 rebuild.

* Mon Dec 23 2019 Andy Li <andy@onthewings.net> - 1.5.0-1
- New upstream release (RHBZ#1772588).
- Remove unneeded BuildRequires on opam-installer.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-2
- OCaml 4.08.1 (rc2) rebuild.

* Mon Jul 29 2019 Andy Li <andy@onthewings.net> - 1.4.0-1
- New upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Andy Li <andy@onthewings.net> - 1.3.1-1
- New upstream release (RHBZ#1707889).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Andy Li <andy@onthewings.net> - 1.1.0-1
- New upstream release.

* Wed Aug 01 2018 Andy Li <andy@onthewings.net> - 1.0.11-1
- New upstream release (RHBZ#1588241).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Andy Li <andy@onthewings.net> - 1.0.10-1
- New upstream release (RHBZ#1564343).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Andy Li <andy@onthewings.net> - 1.0.7-1
- Initial RPM release.
