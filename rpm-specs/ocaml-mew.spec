%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname mew

Name:           ocaml-%{srcname}
Version:        0.1.0
Release:        5%{?dist}
Summary:        Modal Editing Witch

License:        MIT
URL:            https://github.com/kandu/mew
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 1.1.0
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-trie-devel

%description
This is the core module of mew, a general modal editing engine generator.
You can provide `Key`, `Mode`, and `Concurrent` modules to define the
real world environment to get the core component of a modal editing
engine.  The core component supports recursive key mappings associated
with user provided modes.  After the core component is generated, you may
extended it with a translator to interpret user key sequences to get a
complete modal editing engine.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-trie-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

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

# The tests cannot be run, since Fedora does not yet have ppx_expect.
#
#%%check
#dune runtest

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{_libdir}/ocaml/%{srcname}/
%{_libdir}/ocaml/%{srcname}/%{srcname}.cma
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxs
%endif

%files devel
%doc _build/default/_doc/*
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/%{srcname}.a
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmx
%{_libdir}/ocaml/%{srcname}/%{srcname}.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/%{srcname}*.cmt

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
