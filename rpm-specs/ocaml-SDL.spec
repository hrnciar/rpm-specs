%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-SDL
Version:        0.9.1
Release:        44%{?dist}
Summary:        OCaml bindings for SDL
License:        LGPLv2+

URL:            http://ocamlsdl.sourceforge.net
Source0:        http://downloads.sourceforge.net/ocamlsdl/ocamlsdl-%{version}.tar.gz
Source1:        ocamlsdl-0.7.2-htmlref.tar.gz

# Fix for safe-string in OCaml 4.06.
Patch1:         ocamlsdl-0.9.1-safe-string.patch

BuildRequires:  ocaml-lablgl-devel
BuildRequires:  SDL_ttf-devel, SDL_mixer-devel, SDL_image-devel 
BuildRequires:  ocaml
Requires:       ocaml


%description
Runtime libraries to allow programs written in OCaml to write to SDL 
(Simple DirectMedia Layer) interfaces.


%package        devel
Summary:        Development files for ocamlSDL
Requires:       %{name} = %{version}-%{release} 


%description    devel
The ocamlSDL-devel package provides libraries and headers for developing 
applications using ocamlSDL


%prep
%setup -q -n ocamlsdl-%{version} -a 1
%autopatch -p1


%build
%configure
make %{?_smp_mflags}



%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc README COPYING AUTHORS NEWS
%{_libdir}/ocaml/sdl
%{_libdir}/ocaml/stublibs/*.so*
%if %opt
%exclude %{_libdir}/ocaml/sdl/*.a
%exclude %{_libdir}/ocaml/sdl/*.cmxa
%endif
%exclude %{_libdir}/ocaml/sdl/*.mli


%files devel
%doc htmlref/
%if %opt
%{_libdir}/ocaml/sdl/*.a
%{_libdir}/ocaml/sdl/*.cmxa
%endif
%{_libdir}/ocaml/sdl/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-44
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-43
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-42
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-41
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-40
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-38
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-37
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-36
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-35
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-34
- Enable lablgl again (enables Sdlgl submodule).

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-33
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-32
- Drop lablgl dependency.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-28
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-27
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-25
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-24
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-21
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-20
- Bump release and rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-19
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 0.9.1-17
- remove ExcludeArch

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-16
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-14
- Revert some patches and build for OCaml 4.02.3.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-11
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-10
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-8
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-7
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-3
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.1-1
- New upstream version 0.9.1.
- OCaml 4.01.0 rebuild.
- Modernize the spec file.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Bruno Wolff III <bruno@wolff.to> - 0.8.0-7
- Rebuild for OCaml 4.0.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.0-5
- Rebuild for OCaml 4.00.0.

* Sat Jan 07 2012 Richard W.M. Jones <rjones@redhat.com> - 0.8.0-4
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Richard W.M. Jones <rjones@redhat.com> - 0.8.0-2
- New upstream version 0.8.0.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-21
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-19
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-17
- Force rebuild.

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-16
- Rebuild.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-15
- Rebuild for OCaml 3.11.0

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.2-14
- fix license tag

* Mon Jun  2 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-13
- labgl -> ocaml-lablgl-devel

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-12
- Rebuild for OCaml 3.10.2.

* Sat Apr 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.7.2-11
- Add commas in dependencies & rebuild.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> 0.7.2-10
- Rebuild for ppc64.

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> 0.7.2-9
- *.so.owner files aren't being generated by this ocamlfind.

* Wed Feb 13 2008 Richard W.M. Jones <rjones@redhat.com> 0.7.2-8
- Rebuild for OCaml 3.10.1.
- Generate correct provides and requires.
- Fix 'make install' rule for new ocamlfind.
- Fix paths to conform with OCaml packaging guidelines.

* Wed May 09 2007 Nigel Jones <dev@nigelj.com> 0.7.2-7
- ExcludeArch ppc64 until ocaml builds

* Fri May 04 2007 Nigel Jones <dev@nigelj.com> 0.7.2-6
- Fix download URL and remove ldconfig

* Fri May 04 2007 Nigel Jones <dev@nigelj.com> 0.7.2-5
- Minor fixups per review

* Thu May 03 2007 Nigel Jones <dev@nigelj.com> 0.7.2-4
- Rename per policy
- Revert -3 changes
- Add htmlref

* Thu Apr 26 2007 Nigel Jones <dev@nigelj.com> 0.7.2-3
- Provide ocamlSDL-static, add COPYING to -devel as docs.

* Wed Apr 11 2007 Nigel Jones <dev@nigelj.com> 0.7.2-2
- Fix missing dependencies

* Tue Apr 10 2007 Nigel Jones <dev@nigelj.com> 0.7.2-1
- Initial spec file

