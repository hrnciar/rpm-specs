%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-mysql
Version:        1.2.2
Release:        16%{?dist}
Summary:        OCaml library for accessing MySQL databases
License:        LGPLv2+ with exceptions

URL:            https://github.com/ygrek/ocaml-mysql
Source0:        https://github.com/ygrek/ocaml-mysql/releases/download/v1.2.2/ocaml-mysql-1.2.2.tar.gz

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  mariadb-connector-c-devel
# XXX openssl-devel should be required by mariadb-connector-c-devel
# but it is not so we have to explicitly request it here.  See also
# https://bugzilla.redhat.com/show_bug.cgi?id=1493692#c4
BuildRequires:  openssl-devel
BuildRequires:  chrpath


%description
ocaml-mysql is a package for ocaml that provides access to mysql
databases. It consists of low level functions implemented in C and a
module Mysql intended for application development.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q


%build
LDFLAGS="-L%{_libdir}/mariadb" \
%configure
make all
%if %opt
make opt
%endif

chrpath --delete dll*.so


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install


%files
%doc COPYING
%{_libdir}/ocaml/mysql
%if %opt
%exclude %{_libdir}/ocaml/mysql/*.a
%exclude %{_libdir}/ocaml/mysql/*.cmxa
%exclude %{_libdir}/ocaml/mysql/*.cmx
%endif
%exclude %{_libdir}/ocaml/mysql/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING CHANGES README VERSION
%if %opt
%{_libdir}/ocaml/mysql/*.a
%{_libdir}/ocaml/mysql/*.cmxa
%{_libdir}/ocaml/mysql/*.cmx
%endif
%{_libdir}/ocaml/mysql/*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-16
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-15
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-13
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-12
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-11
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-10
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-9
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-7
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-6
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-5
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-4
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-3
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-2
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-1
- New upstream version 1.2.2.
- Drop camlp4 dependency.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-14
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-13
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-11
- OCaml 4.06.0 rebuild.

* Mon Oct 23 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-10
- Use mariadb-connector-c-devel (RHBZ#1493692).

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-9
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-6
- Rebuild against latest mariadb.

* Wed Jul 05 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-5
- Add upstream patch to fix configure against MariaDB 10.2 (RHBZ#1467652).

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-4
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-1
- New upstream version 1.2.1.
- Remove int64_t fix, since that is now upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-2
- OCaml 4.02.3 rebuild.

* Mon Jul 20 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-1
- New upstream version 1.2.0.
- Fix bytecode builds.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-5
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-4
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-2
- ocaml-4.02.1 rebuild.

* Mon Nov 03 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-1
- New upstream version 1.1.3.
- Remove paths patch, which seems unneeded now.
- mysql-devel -> mariadb-devel

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-6
- Bump release and rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-5
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-4
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-2
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-1
- New upstream version 1.1.2.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-6
- OCaml 4.01.0 rebuild.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-4
- Remove direct dependency of mysql-libs, since RPM picks up the
  correct dependency implicitly (RHBZ#962742).

* Fri Mar  1 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-3
- Ensure we link to mysql client shared library (RHBZ#916822, thanks Sato Ichi).
- Move configure into build section, and replace with RPM macro.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-1
- New upstream version 1.1.1.
- Clean up the spec file.
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- Rebuild for OCaml 4.00.0.

* Wed Jan 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- New upstream version 1.1.0.
- It is now hosted on OCaml Forge.
- Rebuild for OCaml 3.12.1.
- Remove patch, now upstream.
- HTML docs are not built, so don't include them in the package.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-13
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-12
- Rebuild for OCaml 3.11.2.

* Fri Oct 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-11
- Patch for CVE 2009-2942 Missing escape function (RHBZ#529321).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-9
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-7
- Force another rebuild to try to get updated MySQL client deps.

* Sat Jan 17 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-6
- Requires mysql-libs, not automatically found.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-5
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-4
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-3
- Rebuild for OCaml 3.10.2

* Mon Mar  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-2
- Don't need 'ExcludeArch: ppc64' any more.
- Add missing BR for ocaml-camlp4-devel.
- Test build in mock.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-1
- Initial RPM release.
