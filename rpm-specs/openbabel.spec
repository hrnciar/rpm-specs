%global commit 3a63a9849f8d9719c5989c43875d51be50c53019
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%{!?perl_vendorarch:%global perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)}

# we don't want to provide private Perl or Python extension libs
%global __provides_exclude_from ^(%{perl_vendorarch}/auto|%{python3_sitearch})/.*\\.so$

Name: openbabel
Version: 2.4.1
Release: 30%{?dist}
Summary: Chemistry software file format converter
License: GPLv2
URL: https://openbabel.org/
Source0: https://github.com/openbabel/openbabel/archive/openbabel-%(echo %{version} | tr '.' '-').tar.gz
Source1: obgui.desktop
# fix perl modules install path
Patch1: %{name}-perl.patch
# fix plugin directory location (#680292, patch by lg)
Patch4: openbabel-plugindir.patch
# fix SWIG_init even when not using swig (#772149)
Patch6: openbabel-noswig-rubymethod.patch
# On F-17, directory for C ruby files changed to use vendorarch directory
Patch7: openbabel-ruby19-vendorarch.patch
# temporarily disable some tests on:
# - ppc64 and s390(x) to unblock other builds (#1108103)
# - ARM (#1094491)
# - aarch64 (#1094513)
# Upstream bugs: https://sourceforge.net/p/openbabel/bugs/927/ https://sourceforge.net/p/openbabel/bugs/945/
Patch8: openbabel-disable-tests.patch
Patch9: openbabel-narrowing-conversion.patch
# Fix path to libdir in .pc file
# https://bugzilla.redhat.com/show_bug.cgi?id=1669664
Patch10: openbabel-fix-libdir-in-pkgconfig.patch
# Math 4 test is failing on s390x only
Patch11: openbabel-disable-tests-s390x.patch
# Fix inconsistent whitespace
Patch12: openbabel-taberror.patch
# Fix import of dl module in python3.7
# https://github.com/openbabel/openbabel/pull/372
Patch13: openbabel-python-dl.patch
BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: inchi-devel >= 1.0.3
BuildRequires: libxml2-devel
BuildRequires: swig
BuildRequires: wxGTK3-devel
BuildRequires: ImageMagick

%description
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the command-line utility, which is intended to
be used as a replacement for the original babel program, to translate
between various chemical file formats as well as a wide variety of
utilities to foster development of other open source scientific
software.

%package devel
Summary: Development tools for programs which will use the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package includes the header files and libraries
necessary for developing programs using the Open Babel library.

%package doc
Summary: Additional documentation for the Open Babel library
BuildArch: noarch

%description doc
This package contains additional documentation for Open Babel.

%package gui
Summary: Chemistry software file format converter - GUI version

%description gui
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the graphical interface.

%package libs
Summary: Chemistry software file format converter - libraries

%description libs
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the C++ library, which includes all of the
file-translation code.

%package -n perl-%{name}
Summary: Perl wrapper for the Open Babel library
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: perl-devel
BuildRequires: perl-generators

%description -n perl-%{name}
Perl wrapper for the Open Babel library.

%package -n python3-%{name}
Summary: Python wrapper for the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{name}}
Obsoletes: python2-%{name} < 2.4.1-21

%description -n python3-%{name}
Python3 wrapper for the Open Babel library.

%package -n ruby-%{name}
Summary: Ruby wrapper for the Open Babel library
Requires: ruby(release)
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: ruby-devel

%description -n ruby-%{name}
Ruby wrapper for the Open Babel library.

%prep
%setup -q -n %{name}-%{name}-%(echo %{version} | tr '.' '-')
%patch1 -p1 -b .perl_path
%patch4 -p1 -b .plugindir
%patch6 -p1 -b .noswig_ruby
%patch7 -p1 -b .ruby_vendor
%ifarch aarch64 %{arm} %{power64} s390 s390x
%patch8 -p1 -b .tests
%endif
%ifarch s390x
%patch11 -p1 -b .s390x
%endif
%patch9 -p1 -b .nc
%patch10 -p1
%patch12 -p1 -b .taberr
%patch13 -p1 -b .py3dl
# convert to Unix line endings
dos2unix -k \
  data/chemdrawcdx.h \
  include/openbabel/{tautomer.h,math/align.h} \
  src/math/align.cpp \
  test/testsmartssym.py \

convert src/GUI/babel.xpm -transparent white babel.png

# Remove duplicate html files
pushd doc
for man in *.1; do
 html=`basename $man .1`.html
 if [ -f $html ]; then
   rm $html
 fi
done
popd

%build
%cmake \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DBUILD_GUI:BOOL=ON \
 -DPYTHON_BINDINGS:BOOL=ON \
 -DPYTHON_EXECUTABLE=%{__python3} \
 -DPERL_BINDINGS:BOOL=ON \
 -DRUBY_BINDINGS:BOOL=ON \
 -DOPENBABEL_USE_SYSTEM_INCHI=true \
 -DENABLE_VERSIONED_FORMATS=false \
 -DRUN_SWIG=true \
 -DENABLE_TESTS:BOOL=ON \
 -DOPTIMIZE_NATIVE=OFF \
 .
make VERBOSE=1 %{?_smp_mflags}

%install
make VERBOSE=1 DESTDIR=%{buildroot} install

rm %{buildroot}%{_libdir}/cmake/openbabel2/*.cmake

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm644 babel.png %{buildroot}%{_datadir}/pixmaps/babel.png

%if 1
%check
# rm the built ruby bindings for testsuite to succeed (bug #1191173)
rm %{_lib}/openbabel.so
export CTEST_OUTPUT_ON_FAILURE=1 PYTHONPATH=%{buildroot}%{python3_sitearch}
%make_build test
%endif

%ldconfig_scriptlets libs

%files
%{_bindir}/babel
%{_bindir}/ob*
%{_bindir}/roundtrip
%{_mandir}/man1/*.1*
%exclude %{_bindir}/obgui
%exclude %{_mandir}/man1/obgui.1*

%files devel
%{_includedir}/%{name}-2.0
%{_libdir}/libopenbabel.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc doc/*.html doc/README* doc/dioxin.*

%files gui
%{_bindir}/obgui
%{_datadir}/applications/obgui.desktop
%{_datadir}/pixmaps/babel.png
%{_mandir}/man1/obgui.1*

%files libs
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_libdir}/libopenbabel.so.*

%files -n perl-%{name}
%{perl_vendorarch}/Chemistry/OpenBabel.pm
%dir %{perl_vendorarch}/*/Chemistry/OpenBabel
%{perl_vendorarch}/*/Chemistry/OpenBabel/OpenBabel.so

%files -n python3-%{name}
%{python3_sitearch}/_openbabel.so
%{python3_sitearch}/openbabel.py
%{python3_sitearch}/pybel.py
%{python3_sitearch}/__pycache__/*

%files -n ruby-%{name}
%{ruby_vendorarchdir}/openbabel.so

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-30
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-29
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.1-27
- F-32: rebuild against ruby27

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-26
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-25
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Petr Pisar <ppisar@redhat.com> - 2.4.1-23
- Obsolete by name only (bug #1685183)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-22
- Perl 5.30 rebuild

* Fri Mar 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.4.1-21
- drop python2 subpackage (#1648558)
- fix running the testsuite with python3
- fix line endings for some source files

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.1-19
- F-30: rebuild again against ruby26

* Sun Jan 27 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.4.1-18
- Fix path to libdir in .pc (#1669664)
- Use https for URL:
- Exclude obgui from the main openbabel package
- Disable failing test on s390x/F29+

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.1-17
- F-30: rebuild against ruby26

* Wed Nov 07 2018 Scott Talbert <swt@techie.net> - 2.4.1-16
- Rebuild with wxWidgets 3.0
- Exclude obgui from the main openbabel package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 2.4.1-14
- Perl 5.28 rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-13
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-12
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.1-10
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.1-9
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.1-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 2.4.1-3
- Rebuild for eigen3-3.3.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-2
- Rebuild for Python 3.6

* Tue Oct 11 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.4.1-1
- update to 2.4.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.90-0.11.20160216git3a63a98
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.90-0.10.20160216git3a63a98
- Perl 5.24 rebuild

* Thu Feb 18 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.3.90-0.9.20160216git3a63a984
- drop redundant BuildRoot and defattr
- fix macro usage
- update to current Git master HEAD
- fix narrowing conversion compilation error
- add python3 subpackage (#1285258)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.90-0.8.20150402gita345105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 2.3.90-0.7.20150402gita345105
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.90-0.6.20150402gita345105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.90-0.5.20150402gita345105
- Perl 5.22 rebuild

* Thu Apr 16 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.3.90-0.4.20150402gita345105
- updated to current Git master HEAD
- dropped obsolete patches

* Wed Mar 25 2015 Rex Dieter <rdieter@fedoraproject.org> 2.3.90-0.3.20150204git
- rebuild (gcc5)

* Thu Feb 12 2015 Dominik Mierzejewski <rpm@greysector.net> 2.3.90-0.2.20150204git75414ad
- restore disttag, which got accidentally removed during last rebase

* Sat Feb 07 2015 Dominik Mierzejewski <rpm@greysector.net> 2.3.90-0.1.20150204git75414ad
- update to current Git master HEAD
- drop obsolete patches
- rebase remaining patches
- drop zlib-devel from BR (required by libxml2-devel)
- add gcc-c++ to BR
- fix building bindings with swig-3.x
- drop old Obsoletes: and Provides:
- rm the built ruby bindings for testsuite to succeed (bug #1191173)

* Tue Jan 27 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.3.2-11
- Unify patches which disable tests on ppc64, s390(x), arm and enable
  result also for aarch64. rhbugs: #1108103 #1094491 #1094513

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.2-10
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Remove deprecated Config:: usage

* Thu Nov 13 2014 Dan Horák <dan[at]danny.cz> - 2.3.2-9
- disable some tests also on s390(x)

* Wed Oct 15 2014 Karsten Hopp <karsten@redhat.com> 2.3.2-8
- disable some tests on ppc64 to unblock other builds (#1108103)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.2-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Dominik Mierzejewski <rpm@greysector.net> 2.3.2-4
- fix and enable testsuite
- drop ancient Obsoletes: (rhbz#1002135)
- drop ruby < 2.0 conditional Requires:
- temporarily disable two tests failing on ARM (rhbz#1094491)

* Fri Apr 25 2014 Vít Ondruch <vondruch@redhat.com> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.3.2-2
- Perl 5.18 rebuild

* Thu Jul 18 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.2-1
- Turned off versioned formats.
- Filter out private provides.
- Update to 2.3.2.

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.3.1-9
- Perl 5.18 rebuild

* Fri Mar 22 2013 Vít Ondruch <vondruch@redhat.com> - 2.3.1-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2.3.1-5
- Perl 5.16 rebuild

* Fri Apr  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.3.1-4
- Fix several issues related to ruby modules
 - Fix build with gcc47 (on Linux)
 - Fix SWIG_init even when not using swig (#772149)
 - Use vendorarchdir instead of sitearch on F-17+
 - Fix ruby(abi) requirement

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Dominik Mierzejewski <rpm@greysector.net> 2.3.1-1
- update to 2.3.1
- drop obsolete patches (merged upstream)
- add desktop file for the GUI

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.3.0-5
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.3.0-4
- Perl 5.14 mass rebuild

* Tue Mar 22 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.3.0-3
- fix plugin directory location (#680292, patch by lg)
- show forcefields list in obenergy output (#680292, patch by lg)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Dominik Mierzejewski <rpm@greysector.net> 2.3.0-1
- build system switched to cmake
- enabled GUI
- enabled Eigen2
- updated to 2.3.0 final
- patched to fix various build issues
- split libs and GUI into separate subpackages
- fixed rpmlint warnings about strange file permissions

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 07 2010 Dominik Mierzejewski <rpm@greysector.net> 2.2.3-3
- rebuild against inchi 1.0.3

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.3-2
- Mass rebuild with perl-5.12.0

* Wed Aug 26 2009 Dominik Mierzejewski <rpm@greysector.net> 2.2.3-1
- updated to 2.2.3
- dropped obsolete patch
- fixed configure to detect external inchi (both pre-1.0.2 and 1.0.2)
- re-enabled inchi tests

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-0.2.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Dominik Mierzejewski <rpm@greysector.net> 2.2.1-0.1.b3
- update to 2.2.1 beta3
- drop some obsolete workarounds

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.2.0-2
- Rebuild for Python 2.6

* Sun Jul 06 2008 Dominik Mierzejewski <rpm@greysector.net> 2.2.0-1
- updated to 2.2.0
- new URL
- dropped Python binding split patch (broken, reverted upstream)
- fixed testsuite and disabled inchi tests temporarily
- added strict perl version requirements (patch by Paul Howarth, bug #453120)
- fixed some rpmlint warnings
- merged a sed call into -rpm patch

* Fri Jun 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.2.0-0.5.b5
- backport upstream patch to split Python binding (should fix #427700 for good)
- drop no longer needed ppc64 SWIG/GCC flag hackery

* Thu May 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.2.0-0.4.b5
- update to 2.2.0 beta5

* Fri May 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.2.0-0.3.b4
- generate Python binding with -fastdispatch on F9+ ppc64 (#427700)
- add -mno-sum-in-toc to optflags on F9+ ppc64 (#427700)

* Sun Mar 02 2008 Dominik Mierzejewski <rpm@greysector.net> 2.2.0-0.2.b4
- updated to 2.2.0 beta4
- enable CML tests again (fixed upstream)

* Fri Feb 22 2008 Dominik Mierzejewski <rpm@greysector.net> 2.2.0-0.1.b3
- updated to 2.2.0 beta3
- renamed language bindings subpackages
- added ruby bindings
- fixed ruby buildings build with local shared lib
- disable CML tests (broken upstream)

* Mon Jan 07 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-4
- work around gcc bug: http://gcc.gnu.org/PR34708

* Sun Jan 06 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-3
- fix build with gcc-4.3
- include python egg-info

* Wed Nov 28 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-2
- build against external inchi

* Fri Aug 17 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.1-1
- updated to 2.1.1
- better work around for testsuite crash
- updated the License tag according to the new guidelines

* Tue Apr 17 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-2
- work around testsuite crash

* Mon Apr 16 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-1
- updated to 2.1.0 final

* Thu Mar 29 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-0.3.b8
- updated to beta8
- dropped upstream'd patch

* Sun Mar 18 2007 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-0.2.b6
- updated to beta6
- dropped upstream'd patch
- fixed my name in ChangeLog
- copied inchi header for inchi-devel (TODO: make inchi a separate package)
- added %%check

* Sun Dec 17 2006 Dominik Mierzejewski <rpm@greysector.net> 2.1.0-0.1.b4
- update to 2.1.0b4 to fix building with new python
- dropped obsolete patch
- ensure proper inchi versioning

* Tue Oct 03 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-5
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-4
- .pyo files no longer ghosted
- fix chicken-and-egg problem when building perl and python bindings

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-3
- simplified autotools invocation
- mass rebuild

* Mon Aug 07 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-2
- simplified file lists and permissions
- removed weird character from inchi summary and description
- added missing pkgconfig Req: for -devel

* Sat Aug 05 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.2-1
- updated to 2.0.2
- dropped GCC4 fix (upstream'd)
- split off inchi package
- added python and perl bindings packages

* Sat Jan 07 2006 Dominik Mierzejewski <rpm@greysector.net> 2.0.0-1
- updated to 2.0.0
- fix compilation with GCC4
- FE compliance

* Thu Feb 10 2005 Dominik Mierzejewski <rpm@greysector.net> 1.100.2-1
- rebuilt for Fedora 3

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.100.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Wed Mar 03 2004 Michael Shigorin <mike@altlinux.ru> 1.100.2-alt1
- 1.100.2

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 1.100.1-alt2
- removed *.la
- don't package static library by default

* Mon Sep 22 2003 Michael Shigorin <mike@altlinux.ru> 1.100.1-alt1
- 1.100.1
- #2994 fixed; thanks to Alex Ott (ott@) for a pointer
- spec cleanup (underlibification fixup)

* Mon Jun 30 2003 Michael Shigorin <mike@altlinux.ru> 1.100.0-alt1
- built for ALT Linux
- based on Mandrake Cooker spec by:
  * Lenny Cartier <lenny@mandrakesoft.com>
  * Austin Acton <aacton@yorku.ca>
- spec cleanup
