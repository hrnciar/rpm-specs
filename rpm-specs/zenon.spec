%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global coqver 8.12.0

Name:		zenon
Version:	0.8.4
Release:	17%{?dist}
Summary:	Automated theorem prover for first-order classical logic
License:	BSD
URL:		http://zenon-prover.org/
Source0:	https://github.com/zenon-prover/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	http://zenon-prover.org/zenlpar07.pdf
Source2:	%{name}-tptp-COM003+2.p
Source3:	%{name}-tptp-ReadMe
# Basic documentation (man pages). Submitted upstream 2008-07-25:
Source4:	%{name}.1
Source5:	%{name}-format.5
# Adapt to coq 8.9
Patch0:		%{name}-coq89.patch
# Adapt to ocaml 4.08 and later
Patch1:		%{name}-ocaml.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1874879
ExcludeArch: s390x

BuildRequires:	coq = %{coqver}
BuildRequires:	ghostscript-core
BuildRequires:	ImageMagick
BuildRequires:	ocaml

Requires:	coq%{?_isa} = %{coqver}
Requires:	coreutils

%description
Zenon is an automated theorem prover for first order classical logic
with equality, based on the tableau method.  Zenon can read input files
in TPTP, Coq, Focal, and its own Zenon format.  Zenon can directly
generate Coq proofs (proof scripts or proof terms), which can be
reinserted into Coq specifications.  Zenon can also be extended.

%prep
%autosetup -p0

cp -p %{SOURCE1} .

# Generate debuginfo
sed -i 's/^\(CAMLFLAGS = \).*/\1-g/' Makefile

%build
./configure -prefix %{_prefix} -libdir %{_datadir}/%{name} -sum md5sum

mkdir examples
cp -p %{SOURCE2} examples/tptp-COM003+2.p
cp -p %{SOURCE3} examples/tptp-ReadMe

# Work around Makefile errors (fails if no ocamlopt, uses _bytecode_ otherwise)
%ifarch %{ocaml_native_compiler}
  make %{?_smp_mflags} zenon.bin
  cp -p zenon.bin zenon
%else
  make %{?_smp_mflags} zenon.byt
  cp -p zenon.byt zenon
%endif
# Use of %%{?_smp_mflags} sometimes leads to build failures
make coq

%install
%make_install

install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_mandir}/man5/
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE5} %{buildroot}%{_mandir}/man5/

# Put the coq files where coq can find them
mkdir -p %{buildroot}%{_libdir}/coq/user-contrib
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/coq/user-contrib/Zenon

%check
# Sanity test. Can we prove TPTP v3.4.2 test COM003+2 (the halting problem)?
# tptp-ReadMe has test's license conditions ("must credit + note changes").
# TPTP from: http://www.cs.miami.edu/~tptp/TPTP/Distribution/TPTP-v3.4.2.tgz
result=`./zenon -p0 -itptp examples/tptp-COM003+2.p`
if [ "$result" = "(* PROOF-FOUND *)" ] ; then
 echo "Test succeeded"
else
 echo "TEST FAILED"
 false
fi

%files
%doc zenlpar07.pdf examples
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/coq/user-contrib/Zenon
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-17
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-16
- Rebuild for coq 8.12.0

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-16
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-13
- Rebuild for coq 8.11.2

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-12
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-10
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-9
- Rebuild for coq 8.11.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-7
- OCaml 4.10.0+beta1 rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-6
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-5
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-3
- Rebuild for coq 8.9.1
- Add -coq89 patch to adapt to coq 8.9.x

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- New upstream release
- Drop -unsafe-string workaround

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 0.8.2-11
- Rebuild for coq 8.7.1
- Compile with -unsafe-string until the code can be migrated

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 0.8.2-9
- Rebuild for coq 8.6.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 0.8.2-5
- Rebuild for coq 8.6

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 0.8.2-4
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-3
- Rebuild for coq 8.5pl3

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-2
- Rebuild for coq 8.5pl2

* Fri Jun 10 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream release

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- New upstream release

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-8
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-7
- Rebuild for coq 8.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 0.8.0-4
- Rebuild for coq 8.4pl6

* Wed Jan  7 2015 Jerry James <loganjerry@gmail.com> - 0.8.0-3
- Update URLs

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 0.8.0-2
- Rebuild for coq 8.4pl5

* Thu Oct 23 2014 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- New upstream release
- Sources for the icon are no longer provided
- Fix license handling

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-13
- Drop bz 921706 workaround; now unnecessary

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-11
- Rebuild for coq 8.4pl4
- Add workaround for bz 921706

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-10
- Remove ocaml_arches macro (bz 1087794)

* Sat Dec 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-9
- Pass -g to ocamlopt, don't strip executable too early.

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-8
- Rebuild for coq 8.4pl3
- Enable debuginfo generation

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  8 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-6
- Rebuild for coq 8.4pl2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-4
- Rebuild for coq 8.4pl1

* Thu Dec 13 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-3
- Rebuild for OCaml 4.00.1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-2
- Rebuild for coq 8.4

* Mon Jul 30 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-1
- New upstream release
- Install the coq files where coq can find them automatically

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.6.3-5
- Rebuild for OCaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-4
- Rebuild for coq 8.3pl3

* Mon Nov 14 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-3
- Change ExclusiveArch to %%{ocaml_arches}

* Thu Jul 14 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-2
- Move the coq files back to /usr/share to avoid a dependency on coq
- Add paper describing zenon to %%doc

* Tue Jul 12 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- New upstream release
- Drop unnecessary spec file elements (BuildRoot, etc.)
- Execstack flag clearing no longer necessary
- Build on exactly the arches that coq builds on
- Build the icons

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 22 2009 Dennis gilmore <dennis@ausil.us> - 0.5.0-7
- ExcludeArch sparc64  no ocaml

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-6
- Use bzipped upstream tarball.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Karsten Hopp <karsten@redhat.com> 0.5.0-4.1
- ocaml not available on mainframes, add excludearch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-3
- Add documentation for Zenon and its built-in format as man pages
  (man pages used so Debian, etc., will use them too)
- Fix release number so it increases everywhere

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-2.1
- macro fc8 failed, minor rebuild for Fedora 8

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-2
- Moved examples to an "examples" subdirectory in /usr/share/doc/NAME-VERSION
- Moved "check" to be after "install" in spec file (that's when it's executed)
- Exclude ppc64 for Fedora 8 (it works on 9 and 10, but not 8)

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-1
- Initial package
