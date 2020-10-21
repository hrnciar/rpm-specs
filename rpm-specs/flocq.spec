# This package is installed into an archful location, but contains no ELF
# objects.
%global debug_package %{nil}

%global flocqdir %{_libdir}/ocaml/coq/user-contrib/Flocq
%global coqver 8.12.0

Name:           flocq
Version:        3.3.1
Release:        7%{?dist}
Summary:        Formalization of floating point numbers for Coq

License:        LGPLv3+
URL:            http://flocq.gforge.inria.fr/
Source0:        https://gforge.inria.fr/frs/download.php/file/38329/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  remake
BuildRequires:  coq = %{coqver}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Requires:       coq%{?_isa} = %{coqver}

# https://bugzilla.redhat.com/show_bug.cgi?id=1874879
ExcludeArch:    s390x

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Coq files for flocq.  These files are
not needed to use flocq.  They are made available for informational
purposes.

%prep
%autosetup -p1

%build
# We do NOT want to specify --libdir, and we don't need CFLAGS, etc.
./configure

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags} all doc

%install
sed -i "s,%{_libdir},$RPM_BUILD_ROOT%{_libdir}," Remakefile
remake install

# Also install the source files
cp -p src/*.v $RPM_BUILD_ROOT%{flocqdir}
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/IEEE754/*.v $RPM_BUILD_ROOT%{flocqdir}/IEEE754
cp -p src/Pff/*.v $RPM_BUILD_ROOT%{flocqdir}/Pff
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

# And the opam file
cp -p opam $RPM_BUILD_ROOT%{flocqdir}

%files
%doc AUTHORS NEWS.md README.md html
%license COPYING
%{flocqdir}
%exclude %{flocqdir}/*.v
%exclude %{flocqdir}/*/*.v

%files source
%{flocqdir}/*.v
%{flocqdir}/Calc/*.v
%{flocqdir}/Core/*.v
%{flocqdir}/IEEE754/*.v
%{flocqdir}/Pff/*.v
%{flocqdir}/Prop/*.v

%changelog
* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-7
- Flocq is installed in an archful directory, so cannot be noarch
- ExcludeArch s390x due to bz 1874879

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.1-6
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-5
- Rebuild for coq 8.12.0
- Revert to a noarch package

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.1-5
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-4
- Rebuild to fix OCaml dependencies

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-2
- Rebuild for coq 8.11.2

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-3
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.2.1-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-1
- Version 3.2.1
- Drop -coq811 patch in favor of upstream's solution

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.2.0-8
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-7
- Add -coq811 patch so gappalib-coq can be built with coq 8.11

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-6
- Rebuild for coq 8.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 3.2.0-3
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-2
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- New upstream release

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-8
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-7
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 2.6.0-6
- Rebuild for coq 8.7.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-4
- Rebuild against new Coq package.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-3
- Bump release and rebuild.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- OCaml 4.06.0 rebuild.

* Thu Oct  5 2017 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream release

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-12
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-9
- Bump release and rebuild.

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-8
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-7
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-6
- Rebuild to fix coq consistency issue

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-4
- Rebuild for coq 8.6

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-3
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-2
- Rebuild for coq 8.5pl3

* Thu Sep 29 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-3
- Rebuild for coq 8.5pl2

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-2
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- New upstream release

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-10
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-9
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 2.4.0-7
- Rebuild for coq 8.4pl6

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-6
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-5
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-4
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-3
- Rebuild with coq that was rebuilt with ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-2
- Rebuild for coq 8.4pl5

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- New upstream release

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-9
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-8
- Bump release and rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-7
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-4
- Bump and rebuild as part of ocaml rebuild
- Fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-2
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- New upstream release
- Remove ocaml_arches macro (bz 1087794)

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- New upstream release

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Rebuild for coq 8.4pl3

* Sat Aug 10 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- New upstream release
- Builds now done with remake instead of make

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-5
- Rebuild for coq 8.4pl2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-3
- Rebuild for coq 8.4pl1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-2
- Rebuild for coq 8.4

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- New upstream release
- Build for OCaml 4.0.0 and coq 8.3pl4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 2.0.0-3
- Rebuild for OCaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-2
- Rebuild for coq 8.3pl3

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- New upstream release
- Change subpackage from -devel to -source to match gappalib-coq.

* Fri Oct 28 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-3
- Fix broken version numbers in BR and Requires

* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Initial RPM
