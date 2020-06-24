Name:           ocaml-mmap
Version:        1.1.0
Release:        10%{?dist}
Summary:        File mapping functionality

%global libname mmap

# License is LGPL 2.1 with standard OCaml exceptions
License:        LGPLv2+ with exceptions
URL:            https://github.com/mirage/mmap
Source0:        https://github.com/mirage/mmap/archive/v%{version}/mmap-v%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

BuildRequires:  ocaml-dune

%description
This project provides a Mmap.map_file functions for mapping files
in memory. This function is the same as the Unix.map_file function
added in OCaml >= 4.06.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
# It might be nice to have a %jbuilder macro that just does this.
dune build -p %{libname} %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/ocaml/%{libname}/
cp -aLr _build/install/default/lib/%{libname}/* %{buildroot}%{_libdir}/ocaml/%{libname}/

%check
dune runtest

%files
%license LICENSE
%doc README.md CHANGES.md
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%endif
%exclude %{_libdir}/ocaml/%{libname}/*.mli


%files devel
#license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%endif
%{_libdir}/ocaml/%{libname}/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-9
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-8
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-7
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-5
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-4
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-3
- OCaml 4.08.1 (final) rebuild.

* Tue Aug 06 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-2
- Switched to github tag archive with tests, license file.
- Added missing isa to devel package requirement.
- Added "dune runtest" to check section.
- Cleaned up files paths to use ocaml/libname rather than ocaml/*.

* Tue Jul 30 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial package.
