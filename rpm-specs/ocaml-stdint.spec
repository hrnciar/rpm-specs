%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname stdint

Name:           ocaml-%{srcname}
Version:        0.6.0
Release:        5%{?dist}
Summary:        Various signed and unsigned integers for OCaml

License:        MIT
URL:            https://github.com/andrenth/%{name}
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  ocaml >= 4.07
BuildRequires:  ocaml-dune >= 1.11
BuildRequires:  ocaml-odoc

%description
The stdint library provides signed and unsigned integer types of various
fixed widths: 8, 16, 24, 32, 40, 48, 56, 64 and 128 bits.

This interface is similar to Int32 and Int64 from the base library but
provides more functions and constants like arithmetic and bit-wise
operations, constants like maximum and minimum values, infix operators
converting to and from every other integer type (including int, float and
nativeint), parsing from and conversion to readable strings (binary,
octal, decimal, hexadecimal), and conversion to and from buffers in both
big endian and little endian byte order.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build %{?_smp_mflags}
dune build %{?_smp_mflags} @doc

# Relink the stublib with RPM_LD_FLAGS
cd _build/default/lib
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -o stdint_stubs $(ar t libstdint_stubs.a)
cd -

%install
dune install --destdir=%{buildroot}

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

%check
dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllstdint_stubs.so

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.a
%{_libdir}/ocaml/%{srcname}/*.cmx
%{_libdir}/ocaml/%{srcname}/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/*.cmt
%{_libdir}/ocaml/%{srcname}/*.cmti
%{_libdir}/ocaml/%{srcname}/*.mli
%{_libdir}/ocaml/%{srcname}/*.h

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-2
- OCaml 4.10.0 final

* Thu Feb  6 2020 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- Initial RPM
