%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           ocaml-re
Version:        1.9.0
Release:        18%{?dist}
Summary:        A regular expression library for OCaml

License:        LGPLv2 with exceptions
URL:            https://github.com/ocaml/ocaml-re
Source0:        https://github.com/ocaml/%{name}/archive/%{version}/ocaml-re-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-dune

%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=1792031
Requires:       ocaml-seq-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocaml-re-%{version}

%build
dune build -p re --verbose %{?_smp_mflags}

%install

# jbuilder/dune 1.0+ supports installing without opam-installer,
# which means in theory we could do something like the below even for
# "ocaml critical path" packages (e.g. dependencies of opam and opam-installer).

# However... in this package it seems to stop RPM from finding debug info
# correctly. I am not sure why. :(

#export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
#mkdir -p $OCAMLFIND_DESTDIR
#jbuilder install --destdir %{buildroot}
#rm -r %{buildroot}/doc/re/

# So use the "manual jbuilder install" technique instead.
mkdir -p %{buildroot}%{_libdir}/ocaml
cp -aLr _build/install/default/lib/* %{buildroot}%{_libdir}/ocaml/

%files
%doc CHANGES.md
%doc README.md
%license LICENSE.md
%{_libdir}/ocaml/re
%if %{native_compiler}
%exclude %{_libdir}/ocaml/re/*.a
%exclude %{_libdir}/ocaml/re/*.cmxa
%exclude %{_libdir}/ocaml/re/*.cmx
%endif
%exclude %{_libdir}/ocaml/re/*.mli

%files devel
%if %{native_compiler}
%{_libdir}/ocaml/re/*.a
%{_libdir}/ocaml/re/*.cmx
%{_libdir}/ocaml/re/*.cmxa
%endif
%{_libdir}/ocaml/re/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-18
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-17
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-13
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-12
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-11
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-9
- OCaml 4.10.0+beta1 rebuild.

* Fri Jan 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-8
- Make devel subpackage depend on ocaml-seq-devel (RHBZ#1792031).

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-7
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-6
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-5
- Add BR ocaml-seq (RHBZ#1735476).

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.9.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.9.0-1
- Updated to latest upstream release (rhbz#1550761).

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-4
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-3
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.7.3-1
- Update to 1.7.3, switch to jbuilder.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-4
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.1-2
- OCaml 4.06.0 rebuild.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.7.1-1
- Update to latest ocaml-re release.
- Use configure script directly in build section.
- Do parallel build using smp_flags macro.

* Thu Sep 3 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.4.1-1
- New upstream release
- Remove upstreamed patch

* Tue Feb 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-4
- Fix missing 'isa' macro in devel depends

* Sat Jan 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-3
- Change patch filename to have .patch suffix
- Remove whitespace

* Fri Dec 12 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-2
- Minor updates to the SPEC file. Now rpmlint gives no errors.

* Sat Jun  7 2014 David Scott <dave.scott@citrix.com> - 1.2.2-1
- Update to 1.2.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 1.2.1-2
- Split files correctly between base and devel packages

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.2.1-1
- Initial package

