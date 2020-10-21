Name:           ocaml-curl
Version:        0.9.1
Release:        8%{?dist}
Summary:        OCaml Curl library (ocurl)
License:        MIT

URL:            http://ocurl.forge.ocamlcore.org/
Source0:        https://github.com/ygrek/ocurl/archive/%{version}/ocurl-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
BuildRequires:  curl-devel >= 7.28.0
BuildRequires:  ocaml-lwt-ppx-devel
BuildRequires:  gawk

# Explicitly require Curl (fixes #711261). Since ocaml-curl uses
# -custom rather than ocamlmklib, automatic detection is infeasible.
Requires: curl-devel >= 7.28.0


%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n ocurl-%{version}

# Files in the archive have spurious +x mode.
find -type f | xargs chmod 0644
chmod 0755 configure install-sh

# Link with debuginfo and RPM_LD_FLAGS
sed -i "s|\$(OCAMLMKLIB)|& -g -ldopt '%build_ldflags'|" Makefile.in


%build
# Parallel builds don't work.
unset MAKEFLAGS

# Add -fPIC to avoid:
# /usr/bin/ld: /usr/lib64/ocaml/curl/libcurl-helper.a(curl-helper.o):
# relocation R_X86_64_32S against `.rodata' can not be used when
# making a shared object; recompile with -fPIC
CFLAGS="%{build_cflags} -fPIC" \
%configure --libdir=%{_libdir} --with-findlib

make
make doc


%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Make clean in the examples dir so our docs don't contain binaries.
make -C examples clean


%files
%license COPYING
%{_libdir}/ocaml/curl
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/curl/*.a
%exclude %{_libdir}/ocaml/curl/*.cmx
%exclude %{_libdir}/ocaml/curl/*.cmxa
%endif
%exclude %{_libdir}/ocaml/curl/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc doc examples
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/curl/*.a
%{_libdir}/ocaml/curl/*.cmx
%{_libdir}/ocaml/curl/*.cmxa
%endif
%{_libdir}/ocaml/curl/*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-8
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-7
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-5
- Rebuild to resolve build order symbol problems.

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-4
- Rebuild for ocaml-lwt 5.3.0

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-1
- New upstream version 0.9.1.
- Remove all patches; they have been upstreamed.
- Change source URL to include the package name.
- BR ocaml-lwt-ppx-devel instead of ocaml-lwt-devel.
- Invoke ocamlmklib with -g and $RPM_LD_FLAGS.
- BR ocaml-ocamldoc and build documentation.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-2
- OCaml 4.10.0 final.

* Fri Jan 31 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-1
- New upstream version 0.9.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.8.2-5
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.8.2-4
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.8.2-1
- new upstream release 0.8.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-13
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-12
- OCaml 4.07.0-rc1 rebuild.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.9-11
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-9
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-8
- Bump and rebuild for updated ocaml-lwt.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-7
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-4
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov  7 2016 Richard W.M. Jones <rjones@redhat.com> - 0.7.9-1
- New upstream version 0.7.9.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug  3 2015 Richard W.M. Jones <rjones@redhat.com> - 0.7.5-1
- New upstream version of ocurl 0.7.5.
- Remove patch because *.o and *.cmx files are installed now.
- Add support for lwt (requires also camlp4, libev).
- Don't need to add -g option since it's added upstream now.
- Don't copy curl.mli into libdir because upstream installs it.
- Add -fPIC option when building curl-helper.o.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-21
- OCaml 4.02.3 rebuild.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-20
- Remove ExcludeArch since bytecode build should now work.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-19
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-18
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-17
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-16
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-15
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-13
- ocaml-4.02.0-0.8.git10e45753.fc22 build.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-12
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-10
- Rebuild for OCaml 4.01.0.
- Debuginfo does not work for this package.
- Include *.cmx & *.o files in -devel package (for inlining).
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Michael Ekstrand <michael@elehack.net> - 0.5.3-7
- Rebuild for OCaml 4 update

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-5
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-4
- Rebuild for OCaml 3.12.1.

* Tue Jun  7 2011 Michael Ekstrand <michael@elehack.net> - 0.5.3-3
- Add curl-devel to Requires (#711261)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 0.5.3-1
- New upstream version 0.5.3.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-3
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-1
- New upstream version 0.5.1.
- Rebuild for OCaml 3.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-3
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-2
- Rebuild for OCaml 3.11.0

* Sun Aug 31 2008 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-1
- New upstream release 0.5.0.

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.1-9
- fix license tag

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-8
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-7
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-6
- Force rebuild for OCaml 3.10.1.

* Thu Sep  6 2007 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-5
- Force rebuild because of changed build-requires/provides scripts in OCaml.

* Thu Aug 30 2007 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-4
- Force rebuild because of changed BRs in base OCaml.

* Thu Aug  2 2007 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-3
- ExcludeArch ppc64
- Remove Requires curl, which is not necessary.
- Use %%-doc to handle docs in the devel package.

* Mon Jun 11 2007 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-2
- Updated to latest packaging guidelines.

* Sat May 26 2007 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-1
- Initial RPM release.
