%global extraver 11

Name:           ocaml-mccs
Version:        1.1
Release:        30.%{extraver}%{?dist}
Summary:        Multi Criteria CUDF Solver with OCaml bindings

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# Original C/C++ code is BSD, OCaml bindings are LGPL.
# Linking exception, see included COPYING file.
License:        BSD and LGPLv3+ with exceptions

URL:            https://github.com/AltGr/ocaml-mccs

# Upstream's use of a '+' instead of a '.' makes this hard to use a macro.
Source0:        https://github.com/AltGr/ocaml-mccs/archive/%{version}+%{extraver}/%{name}-%{version}-%{extraver}.tar.gz

# Hacky workaround for:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/M2VM5DNB7HSAJIFDGT4WAIZDA5JPE5KM/
Patch1:         ocaml-mccs-1.1-c++-flags.patch
Patch2:         ocaml-mccs-gcc11.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  gcc, gcc-c++
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  glpk-devel

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem
solver developed at UNS during the European MANCOOSI project.

This project contains a stripped-down version of the mccs solver,
taken from snapshot 1.1, with a binding as an OCaml library, and
building with dune.

The binding enables interoperation with binary CUDF data from the
OCaml CUDF library, and removes the native C++ parsers and printers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}-%{extraver} -p1

%build
dune build -p mccs

%install
# This is an opam dependency. Tragically it means we must manually install,
# since the dune install command only works with opam-installer.
mkdir -p %{buildroot}%{_libdir}/ocaml
cp -aLr _build/install/default/lib/* %{buildroot}%{_libdir}/ocaml/

%files
%license LICENCE
%doc README.md
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.cmxa
%endif
%exclude %{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/stublibs/*.so

%files devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-30.11
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-29.11
- OCaml 4.11.0 rebuild

* Wed Jul 29 2020 Jeff Law <law@redha.com> - 1.1-27.12
- Make comparison object be invocable as const

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-26.11
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-25.11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-24.11
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-23.11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-22.11
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-21.11
- New version 1.1+11.
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-19.10
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-18.10
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-17.10
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1-15.10
- Updated to latest upstream release (rhbz#1724723).

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-14.8
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-13.8
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-10.8
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-9.8
- OCaml 4.07.0-rc1 rebuild.

* Wed Jun 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-8.8
- Updated to latest upstream release (rhbz#1584456).

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-7.7
- Update to latest upstream release (rhbz#1577188).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-5.5
- Updated to latest upstream release (#1512145).

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-4.4
- OCaml 4.06.0 rebuild.

* Sat Nov 25 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.3-4
- Update to latest upstream release (#1512145).

* Sun Oct 22 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-2.3b
- Update to latest upstream release.

* Sat Sep 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-1.2c
- Initial package.
