%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}

Name:           ocaml-perl4caml
Version:        0.9.5
Release:        83%{?dist}
Summary:        OCaml library for calling Perl libraries and code
License:        LGPLv2+ with exceptions

URL:            http://git.annexia.org/?p=perl4caml.git;a=summary
# There is currently no website hosting the tarballs.
Source0:        perl4caml-%{version}.tar.gz

# Include upstream patch for Perl 5.12:
# http://git.annexia.org/?p=perl4caml.git;a=commitdiff_plain;h=4cb12aa05bd5aa69ccfa1c6d41ab10bc79a3c3a3
Patch0:         perl4caml-0.9.5-svtrv.patch

# Upstream patch to fix build for OCaml 4.04.
Patch1:         perl4caml-0.9.5-fix-use-of-camlparam-etc-macros.patch

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-devel >= 5.8
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Embed)

# Perl4caml provides type-safe wrappers for these Perl modules:
#Requires:  perl-Date-Calc
##Requires:  perl-Date-Format
##Requires:  perl-Date-Parse
##Requires:  perl-Net-Google
##Requires:  perl-HTML-Element
#Requires:  perl-HTML-Parser
#Requires:  perl-HTML-Tree
#Requires:  perl-libwww-perl
#Requires:  perl-Template-Toolkit
#Requires:  perl-URI
#Requires:  perl-WWW-Mechanize

# RHBZ#533948
Requires: perl-libs%{?_isa}

# We're also going to pick up a versioned dependency, to help track things:
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Perl4caml allows you to use Perl code within Objective CAML (OCaml),
thus neatly side-stepping the (old) problem with OCaml which was that
it lacked a comprehensive set of libraries. Well now you can use any
part of CPAN in your OCaml code.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n perl4caml-%{version}
%patch0 -p1
%patch1 -p1
find -name .cvsignore -exec rm {} \;


%build
# Parallel builds don't work:
unset MAKEFLAGS

make EXTRA_EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
%if %opt
     OCAMLC="ocamlc.opt" OCAMLOPT="ocamlopt.opt -g"
%else
     OCAMLC="ocamlc" \
     perl4caml.cma META html
%endif
rm -f examples/*.{cmi,cmo,cmx,o,bc,opt}


%check
%if %opt
# Parallel builds don't work:
unset MAKEFLAGS

# Set the library path used by ocamlrun so it uses the library
# we just built in the current directory.
CAML_LD_LIBRARY_PATH=`pwd` make test
%endif


%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $DESTDIR/%{_libdir}/ocaml/stublibs

%if %opt
make install
%else
# Install by hand so we don't try to install *.cmx{,a} files on bytecode arch.
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0755 -d $DESTDIR/%{_libdir}/ocaml/stublibs
install -c -m 0644 perl.cmi perl.mli perl4caml.cma \
	libperl4caml.a META \
	wrappers/*.ml wrappers/*.cmi \
	$DESTDIR/%{_libdir}/ocaml/perl
install -c -m 0644 dllperl4caml.so $DESTDIR/%{_libdir}/ocaml/stublibs
%endif

# Don't delete rpath!  See:
# https://www.redhat.com/archives/fedora-packaging/2008-March/thread.html#00070


%files
%doc COPYING.LIB
%{_libdir}/ocaml/perl
%if %opt
%exclude %{_libdir}/ocaml/perl/*.a
%exclude %{_libdir}/ocaml/perl/*.cmxa
%endif
%exclude %{_libdir}/ocaml/perl/*.mli
%exclude %{_libdir}/ocaml/perl/*.ml
%{_libdir}/ocaml/stublibs/*.so


%files devel
%doc COPYING.LIB AUTHORS doc/* examples html README
%if %opt
%{_libdir}/ocaml/perl/*.a
%{_libdir}/ocaml/perl/*.cmxa
%endif
%{_libdir}/ocaml/perl/*.mli
%{_libdir}/ocaml/perl/*.ml


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-83
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-82
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-80
- Perl 5.32 rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-79
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-78
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-77
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-76
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-75
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-73
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-72
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-71
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-70
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-69
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-67
- OCaml 4.08.0 (final) rebuild.

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-66
- Perl 5.30 rebuild

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-65
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-62
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-61
- Perl 5.28 rebuild

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-60
- OCaml 4.07.0-rc1 rebuild.

* Thu Apr 26 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-59
- OCaml 4.07.0-beta2 rebuild.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.5-58
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-56
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-55
- Bump release and rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-54
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-51
- OCaml 4.04.2 rebuild.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-50
- Perl 5.26 rebuild

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-49
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-47
- Rebuild for OCaml 4.04.0.
- Include upstream fix for CAMLparam macro misuse.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-45
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-43
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-42
- Enable bytecode compiles.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-41
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-40
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-38
- Perl 5.22 rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-37
- ocaml-4.02.1 rebuild.

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-36
- Perl 5.20 rebuild

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-35
- ocaml-4.02.0 final rebuild.

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.9.5-34
- Perl 5.20 rebuild

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-33
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-31
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-30
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-27
- OCaml 4.01.0 rebuild.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9.5-25
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-23
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.9.5-21
- Perl 5.16 rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-20
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-19
- Rebuild for OCaml 3.12.1.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.9.5-18
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-16
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Sun Jun 27 2010 Ralf Corsepius <corsepiu@fedoraproject.org> - 0.9.5-15
- Once more rebuild with perl-5.12.x.

* Tue Jun  8 2010 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-14
- Fix for perl-libs dependency (RHBZ#533948).
- Include upstream patch for Perl 5.12 (Iain Arnell).

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.9.5-13
- Mass rebuild with perl-5.12.0

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-12
- Rebuild for OCaml 3.11.2.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.9.5-11
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-9
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-7
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-6
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-5
- Rebuild for OCaml 3.10.2.

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.5-4
- add Requires for versioned perl (libperl.so)

* Wed Mar 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-3
- Fix %%check rule (#436785).
- Use rpath for dllperl4caml.so as per this thread:
  https://www.redhat.com/archives/fedora-packaging/2008-March/thread.html#00070
  (#436807).
- Require rpath.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-2
- Rebuild for ppc64.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.5-1
- New upstream release 0.9.5.
- Clarify license is LGPLv2+ with exceptions
- Remove excessive BuildRequires - Perl modules not needed for building.
- Pass RPM C flags to the make.
- 'make test' fails where perl4caml is already installed.

* Sat Feb 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.4-1
- Initial RPM release.
