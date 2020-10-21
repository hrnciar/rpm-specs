Name:     gprolog
Version:	1.4.5
Release:	6%{?dist}
Summary: 	GNU Prolog is a free Prolog compiler

License:	GPLv2+
URL: 		http://www.gprolog.org
Source: 	http://www.gprolog.org/gprolog-%{version}.tar.gz
Patch0:   gprolog.make-print-submake-output.patch

BuildRequires:  gcc-c++
BuildRequires:  gdb-headless

ExclusiveArch:	x86_64 %{ix86} ppc alpha

Obsoletes:	gprolog-examples < 1.4.0
Provides:	gprolog-examples = %{version}-%{release}

%description 
GNU Prolog is a native Prolog compiler with constraint solving over
finite domains (FD) developed by Daniel Diaz
(http://loco.inria.fr/~diaz).

GNU Prolog is a very efficient native compiler producing (small)
stand-alone executables. GNU-Prolog also offers a classical
top-level+debugger.

GNU Prolog conforms to the ISO standard for Prolog but also includes a
lot of extensions (global variables, DCG, sockets, OS interface,...).

GNU Prolog also includes a powerful constraint solver over finite
domains with many predefined constraints+heuristics.


%package docs
Summary:	Documentation for GNU Prolog
Requires:	%{name} = %{version}-%{release}

%description docs
Documentation for GNU Prolog.

%prep
%autosetup -p1

%build
# This package fails to build with LTO due to undefined symbols.  LTO
# was disabled in OpenSuSE as well, but with no real explanation why
# beyond the undefined symbols.  It really shold be investigated further.
# Disable LTO
%define _lto_cflags %{nil}

cd src

# BZ #1799464
%define _legacy_common_support 1

# See http://lists.gnu.org/archive/html/bug-prolog/2016-08/msg00006.html
# for the discussion on adding '--disable-regs'
./configure \
      --with-install-dir=$RPM_BUILD_ROOT%{_libdir}/gprolog-%{version} \
      --without-links-dir --without-examples-dir \
      --with-doc-dir=dist-doc \
      --with-c-flags="$RPM_OPT_FLAGS" \
      --disable-regs

# _smp_flags seems to make trouble
make

%check
cd src
#
export PATH=$RPM_BUILD_ROOT%{_bindir}:$PATH
#
make check

%install
cd src
(
    make install
    mkdir $RPM_BUILD_ROOT%{_bindir}
    cd $RPM_BUILD_ROOT%{_libdir}/gprolog-%{version}/bin
    for i in *; do
 	ln -s ../%{_lib}/gprolog-%{version}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
    done
)
rm -f dist-doc/*.{chm,dvi,ps}
rm -f dist-doc/compil-scheme.pdf
rm -f dist-doc/debug-box.pdf

for file in ChangeLog COPYING NEWS VERSION
do
    rm -f $RPM_BUILD_ROOT%{_libdir}/gprolog-%{version}/$file
done

%files
%doc README COPYING ChangeLog NEWS PROBLEMS VERSION
%{_bindir}/*
%{_libdir}/gprolog-%{version}

%files docs
%doc src/dist-doc/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 1.4.5-5
- Disable LTO

* Mon Feb 17 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.4.5-4
- Add -fcommon to fix FTBFS #1799464
- Add BR: gdb-headless
- Adapt patch to display the output of sub-make

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Till Hofmann <thofmann@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.4.4-13
- Remove unnecessary defattrs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 27 2016 Till Hofmann <till.hofmann@posteo.de> - 1.4.4-8
- Add patch to pipe make's output in rm_make to /dev/null instead of /tmp/make

* Fri Aug 26 2016 Till Hofmann <till.hofmann@posteo.de> - 1.4.4-7
- Add --disable-regs to fix FTBFS (#1307590)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.4-1
- New upstream release

* Mon Apr  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.3-1
- Update to 1.4.3

* Sat Feb  2 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.2-2
- Fix wrong license specification

* Sat Dec 15 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.2-1
- New upstream release

* Thu Oct  4 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.1-2
- Remove reference to test pach

* Thu Oct  4 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.1-1
- New upstream release
- Clean up SPEC file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.4.0-4
- Add additioal comment about state of PPC build patch

* Wed Nov 30 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.4.0-3
- Fix PPC build issue (#758825)

* Sun Jul  3 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.4.0-2
- Built with $$RPM_OPT_FLAGS (#718457)

* Wed Jun 29 2011 Jochen Schmitt <s4504kr@omega.inet.herr-schmitt.de> 1.4.0-1
- New upstream release (#717592)
- Remove examples subpackage
- Fix FTBFS (#715840)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-4
- Fix dependency issue

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-3
- Supporting noarch subpackages

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.3.1-1
- New upstream release

* Mon Jun 16 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-17
- Remove TRAILSZ and GLOBALSZ environment variables

* Sun Jun 15 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-16
- Fix FTBFS (#440495)

* Wed Apr  9 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-15
- Exclude x86_64 because a build failure (#440945)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 1.3.0-14
- Autorebuild for GCC 4.3

* Sun Feb 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-13
- Rebuild for gcc-4.3

* Wed Jan 23 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-12
- Rebuild

* Tue Oct  9 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-11
- Add the alpha architecture to tue supported plattforms (#313571)

* Wed Aug  8 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-10
- Changing license tag

* Wed Jun 13 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-9
- Rebuild to solve a koji issue.

* Thu May 24 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-8
- Include the PPC arch to build
- Remove _smp_mflags becouse is make trouble
- Used unmodified optflags

* Sun Mar 25 2007 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-1
- New upstream version

* Thu Sep  7 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-8
- Fix broken symlib (#205118)

* Mon Sep  4 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-7
- Exclude PPC arch, becouse it produced a strange error on FC-6

* Sun Sep  3 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-6
- Rebuild for FC-6

* Mon May 15 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-5
- Remove compil-scheme.pdf and debug-box.pdf from the docs package

* Wed Apr 19 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-3
- Delete unnecessaries files from ExamplesPI

* Thu Mar 30 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-2
- Remove sed-command
- Correct typo about usable compiler options
- Add comment about the source of the patches

* Wed Mar 29 2006 Jochen Schmitt <Jochen herr-schmitt de> 1.2.19-1
- Initial RPM package for Fedora Extras
