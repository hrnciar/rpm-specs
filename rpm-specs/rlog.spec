Name:		rlog
Summary:	Runtime Logging for C++
Version:	1.4
Release:	30%{?dist}
License:	LGPLv2+
Url:		http://arg0.net/rlog
VCS:		http://rlog.googlecode.com/svn/trunk
Source0:	http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz.asc
BuildRequires:  gcc-c++
%ifarch %{valgrind_arches}
BuildRequires:	valgrind-devel
%endif
# For autoreconf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
RLog provides a flexible message logging facility for C++ programs and
libraries.  It is meant to be fast enough to leave in production code.

%package devel
Summary:	Runtime Logging for C++ - development files
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
BuildRequires:	doxygen tetex-latex

%description devel
Files needed for developing apps using rlog

%prep
%setup -q
# Disabled: rebuilding docs fails on latex
#%{__rm} -rf docs/html
#%{__rm} -rf docs/latex

%build
autoreconf -ivf
%configure --disable-static \
%ifarch %{valgrind_arches}
    --enable-valgrind
%else
    %{nil}
%endif
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/rlog

%ldconfig_scriptlets

%files
%{_libdir}/librlog.so.*
%doc README AUTHORS COPYING

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/librlog.so
%doc docs/html docs/latex/refman.pdf

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-18
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Dan Horák <dan[at]danny.cz> - 1.4-15
- fix build on arches without valgrind

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4-13
- Reconfigure to allow building on AArch64
- Cleanup spec-file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 20 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.4-8
- No valgrind for s390/s390x
- Drop support for Fedora < 8
- Enable valgrind on EL-6

* Sun Sep 27 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.4-7
- Fixed building against valgrind

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.4-5
- Fix FTBFS: do not rebuild docs as it fails on latex

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4-3
- Fixed url (BZ# 472665)

* Tue Sep  2 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4-2
- Fix build for F-8
- Fixed license header (LGLV21+ -> LGPLv2+)

* Sat Jul 12 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4-1
- Ver. 1.4
- Dropped upstreamed patch
- Enabled valgrind on all supported platforms

* Fri Jun  6 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.7-7
- Get rid of whitespaces (cosmetic)
- Note about patch status (applied upstream)

* Fri Feb 22 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.7-6
- Changed source paths
- Fixed build with GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.7-5
- Autorebuild for GCC 4.3

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.3.7-4
- Proper license header (LGPL v 2.1 or any later version)

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.3.7-3%{?dist}
- Rebuild for FC6

* Wed Mar 29 2006 Peter Lemenkov <lemenkov@newmail.ru> 1.3.7-2
- rebuild

* Sun Nov 13 2005 Peter Lemenkov <lemenkov@newmail.ru> 1.3.7-1
- Initial build for FC-Extras
- Release v1.3.7

* Mon Nov 8 2004 Valient Gough <vgough@pobox.com>
- Release v1.3.5
- Add initial attempt at Win32 support (due to help from Vadim Zeitlin)
- Fixes to build on Suse 9.2 (replaced old KDE based autoconf scripts)
- Add "info" channel, and rInfo() macro.
* Mon May 31 2004 Valient Gough <vgough@pobox.com>
- Release v1.3.4
- Portibility changes to allow rlog to build with older C++ compilers and on
  non-x86 computers.
- Add extra ERROR_FMT() macro which allows format string to be passed on Error
  construction.
- Add valgrind support to allow valgrind trace from any assert when running
  under valgrind.
- Update admin dir.
* Sat Mar 13 2004 Valient Gough <vgough@pobox.com>
- Release v1.3.1
- added pkg-config file librlog.pc
- changed license to LGPL
- added rAssertSilent macro
- fixes for special case checks of printf attribute
* Sat Feb 8 2004 Valient Gough <vgough@pobox.com>
- Release v1.3
