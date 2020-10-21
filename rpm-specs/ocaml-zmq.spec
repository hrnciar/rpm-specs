%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname zmq

Name:           ocaml-%{srcname}
Version:        5.1.3
Release:        8%{?dist}
Summary:        ZeroMQ bindings for OCaml

License:        MIT
URL:            https://github.com/issuu/%{name}
Source0:        %{url}/releases/download/%{version}/%{srcname}-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mmap-devel
BuildRequires:  ocaml-ocplib-endian-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-stdint-devel >= 0.4.2
BuildRequires:  pkgconfig(libzmq)

%description
This library contains basic OCaml bindings for ZeroMQ.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%package        lwt
Summary:        LWT-aware ZeroMQ bindings for OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    lwt
This library contains lwt-aware OCaml bindings for ZeroMQ.

%package        lwt-devel
Summary:        Development files for %{name}-lwt
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}

%description    lwt-devel
The %{name}-lwt-devel package contains libraries and signature
files for developing applications that use %{name}-lwt.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# We cannot build the async-aware bindings until ocaml-async-kernel and
# ocaml-async-unix have been added to Fedora.
rm -fr zmq-async*

%build
dune build %{?_smp_mflags}
dune build %{?_smp_mflags} @doc

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
%license LICENSE.md
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/deferred/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/%{srcname}.cma
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmi
%{_libdir}/ocaml/%{srcname}/deferred/*.cma
%{_libdir}/ocaml/%{srcname}/deferred/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxs
%{_libdir}/ocaml/%{srcname}/deferred/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllzmq_stubs.so

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/lib%{srcname}_stubs.a
%{_libdir}/ocaml/%{srcname}/%{srcname}.a
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmx
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxa
%{_libdir}/ocaml/%{srcname}/deferred/*.a
%{_libdir}/ocaml/%{srcname}/deferred/*.cmx
%{_libdir}/ocaml/%{srcname}/deferred/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmt
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmti
%{_libdir}/ocaml/%{srcname}/%{srcname}.mli
%{_libdir}/ocaml/%{srcname}/deferred/*.cmt
%{_libdir}/ocaml/%{srcname}/deferred/*.cmti
%{_libdir}/ocaml/%{srcname}/deferred/*.mli

%files lwt
%dir %{_libdir}/ocaml/%{srcname}-lwt/
%{_libdir}/ocaml/%{srcname}-lwt/META
%{_libdir}/ocaml/%{srcname}-lwt/*.cma
%{_libdir}/ocaml/%{srcname}-lwt/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-lwt/*.cmxs
%endif

%files lwt-devel
%{_libdir}/ocaml/%{srcname}-lwt/dune-package
%{_libdir}/ocaml/%{srcname}-lwt/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}-lwt/*.a
%{_libdir}/ocaml/%{srcname}-lwt/*.cmx
%{_libdir}/ocaml/%{srcname}-lwt/*.cmxa
%endif
%{_libdir}/ocaml/%{srcname}-lwt/*.cmt
%{_libdir}/ocaml/%{srcname}-lwt/*.cmti
%{_libdir}/ocaml/%{srcname}-lwt/*.mli

%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE.md

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-8
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-7
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-2
- Update all OCaml dependencies for RPM 4.16.

* Fri Feb  7 2020 Jerry James <loganjerry@gmail.com> - 5.1.3-1
- Initial RPM
