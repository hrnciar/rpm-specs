%{?mingw_package_header}

Name:           mingw-atkmm
Version:        2.24.3
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for the ATK library

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.24/atkmm-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-libsigc++20
BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-glibmm24 >= 2.24
BuildRequires:  mingw64-glibmm24 >= 2.24

%description
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package -n mingw32-atkmm
Summary:        MinGW Windows C++ interface for the ATK library
# mingw32-atkmm files used to be part of mingw32-gtkmm24
Conflicts:      mingw32-gtkmm24 < 2.21.1

# Fix upgrade path for people who are upgrading from the mingw-w64 testing repo
Obsoletes:      mingw32-atkmm-static < 2.22.6-3
Provides:       mingw32-atkmm-static = 2.22.6-3

%description -n mingw32-atkmm
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package -n mingw64-atkmm
Summary:        MinGW Windows C++ interface for the ATK library

# Fix upgrade path for people who are upgrading from the mingw-w64 testing repo
Obsoletes:      mingw64-atkmm-static < 2.22.6-3
Provides:       mingw64-atkmm-static = 2.22.6-3

%description -n mingw64-atkmm
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n atkmm-%{version}


%build
%mingw_configure --disable-static --disable-documentation
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la


%files -n mingw32-atkmm
%license COPYING
%{mingw32_includedir}/atkmm-1.6
%{mingw32_libdir}/atkmm-1.6
%{mingw32_libdir}/pkgconfig/atkmm-1.6.pc
%{mingw32_libdir}/libatkmm-1.6.dll.a
%{mingw32_bindir}/libatkmm-1.6-1.dll

%files -n mingw64-atkmm
%license COPYING
%{mingw64_includedir}/atkmm-1.6
%{mingw64_libdir}/atkmm-1.6
%{mingw64_libdir}/pkgconfig/atkmm-1.6.pc
%{mingw64_libdir}/libatkmm-1.6.dll.a
%{mingw64_bindir}/libatkmm-1.6-1.dll


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.24.3-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.24.3-1
- Update to 2.24.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.2-1
- update to 2.24.2

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Wed Sep 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.23.1-1
- update to 2.23.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 2.22.7-6
- Rebuild against latest mingw-gcc

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.22.7-5
- Use license macro for the COPYING file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.7-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 2.22.7-1
- Update to 2.22.7
- Drop the pkgconfig deps

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.6-6
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.6-4
- Fix upgrade path for people upgrading from the mingw-w64 testing repo
- Cleaned up some unneeded %%global tags
 
* Thu Mar 15 2012 Kalev Lember <kalevlember@gmail.com> - 2.22.6-3
- Build 64 bit Windows binaries

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.6-2
- Renamed the source package to mingw-atkmm (RHBZ #800844)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.22.6-1
- Update to 2.22.6
- Remove .la files
- Switch to .xz tarballs
- Spec cleanup for recent rpmbuild

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.5-4
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 2.22.5-2
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.5-1
- Update to 2.22.5

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.2-2
- Rebuilt for proxy-libintl removal

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.22.2-1
- update to 2.22.2 to match native

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.22.0-1
- Initial RPM release.
