Name:           ocaml-zip
Version:        1.10
Release:        5%{?dist}
Summary:        OCaml library for reading and writing zip, jar and gzip files
License:        LGPLv2 with exceptions

%global upver %(sed 's/\\.//' <<< %{version})

URL:            https://xavierleroy.org/software.html
Source0:        https://github.com/xavierleroy/camlzip/archive/rel%{upver}.tar.gz

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  pkgconfig(zlib)


%description
This Objective Caml library provides easy access to compressed files
in ZIP and GZIP format, as well as to Java JAR files. It provides
functions for reading from and writing to compressed files in these
formats.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n camlzip-rel%{upver}

# Do not try to overwrite the system ld.conf
sed -i "s,ocamlfind install,& -ldconf $PWD/ld.conf," Makefile

# The META file has the wrong version number
sed -i 's/1\.09/%{version}/' META-zip


%build
make all
%ifarch %{ocaml_native_compiler}
make allopt
%endif
make doc

# Relink the stublibs with $RPM_LD_FLAGS.
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -lz -o camlzip $(ar t libcamlzip.a)


%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/zip
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ocaml/stublibs

export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
export EXT_DLL=.so

touch ld.conf
make install


%check
export LD_LIBRARY_PATH=$PWD
make -C test
test/testzlib Makefile Makefile.gz
test/testzlib -d Makefile.gz Makefile.uncompressed
cmp Makefile Makefile.uncompressed


%files
%license LICENSE
%{_libdir}/ocaml/camlzip/
%dir %{_libdir}/ocaml/zip/
%{_libdir}/ocaml/zip/META
%{_libdir}/ocaml/zip/*.cma
%{_libdir}/ocaml/zip/*.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/zip/*.cmxs
%endif
%{_libdir}/ocaml/stublibs/dllcamlzip.so
%{_libdir}/ocaml/stublibs/dllcamlzip.so.owner


%files devel
%doc Changes README doc
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/zip/*.a
%{_libdir}/ocaml/zip/*.cmxa
%{_libdir}/ocaml/zip/*.cmx
%endif
%{_libdir}/ocaml/zip/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.10-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.10-4
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.10-3
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.10-2
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 1.10-1
- Version 1.10
- New URLs
- Add check script

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.06-24
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.06-22
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.06-21
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.06-20
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.06-19
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.06-18
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.06-16
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.06-15
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.06-12
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1.06-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.06-9
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.06-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.06-5
- OCaml 4.04.2 rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 1.06-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 1.06-2
- Rebuild for OCaml 4.04.0.

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 1.06-1
- New upstream version 1.06.
- Remove ints patch, not needed with current version.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-13
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-12
- s/390x: Don't install *.cmx* files.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-11
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-10
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.05-9
- ocaml-4.02.1 rebuild.

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 1.05-8
- Add -fix-ints patch to fix build
- Drop obsolete ExcludeArch
- Fix license handling

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-8
- Bump release and rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-7
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-3
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.05-1
- New upstream version 1.05.
- OCaml 4.01.0 rebuild.
- Modernize spec file.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.04-10
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.04-8
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 1.04-7
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Richard W.M. Jones <rjones@redhat.com> - 1.04-5
- Project has moved, new source URLs.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.04-4
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.04-2
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.04-1
- New upstream release (resolves rhbz#490407).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-6
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-5
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-4
- Rebuild for OCaml 3.10.2

* Mon Mar 31 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-3
- Add unix as a dependency to the META-file (rhbz #439652).

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-2
- Rebuild for ppc64.

* Fri Feb 22 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-1
- Initial RPM release.
