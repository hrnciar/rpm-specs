%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname mew-vi
%global upname  mew_vi

Name:           ocaml-%{srcname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Modal Editing Witch, VI interpreter

License:        MIT
URL:            https://github.com/kandu/mew_vi
Source0:        %{url}/archive/%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 1.1.0
BuildRequires:  (ocaml-mew-devel >= 0.1.0 and ocaml-mew-devel < 0.2)
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-react-devel

%description
This is a vi-like modal editing engine generator.  Provide `Key`, `Mode`,
and `Concurrent` modules to define the real world environment to get a
handy vi-like modal editing engine.  Feed the the `i` channel user input
and get the vi actions from the `action_output` channel.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-mew-devel%{?_isa}
Requires:       ocaml-react-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    docs
Documentation for %{name}.

%prep
%autosetup -n %{upname}-%{version}

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
%dir %{_libdir}/ocaml/%{upname}/
%{_libdir}/ocaml/%{upname}/%{upname}.cma
%{_libdir}/ocaml/%{upname}/%{upname}*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.a
%{_libdir}/ocaml/%{upname}/%{upname}*.cmx
%{_libdir}/ocaml/%{upname}/%{upname}.cmxa
%endif
%{_libdir}/ocaml/%{upname}/%{upname}*.cmt

%files docs
%doc _build/default/_doc/*
%license LICENSE

%changelog
* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1.0-1
- Initial RPM
