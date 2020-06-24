Name:           ocaml-ocplib-endian
Version:        1.0
Release:        10%{?dist}
Summary:        Functions to read/write int16/32/64 from strings, bigarrays

%global libname ocplib-endian

# License is LGPL 2.1 with standard OCaml exceptions
License:        LGPLv2+ with exceptions
URL:            https://github.com/OCamlPro/ocplib-endian
Source0:        https://github.com/OCamlPro/ocplib-endian/archive/%{version}/ocplib-endian-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-cppo

BuildRequires:  ocaml-ocamlbuild-devel
BuildRequires:  ocaml-ocamldoc

%description
Optimised functions to read and write int16/32/64 from strings,
bytes and bigarrays, based on primitives added in version 4.01.

The library implements three modules:

EndianString works directly on strings, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBytes works directly on bytes, and provides submodules
BigEndian and LittleEndian, with their unsafe counter-parts;
EndianBigstring works on bigstrings (Bigarrays of chars),
and provides submodules BigEndian and LittleEndian, with their
unsafe counter-parts;

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
ocaml setup.ml -configure --enable-tests
%make_build build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install DESTDIR=%{buildroot}

%check
# Tests seem to fail on s390x (maybe all big endian architectures).
# See https://github.com/OCamlPro/ocplib-endian/issues/20
%ifnarch s390x
make test
%endif

%files
%license COPYING.txt
%doc README.md CHANGES.md
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%endif
%exclude %{_libdir}/ocaml/%{libname}/*.mli


%files devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%endif
%{_libdir}/ocaml/%{libname}/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0-9
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0-8
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0-7
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0-5
- OCaml 4.10.0+beta1 rebuild.

* Sun Jan 12 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0-4
- OCaml 4.09.0 (final) rebuild.

* Mon Oct 14 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0-3
- Disable tests on s390x for now.

* Mon Oct 14 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0-2
- Fix devel package Requires; switch to make_build macro.

* Mon Oct 14 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0-1
- Initial package.
