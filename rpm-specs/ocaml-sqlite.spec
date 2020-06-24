%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if !%{opt}
%global debug_package %{nil}
%endif

# 4.1.3 is the last version before jbuilder.  Although we have
# jbuilder we lack some other OCaml libraries needed for this
# package.

Name:           ocaml-sqlite
Version:        4.1.3
Release:        12%{?dist}
Summary:        OCaml library for accessing SQLite3 databases
License:        BSD

URL:            https://github.com/mmottl/sqlite3-ocaml
Source0:        https://github.com/mmottl/sqlite3-ocaml/archive/v4.1.3.tar.gz

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  sqlite-devel >= 3


%description
SQLite 3 database library wrapper for OCaml.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel%{?_isa} >= 3


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n sqlite3-ocaml-%{version}


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --docdir=%{_pkgdocdir} \
  --destdir $RPM_BUILD_ROOT
make all


%check
%if %opt
./configure --prefix=%{_prefix} --libdir=%{_libdir} --docdir=%{_pkgdocdir} \
  --destdir $RPM_BUILD_ROOT --enable-tests
make test
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Remove the documentation from _docdir, we will install it ourselves.
rm -rf $RPM_BUILD_ROOT%{_docdir}


%files
%doc COPYING.txt
%{_libdir}/ocaml/sqlite3
%if %opt
%exclude %{_libdir}/ocaml/sqlite3/*.a
%exclude %{_libdir}/ocaml/sqlite3/*.cmxa
%exclude %{_libdir}/ocaml/sqlite3/*.cmx
%endif
%exclude %{_libdir}/ocaml/sqlite3/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc CHANGES.txt README.md TODO.md
%if %opt
%{_libdir}/ocaml/sqlite3/*.a
%{_libdir}/ocaml/sqlite3/*.cmxa
%{_libdir}/ocaml/sqlite3/*.cmx
%endif
%{_libdir}/ocaml/sqlite3/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-12
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-11
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-10
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-8
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-6
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-5
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-4
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-3
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-2
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-1
- New upstream version 4.1.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-9
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-5
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 4.0.6-2
- rebuild for s390x codegen bug

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 4.0.6-1
- New upstream version 4.0.6.
- Explicit dependency on ocamlbuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-6
- Bump and rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-5
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-2
- New upstream version 2.0.9.
- Disable the tests for bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-8
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-7
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-6
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-5
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-4
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-2
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-1
- New upstream version 2.0.6.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- New upstream version 2.0.5
- Enable debuginfo for non-bytecode builds only
- BR ocaml-findlib instead of ocaml-findlib-devel
- Drop chrpath BR, no longer needed

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-3
- Remove ocaml_arches macro (RHBZ#1087794).

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-2
- Remove 'Group' line.

* Tue Sep 17 2013 Jerry James <loganjerry@gmail.com> - 2.0.4-1
- New upstream release
- Build for OCaml 4.01.0
- Enable debuginfo
- Modernize spec file
- Drop all patches, none are needed

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.6.3-3
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Richard W.M. Jones <rjones@redhat.com> - 1.6.3-1
- New upstream version 1.6.3.
- Change download URLs.

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1.6.1-2
- Rebuild for OCaml 4.00.0.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 1.6.1-1
- New upstream version 1.6.1.
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 1.5.9-1
- New upstream version 1.5.9.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.5.6-3
- Rebuild for OCaml 3.11.2.

* Sun Oct  4 2009 Richard W.M. Jones <rjones@redhat.com> - 1.5.6-2
- New upstream version 1.5.6.
- Upstream tests should be fixed now, so reenable all of them.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-1
- Rebuild for OCaml 3.11.1
- New upstream version 1.5.0.
- Fix tests.
- Fix documentation.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-4
- Rebuild for OCaml 3.11.0.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-3
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-2
- Rebuild for OCaml 3.11.0

* Sun Aug 31 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-1
- New upstream version 1.2.0.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-2
- Rebuild for OCaml 3.10.2

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-1
- Jump in upstream version to 1.0.3.
- New upstream URL.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-3
- Build for ppc64.

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-2
- Added BR ocaml-camlp4-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-1
- Initial RPM release.
