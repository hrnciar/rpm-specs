# This package doesn't seem to want to make debuginfo either. :(
%global debug_package %{nil}

Name:           ocaml-opam-file-format
Version:        2.0.0
Release:        19%{?dist}
Summary:        Parser and printer for the opam file syntax

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# This is apparently a standard "OCaml exception" and is detailed
# in the license file. That wasn't included in the repo, but I filed
# a ticket (https://github.com/ocaml/opam-file-format/issues/5)
# and now it is, so I've added the commit that added license as a patch.
License:        LGPLv2 with exceptions
URL:            https://github.com/ocaml/opam-file-format/
Source0:        https://github.com/ocaml/%{libname}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml

%description
Parser and printer for the opam file syntax.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version} -p1

# Generate debuginfo, or try to.
sed 's/ocamlc/ocamlc -g/g' -i src/Makefile
sed 's/ocamlopt/ocamlopt -g/g' -i src/Makefile

%build
make byte %{?_smp_mflags}
%ifarch %{ocaml_native_compiler}
make native %{?_smp_mflags}
%endif

%install
make install LIBDIR=%{_libdir}/ocaml DESTDIR=%{buildroot}

# The mli files don't seem to get installed by the makefile.
# This is suboptimal.
cp -a src/*.mli %{buildroot}%{_libdir}/ocaml/%{libname}/

%files
# There is no documentation.
%license LICENSE
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%endif
%exclude %{_libdir}/ocaml/%{libname}/*.mli

%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-19
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-18
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-16
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-15
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-14
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-13
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-12
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-10
- Bump release and rebuild.

* Sat Jan 18 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-9
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-8
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-7
- Bump release and rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-6
- Bump release and rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-5
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-4
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-1
- Updated to latest upstream release (rhbz#1720584).

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.11.beta3
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.10.beta3
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.9.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.8.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.7.beta3
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.6.beta3
- OCaml 4.07.0-rc1 rebuild.

* Thu Apr 26 2018 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.5.beta3
- OCaml 4.07.0-beta2 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-0.3.beta3
- OCaml 4.06.0 rebuild.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 2.0.0-0.2.beta3
- Modernize ocaml packaging, use macro for testing native compiler.
- Remove manual invocation of ocaml dependency generator.
- Add -g to ocamlc, ocamlopt invocations, but this still doesn't make debuginfo.
- Use global instead of define for libname macro.

* Tue Aug  1 2017 Ben Rosser <rosser.bjr@gmail.com> 2.0.0-0.1.beta3
- Initial package.
