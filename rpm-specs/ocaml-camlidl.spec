%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

%global shortversion 109

Name:           ocaml-camlidl
Version:        1.09
Release:        4%{?dist}
Summary:        Stub code generator and COM binding for Objective Caml
License:        QPL and LGPLv2 with exceptions

URL:            http://caml.inria.fr/pub/old_caml_site/camlidl/
Source0:        https://github.com/xavierleroy/camlidl/archive/camlidl%{shortversion}.tar.gz
# This is the latest prebuilt documentation available.
# Actually building the documentation requires many TeX tools.
Source1:        http://caml.inria.fr/pub/old_caml_site/distrib/bazar-ocaml/camlidl-1.05.doc.pdf
# META file from Debian (RHBZ#1026991).
Source2:        META.camlidl.in

# Both patches sent upstream on 2020-05-20.
# Allow destdir installs.
Patch1:         0001-Allow-destdir-installs.patch
# Pass -g option to ocamlmklib.
Patch2:         0002-Pass-g-option-to-ocamlmklib.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-interpreter


%description
CamlIDL is a stub code generator and COM binding for Objective Caml.

CamlIDL comprises two parts:

* A stub code generator that generates the C stub code required for
  the Caml/C interface, based on an MIDL specification. (MIDL stands
  for Microsoft's Interface Description Language; it looks like C
  header files with some extra annotations, plus a notion of object
  interfaces that look like C++ classes without inheritance.)

* A (currently small) library of functions and tools to import COM
  components in Caml applications, and export Caml code as COM
  components.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n camlidl-camlidl%{shortversion} -p1

sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%{_libdir}/ocaml|' \
    -e 's|^BINDIR=.*|BINDIR=%{_bindir}|' \
    -e 's|^CFLAGS=.*|CFLAGS=%{optflags}|' \
%if %opt
    -e 's|^OCAMLC=.*|OCAMLC=ocamlc.opt -g|' \
    -e 's|^OCAMLOPT=.*|OCAMLOPT=ocamlopt.opt -g|' \
%endif
    < config/Makefile.unix \
    > config/Makefile

cp %{SOURCE1} .


%build
# Parallel builds will fail.
make


%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/caml
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/stublibs
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

# Install META file (RHBZ#1026991).
sed 's/@VERSION@/%{version}/' < %{SOURCE2} > $RPM_BUILD_ROOT/%{_libdir}/ocaml/META.camlidl

make DESTDIR=$RPM_BUILD_ROOT install


%files
%doc LICENSE
%{_libdir}/ocaml/*.*
%if %opt
%exclude %{_libdir}/ocaml/*.a
%exclude %{_libdir}/ocaml/*.cmxa
%endif
%{_libdir}/ocaml/stublibs/*.so
%{_bindir}/camlidl


%files devel
%doc LICENSE README Changes camlidl-1.05.doc.pdf tests
%if %opt
%{_libdir}/ocaml/*.a
%{_libdir}/ocaml/*.cmxa
%endif
%{_libdir}/ocaml/caml/*.h


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.09-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.09-3
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.09-1
- New upstream version 1.09.
- https://github.com/xavierleroy/camlidl/issues/18

* Wed May 20 2020 Richard W.M. Jones <rjones@redhat.com> - 1.08-1
- New upstream version 1.08.

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-64
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-63
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-62
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-61
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-60
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-58
- Bump release and rebuild.

* Sat Jan 18 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-57
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.05-56
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.05-55
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.05-54
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.05-53
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.05-51
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.05-50
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.05-47
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1.05-46
- OCaml 4.07.0-rc1 rebuild.

* Thu Apr 26 2018 Richard W.M. Jones <rjones@redhat.com> - 1.05-45
- OCaml 4.07.0-beta2 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.05-43
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.05-42
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.05-39
- OCaml 4.04.2 rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 1.05-38
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.05-36
- Rebuild for OCaml 4.04.0.

* Tue Sep 27 2016 Dan Horák <dan[at]danny.cz> - 1.05-35
- disable debuginfo subpackage on interpreted builds

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-33
- OCaml 4.02.3 rebuild.

* Mon Jul 20 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-32
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-31
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-30
- ocaml-4.02.2 rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-29
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-28
- ocaml-4.02.0 final rebuild.

* Fri Aug 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-27
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-25
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 1.05-24
- Rebuild for OCaml 4.02.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov  5 2013 Richard W.M. Jones <rjones@redhat.com> - 1.05-22
- Add META file (RHBZ#1026991).

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.05-21
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 1.05-17
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 8 2012 Orion Poplawski <orion@cora.nwra.com> - 1.05-15
- Rebuild for OCaml 4.00.0.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 1.05-14
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Orion Poplawski <orion@cora.nwra.com> - 1.05-12
- Rebuild for OCaml 3.12

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.05-11
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.05-9
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-7
- Rebuild for OCaml 3.11.0 release.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-6
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-5
- Rebuild for OCaml 3.10.2.

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-4
- Added tests subdirectory to the documentation.

* Wed Mar  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-3
- Removed -doc subpackage and placed documentation in -devel.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-2
- Rebuild for ppc64.

* Wed Feb 20 2008 Richard W.M. Jones <rjones@redhat.com> - 1.05-1
- Initial RPM release.
