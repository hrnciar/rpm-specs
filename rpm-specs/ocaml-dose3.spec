# We need the ocaml bz2 bindings to run the unit tests via ounit.
# There is also a separate test data repository for a different set of tests
# that is distributed separately.

# Currently packaging a snapshot to build with newer ocaml.
%global commit0 2c1b8df9064d645fac273e3ca96b5c0d92bf6e9f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           ocaml-dose3
Version:        5.0.1
Release:        29.20180821git%{shortcommit0}%{?dist}
Summary:        Framework for managing distribution packages and dependencies

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# Linking exception, see included COPYING file.
License:        LGPLv3+ with exceptions
URL:            http://www.mancoosi.org/software/

#Source0:        https://gforge.inria.fr/frs/download.php/file/36063/dose3-{version}.tar.gz
Source0:       https://scm.gforge.inria.fr/anonscm/gitweb?p=dose/dose.git;a=snapshot;h=%{commit0};sf=tgz#/dose-%{shortcommit0}.tar.gz

# One remaining safe-string fix.
Patch0:        ocaml-dose3-safe-string.patch

# The option to enable debuginfo generation (-tag debug) was commented out
# in the Makefile, so comment it back in.
Patch1:        ocaml-dose3-makefile-debug.patch

# Use ounit2.
Patch2:         dose-2c1b8df-ounit2.patch
BuildRequires:  autoconf, automake

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-expat-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-seq-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-ounit-devel

BuildRequires:  rpm-devel
BuildRequires:  zlib-devel

BuildRequires:  perl, perl-generators

# Needs latex for documentation.
BuildRequires:  texlive
BuildRequires:  texlive-comment
BuildRequires:  hevea
BuildRequires:  graphviz

# Depend on pod2man, pod2html.
BuildRequires:  /usr/bin/pod2man
BuildRequires:  /usr/bin/pod2html

%description
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems
(monitoring package evolutions, correct and complete dependency resolution,
repository-wide uninstallability checks).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

# Since these are applications, I think the correct name is "dose3-tools"
# and not "ocaml-dose3-tools", but I'm happy to change it if necessary.

%package -n dose3-tools
Summary:        Tools suite from the dose3 framework

%description -n dose3-tools
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

This package contains the tools shipped with the dose3 framework
for manipulating packages of various formats.

%prep
%autosetup -p1 -n dose-%{shortcommit0} #dose3-%{version}
# Patch 2 touches configure.ac.
autoreconf -i

# I think we want to package the .cmx files if possible.
sed "s/*.cmx /*.cmxignore /g" -i Makefile
sed "s,*.cmxs,*.cmxs _build/doselibs/*.cmx,g" -i Makefile
sed "s,cmxa cmxs,cmx cmxa cmxs,g" -i Makefile.config.in

# Fix an issue with re 1.7.3+
sed "s/module Str = Re_str/module Str = Re.Str/g" -i rpm/version.ml

%build
%configure --with-zip --with-oUnit --with-rpm4 --with-xml

# Build fails when built with %{?_smp_mflags} and thus we can't use the magic macro.
make
make doc man

%install
# Apparently, the make_install macro doesn't work on rawhide?
# fails with something like: install -- invalid option a
# So...
make install DESTDIR=%{buildroot}

# Install manpages.
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.8 %{buildroot}%{_mandir}/man8/
cp -a doc/manpages/*.5 %{buildroot}%{_mandir}/man5/
cp -a doc/manpages/*.1 %{buildroot}%{_mandir}/man1/

# Rewrite symlinks.
rm -f %{buildroot}%{_bindir}/rpmcheck
rm -f %{buildroot}%{_bindir}/debcheck
rm -f %{buildroot}%{_bindir}/eclipsecheck
ln -s %{_bindir}/distcheck %{buildroot}%{_bindir}/rpmcheck
ln -s %{_bindir}/distcheck %{buildroot}%{_bindir}/debcheck
ln -s %{_bindir}/distcheck %{buildroot}%{_bindir}/eclipsecheck

%files
%license COPYING
%doc README.architecture
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.cmxa
%endif
%exclude %{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cmi

%files -n dose3-tools
%license COPYING
%doc doc/debcheck.primer/*.pdf
%doc doc/apt-external-solvers.primer/*.pdf
%doc doc/apt-cudf/
%{_bindir}/apt-cudf
%{_bindir}/ceve
%{_bindir}/challenged
%{_bindir}/deb-buildcheck
%{_bindir}/deb-coinstall
%{_bindir}/debcheck
%{_bindir}/eclipsecheck
%{_bindir}/distcheck
%{_bindir}/outdated
%{_bindir}/rpmcheck
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-29.20180821git2c1b8df
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-28.20180821git2c1b8df
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-27.20180821git2c1b8df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-26.20180821git2c1b8df
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-25.20180821git2c1b8df
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-24.20180821git2c1b8df
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-23.20180821git2c1b8df
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-22.20180821git2c1b8df
- OCaml 4.10.0 final.

* Fri Feb 07 2020 Ben Rosser <rosser.bjr@gmail.com> - 5.0.1-21.20180821git2c1b8df
- Rebuild against ocamlgraph-1.8.8-14.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-20.20180821git2c1b8df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-19.20180821git2c1b8df
- OCaml 4.10.0+beta1 rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-18.20180821git2c1b8df
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-17.20180821git2c1b8df
- Rebuild against new ocaml-lablgtk.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-16.20180821git2c1b8df
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-15.20180821git2c1b8df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.1-14.20180821git2c1b8df
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:03 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.1-13.20180821git2c1b8df
- Rebuild for RPM 4.15

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-12.20180821git2c1b8df
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 5.0.1-11.20180821git2c1b8df
- Fix build with ocaml-re 1.7.3.

* Tue Aug 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 5.0.1-10.20180821git2c1b8df
- Update to newer SCM (git) checkout.
- Modify Makefile in prep section in order to install cmx files.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9.20171203git09392e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-8.20171203git09392e2
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-7.20171203git09392e2
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-6.20171203git09392e2
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5.20171203git09392e2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Ben Rosser <rosser.bjr@gmail.com> 5.0.1-4.20171203git09392e2
- Update to latest git snapshot and fix safe-string issues (#1520039).

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 5.0.1-3
- OCaml 4.06.0 rebuild.

* Fri Sep 01 2017 Ben Rosser <rosser.bjr@gmail.com> 5.0.1-2
- Use configure macro to avoid specifying prefix, libdir, bindir by hand.
- Remove Requires on main package from dose3-tools subpackage.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 5.0.1-1
- There are far newer versions; package latest release.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 4.2-2
- Successfully link against ocamlgraph.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 4.2-1
- Initial package.
