%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if ! %opt
%global debug_package %{nil}
%endif

Name:           ocaml-json-wheel
Version:        1.0.6
Release:        43%{?dist}
Summary:        OCaml library for parsing JSON
License:        BSD

URL:            http://martin.jambon.free.fr/json-wheel.html
Source0:        http://martin.jambon.free.fr/json-wheel-%{version}.tar.bz2

# Safe-string fixes for OCaml 4.06.
Patch1:         json-wheel-1.0.6-safe-string.patch

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  pcre-devel


%description
JSON library for OCaml following RFC 4627.

If you use this library, consider installing ocaml-json-static, the
syntax extension to the language which makes using JSON much easier.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n json-wheel-%{version}
%autopatch -p1


%build
# Parallel builds don't work.
unset MAKEFLAGS
make all \
%if %opt
  OCAMLOPT="ocamlopt -g" opt
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}

make BINDIR=$RPM_BUILD_ROOT%{_bindir} install


%files
%doc LICENSE
%{_libdir}/ocaml/json-wheel
%if %opt
%exclude %{_libdir}/ocaml/json-wheel/*.a
%exclude %{_libdir}/ocaml/json-wheel/*.o
%exclude %{_libdir}/ocaml/json-wheel/*.cmxa
%exclude %{_libdir}/ocaml/json-wheel/*.cmx
%{_bindir}/jsoncat
%endif
%exclude %{_libdir}/ocaml/json-wheel/*.cmo
%exclude %{_libdir}/ocaml/json-wheel/*.mli
%exclude %{_libdir}/ocaml/json-wheel/*.ml


%files devel
%doc LICENSE Changes README html
%if %opt
%{_libdir}/ocaml/json-wheel/*.a
%{_libdir}/ocaml/json-wheel/*.o
%{_libdir}/ocaml/json-wheel/*.cmxa
%{_libdir}/ocaml/json-wheel/*.cmx
%endif
%{_libdir}/ocaml/json-wheel/*.cmo
%{_libdir}/ocaml/json-wheel/*.mli
%{_libdir}/ocaml/json-wheel/*.ml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-39
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-38
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-36
- Rebuild against new ocamlnet.

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-35
- OCaml 4.06.0 rebuild.
- Safe string fixes.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-34
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-31
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-30
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-28
- Rebuild for OCaml 4.04.0.

* Wed Oct 19 2016 Dan Horák <dan[at]danny.cz> - 1.0.6-27
- disable debuginfo subpackage on interpreted builds

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-25
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-24
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-23
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-22
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-20
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-19
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-18
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-16
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-15
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-13
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.0.6-10
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-8
- Rebuild for OCaml 4.00.0.

* Sun Jan 08 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-7
- Rebuild for OCaml 3.12.1.

* Wed Sep 21 2011 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-5
- Bump for rebuilt ocamlnet.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-4
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-3
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-1
- New upstream version 1.0.6.
- Rebuild for OCaml 3.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-7
- Rebuild.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-6
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-5
- Rebuild for OCaml 3.10.2

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-4
- Remove ExcludeArch ppc64.

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-3
- Don't distribute the *.cmo and *.o files.
- Better way to install jsoncat in the right directory.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-2
- Missing BR ocaml-pcre-devel.
- Missing BR pcre-devel.

* Thu Feb 28 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-1
- Initial RPM release.
