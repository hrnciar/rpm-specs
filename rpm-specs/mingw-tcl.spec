%{?mingw_package_header}

%global majorver1 8
%global majorver2 6
%global majorver %{majorver1}.%{majorver2}
%global	vers %{majorver}.8

%global name1 tcl

Summary: MinGW Windows Tool Command Language, pronounced tickle
Name: mingw-%{name1}
Version: %{vers}
Release: 5%{?dist}
License: TCL
URL: http://tcl.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/tcl/%{name1}-core%{version}-src.tar.gz
BuildArch: noarch
Buildrequires: autoconf
BuildRequires: file
BuildRequires: m4
BuildRequires: net-tools
BuildRequires: tcl
BuildRequires: mingw32-filesystem
BuildRequires: mingw64-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: mingw32-cpp
BuildRequires: mingw64-cpp
BuildRequires: mingw32-runtime
BuildRequires: mingw64-runtime
BuildRequires: mingw32-headers
BuildRequires: mingw64-headers
BuildRequires: mingw32-zlib
BuildRequires: mingw64-zlib
Patch0: tcl-8.6.3-autopath.patch
Patch1: tcl-8.6.8-conf.patch
Patch2: tcl-8.6.8-hidden.patch
# Upstream ticket:
# https://core.tcl.tk/tcl/tktview/7d0db7c388f52de81faf12da332bc97a24f7b9e5
Patch3: tcl-8.6.5-parallel-make-fix.patch
Patch4: tcl-8.5.6-mingw.patch
Patch5: tcl-nativetclsh.patch
Patch6: tcl-mingw-w64-compatibility.patch
Patch7: tcl-8.6.1-nativezlib.patch

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.


%package -n mingw32-%{name1}
Summary: MinGW Windows Tool Command Language, pronounced tickle

%description -n mingw32-%{name1}
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.

%package -n mingw64-%{name1}
Summary: MinGW Windows Tool Command Language, pronounced tickle

%description -n mingw64-%{name1}
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks. When paired with the
Tk toolkit, Tcl provides a fastest and powerful way to create
cross-platform GUI applications.  Tcl can also be used for a variety
of web-related tasks and for creating powerful command languages for
applications.


%{?mingw_debug_package}


%prep
%setup -q -n %{name1}%{version}
chmod -x generic/tclThreadAlloc.c

%patch0 -p1 -b .autopath
%patch1 -p1 -b .conf
%patch2 -p1 -b .hidden
%patch3 -p1 -b .parallel-make-fix
%patch4 -p0 -b .mingw32
%patch5 -p0 -b .nativetclsh
%patch6 -p0 -b .mingw-w64
%patch7 -p1 -b .nativezlib

%build
pushd win
autoconf
%{mingw_configure} --disable-threads --enable-shared
# builds fail sometimes with %{?_smp_mflags}, so don't use
%{mingw_make} TCL_LIBRARY=%{mingw32_datadir}/%{name1}%{majorver}
popd

%install
make install -C win/build_win32 INSTALL_ROOT=$RPM_BUILD_ROOT TCL_LIBRARY=%{mingw32_datadir}/%{name1}%{majorver}
make install -C win/build_win64 INSTALL_ROOT=$RPM_BUILD_ROOT TCL_LIBRARY=%{mingw64_datadir}/%{name1}%{majorver}

ln -s tclsh%{majorver1}%{majorver2}.exe $RPM_BUILD_ROOT%{mingw32_bindir}/tclsh.exe
ln -s tclsh%{majorver1}%{majorver2}.exe $RPM_BUILD_ROOT%{mingw64_bindir}/tclsh.exe

mv $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.a $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.a $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.a $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.a $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a

# for linking with -lib%{name1}
ln -s lib%{name1}%{majorver1}%{majorver2}.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}.dll.a
ln -s lib%{name1}%{majorver1}%{majorver2}.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}.dll.a

#mkdir -p $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}
#mkdir -p $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}
ln -s ../share/%{name1}%{majorver} $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}
ln -s ../share/%{name1}%{majorver} $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}

# postgresql and maybe other packages too need tclConfig.sh
# paths don't look at /usr/lib for efficiency, so we symlink into tcl8.5 for now
ln -s %{mingw32_libdir}/%{name1}Config.sh $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}/%{name1}Config.sh
ln -s %{mingw32_libdir}/%{name1}Config.sh $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}/%{name1}Config.sh

mkdir -p $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/{generic,win}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/{generic,win}
find generic win -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/'{}' ';'
find generic win -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/'{}' ';'
( cd $RPM_BUILD_ROOT/%{mingw32_includedir}
	for i in *.h ; do
		[ -f $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/generic/$i ] && ln -sf ../../$i $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/generic ;
	done
) || true
( cd $RPM_BUILD_ROOT/%{mingw64_includedir}
	for i in *.h ; do
		[ -f $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/generic/$i ] && ln -sf ../../$i $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/generic ;
	done
) || true

# fix executable bits
chmod a-x $RPM_BUILD_ROOT/%{mingw32_datadir}/%{name1}%{majorver}/encoding/*.enc
chmod a-x $RPM_BUILD_ROOT/%{mingw64_datadir}/%{name1}%{majorver}/encoding/*.enc
chmod a-x $RPM_BUILD_ROOT/%{mingw32_libdir}/*/pkgIndex.tcl
chmod a-x $RPM_BUILD_ROOT/%{mingw64_libdir}/*/pkgIndex.tcl

# remove buildroot traces
sed -i -e "s|$PWD/win|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}Config.sh
sed -i -e "s|$PWD/win|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}Config.sh
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/%{name1}%{majorver}/tclAppInit.c
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/%{name1}%{majorver}/tclAppInit.c
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/%{name1}%{majorver}/ldAix
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/%{name1}%{majorver}/ldAix

# move windows packages to where tcl85.dll will find them
mv $RPM_BUILD_ROOT/%{mingw32_libdir}/dde* $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}/
mv $RPM_BUILD_ROOT/%{mingw64_libdir}/dde* $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}/
mv $RPM_BUILD_ROOT/%{mingw32_libdir}/reg* $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}/
mv $RPM_BUILD_ROOT/%{mingw64_libdir}/reg* $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}/

# remove local zlib
rm -f $RPM_BUILD_ROOT/%{mingw32_bindir}/zlib1.dll
rm -f $RPM_BUILD_ROOT/%{mingw64_bindir}/zlib1.dll


%files -n mingw32-%{name1}
%{mingw32_bindir}/%{name1}sh.exe
%{mingw32_bindir}/%{name1}sh%{majorver1}%{majorver2}.exe
%{mingw32_bindir}/%{name1}%{majorver1}%{majorver2}.dll
%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
%{mingw32_libdir}/lib%{name1}.dll.a
%{mingw32_libdir}/%{name1}Config.sh
%{mingw32_datadir}/%{name1}%{majorver}
%exclude %{mingw32_datadir}/%{name1}%{majorver}/dde1.4/tcldde14.dll.debug
%exclude %{mingw32_datadir}/%{name1}%{majorver}/reg1.3/tclreg13.dll.debug
%{mingw32_datadir}/%{name1}%{majorver1}
%{mingw32_includedir}/*
%{mingw32_libdir}/%{name1}%{majorver}
%doc README changes 
%doc license.terms

%files -n mingw64-%{name1}
%{mingw64_bindir}/%{name1}sh.exe
%{mingw64_bindir}/%{name1}sh%{majorver1}%{majorver2}.exe
%{mingw64_bindir}/%{name1}%{majorver1}%{majorver2}.dll
%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
%{mingw64_libdir}/lib%{name1}.dll.a
%{mingw64_libdir}/%{name1}Config.sh
%{mingw64_datadir}/%{name1}%{majorver}
%exclude %{mingw64_datadir}/%{name1}%{majorver}/dde1.4/tcldde14.dll.debug
%exclude %{mingw64_datadir}/%{name1}%{majorver}/reg1.3/tclreg13.dll.debug
%{mingw64_datadir}/%{name1}%{majorver1}
%{mingw64_includedir}/*
%{mingw64_libdir}/%{name1}%{majorver}
%doc README changes 
%doc license.terms

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.8-1
- update to 8.6.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.7-1
- update to 8.6.7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.6-1
- update to 8.6.6

* Fri Jul 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.5-1
- update to 8.6.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.4-1
- update to 8.6.4

* Thu Dec  4 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.3-1
- update to 8.6.3

* Wed Oct  1 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.2-1
- update to 8.6.2

* Fri Jun 13 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.6.1-1
- update to 8.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar  6 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.15-1
- update to 8.5.15

* Tue Sep 17 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.14-2
- rename EXCEPTION_REGISTRATION to avoid define clash with new mingw headers

* Tue Sep  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.14-1
- update to 8.5.14

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.13-3
- %%{mingw32_libdir}/tcl8.5 and %%{mingw64_libdir}/tcl8.5 are symlinks, not folders
- Fixes FTBFS against latest RPM

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.13-1
- update to 8.5.13

* Fri Aug  3 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.11-6
- enable 64bit compile

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 08 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.11-4
- Prevent a file conflict with files from the debuginfo package

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 8.5.11-3
- Renamed the source package to mingw-tcl (#801032)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.11-2
- Rebuild against the mingw-w64 toolchain
- Added a patch to fix compatibility with the mingw-w64 toolcain

* Mon Jan 16 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.11-1
- update 8.5.11

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 10 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.9-4
- put the reg and dde libraries where tcl85.dll searches for it
 
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.9-2
- put the tcl library where tclsh.exe searches for it

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.9-1
- update to 8.5.9

* Thu Aug  5 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.8-1
- update to 8.5.8

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-6
- add debuginfo packages

* Sat May 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-5
- rebuilt

* Sat May 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-4
- use native shell to install tz data

* Sat May 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-3
- fix BRs

* Fri May 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-2
- remove check section

* Thu May 21 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.7-1
- update to 8.5.7
- simplify dir ownership

* Thu May 21 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 8.5.6-1
- copy from native
