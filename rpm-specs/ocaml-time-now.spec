%global srcname time-now
%global upname  time_now

Name:           ocaml-%{srcname}
Version:        0.14.0
Release:        3%{?dist}
Summary:        Get the current time in OCaml

License:        MIT
URL:            https://github.com/janestreet/%{upname}
Source0:        %{url}/archive/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-jane-street-headers-devel >= 0.14
BuildRequires:  ocaml-jst-config-devel >= 0.14
BuildRequires:  ocaml-ppx-base-devel >= 0.14
BuildRequires:  ocaml-ppx-optcomp-devel >= 0.14
BuildRequires:  ocaml-odoc

%description
This package provides a single OCaml function to report the current time
in nanoseconds since the start of the Unix epoch.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-jane-street-headers-devel
Requires:       ocaml-jst-config-devel%{?_isa}
Requires:       ocaml-ppx-base-devel%{?_isa}
Requires:       ocaml-ppx-optcomp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{upname}-%{version}

%build
dune build %{?_smp_mflags} --display=verbose
dune build %{?_smp_mflags} @doc

# Relink the stublibs with $RPM_LD_FLAGS.
cd _build/default/src
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -o time_now_stubs \
  $(ar t libtime_now_stubs.a)
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
%license LICENSE.md
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/runtime.js
%{_libdir}/ocaml/%{upname}/*.cma
%{_libdir}/ocaml/%{upname}/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dlltime_now_stubs.so

%files devel
%doc _build/default/_doc/_html/*
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/*.a
%{_libdir}/ocaml/%{upname}/*.cmx
%{_libdir}/ocaml/%{upname}/*.cmxa
%endif
%{_libdir}/ocaml/%{upname}/*.cmt
%{_libdir}/ocaml/%{upname}/*.cmti
%{_libdir}/ocaml/%{upname}/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Mon Jun 22 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
