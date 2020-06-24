Name:           ocaml-seq
Version:        0.1
Release:        14%{?dist}
Summary:        Compatibility package for OCaml's standard iterator type
License:        LGPLv2+ with exceptions

URL:            https://github.com/c-cube/seq
Source0:        https://github.com/c-cube/seq/archive/0.1.tar.gz

# Upstream patches since 0.1 was released.
Patch0001:      0001-switch-between-definition-alias-module-depending-on-.patch
Patch0002:      0002-fix-opam-set-LGPL-as-the-license-close-2.patch
Patch0003:      0003-fix-opam-specify-constraints-on-ocaml-4.07.patch
Patch0004:      0004-add-license.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlbuild-devel


%description
Compatibility package for OCaml's standard iterator type starting from 4.07.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n seq-%{version}
%autopatch -p1


%build
make %{?_smp_mflags} all


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

# Don't ship the .ml file.
rm $OCAMLFIND_DESTDIR/seq/seq.ml


%files
%doc README.md
%license LICENSE
%{_libdir}/ocaml/seq
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/seq/*.a
%exclude %{_libdir}/ocaml/seq/*.cmxa
%exclude %{_libdir}/ocaml/seq/*.cmx
%endif
%exclude %{_libdir}/ocaml/seq/*.mli
%exclude %{_libdir}/ocaml/seq/META


%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/seq/*.a
%{_libdir}/ocaml/seq/*.cmxa
%{_libdir}/ocaml/seq/*.cmx
%endif
%{_libdir}/ocaml/seq/*.mli
%{_libdir}/ocaml/seq/META


%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-13
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-12
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-11
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-10
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-8
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-7
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-6
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-5
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-4
- OCaml 4.08.1 (rc2) rebuild.

* Thu Aug  1 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-3
- Add license file from upstream.

* Thu Aug  1 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-2
- Add a link to upstream bug about the license.
- Don't install seq.ml file.
- Don't package META twice.

* Thu Aug  1 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1-1
- Initial version.
