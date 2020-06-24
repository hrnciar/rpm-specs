Name:           ocaml-num
Version:        1.4
Release:        0.2%{?dist}
Summary:        Legacy Num library for arbitrary-precision integer and rational arithmetic
License:        LGPLv2+ with exceptions

URL:            https://github.com/ocaml/num
#Source0:        https://github.com/ocaml/num/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/ocaml/num/archive/v1.3.tar.gz

# All patches since 1.3 was released.
Patch1:         0001-Bump-version.patch
Patch2:         0002-Fix-usage-of-bytes-vs-string.patch
Patch3:         0003-Get-rid-of-Bytes.unsafe_of_string.patch

# Downstream patches to add -g flag.
Patch4:         0004-toplevel-Add-g-flag.patch
Patch5:         0005-src-Add-g-flag-to-mklib.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel


%description
This library implements arbitrary-precision arithmetic on big integers
and on rationals.

This is a legacy library. It used to be part of the core OCaml
distribution (in otherlibs/num) but is now distributed separately. New
applications that need arbitrary-precision arithmetic should use the
Zarith library (https://github.com/ocaml/Zarith) instead of the Num
library, and older applications that already use Num are encouraged to
switch to Zarith. Zarith delivers much better performance than Num and
has a nicer API.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
#%%setup -q -n num-%%{version}
%setup -q -n num-1.3
%autopatch -p1


%build
make %{?_smp_mflags} all


%check
make -j1 test


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

find $OCAMLFIND_DESTDIR -name '*.cmti' -delete


%files
%doc Changelog README.md
%license LICENSE
%{_libdir}/ocaml/*.cmi
%{_libdir}/ocaml/*.cma
%{_libdir}/ocaml/*.cmxs
%{_libdir}/ocaml/num
%{_libdir}/ocaml/num-top
%{_libdir}/ocaml/stublibs/dll*.so
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*.a
%exclude %{_libdir}/ocaml/*.cmxa
%exclude %{_libdir}/ocaml/*.cmx
%endif
%exclude %{_libdir}/ocaml/*.mli


%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*.a
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.cmx
%endif
%{_libdir}/ocaml/*.mli


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4-0.2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Thu Apr 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4-0.1
- Move to a pre-release of num 1.4.

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-24
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-23
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-22
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-21
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-19
- OCaml 4.10.0+beta1 rebuild.

* Fri Jan 10 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-18
- Bump release and rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-17
- OCaml 4.09.0 for riscv64

* Thu Dec 05 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-16
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-15
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-14
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-12
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-11
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-8
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-7
- Bump release and rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-6
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-4
- OCaml 4.06.0 rebuild.

* Wed Nov  8 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-3
- Initial RPM version.
- Fix Source0 to use nice package name.
- Fix DESTDIR installs again.
