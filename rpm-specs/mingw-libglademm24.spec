%{?mingw_package_header}

%global mingw_pkg_name libglademm24

# 64 bit does not build due to too old autotools
%global mingw_build_win64 0

Name:           mingw-%{mingw_pkg_name}
Version:        2.6.7
Release:        29%{?dist}

Summary:        MinGW Windows C++ wrapper for libglade

License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gtkmm24 >= 2.6.0
BuildRequires:  mingw32-libglade2 >= 2.6.1
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gtkmm24 >= 2.6.0
BuildRequires:  mingw64-libglade2 >= 2.6.1
BuildRequires:  mingw64-libpng

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.


%if 0%{?mingw_build_win32} == 1
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Windows C++ wrapper for libglade

%description -n mingw32-%{mingw_pkg_name}
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.
%endif

%if 0%{?mingw_build_win64} == 1
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Windows C++ wrapper for libglade

%description -n mingw64-%{mingw_pkg_name}
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.
%endif


%{?mingw_debug_package}


%prep
%setup -q -n libglademm-%{version}


%build
MINGW32_CXXFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -std=c++11'
MINGW64_CXXFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -std=c++11'
export MINGW32_CXXFLAGS
export MINGW64_CXXFLAGS
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
%if 0%{?mingw_build_win32} == 1
rm -rf ${RPM_BUILD_ROOT}%{mingw32_docdir}/gnomemm-2.6/libglademm-2.4/*
rm -f ${RPM_BUILD_ROOT}%{mingw32_datadir}/devhelp/books/libglademm-2.4/*
%endif
%if 0%{?mingw_build_win64} == 1
rm -rf ${RPM_BUILD_ROOT}%{mingw64_docdir}/gnomemm-2.6/libglademm-2.4/*
rm -f ${RPM_BUILD_ROOT}%{mingw64_datadir}/devhelp/books/libglademm-2.4/*
%endif
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.exe" -exec rm -f {} ';'


%if 0%{?mingw_build_win32} == 1
%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{mingw32_bindir}/libglademm-2.4-1.dll
%{mingw32_includedir}/libglademm-2.4
%{mingw32_libdir}/libglademm-2.4.dll.a
%{mingw32_libdir}/libglademm-2.4
%{mingw32_libdir}/pkgconfig/*.pc
%endif

%if 0%{?mingw_build_win64} == 1
%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{mingw64_bindir}/libglademm-2.4-1.dll
%{mingw64_includedir}/libglademm-2.4
%{mingw64_libdir}/libglademm-2.4.dll.a
%{mingw64_libdir}/libglademm-2.4
%{mingw64_libdir}/pkgconfig/*.pc
%endif

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.6.7-28
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-20
- rebuild with C++11 flags

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.7-15
- Renamed the source package to mingw-libglademm24 (RHBZ #800910)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.6.7-14
- Rebuild against the mingw-w64 toolchain

* Wed Feb 01 2012 Kalev Lember <kalevlember@gmail.com> - 2.6.7-13
- Rebuilt for libpng 1.5
- Spec cleanup
- Dropped .la files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 2.6.7-11
- Rebuilt against win-iconv

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 2.6.7-10
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-7
- add debuginfo packages

* Wed Apr 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-6
- rebuild

* Sun Apr 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-5
- untangle BR and BA
- remove docs

* Sat Apr 18 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-4
- BR mingw32-gcc-c++
- remove --enable-docs

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-3
- unfiy main and devel subpackages

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.6.7-2
- copy from native package
