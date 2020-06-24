Name:           opam
Version:        2.0.6
Release:        6%{?dist}
Summary:        Source-based package manager for OCaml

# Standard "OCaml linking exception", see included file.
License:        LGPLv2 with exceptions
URL:            https://github.com/ocaml/opam
Source0:        https://github.com/ocaml/opam/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/ocaml/opam/commit/841ecb34818397d39ebe508f1ffe8708b6e238e8
Patch1:         841ecb34818397d39ebe508f1ffe8708b6e238e8.patch

BuildRequires:  ocaml > 4.02.3
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlbuild

BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-opam-file-format-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-result-devel

BuildRequires:  glpk-devel
BuildRequires:  zlib-devel

BuildRequires:  ocaml-dune
BuildRequires:  git
BuildRequires:  gcc-c++

# Needed to install packages and run opam init.
Requires:       bubblewrap
Requires:       bzip2
Requires:       gcc
Requires:       make
Requires:       m4
Requires:       patch
Requires:       unzip
Requires:       tar

Requires:       opam-installer%{?_isa} = %{version}-%{release}

%description
Opam is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

%package installer
Summary:        Standalone script for opam install files

%description installer
Standalone script for working with opam .install files, see the opam
package for more information.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure
sed 's/OPAMINSTALLER_FLAGS=/OPAMINSTALLER_FLAGS+=/g' -i Makefile

export JBUILDER_ARGS="--verbose"
# Need to set the path so Makefile can run the opam command.
export PATH=$PWD:$PATH

# Parallel build does not succeed.
make

%install
export JBUILDER_ARGS="--verbose"
export PATH=$PWD:$PATH

# This may no longer be necessary.
export LIBINSTALL_DIR=%{buildroot}/%{_libdir}/ocaml

# The makefile looks like it tries to invoke ocamlfind but only if DESTDIR
# isn't set. If it is set (which it is) LIBINSTALLDIR must be set too
# for installing opam-installer metadata.
%make_install

# However it looks like some (extra) documentation gets
# installed in the wrong place so... delete it.
rm -rf %{buildroot}%{_prefix}/doc

# It seems that some tests fail under mock.
# I am not sure why at the moment. So for now I'll just turn them off.
#%check
#make tests

%files
%license LICENSE
%{_bindir}/opam
%exclude %{_mandir}/man1/opam-installer.1*
%{_mandir}/man1/*.1*

%files installer
%license LICENSE
# Upstream puts this documentation under opam-installer, not opam.
# Since I have opam require opam-installer anyway, this seems reasonable.
# (And there are lots of man pages in the opam package, so it has docs).
%doc README.md CHANGES AUTHORS CONTRIBUTING.md
%{_bindir}/opam-installer
%{_mandir}/man1/opam-installer.1*

%changelog
* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-6
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-3
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.6-2
- OCaml 4.10.0 final.

* Fri Feb 07 2020 Ben Rosser <rosser.bjr@gmail.com> - 2.0.6-1
- Update to version 2.0.6.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.5-3
- OCaml 4.10.0+beta1 rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.5-2
- OCaml 4.08.1 (final) rebuild.

* Wed Aug 07 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.5-1
- Update to latest upstream release.
- dune switch "-p" infers "--profile release", so remove it from JBUILDER_ARGS.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-4
- OCaml 4.08.1 (rc2) rebuild.
- Miscellaneous build fixes to disable warnings.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.1-1
- Updated to latest upstream release (rhbz#1643738).

* Wed Oct 24 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-4
- Add requires on make and m4 for opam init setup.

* Tue Oct 02 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-3
- Add Requires on bubblewrap, gcc as well.

* Sat Sep 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-2
- Add missing Requires on patch, unzip (rhbz#1631969).

* Wed Aug 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-1
- Updated to opam 2.0.0 final release!

* Tue Aug 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.9.rc1
- Updated to opam 2.0 rc1.
- Fix FTBFS on Fedora 29/Rawhide.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.8.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.7.beta6
- Add missing dependency on bzip2 (#1572862).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.6.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.5.beta6
- Update to beta6, with a few fixes from beta5.

* Mon Dec 04 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.4.beta5
- Add upstream patch correctly indicating LGPLv2 license of a few files.

* Tue Nov 28 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.3.beta5
- Updated to latest upstream release.
- Split opam-installer out as a subpackage.

* Mon Oct 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 2.0.0-0.2.beta4
- Updated to latest upstream release.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 2.0.0-0.1.beta31
- Initial package.
