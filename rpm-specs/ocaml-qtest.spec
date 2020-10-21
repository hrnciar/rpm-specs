Name:           ocaml-qtest
Version:        2.11.1
Release:        1%{?dist}
Summary:        Inline (Unit) Tests for OCaml

License:        GPLv3+
URL:            https://github.com/vincent-hugot/qtest
Source0:        https://github.com/vincent-hugot/qtest/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.1
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-qcheck-devel >= 0.14
BuildRequires:  help2man


%description
qtest extracts inline unit tests written using a special syntax in
comments. Those tests are then run using the oUnit framework and the
qcheck library. The possibilities range from trivial tests -- extremely
simple to use -- to sophisticated random generation of test cases.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch


%description    doc
Documentation for %{name}.


%prep
%autosetup -n qtest-%{version}


%build
dune build @install --profile release
dune build @doc


%install
dune install --destdir="%{buildroot}" --verbose

# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete

# These files will be installed using the doc and license directives
rm -r %{buildroot}%{_prefix}/doc

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

# generate manpage
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/qtest \
    --output %{buildroot}/%{_mandir}/man1/qtest.1 \
    --name "Inline (Unit) Tests for OCaml" \
    --version-string %{version} \
    --no-info


%check
make test -W build # ignore dependency on "build" target


%files
%doc README.adoc HOWTO.adoc
%license LICENSE
%{_bindir}/qtest
%{_mandir}/man1/qtest.1*
%{_libdir}/ocaml/qtest
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/qtest/lib/*.a
%exclude %{_libdir}/ocaml/qtest/lib/*.cmxa
%exclude %{_libdir}/ocaml/qtest/lib/*.cmx
%endif

%files devel
%doc README.adoc HOWTO.adoc
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/qtest/lib/*.a
%{_libdir}/ocaml/qtest/lib/*.cmxa
%{_libdir}/ocaml/qtest/lib/*.cmx
%endif


%files doc
%doc _build/default/_doc/_html/
%doc _build/default/_doc/_mlds/
%doc _build/default/_doc/_odoc/
%license LICENSE


%changelog
* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 2.11.1-1
- Version 2.11.1

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.11-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.11-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Jerry James <loganjerry@gmail.com> - 2.11-1
- New upstream release (bz 1835054)

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-13
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-12
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-11
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-10
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 2.10.1-9
- Rebuild for ocaml-qcheck 0.13.
- Build documentation with odoc, and ship it in a new doc subpackage.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-7
- OCaml 4.10.0+beta1 rebuild.

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 2.10.1-1
- New upstream release. (RHBZ#1777145)
- Remove unneeded BuildRequires on opam-installer.

* Tue Aug 06 2019 Andy Li <andy@onthewings.net> - 2.9-6
- OCaml 4.08.1 rebuild.

* Mon Jul 29 2019 Andy Li <andy@onthewings.net> - 2.9-5
- Update build depends and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Andy Li <andy@onthewings.net> - 2.9-1
- New upstream release (RHBZ#1570332).
- Enable devel and debug packages.

* Fri Apr 06 2018 Andy Li <andy@onthewings.net> - 2.8-1
- New upstream release.
- Remove ocaml-qtest-LICENSE.patch which has been applied upstream.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Andy Li <andy@onthewings.net> - 2.7-1
- Initial RPM release.
