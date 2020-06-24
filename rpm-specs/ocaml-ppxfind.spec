%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname ppxfind

Name:           ocaml-%{srcname}
Version:        1.4
Release:        7%{?dist}
Summary:        Tool to apply OCaml ppx rewriters to a file

License:        BSD
URL:            https://github.com/diml/%{srcname}
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-migrate-parsetree-devel

%description
Ppxfind is a small command line tool that enables the application of ppx
rewriters to a file.  It supports both new style ppx rewriters
(driverized) and old style rewriters.

At the moment new style ppx rewriters are executed in byte-code mode as
Ppxfind relies on dynamic loading and the packaging of a lot of ppx
rewriters is incomplete, i.e. the cmxs files are missing.

%prep
%autosetup -n %{srcname}-%{version} -p0

# Use native compilation when available
%ifarch %{ocaml_native_compiler}
sed -i 's/byte/native/' src/dune
%endif

%build
dune build %{?_smp_mflags}
dune build @install

# Make a man page
cd _build/install/default/bin
help2man -N --version-string=%{version} -o ../../../../ppxfind.1 ./ppxfind
cd -

%install
dune install --destdir=%{buildroot}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p ppxfind.1 %{buildroot}%{_mandir}/man1

%files
%doc CHANGES.md README.md
%license LICENSE.md
%{_bindir}/%{srcname}
%{_libdir}/ocaml/%{srcname}/
%{_mandir}/man1/%{srcname}.1*

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4-6
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 1.4-5
- Rebuild for ocaml-migrate-parsetree 1.7
- Drop unneeded ppxfind-migrate-parsetree15 patch

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4-4
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 10 2020 Jerry James <loganjerry@gmail.com> - 1.4-3
- Restore compatibility with ocaml-migrate-parsetree 1.5

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 1.4-2
- OCaml 4.10.0 final

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 1.4-1
- Version 1.4

* Wed Feb  5 2020 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
