Name:           ocaml-ocp-indent
Version:        1.7.0
Release:        11%{?dist}
Summary:        A simple tool to indent OCaml programs

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# The entire source code is LGPLv2 with exceptions except
# src/approx_tokens.ml is QPL
License:        (LGPLv2 with exceptions) and QPL
URL:            https://github.com/OCamlPro/%{libname}
Source0:        https://github.com/OCamlPro/%{libname}/archive/%{version}/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-result-devel
# Required for tests, not available in Fedora
#BuildRequires:  craml
BuildRequires:  emacs
# For byte-compile elisp
#BuildRequires:  emacs-auto-complete
#BuildRequires:  emacs-tuareg
# The following two are not yet available in Fedora.
# So byte compilation is disabled
#BuildRequires:  emacs-company
#BuildRequires:  emacs-iedit
BuildRequires:  vim-enhanced
Requires:       emacs-filesystem >= %{_emacs_version}
Requires:       vim-filesystem

%description
Ocp-indent is based on an approximate, tolerant OCaml parser and a simple stack
machine ; this is much faster and more reliable than using regexps. Presets and
configuration options available, with the possibility to set them project-wide.
Supports most common syntax extensions, and extensible for others.

Includes:

- An indentor program, callable from the command-line or from within editors
- Bindings for popular editors
- A library that can be directly used by editor writers, or just for
  fault-tolerant/approximate parsing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{libname}-%{version}


%build
dune build %{?_smp_mflags} --profile=release


%install
dune install \
     --destdir=%{buildroot} \
     --prefix=%{_prefix} \
     --libdir=%{_libdir}/ocaml \
     --mandir=%{_mandir}

chmod 755 %{buildroot}%{_libdir}/ocaml/%{libname}/*/*.cmxs

# Reinstall vim files to Fedora default location
mkdir -p %{buildroot}%{vimfiles_root}
mv %{buildroot}%{_datadir}/%{libname}/vim/* %{buildroot}%{vimfiles_root}
rmdir %{buildroot}%{_datadir}/%{libname}/vim
rmdir %{buildroot}%{_datadir}/%{libname}
# Reinstall documents using %%doc later
rm -fr %{buildroot}%{_prefix}/doc

%check
#Tests only run on a git checkout
# ./tests/test.sh


%files
%doc README.md CHANGELOG
%license LICENSE
%{_bindir}/*
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*/*.a
%exclude %{_libdir}/ocaml/%{libname}/*/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/%{libname}/*/*.mli
%exclude %{_libdir}/ocaml/%{libname}/*/*.ml
%{_emacs_sitelispdir}/*
%{vimfiles_root}/*/*
%{_mandir}/man1/%{libname}*

%files devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*/*.a
%{_libdir}/ocaml/%{libname}/*/*.cmxa
%{_libdir}/ocaml/%{libname}/*/*.cmx
%endif
%{_libdir}/ocaml/%{libname}/*/*.mli
%{_libdir}/ocaml/%{libname}/*/*.ml

%changelog
* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-10
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-8
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-6
- OCaml 4.10.0+beta1 rebuild.
- Use dune install --destdir option.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-5
- OCaml 4.09.0 (final) rebuild.

* Wed Sep 18 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- Bump release and rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-2
- Make cmxs files executable to properly generate debuginfo

* Fri Apr  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.7.0-1
- Initial packaging

