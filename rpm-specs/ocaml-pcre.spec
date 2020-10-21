Name:           ocaml-pcre
Version:        7.2.3
Release:        32%{?dist}
Summary:        Perl compatibility regular expressions (PCRE) for OCaml

License:        LGPLv2
URL:            https://github.com/mmottl/pcre-ocaml/
Source0:        https://github.com/mmottl/pcre-ocaml/releases/download/v%{version}/pcre-ocaml-%{version}.tar.gz

BuildRequires:  ocaml >= 3.12.1-3
BuildRequires:  ocaml-findlib-devel
BuildRequires:  pcre-devel
BuildRequires:  gawk
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlbuild


%description
Perl compatibility regular expressions (PCRE) for OCaml.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
# This isn't quite right - we need to specify same architecture of pcre-devel
Requires:       pcre-devel


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pcre-ocaml-%{version}
./configure \
  --prefix %{_prefix} \
  --docdir %{_docdir} \
  --destdir $RPM_BUILD_ROOT


%build
make all


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Installs API docs in %{_docdir}/api.  Install this using %doc instead.
mv $RPM_BUILD_ROOT%{_docdir}/api .


%files
%doc COPYING.txt
%{_libdir}/ocaml/pcre
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/pcre/*.a
%exclude %{_libdir}/ocaml/pcre/*.cmxa
%endif
%exclude %{_libdir}/ocaml/pcre/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING.txt README.md api
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/pcre/*.a
%{_libdir}/ocaml/pcre/*.cmxa
%endif
%{_libdir}/ocaml/pcre/*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-32
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-31
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-29
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-28
- Bump release and rebuild.

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-27
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-26
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-25
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-24
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-22
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-21
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-20
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-19
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-18
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-16
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-15
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-12
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-9
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-5
- OCaml 4.04.2 rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-4
- Rebuild for OCaml 4.04.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 7.2.3-2
- rebuild for s390x codegen bug

* Fri Nov 04 2016 Richard W.M. Jones <rjones@redhat.com> - 7.2.3-1
- New upstream version 7.2.3.
- Add missing dependency on ocamlbuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.5-2
- OCaml 4.02.3 rebuild.

* Mon Jul 20 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.5-1
- New upstream version 7.1.5.
- Fix bytecode-only build.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-8
- Bump release and rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-7
- ocaml-4.02.2 rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-6
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-5
- ocaml-4.02.0 final rebuild.

* Fri Aug 22 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-4
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-2
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Thu Jul 17 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.1-1
- New upstream version 7.1.1.
- New upstream URL.
- Rebuild for OCaml 4.02.0 beta.
- Some spec file modernization.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 7.0.2-5
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Richard W.M. Jones <rjones@redhat.com> - 7.0.2-2
- New upstream version 7.0.2.
- Rebuild for OCaml 4.00.1.
- Fix homepage and source.
- Clean up the spec file.
- Add dependency on ocamldoc.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 6.2.5-3
- Rebuild for OCaml 4.00.0.

* Sat Apr 28 2012 Richard W.M. Jones <rjones@redhat.com> - 6.2.5-2
- Bump and rebuild against new OCaml compiler in ARM.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 6.2.5-1
- New upstream version 6.2.5.
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 6.1.1-1
- New upstream version 6.1.1.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 6.0.1-2
- Rebuild for OCaml 3.11.2.

* Sun Oct  4 2009 Richard W.M. Jones <rjones@redhat.com> - 6.0.1-1
- New upstream version 6.0.1.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-3
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-2
- Rebuild for OCaml 3.11.0

* Sun Aug 31 2008 Richard W.M. Jones <rjones@redhat.com> - 5.15.0-1
- New upstream release 5.15.0.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 5.14.0-2
- Rebuild for OCaml 3.10.2

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 5.14.0-1
- New upstream release 5.14.0.
- -devel subpackage should depend on pcre-devel.
- Fixed upstream URL.
- Changed to use .bz2 package.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 5.13.0-2
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 5.13.0-1
- New upstream version 5.13.0.
- Rebuild for OCaml 3.10.1.

* Tue Sep 18 2007 Richard W.M. Jones <rjones@redhat.com> - 5.12.2-1
- New upstream version 5.12.2.
- Clarified license is LGPLv2.
- Strip .so file.

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-9
- Force rebuild because of updated requires/provides scripts in OCaml.

* Mon Sep  3 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-8
- Force rebuild because of base OCaml.

* Thu Aug 30 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-7
- Force rebuild because of changed BRs in base OCaml.

* Wed Aug  1 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-6
- ExcludeArch ppc64

* Mon Jun 11 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-5
- Updated to latest packaging guidelines.

* Sat Jun  2 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-4
- Handle bytecode-only architectures.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-3
- Put the stubs in stublibs subdirectory.

* Fri May 25 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-2
- Use ocaml find-requires, find-provides

* Sat May 19 2007 Richard W.M. Jones <rjones@redhat.com> - 5.11.4-1
- Initial RPM release.
