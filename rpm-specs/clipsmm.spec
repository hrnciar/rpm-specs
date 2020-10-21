%global clipsver 6.30

Summary:          C++ interface to the CLIPS expert system C library
Name:             clipsmm
Version:          0.3.5
Release:          9%{?dist}
License:          GPLv3
URL:              http://clipsmm.sourceforge.net
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# https://github.com/timn/clipsmm/pull/1
Patch0:           clipsmm.fix-multifield-retval-with-multi-env.patch
# https://github.com/timn/clipsmm/pull/2
Patch1:           clipsmm.fix-add-symbol-with-multiple-environments.patch
BuildRequires:    clips-devel >= %{clipsver} 
BuildRequires:    gcc-c++
BuildRequires:    glibmm24-devel >= 2.6.0 
BuildRequires:    cppunit-devel >= 1.11 
BuildRequires:    doxygen, libxslt
BuildRequires:    pkgconfig, m4, libtool

%description
The clipsmm library provides a C++ interface to the CLIPS C library.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%package          devel
Summary:          Headers for developing C++ applications with CLIPS
Requires:         %{name} = %{version}-%{release}
Requires:         clips-devel >= %{clipsver} 
Requires:         glibmm24-devel >= 2.6.0 
Requires:         pkgconfig

%description    devel
This package contains the libraries and header files needed for
developing clipsmm applications.

clipsmm provides a C++ interface to the CLIPS C library.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%package          doc
Summary:          Documentation for the C++ clipsmm library
Requires:         devhelp
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:        noarch
%endif

%description      doc
This package contains developer's documentation for the clipsmm
library. clipsmm provides C++ based bindings for the C based
CLIPS library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser. 

If using a web browser the documentation is installed in the gtk-doc
hierarchy and can be found at /usr/share/gtk-doc/html/clipsmm-0.3

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the
construction of rule and/or object based expert systems.

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now
widely used throughout the government, industry, and academia.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --enable-static=no --enable-unit-tests --enable-doc
%{__make} %{?_smp_mflags}
make docs

%install
%{__make} DESTDIR=%{buildroot} INSTALL="%{__install} -p" install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%{__mkdir} -p %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/reference/html/
%{__install} -p --mode=0664 -t %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/reference/html/ doc/reference/html/*
%{__install} -p --mode=0664 -t %{buildroot}%{_datadir}/gtk-doc/html/clipsmm-0.3/ doc/clipsmm-0.3.devhelp

%check
cd unit_tests
./clipsmm_unit_tests

%files
%{_libdir}/libclipsmm.so.*
%doc AUTHORS COPYING

%files devel
%{_libdir}/libclipsmm.so
%{_libdir}/pkgconfig/clipsmm-1.0.pc
%{_includedir}/clipsmm-0.3/
%doc ChangeLog

%files doc
%doc %{_datadir}/gtk-doc/html/clipsmm-0.3/
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.3.5-6
- Add patch from upstream PR #2 to fix AddSymbol with multiple environments

* Wed May 15 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.3.5-5
- Add patch to fix multifield return values with multiple environments

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Tim Niemueller <tim@niemueller.de> - 0.3.5-1
- Upgrade to 0.3.5

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Tim Niemueller <tim@niemueller.de> - 0.3.4-1
- Upgrade to 0.3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tim Niemueller <tim@niemueller.de> - 0.3.3-1
- Upgrade to 0.3.3

* Tue Mar 05 2013 Tim Niemueller <tim@niemueller.de> - 0.3.2-1
- Upgrade to 0.3.2.

* Sat Feb 09 2013 Tim Niemueller <tim@niemueller.de> - 0.3.0-1
- Upgrade to 0.3.0

* Thu Sep 27 2012 Tim Niemueller <tim@niemueller.de> - 0.2.1-3
- Own gtk-doc dir and no longer depend on it, fixes #604341

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 04 2012 Tim Niemueller <tim@niemueller.de> - 0.2.1-1
- Upgrade to 0.2.1, fixes C++0x detection

* Sat Oct 29 2011 Tim Niemueller <tim@niemueller.de> - 0.2.0-1
- Upgrade to 0.2.0

* Fri Sep 30 2011 Tim Niemueller <tim@niemueller.de> - 0.1.0-5
- Added patch to extend functionality

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.1.0-3el
- Rebuilt for EPEL-6

* Tue Mar  9 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.1.0-3
- Add libtermcap dependency for Fedora <= 9 and EL <= 5

* Wed Sep  2 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.1.0-2
- Bump release to rebuild against newer clips

* Mon Jul 27 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.1.0-1
- New release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 03 2008 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.7-4
- Bump release for make-tag error

* Mon Mar 03 2008 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.7-3
- Added boost-devel dependency

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.7-2
- Autorebuild for GCC 4.3

* Sun Nov 12 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.7-1
- New release

* Sun Aug  6 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.6-1
- New release
- Added m4 to BuildRequires

* Mon Jul 31 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.5-1
- New release fixes autoconf generated headers
- Removed pkgconfig from BuildRequires
- Added pkgconfig to -devel Requires

* Sun Jul 30 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.4-2
- Changed make to %%{__make}
- Changed %%{name} to autoconf subst that puts specific name in devel requires
- Added comment regarding why cp occurs for docs
- Added package name to globs in so libs, .pc and demos
- Changed clips-libs BuildRequires to clips-devel
- Added cppunit-devel BuildRequires

* Sat Jul 29 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.4-1
- New release

* Fri Jul 21 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.3-1
- New release

* Thu Jul 20 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.2-1
- New release

* Sun Jun 25 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 0.0.1-1
- Initial release
