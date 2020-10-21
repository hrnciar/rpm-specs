%define         solib tolua++-5.3

Name:           tolua++
Version:        1.0.93
Release:        30%{?dist}
Summary:        A tool to integrate C/C++ code with Lua
License:        MIT
# Upstream is defunct, so no URL
Source0:        %{name}-%{version}.tar.bz2
Patch0:         tolua++-1.0.93-no-buildin-bytecode.patch
Patch1:         tolua++-1.0.93-lua52.patch
Patch2:         tolua++-1.0.93-scons304.patch
BuildRequires:  gcc-c++
BuildRequires:  python3-scons
BuildRequires:  lua-devel >= 5.3

%description
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++.


%package devel
Summary:        Development files for tolua++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua-devel >= 5.3

%description devel
Development files for tolua++


%prep
%autosetup -p1
sed -i 's/\r//' doc/%{name}.html


%build
scons %{?_smp_mflags} -Q CCFLAGS="%{optflags} $(pkg-config --cflags lua)" tolua_lib=%{solib} LINKFLAGS="-Wl,-soname,lib%{solib}.so" shared=1
# Relink the tolua++ binary, to link it without the soname which we add to
# LINKFLAGS to build a shared lib
gcc -o bin/%{name} src/bin/tolua.o -Llib -l%{solib} -llua -ldl -lm


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 bin/%{name}  $RPM_BUILD_ROOT%{_bindir}
install -m 755 lib/lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}/libtolua++.so
install -p -m 644 include/%{name}.h $RPM_BUILD_ROOT%{_includedir}
# For use with Patch2 (not working yet)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 src/bin/lua/*.lua $RPM_BUILD_ROOT%{_datadir}/%{name}


%ldconfig_scriptlets


%files
%doc README
%license COPYRIGHT
%{_libdir}/lib%{solib}.so
%{_datadir}/%{name}


%files devel
%doc doc/*
%{_bindir}/%{name}
%{_libdir}/libtolua++.so
%{_includedir}/%{name}.h


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Hans de Goede <hdegoede@redhat.com> - 1.0.93-29
- Fix FTBFS (rhbz#1800202)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Hans de Goede <hdegoede@redhat.com> - 1.0.93-27
- Fix FTBFS (rhbz#1676145)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Tim Niemueller <tim@niemueller.de> - 1.0.93-23
- Add BR gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.93-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Tim Niemueller <tim@niemueller.de> - 1.0.93-17
- Update library name to reflect linking with Lua 5.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.93-15
- Drop unused patches
- Re-add comment about why we need to relink tolua++ after calling scons

* Mon Dec 15 2014 Tim Niemueller <tim@niemueller.de> - 1.0.93-14
- Compatibility with Lua 5.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.93-12
- Use the pre-generated toluabind.c everywhere but x86_64, something goes wrong
  when re-generating it (bootstrap) elsewhere (rhbz#1094103)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.93-10
- Use the pre-generated toluabind.c on non x86, as something goes wrong
  when re-generating it (bootstrap) on non x86. This fixes tolua++
  segfaulting on arm, and hopefully also on ppc (rhbz#704372)

* Fri Aug 09 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.93-9
- Honor the compiler include path when opening lua.h

* Sun Aug 04 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.93-8
- Switch over to compat-lua-5.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 12 2011 Tim Niemueller <tim@niemueller.de> - 1.0.93-3
- Exclude ppc, there are problems according to bz #704372

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 25 2010 Tim Niemueller <tim@niemueller.de> - 1.0.93-1
- Upgrade to 1.0.93

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 13 2008 Tim Niemueller <tim@niemueller.de> - 1.0.92-7
- Added patch to make tolua++ compatible with GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.92-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Ian Chapman <packages@amiga-hardware.com> 1.0.92-5
- Release bump for F8 mass rebuild
- Updated license due to new guidelines

* Mon Aug 28 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-4
- Release bump for FC6 mass rebuild

* Sat Jun 03 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-3
- Fixed issue with where tolua++ was tagged with an soname the same as the lib
  meaning ld would fail to locate the library.

* Fri Jun 02 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-2
- Changed license from Freeware Style to just Freeware
- Changed => to more conventional >= for (build)requires
- Moved %%{_bindir}/tolua++ to devel package
- Now adds soname to library

* Fri Jun 02 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-1
- Initial Release
