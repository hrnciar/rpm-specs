%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global libname yojson

Name:           ocaml-%{libname}
Version:        1.7.0
Release:        10%{?dist}
Summary:        An optimized parsing and printing library for the JSON format

License:        BSD
URL:            https://github.com/ocaml-community/%{libname}
Source0:        %{url}/releases/download/%{version}/%{libname}-%{version}.tbz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-dune

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n %{libname}-%{version}


%build
dune build


%install
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml

cp -L _build/install/default/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -rL _build/install/default/lib/* $RPM_BUILD_ROOT%{_libdir}/ocaml

# We do not want the source code
rm -f $RPM_BUILD_ROOT/%{_libdir}/ocaml/yojson/*.ml


# Testing requires ocaml-alcotest, which we do not have in Fedora.
# See https://github.com/mirage/alcotest.
#%%check
#dune runtest


%files
%doc README.md
%license LICENSE.md
%{_libdir}/ocaml/%{libname}/
%ifarch %{ocaml_native_compiler}
%{_bindir}/ydump
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%endif
%exclude %{_libdir}/ocaml/%{libname}/*.mli


%files devel
%doc Changes CHANGES.md examples
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.cmxa
%endif
%{_libdir}/ocaml/%{libname}/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-9
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-8
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-7
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-5
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- OCaml 4.09.0 (final) rebuild.

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-3
- Rebuild for ocaml-easy-format 1.3.2 and ocaml-biniou 1.2.1

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-2
- Rebuild for ocaml-easy-format 1.3.1

* Tue Jul 30 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-1
- New upstream version 1.7.0 (bz 1446344)
- BR ocaml-dune instead of jbuilder
- Use the %%license macro
- Comment out %%check until alcotest is available

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-9
- Bump release and rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-8
- Bump release and rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-7
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-1
- New upstream version 1.4.0.
- Remove opt macro.
- Enable debuginfo everywhere.
- OCaml 4.06.0 rebuild.
- Enable SMP builds.
- New upstream URL.
- Remove test files and use upstream tests.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-24
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-21
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-20
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.1.8-18
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-17
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-15
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-14
- Fix bytecode build.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-13
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-12
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-10
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-9
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-8
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-6
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 28 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-5
- Rebuild for OCaml 4.02.0 beta.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jaromir Capik <jcapik@redhat.com> - 1.1.8-3
- Removing ExclusiveArch

* Sat Feb  8 2014 Michel Salim <salimma@fedoraproject.org> - 1.1.8-2
- Incorporate review feedback

* Mon Jan 20 2014 Michel Salim <salimma@fedoraproject.org> - 1.1.8-1
- Initial package
