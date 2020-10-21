Name:           utop
Version:        2.6.0
Release:        3%{?dist}
Summary:        Improved toplevel for OCaml

License:        BSD
URL:            https://github.com/ocaml-community/utop
Source0:        https://github.com/ocaml-community/%{name}/releases/download/%{version}/%{name}-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-cppo >= 1.1.2
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-findlib >= 1.7.2
BuildRequires:  ocaml-lambda-term-devel >= 3.1.0
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-react-devel >= 1.0.0

# for utop.el
BuildRequires:  emacs-common
Requires:       emacs-filesystem

Provides:       ocaml-%{name}%{?_isa} =  %{version}-%{release}

%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for
OCaml. It can run in a terminal or in Emacs. It supports line
editing, history, real-time and context sensitive completion,
colors, and more.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camomile-devel%{?_isa}
Requires:       ocaml-lambda-term-devel%{?_isa}
Requires:       ocaml-lwt-react-devel%{?_isa}
Requires:       ocaml-react-devel%{?_isa}
Provides:       ocaml-%{name}-devel%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global debug_package %{nil}

%prep
%autosetup

%build
dune build --verbose \
    --for-release-of-packages=%{name} \
    %{?_smp_mflags}

%install
dune install --verbose \
    --for-release-of-packages=%{name} \
    --destdir=%{buildroot} \
    --libdir=%{_libdir}/ocaml

rm -f %{buildroot}/usr/doc/%{name}/{LICENSE,CHANGES.md,README.md}

%files
%license LICENSE
%doc README.md CHANGES.md
%{_bindir}/%{name}*
%{_libdir}/ocaml/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%{_emacs_sitelispdir}/%{name}.el
%{_datadir}/%{name}
%exclude %{_libdir}/ocaml/%{name}/*.mli

%files devel
%{_libdir}/ocaml/%{name}/*.mli


%changelog
* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Update to 2.6.0
- Add ocaml-lwt-react-devel and ocaml-react-devel BRs
- Drop unneeded ocaml-bisect-ppx, ocaml-seq, and opam-installer BRs

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.3-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.3-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.4.3-1
- Update to 2.4.3
- Add ocaml-bisect-ppx-devel BR
- Remove man page manipulations; they are installed where we want them now

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-2
- Require -devel packages of lwt and lambda-term for build step

* Wed Oct 16 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Mon Aug 12 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.0-2
- Update build scripts

* Fri Feb 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Mon Dec 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-4
- Update URLs

* Mon Dec 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-3
- Rebuild with lambda-term 1.13

* Sun Aug 12 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-2
- Fix installing man pages

* Sun Jul 15 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2.1.0-2
- Rebuild with findlib 1.8.0

* Mon Mar 05 2018 Sergey Avseyev <sergey.avseyev@gmail.com> 2.1.0-1
- Initial packaging.
