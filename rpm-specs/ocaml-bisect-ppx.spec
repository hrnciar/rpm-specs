%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname bisect-ppx
%global upname  bisect_ppx

# Running the tests requires ocaml-ounit, which introduces a circular
# dependency (also involving ocaml-lwt).  By disabling the tests we
# can break this cycle.
%bcond_with tests

# Building the documentation requires ocaml-odoc, which depends transitively
# on this package.
%bcond_with odoc

Name:           ocaml-%{srcname}
Version:        2.4.1
Release:        6%{?dist}
Summary:        Code coverage for OCaml and Reason

License:        MIT
URL:            https://aantron.github.io/bisect_ppx/
Source0:        https://github.com/aantron/%{upname}/archive/%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  git-core
BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-migrate-parsetree-devel >= 1.7.0
%if %{with odoc}
BuildRequires:  ocaml-odoc
%else
BuildRequires:  ocaml-ocamldoc
%endif
%if %{with tests}
BuildRequires:  ocaml-ounit-devel
%endif
BuildRequires:  ocaml-ppx-tools-versioned-devel >= 5.4.0

%description
Bisect_ppx is a code coverage tool for OCaml.  It helps you test
thoroughly by showing which parts of your code are *not* tested.  It is
a small preprocessor that inserts instrumentation at places in your
code, such as if-then-else and match expressions.  After you run tests,
Bisect_ppx gives a nice HTML report showing which places were visited
and which were missed.

Usage is simple - add package bisect_ppx when building tests, run your
tests, then run the Bisect_ppx report tool on the generated visitation
files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-tools-versioned-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n %{upname}-%{version}

%build
dune build %{?_smp_mflags}

%if %{with odoc}
dune build %{?_smp_mflags} @doc
%else
mkdir html
ocamldoc -html -d html \
  -I _build/default/src/report/.report.eobjs/byte \
  -I +ppx_tools_versioned \
  _build/default/src/common/*.mli \
  _build/default/src/runtime/native/*.mli \
  _build/default/src/ppx/{exclude,exclusions,instrument}.mli \
  _build/default/src/report/*.mli
%endif

%install
dune install --destdir=%{buildroot}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/bisect-ppx-report --help groff > \
  %{buildroot}%{_mandir}/man1/bisect-ppx-report.1

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod 0755 {} \+
%endif

%if %{with tests}
%check
make test
%endif

%files
%doc doc/advanced.md doc/CHANGES README.md
%license LICENSE.md
%{_bindir}/bisect-ppx-report
%{_mandir}/man1/bisect-ppx-report.1*
%dir %{_libdir}/ocaml/%{upname}/
%dir %{_libdir}/ocaml/%{upname}/common/
%dir %{_libdir}/ocaml/%{upname}/runtime/
%{_libdir}/ocaml/%{upname}/META
%{_libdir}/ocaml/%{upname}/ppx.exe
%{_libdir}/ocaml/%{upname}/%{upname}.cma
%{_libdir}/ocaml/%{upname}/%{upname}*.cmi
%{_libdir}/ocaml/%{upname}/common/bisect_common.cma
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmi
%{_libdir}/ocaml/%{upname}/runtime/bisect.cma
%{_libdir}/ocaml/%{upname}/runtime/bisect*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.cmxs
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmxs
%{_libdir}/ocaml/%{upname}/runtime/bisect.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{upname}/dune-package
%{_libdir}/ocaml/%{upname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{upname}/%{upname}.a
%{_libdir}/ocaml/%{upname}/%{upname}*.cmx
%{_libdir}/ocaml/%{upname}/%{upname}.cmxa
%{_libdir}/ocaml/%{upname}/common/bisect_common.a
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmx
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmxa
%{_libdir}/ocaml/%{upname}/runtime/bisect.a
%{_libdir}/ocaml/%{upname}/runtime/bisect*.cmx
%{_libdir}/ocaml/%{upname}/runtime/bisect.cmxa
%endif
%{_libdir}/ocaml/%{upname}/%{upname}*.cmt
%{_libdir}/ocaml/%{upname}/%{upname}*.cmti
%{_libdir}/ocaml/%{upname}/*.mli
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmt
%{_libdir}/ocaml/%{upname}/common/bisect_common.cmti
%{_libdir}/ocaml/%{upname}/common/bisect_common.mli
%{_libdir}/ocaml/%{upname}/runtime/bisect*.cmt
%{_libdir}/ocaml/%{upname}/runtime/bisect*.cmti
%{_libdir}/ocaml/%{upname}/runtime/*.mli

%files doc
%if %{with odoc}
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%else
%doc html
%endif
%license LICENSE.md

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-5
- OCaml 4.11.0 rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-4
- Bump and rebuild to fix Location dependency.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.4.1-1
- New upstream release 2.4.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.3.2-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.3.2-2
- OCaml 4.11.0 pre-release attempt 2

* Sun Apr 19 2020 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- Version 2.3.2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1
- Add conditional for building documentation with odoc

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-5.20200106.b2661bf
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-4.20200106.b2661bf
- OCaml 4.10.0 final.
- Disable the tests to avoid circular dependency.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3.20200106.b2661bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-2.20200106.b2661bf
- OCaml 4.10.0+beta1 rebuild.

* Wed Jan  8 2020 Jerry James <loganjerry@gmail.com> - 1.4.1-1.20200106.b2661bf
- Initial RPM
