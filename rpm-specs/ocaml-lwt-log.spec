Name:           ocaml-lwt-log
Version:        1.1.1
Release:        12%{?dist}
Summary:        Lwt logging library

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        LGPLv2+
URL:            https://github.com/ocsigen/lwt_log
Source0:        https://github.com/ocsigen/lwt_log/archive/%{version}/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lwt-devel

BuildRequires:  ocaml-dune

%description
Lwt-friendly logging library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n lwt_log-%{version}

%build
dune build

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
dune install --prefix %{buildroot}%{_prefix}/ --lib %{buildroot}%{_libdir}/ocaml/

# Remove .ml files.
rm -rf %{buildroot}%{_libdir}/ocaml/lwt_log/*.ml
rm -rf %{buildroot}%{_libdir}/ocaml/lwt_log/*/*.ml

# Hmm... the above needs refinement. Remove spurious doc files.
rm -rf %{buildroot}%{_prefix}/doc

# Makes *.cmxs executable such that they will be stripped.
# This will cause debuginfo to be generated!
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

%files
%license COPYING
%doc README.md CHANGES
%{_libdir}/ocaml/lwt_log
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/lwt_log/*/*.a
%exclude %{_libdir}/ocaml/lwt_log/*/*.cmxa
%exclude %{_libdir}/ocaml/lwt_log/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/lwt_log/*/*.mli

%files devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/lwt_log/*/*.a
%{_libdir}/ocaml/lwt_log/*/*.cmxa
%{_libdir}/ocaml/lwt_log/*/*.cmx
%endif
%{_libdir}/ocaml/lwt_log/*/*.mli


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-12
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-7
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-3
- Rebuilt for lwt 4.4.

* Tue Aug 27 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-2
- Rebuilt for lwt 4.3.

* Thu Aug 08 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-1
- Update to latest upstream release, 1.1.1.

* Wed Aug 07 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-5
- Fix use of deprecated Lwt_main.exit_hooks in lwt 4.1+.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-2
- Mark cmxs files as executable to generate debuginfo.
- Correct license (it's LGPLv2+, not BSD).
- Remove license from devel package.
- Fix FSF address in mli header files.

* Tue Oct 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial packaging.
