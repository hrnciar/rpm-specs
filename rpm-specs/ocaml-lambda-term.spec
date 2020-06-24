Name:           ocaml-lambda-term
Version:        2.0.3
Release:        3%{?dist}
Summary:        Terminal manipulation library for OCaml

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        BSD
URL:            https://github.com/ocaml-community/lambda-term
Source0:        https://github.com/ocaml-community/lambda-term/archive/%{version}/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-lwt-log-devel
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-zed-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-mmap-devel
BuildRequires:  ocaml-charinfo-width-devel
BuildRequires:  ocaml-ocplib-endian-devel
BuildRequires:  ocaml-bisect-ppx-devel

BuildRequires:  ocaml-dune

%description
Lambda-term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

The main objective of lambda-term is to provide a higher level functional
interface to terminal manipulation than, for example, ncurses, by providing
a native OCaml interface instead of bindings to a C library.

Lambda-term integrates with zed to provide text edition facilities in
console applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
dune build \
    --verbose \
    --for-release-of-packages=%{libname} \
    %{?_smp_mflags}

# Relink the stublib with RPM_LD_FLAGS
cd _build/default/src
ocamlmklib -g -ldopt "$RPM_LD_FLAGS" -o lambda_term_stubs \
  $(ar t liblambda_term_stubs.a)
cd -

%install
dune install \
    --verbose \
    --for-release-of-packages=%{libname} \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}/ocaml

mkdir -p %{buildroot}%{_mandir}/man{1,5} \
         %{buildroot}%{_datadir}/lambda-term \
         %{buildroot}%{_docdir}
mv %{buildroot}%{_prefix}/doc/lambda-term %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/lambda-term{rc,-inputrc} %{buildroot}%{_datadir}/lambda-term

%check
make test

%files
%license LICENSE
%doc %{_docdir}/lambda-term
%{_libdir}/ocaml/%{libname}
%{_bindir}/lambda-term-actions
%{_mandir}/man1/lambda-term-actions.1*
%{_mandir}/man5/lambda-term-inputrc.5*
%{_datadir}/lambda-term
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/stublibs/*.so

%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.0.3-1
- Version 2.0.3
- Drop unneeded libev-devel BR
- Relink the stublib with $RPM_LD_FLAGS

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-3
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.2-1
- Update build scripts to use dune
- Update to latest upstream release

* Fri Aug 02 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.1-1
- Updated to latest upstream release (rhbz#1714129).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.13-1
- Updated to latest upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Dec 15 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.12.0-1
- Updated to latest upstream release.

* Thu Aug 31 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.11-1
- Initial packaging.
