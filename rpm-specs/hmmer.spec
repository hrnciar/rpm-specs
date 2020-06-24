Name:           hmmer
Version:        3.1b2
Release:        13%{?dist}
Summary:        Profile HMM software for protein sequence analysis

License:        GPLv3
URL:            http://hmmer.janelia.org
Source0:        http://selab.janelia.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz
BuildRequires:  perl

%description
Profile hidden Markov models (profile HMMs) can be used to do sensitive
database searching using statistical descriptions of a sequence family's
consensus.  HMMER is a freely distributable implementation of profile HMM
software for protein sequence analysis.

%package devel
Summary: Library and header files to include hmmer code in other apps
Provides: hmmer-static = %{version}-%{release}

%description devel

Header files and a library of hmmer functions, for developing apps
which will use the library.

%package doc
Summary: Documentation for hmmer
BuildArch: noarch

%description doc
This package includes documentation files for the hmmer software package.


%prep
%setup -q
# See if this helps building on power arch
sed -i '/impl_choice=vmx;;/d' configure


%build
%configure
make %{?_smp_mflags}


%check
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT



%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*


%files devel
%{_includedir}/*
%{_libdir}/*.a


%files doc
%doc COPYRIGHT README release-notes Userguide.pdf tutorial/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-8
- Add missing BuildRequires for perl - needed in the test suite
- #1423711 fix FTBFS

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1b2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-3
- #1284297 provide -static package as per guidelines
- try to fix build failure on power arch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1b2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b2-1
- Update to new upstream version

* Sat Feb 28 2015 Christian Iseli <Christian.Iseli@unil.ch> - 3.1b1-1
- Update to new upstream version
- Split -devel and -doc subpackages
- perl script fix no longer needed

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Christian Iseli <Christian.Iseli@unil.ch> - 3.0-7
- BuildRoot is no longer necessary
- BuildRequire autoconf and run autoreconf prior to configure (#925551)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Christian Iseli <Christian.Iseli@unil.ch> - 3.0-5
- Fix build failure due to old (perl4) code in the test suite

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> - 3.0-1
- New upstream version 3.0
- License is now GPLv3
- configure defaults to multi-threaded
- make install now uses DESTDIR
- copy manpages (rule missing in Makefile, apparently)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-9
- Rebuild for F-11
- Change URL and Source0 links to new location

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.2-8
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-7
 - Fix License tag to GPLv2+.

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-6
 - Rebuild for FC 6.

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-5
 - Minor spec cleanup.  Rebuild for FE 5.

* Fri Dec 23 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-4
 - Rebuild with gcc-4.1.

* Mon Aug 08 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-3
 - Removed altivec switch for ppc: apparently, it only works using Apple's
   GCC compiler.

* Sat Aug 06 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-2
 - Fix spec file according to review.

* Fri Aug 05 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-1
 - Create spec file.
