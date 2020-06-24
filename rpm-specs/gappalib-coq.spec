# On platforms with a native OCaml compiler, proofs can be compiled into cmxs
# files, but there are no source files that rpm recognizes as such.
%ifarch %{ocaml_native_compiler}
%global _debugsource_template %{nil}
%else
%global debug_package %{nil}
%endif

# TESTING NOTE: The testsuite requires that gappalib-coq be installed already.
# Hence, we cannot run it on the koji builders.  The maintainer should always
# install the package and run "remake check" manually before committing.

%global gappadir %{_libdir}/coq/user-contrib/Gappa
%global coqver 8.11.2

Name:           gappalib-coq
Version:        1.4.4
Release:        1%{?dist}
Summary:        Coq support library for gappa

License:        LGPLv2+
URL:            http://gappa.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/file/38338/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  coq = %{coqver}
BuildRequires:  flocq
BuildRequires:  gappa
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-findlib
BuildRequires:  remake

Requires:       coq%{?_isa} = %{coqver}
Requires:       flocq
Requires:       gappa

%description
This support library provides vernacular files so that the certificates
Gappa generates can be imported by the Coq proof assistant.  It also
provides a "gappa" tactic that calls Gappa on the current Coq goal.

Gappa (Génération Automatique de Preuves de Propriétés Arithmétiques --
automatic proof generation of arithmetic properties) is a tool intended
to help verifying and formally proving properties on numerical programs
dealing with floating-point or fixed-point arithmetic.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Coq files for gappalib-coq.  These
files are not needed to use gappalib-coq.  They are made available for
informational purposes.

%prep
%autosetup -p1

# Enable debuginfo
sed -i 's/-pp/-g &/' Remakefile.in

# Workaround broken ocamlopt version detection with beta ocaml versions
sed -i 's/^\(ocamlopt_version=`.*\)\(`\)/\1 | cut -d+ -f1\2/' configure

# Force native compilation when available
%ifarch %{ocaml_native_compiler}
sed -i 's/@COQC@ -R src Gappa/& -native-compiler yes/' Remakefile.in
%endif

%build
# The %%configure macro specifies --libdir, which this configure script
# unfortunately uses to identify where the Coq files should go.  We want
# the default (i.e., ask coq itself where they go).
./configure --prefix=%{_prefix} --datadir=%{_datadir}

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake

remake -d %{?_smp_mflags}

%install
sed -i '/^install:/,/^EXTRA_DIST/s, /usr, %{buildroot}%{_prefix},' Remakefile
mkdir -p %{buildroot}%{gappadir}
remake install
cp -a src/.coq-native %{buildroot}%{gappadir}

# Also install the source files
cp -p src/*.v  %{buildroot}%{gappadir}

%check
remake check

%files
%doc AUTHORS NEWS.md README.md
%license COPYING
%{gappadir}
%exclude %{gappadir}/*.v

%files source
%{gappadir}/*.v

%changelog
* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-1
- Version 1.4.4

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-4
- Rebuild for flocq 3.3.1

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-3
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.3-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-1
- Version 1.4.3
- Drop -coq811 patch in favor of upstream's solution

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-6
- Add -coq811 patch to fix the build with coq 8.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.2-3
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 1.4.2-2
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream release
- Add a check script

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-3
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-2
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream release
- Build with camlp5 since coq now requires it instead of camlp4
- Drop now unneeded patch for building with camlp4
- Drop upstreamed safe-string patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-11
- OCaml 4.06.0 rebuild.

* Thu Oct  5 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-10
- Rebuild for flocq 2.6.0

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-9
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-6
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-5
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-4
- Rebuild to fix coq consistency issue

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Rebuild for coq 8.6

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream release

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-4
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Rebuild for coq 8.5pl3

* Mon Oct 03 2016 Dan Horák <dan[at]danny.cz> - 1.3.1-2
- disable debuginfo subpackage on interpreted builds

* Thu Sep 29 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream release

* Fri Jul 22 2016 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-3
- Rebuild for coq 8.5pl2

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-2
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream release
- Use camlp4 in preference to camlp5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream release

* Thu Jul 30 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-3
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- ocaml-4.02.2 final rebuild.

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream release

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-21
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 1.0.0-19
- Rebuild for coq 8.4pl6

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-18
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-17
- Rebuild for ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-16
- Rebuild for coq 8.4pl5

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-15
- Rebuild for flocq 2.4.0

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-14
- ocaml-4.02.0 final rebuild.

* Mon Aug 25 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-13
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-12
- Add workaround for ocamlopt beta version string
- Fix license handling

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-11
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-9
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-8
- Rebuild for flocq 2.3.0

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-7
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-6
- Rebuild for flocq 2.2.2

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-5
- Rebuild for coq 8.4pl3

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-4
- Rebuild for OCaml 4.01.0
- Enable debuginfo

* Mon Aug 12 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-3
- Rebuild for flocq 2.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream release

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 0.21.1-1
- New upstream release

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.20.0-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.18.0-6
- Rebuild for coq 8.4pl1

* Fri Oct 19 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-5
- Rebuild for OCaml 4.00.1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-4
- Rebuild for coq 8.4

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-3
- Rebuild for coq 8.3pl4, OCaml 4.00.0, and gappa 0.16.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- New upstream release

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 0.17.0-2
- Rebuild for coq 8.3pl3

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 0.17.0-1
- New upstream release

* Sat Oct 29 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-3
- BR ocaml

* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Initial RPM
