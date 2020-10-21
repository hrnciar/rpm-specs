%?mingw_package_header

%global name1 sqlite

%global realver 3330000
%global rpmver 3.33.0.0

# bcond default logic is nicely backwards...
%bcond_with tcl
%global tclversion 8.6

Name:           mingw-%{name1}
Version:        %{rpmver}
Release:        1%{?dist}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine

License:        Public Domain
URL:            http://www.sqlite.org/
Source0:        http://www.sqlite.org/2020/%{name1}-src-%{realver}.zip

BuildArch:      noarch

# Don't try to link against pthreads even if it is available
Patch1001:      sqlite-dont-search-for-pthreads-on-non-unix.patch

# Don't force build exe extension same as target exe extension
Patch1002:      sqlite-mingw-crosscompile.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-pdcurses
BuildRequires:  mingw32-readline
BuildRequires:  mingw32-termcap

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-pdcurses
BuildRequires:  mingw64-readline
BuildRequires:  mingw64-termcap

# For the pthread patch
BuildRequires:  autoconf automake libtool

BuildRequires:  /usr/bin/tclsh

%if %{with tcl}
BuildRequires:  /usr/bin/tclsh
BuildRequires:  mingw32-tcl
%endif


%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.


# Win32
%package -n mingw32-%{name1}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine
Requires:       pkgconfig

%description -n mingw32-%{name1}
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw32-%{name1}-static
Summary:        Static version of MinGW Windows port of sqlite library
Requires:       mingw32-%{name1} = %{version}-%{release}

%description -n mingw32-%{name1}-static
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains static cross-compiled library

# Win64
%package -n mingw64-%{name1}
Summary:        MinGW Windows port of sqlite embeddable SQL database engine
Requires:       pkgconfig

%description -n mingw64-%{name1}
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw64-%{name1}-static
Summary:        Static version of MinGW Windows port of sqlite library
Requires:       mingw64-%{name1} = %{version}-%{release}

%description -n mingw64-%{name1}-static
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexibility of an SQL database without the administrative hassles of
supporting a separate database server.  Version 2 and version 3 binaries
are named to permit each to be installed on a single host

This package contains static cross-compiled library


%?mingw_debug_package


%prep
%setup -q -n %{name1}-src-%{realver}
%patch1001 -p0 -b .pthread
%patch1002 -p0 -b .cc
autoreconf -i --force


%build
# I think there's a bug in the configure script where, if
# cross-compiling, it cannot correctly determine the target executable
# extension (ie. .exe).  As a result it doesn't correctly detect that
# the target is Windows and so tries to use Unix-specific functions
# which don't exist.  In any case we can work around this by forcing
# the extension via this export.
#   - RWMJ 2008-09-30
export config_TARGET_EXEEXT=.exe
# add compile flags to enable rtree, fts3
export MINGW32_CFLAGS="%{mingw32_cflags} -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing"
export MINGW64_CFLAGS="%{mingw64_cflags} -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_DISABLE_DIRSYNC=1 -DSQLITE_ENABLE_FTS3=3 -DSQLITE_ENABLE_RTREE=1 -fno-strict-aliasing"

%mingw_configure %{!?with_tcl:--disable-tcl} --enable-load-extension

# -lc hack
for i in build_win32 build_win64 ; do
    pushd $i
    sed -e s,build_libtool_need_lc=yes,build_libtool_need_lc=no, < libtool > libtool.x
    mv libtool.x libtool
    chmod a+x libtool
    popd
done

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{mingw32_libdir}/libsqlite3.dll.a
chmod 0644 $RPM_BUILD_ROOT%{mingw64_libdir}/libsqlite3.dll.a

%if %{with tcl}
install -d -m755 $RPM_BUILD_ROOT%{mingw32_datadir}/tcl%{tclversion}/sqlite3/
mv $RPM_BUILD_ROOT%{_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl $RPM_BUILD_ROOT%{mingw32_datadir}/tcl%{tclversion}/sqlite3/

install -d -m755 $RPM_BUILD_ROOT%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
mv $RPM_BUILD_ROOT%{_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl $RPM_BUILD_ROOT%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
%endif

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-%{name1}
%doc README.md VERSION
%{mingw32_bindir}/sqlite3.exe
%{mingw32_bindir}/libsqlite3-0.dll
%{mingw32_libdir}/libsqlite3.dll.a
%{mingw32_includedir}/sqlite3.h
%{mingw32_includedir}/sqlite3ext.h
%{mingw32_libdir}/pkgconfig/sqlite3.pc
%if %{with tcl}
%{mingw32_datadir}/tcl%{tclversion}/sqlite3/
%{mingw32_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl
%endif

%files -n mingw32-%{name1}-static
%{mingw32_libdir}/libsqlite3.a

# Win64
%files -n mingw64-%{name1}
%doc README.md VERSION
%{mingw64_bindir}/sqlite3.exe
%{mingw64_bindir}/libsqlite3-0.dll
%{mingw64_libdir}/libsqlite3.dll.a
%{mingw64_includedir}/sqlite3.h
%{mingw64_includedir}/sqlite3ext.h
%{mingw64_libdir}/pkgconfig/sqlite3.pc
%if %{with tcl}
%{mingw64_datadir}/tcl%{tclversion}/sqlite3/
%{mingw64_datadir}/tcl%{tclversion}/sqlite3/pkgIndex.tcl
%endif

%files -n mingw64-%{name1}-static
%{mingw64_libdir}/libsqlite3.a


%changelog
* Sat Aug 15 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.33.0.0-1
- update to 3.33.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.32.3.0-1
- update to 3.32.3.0

* Tue May 26 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.32.1.0-1
- update to 3.32.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.31.1.0-1
- update to 3.31.1.0

* Sat Jan 25 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.31.0.0-1
- update to 3.31.0.0

* Wed Oct 16 2019 Sandro Mani <manisandro@gmail.com> - 3.30.1.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Oct 11 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.30.1.0-1
- update to 3.30.1.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.29.0.0-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.29.0.0-1
- update to 3.29.0.0

* Tue Apr 16 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.28.0.0-1
- update to 3.28.0.0

* Mon Feb 25 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.27.2.0-1
- update to 3.27.2.0

* Fri Feb 08 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.27.1.0-1
- update to 3.27.1.0

* Thu Feb 07 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.27.0.0-1
- update to 3.27.0.0

* Thu Feb 07 2019 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.26.0.0-1
- update to 3.26.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.24.0.0-1
- update to 3.24.0.0

* Tue Apr 10 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.23.1.0-1
- update to 3.23.1.0

* Tue Apr 03 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.23.0.0-1
- update to 3.23.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.22.0.0-1
- update to 3.22.0.0

* Thu Aug 24 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.20.1.0-1
- update to 3.20.1.0

* Wed Aug 02 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.20.0.0-1
- update to 3.20.0.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.19.3.0-1
- update to 3.19.3.0

* Thu May 25 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.19.1.0-1
- update to 3.19.1.0

* Tue May 23 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.19.0.0-1
- update to 3.19.0.0

* Fri Mar 31 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.18.0.0-1
- update to 3.18.0.0

* Tue Feb 14 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.17.0.0-1
- update to 3.17.0.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.16.2.0-1
- update to 3.16.2.0

* Wed Jan 04 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.16.1.0-1
- update to 3.16.1.0

* Tue Jan 03 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.16.0.0-1
- update to 3.16.0.0

* Thu Dec 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.15.2.0-1
- update to 3.15.2.0

* Tue Nov 08 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.15.1.0-1
- update to 3.15.1.0

* Sun Oct 16 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.15.0.0-1
- update to 3.15.0.0

* Fri Aug 12 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.14.1.0-1
- update to 3.14.1.0

* Tue Apr 19 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.12.2.0-1
- update to 3.12.2.0

* Sun Apr 10 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.12.1.0-1
- update to 3.12.1.0

* Wed Mar 30 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.12.0.0-1
- update to 3.12.0.0

* Fri Mar 04 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.11.1.0-1
- update to 3.11.1.0

* Thu Feb 18 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.11.0.0-1
- update to 3.11.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.10.2.0-1
- update to 3.10.2.0

* Thu Jan 14 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.10.1.0-1
- update to 3.10.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.4.3-1
- Update to 3.8.4.3

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.17-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun  2 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.17-1
- update to 3.7.17

* Sun May 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.16.2-2
- Don't try to link against pthreads even if it is available on win32
  (sqlite uses the native win32 threading API already)

* Mon May  6 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.16.2-1
- update to 3.7.16.2

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.16-1
- Update to 3.7.16

* Sun Mar  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.15.2-1
- Update to 3.7.15.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec  6 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.14.1-1
- Update to 3.7.14.1
- Dropped all patches which are not needed for the mingw target
- There's no need to re-run the autotools any more

* Tue Dec  4 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.13-1
- update to 3.7.13

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.9-6
- Add BR: mingw64-pdcurses

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.9-5
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.9-4
- Dropped .la files

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.9-3
- Renamed the source package to mingw-sqlite (#800450)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.7.9-2
- Rebuild against the mingw-w64 toolchain

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.9-1
- update to 3.7.9

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Ivan Romanov <drizt@land.ru> - 3.7.5-2
- static subpackage

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.5-1
- update to 3.7.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.7.3-1
- update to 3.7.3

* Sun Jan 31 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.22-1
- update to 3.6.22

* Sun Dec  6 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.20-1
- update to 3.6.20

* Sun Sep 20 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.17-1
- update to 3.6.17

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.14.2-1
- update to 3.6.14.2
- add debuginfo packages

* Thu Apr 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.12-4
- fix CFLAGS setting

* Thu Apr 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.12-3
- use Erik van Pienbroek way to add to CFLAGS

* Thu Apr 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 3.6.12-2
- BR tclsh; the build process without tclsh and with extensions
  enabled is broken

* Thu Apr 23 2009 Thomas Sailer <t.sailer@alumni.ee.ethz.ch> - 3.6.12-1
- update to 3.6.12 to match native
- enable rtree, fts3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3.6.6.2-2
- Rebuild for mingw32-gcc 4.4

* Tue Dec 16 2008 Richard Jones <rjones@redhat.com> - 3.6.6.2-1
- New upstream release (to match Fedora native), 3.6.6.2.
- Replace patches with ones from native.
- Rebase -no-undefined patch.
- Remove spurious +x permissions on libsqlite3.dll.a.
- Requires pkgconfig.

* Sat Nov 22 2008 Richard Jones <rjones@redhat.com> - 3.5.9-3
- Rebuild against new readline.

* Fri Oct 31 2008 Richard Jones <rjones@redhat.com> - 3.5.9-2
- Rebuild against latest termcap.

* Thu Sep 25 2008 Richard Jones <rjones@redhat.com> - 3.5.9-1
- Initial RPM release.
