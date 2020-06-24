%{?mingw_package_header}

%global majorver1 8
%global majorver2 6
%global majorver %{majorver1}.%{majorver2}
%global vers %{majorver}.8

%global name1 tk

Summary:   MinGW Windows graphical toolkit for the Tcl scripting language
Name:      mingw-%{name1}
Version:   %{vers}
Release:   7%{?dist}
License:   TCL
URL:       http://tcl.sourceforge.net/
Source0:   http://downloads.sourceforge.net/sourceforge/tcl/%{name1}%{version}-src.tar.gz

BuildRequires: mingw32-tcl = %{version}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-tcl = %{version}
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc

BuildArch: noarch

%description
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.


%package -n mingw32-%{name1}
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw32-%{name1}
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

%package -n mingw64-%{name1}
Summary:   MinGW Windows graphical toolkit for the Tcl scripting language

%description -n mingw64-%{name1}
When paired with the Tcl scripting language, Tk provides a fast and powerful
way to create cross-platform GUI applications.

%{?mingw_debug_package}


%prep
%setup -q -n %{name1}%{version}
iconv -f iso-8859-1 -t utf-8 changes > changes.utf8
touch -r changes changes.utf8
mv changes.utf8 changes

%build
pushd win
MINGW32_CONFIGURE_ARGS="--with-tcl=%{mingw32_libdir}/tcl%{majorver}"
MINGW64_CONFIGURE_ARGS="--with-tcl=%{mingw64_libdir}/tcl%{majorver}"
%{mingw_configure}
# builds fail sometimes with %%{?_smp_mflags}, so don't use
sed -i -e 's,mingw-tcl,tcl,g' build_win*/Makefile
sed -i -e 's,/usr/include,%{mingw32_includedir},g' build_win32/Makefile
sed -i -e 's,/usr/include,%{mingw64_includedir},g' build_win64/Makefile
sed -i -e 's,libtclstub86.a,libtclstub86.dll.a,g' build_win*/Makefile
sed -i -e 's,tcl8.6/libtclstub86,libtclstub86,g' build_win*/Makefile
sed -i -e 's,libtcl86.a,libtcl86.dll.a,g' build_win*/Makefile
sed -i -e 's,tcl8.6/libtcl86,libtcl86,g' build_win*/Makefile
%{mingw32_make} -C build_win32 TCL_LIBRARY=%{mingw32_datadir}/%{name1}%{majorver}
%{mingw64_make} -C build_win64 TCL_LIBRARY=%{mingw64_datadir}/%{name1}%{majorver}
popd

%install
make install -C win/build_win32 INSTALL_ROOT=$RPM_BUILD_ROOT TK_LIBRARY=%{mingw32_datadir}/%{name1}%{majorver}
make install -C win/build_win64 INSTALL_ROOT=$RPM_BUILD_ROOT TK_LIBRARY=%{mingw64_datadir}/%{name1}%{majorver}

ln -s wish%{majorver1}%{majorver2}.exe $RPM_BUILD_ROOT%{mingw32_bindir}/wish.exe
ln -s wish%{majorver1}%{majorver2}.exe $RPM_BUILD_ROOT%{mingw64_bindir}/wish.exe

mv $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.a \
   $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.a \
   $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.a \
   $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.a \
   $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a

# for linking with -lib%%{name1}
ln -s lib%{name1}%{majorver1}%{majorver2}.dll.a \
      $RPM_BUILD_ROOT%{mingw32_libdir}/lib%{name1}.dll.a
ln -s lib%{name1}%{majorver1}%{majorver2}.dll.a \
      $RPM_BUILD_ROOT%{mingw64_libdir}/lib%{name1}.dll.a

mkdir -p $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}

# postgresql and maybe other packages too need tclConfig.sh
# paths don't look at /usr/lib for efficiency, so we symlink into tcl8.5 for now
ln -s %{mingw32_libdir}/%{name1}Config.sh \
      $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}%{majorver}/%{name1}Config.sh
ln -s %{mingw64_libdir}/%{name1}Config.sh \
      $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}%{majorver}/%{name1}Config.sh

mkdir -p $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/{generic/ttk,win}
mkdir -p $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/{generic/ttk,win}
find generic win -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/'{}' ';'
find generic win -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/'{}' ';'
( cd $RPM_BUILD_ROOT/%{mingw32_includedir}
     for i in *.h ; do
         [ -f $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/generic/$i ] && \
         ln -sf ../../$i $RPM_BUILD_ROOT/%{mingw32_includedir}/%{name1}-private/generic ;
     done
) || true
( cd $RPM_BUILD_ROOT/%{mingw64_includedir}
     for i in *.h ; do
         [ -f $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/generic/$i ] && \
         ln -sf ../../$i $RPM_BUILD_ROOT/%{mingw64_includedir}/%{name1}-private/generic ;
     done
) || true

# fix executable bits
chmod a-x $RPM_BUILD_ROOT/%{mingw32_libdir}/*/pkgIndex.tcl
chmod a-x $RPM_BUILD_ROOT/%{mingw64_libdir}/*/pkgIndex.tcl

# remove buildroot traces
sed -i -e "s|$PWD/win|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" $RPM_BUILD_ROOT/%{mingw32_libdir}/%{name1}Config.sh
sed -i -e "s|$PWD/win|%{_libdir}|; s|$PWD|%{_includedir}/%{name}-private|" $RPM_BUILD_ROOT/%{mingw64_libdir}/%{name1}Config.sh
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/%{name1}%{majorver}/tclAppInit.c
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/%{name1}%{majorver}/tclAppInit.c
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/%{name1}%{majorver}/ldAix
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/%{name1}%{majorver}/ldAix

%files -n mingw32-%{name1}
%{mingw32_bindir}/wish*.exe
%{mingw32_bindir}/%{name1}%{majorver1}%{majorver2}.dll
%{mingw32_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
%{mingw32_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
%{mingw32_libdir}/lib%{name1}.dll.a
%{mingw32_libdir}/%{name1}Config.sh
%{mingw32_includedir}/*
%{mingw32_libdir}/%{name1}%{majorver}/
%{mingw32_datadir}/%{name1}%{majorver1}.%{majorver2}
%doc README changes 
%doc license.terms

%files -n mingw64-%{name1}
%{mingw64_bindir}/wish*.exe
%{mingw64_bindir}/%{name1}%{majorver1}%{majorver2}.dll
%{mingw64_libdir}/lib%{name1}%{majorver1}%{majorver2}.dll.a
%{mingw64_libdir}/lib%{name1}stub%{majorver1}%{majorver2}.dll.a
%{mingw64_libdir}/lib%{name1}.dll.a
%{mingw64_libdir}/%{name1}Config.sh
%{mingw64_includedir}/*
%{mingw64_libdir}/%{name1}%{majorver}/
%{mingw64_datadir}/%{name1}%{majorver1}.%{majorver2}
%doc README changes 
%doc license.terms

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.8-1
- Update to 8.6.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 8.6.7-2
- Fix debug file in main package

* Thu Aug 10 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.7-1
- Update to 8.6.7

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.6-1
- Update to 8.6.6

* Wed Jun 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.4-2
- Build mingw64-tk (#1269746)

* Wed Jun 29 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 8.6.4-1
- Update to 8.6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.6.1-1
- Update to 8.6.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.13-4
- Fix FTBFS against latest mingw-w64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.13-1
- Update to 8.5.13 (fixes FTBFS caused by latest mingw-tcl)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 8.5.9-6
- Fix the sed magic after mingw32-tcl -> mingw-tcl rename

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 8.5.9-5
- Renamed the source package to mingw-tk (#801037)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.5.9-4
- Rebuild against the mingw-w64 toolchain
- Fix the compilation with the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Paulo Roma <roma@lcg.ufrj.br> - 8.5.9-1
- Update to 8.5.9 to match rawhide.
- Converted changes to utf8.
- Fixed wish symbolic link.

* Tue Oct 20 2009 Paulo Roma <roma@lcg.ufrj.br> - 8.5.7-5.1
- Copy from native
