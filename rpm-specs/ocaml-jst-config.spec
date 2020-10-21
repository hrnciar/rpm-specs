# This package contains generated C header files.  They differ by architecture,
# so this package cannot be noarch, but there are no ELF objects in it.
%global debug_package %{nil}

%global srcname jst-config

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        3%{?dist}
Summary:        Compile-time configuration for Jane Street libraries

License:        MIT
URL:            https://github.com/janestreet/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14.0
BuildRequires:  ocaml-dune-devel >= 2.0.0
BuildRequires:  ocaml-ppx-assert-devel >= 0.14.0
BuildRequires:  ocaml-stdio-devel >= 0.14.0

%description
This package defines compile-time constants used in Jane Street libraries
such as Base, Core, and Async.

%package        devel
Summary:        Development files for %{name}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-assert-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

%description    devel
This package defines compile-time constants used in Jane Street libraries
such as Base, Core, and Async.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build %{?_smp_mflags} --display=verbose

%install
dune install --destdir=%{buildroot}

# The generated config_h.ml file is empty, and so the rest of the compiled OCaml
# artifacts likewise contain nothing useful.  No consumers need them either, so
# we remove them.
rm -f %{buildroot}%{_libdir}/ocaml/%{srcname}/*.{a,cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{_libdir}/ocaml/%{srcname}/{dune-package,META}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%check
dune runtest

%files devel
%license LICENSE.md
%{_libdir}/ocaml/%{srcname}/

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
