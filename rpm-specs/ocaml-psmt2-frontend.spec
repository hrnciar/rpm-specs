%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname psmt2-frontend

Name:           ocaml-%{srcname}
Version:        0.1
Release:        1%{?dist}
Summary:        Parser and typechecker for an extension of SMT-LIB 2

License:        ASL 2.0
URL:            https://github.com/OCamlPro-Coquera/psmt2-frontend
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-menhir-devel

%description
This package contains a library to parse and typecheck a conservative
extension of the SMT-LIB 2 standard with prenex polymorphism.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# Fix the install directory
sed -i 's/^\(LIBDIR=\).*/\1@libdir@/' Makefile.in

# Generate the configure script
autoconf -f

%build
%configure --libdir=%{_libdir}/ocaml
%make_build

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
make install LIBDIR=%{buildroot}%{_libdir}/ocaml
cp -p opam %{buildroot}%{_libdir}/ocaml/%{srcname}

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/*.a
%{_libdir}/ocaml/%{srcname}/*.cmx
%{_libdir}/ocaml/%{srcname}/*.cmxa
%{_libdir}/ocaml/%{srcname}/*.o
%{_libdir}/ocaml/%{srcname}/*.cmo
%endif
%{_libdir}/ocaml/%{srcname}/*.cmt
%{_libdir}/ocaml/%{srcname}/*.mli

%changelog
* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1-1
- Initial RPM
