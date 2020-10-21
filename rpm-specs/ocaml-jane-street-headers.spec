%global srcname jane-street-headers

# This package creates no ELF files, but cannot be noarch since the install
# location is under _libdir.
%global debug_package %{nil}

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        3%{?dist}
Summary:        Jane Street header files

License:        MIT
URL:            https://github.com/janestreet/jane-street-headers
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-dune >= 2.0.0

%description
This package contains C header files shared between various Jane Street
packages.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package contains C header files shared between various Jane Street
packages.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build %{?_smp_mflags}

%install
dune install --destdir=%{buildroot}

# The generated jane_street_headers.ml file is empty, and so the rest of the
# compiled OCaml artifacts likewise contain nothing useful.  No consumers need
# them either; we remove them.
rm -f %{buildroot}%{_libdir}/ocaml/%{srcname}/*.{cma,cmi,cmt,cmx,cmxa,cmxs,ml}

# Removing those artifacts means we also need to remove references to them
sed -ri '/(archive|plugin)/d' \
        %{buildroot}%{_libdir}/ocaml/%{srcname}/{dune-package,META}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%files devel
%doc README.org
%license LICENSE.md
%{_libdir}/ocaml/%{srcname}/

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Thu Jun 18 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
