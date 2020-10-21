%{?mingw_package_header}

Name:           mingw-harfbuzz
Version:        2.7.2
Release:        1%{?dist}
Summary:        MinGW Windows Harfbuzz library

License:        MIT
URL:            http://www.harfbuzz.org
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz

# Allow the freetype dependency to be optional at runtime
Patch0:         harfbuzz-enable-delayload-freetype.patch
# Invoke versioned python
Patch1:         harfbuzz-python.patch

BuildArch:      noarch

BuildRequires:  python3

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-icu

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-icu

# Needed for the delay-load patch
BuildRequires:  mingw-w64-tools
BuildRequires:  autoconf automake libtool


%description
HarfBuzz is an implementation of the OpenType Layout engine.


# Win32
%package -n mingw32-harfbuzz
Summary:        MinGW Windows Harfbuzz library

%description -n mingw32-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw32-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw32-harfbuzz = %{version}-%{release}
Requires:       mingw32-glib2-static

%description -n mingw32-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.

# Win64
%package -n mingw64-harfbuzz
Summary:        MinGW Windows Harfbuzz library

%description -n mingw64-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw64-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw64-harfbuzz = %{version}-%{release}
Requires:       mingw64-glib2-static

%description -n mingw64-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n harfbuzz-%{version}
autoreconf -i --force


%build
%mingw_configure --enable-shared --enable-static --enable-delay-load
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=%{buildroot}

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-harfbuzz
%license COPYING
%{mingw32_bindir}/hb-ot-shape-closure.exe
%{mingw32_bindir}/hb-shape.exe
%{mingw32_bindir}/hb-subset.exe
%{mingw32_bindir}/hb-view.exe
%{mingw32_bindir}/libharfbuzz-0.dll
%{mingw32_bindir}/libharfbuzz-icu-0.dll
%{mingw32_bindir}/libharfbuzz-subset-0.dll
%{mingw32_includedir}/harfbuzz/
%{mingw32_libdir}/libharfbuzz.dll.a
%{mingw32_libdir}/libharfbuzz-icu.dll.a
%{mingw32_libdir}/libharfbuzz-subset.dll.a
%{mingw32_libdir}/pkgconfig/harfbuzz.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-icu.pc
%{mingw32_libdir}/pkgconfig/harfbuzz-subset.pc
%{mingw32_libdir}/cmake/harfbuzz/

%files -n mingw32-harfbuzz-static
%{mingw32_libdir}/libharfbuzz.a
%{mingw32_libdir}/libharfbuzz-icu.a
%{mingw32_libdir}/libharfbuzz-subset.a

# Win64
%files -n mingw64-harfbuzz
%license COPYING
%{mingw64_bindir}/hb-ot-shape-closure.exe
%{mingw64_bindir}/hb-shape.exe
%{mingw64_bindir}/hb-subset.exe
%{mingw64_bindir}/hb-view.exe
%{mingw64_bindir}/libharfbuzz-0.dll
%{mingw64_bindir}/libharfbuzz-icu-0.dll
%{mingw64_bindir}/libharfbuzz-subset-0.dll
%{mingw64_includedir}/harfbuzz/
%{mingw64_libdir}/libharfbuzz.dll.a
%{mingw64_libdir}/libharfbuzz-icu.dll.a
%{mingw64_libdir}/libharfbuzz-subset.dll.a
%{mingw64_libdir}/pkgconfig/harfbuzz.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-icu.pc
%{mingw64_libdir}/pkgconfig/harfbuzz-subset.pc
%{mingw64_libdir}/cmake/harfbuzz/

%files -n mingw64-harfbuzz-static
%{mingw64_libdir}/libharfbuzz.a
%{mingw64_libdir}/libharfbuzz-icu.a
%{mingw64_libdir}/libharfbuzz-subset.a


%changelog
* Wed Sep 02 2020 Sandro Mani <manisandro@gmail.com> - 2.7.2-1
- Update to 2.7.2

* Fri Aug 21 2020 Sandro Mani <manisandro@gmail.com> - 2.7.1-1
- Update to 2.7.1

* Wed Aug 12 13:40:57 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.6.8-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Sandro Mani <manisandro@gmail.com> - 2.6.8-1
- Update to 2.6.8

* Sun Jun 07 2020 Sandro Mani <manisandro@gmail.com> - 2.6.7-1
- Update to 2.6.7

* Tue May 19 2020 Sandro Mani <manisandro@gmail.com> - 2.6.6-2
- Rebuild (icu)

* Thu May 14 2020 Sandro Mani <manisandro@gmail.com> - 2.6.6-1
- Update to 2.6.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 2.6.4-2
- Rebuild (icu)

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 2.6.4-1
- Update to 2.6.4

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.6.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Oct 01 2019 Sandro Mani <manisandro@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Mon Aug 26 2019 Sandro Mani <manisandro@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Mon Aug 19 2019 Sandro Mani <manisandro@gmail.com> - 2.6.0-1
- Update to 2.6.0

* Tue Aug 13 2019 Sandro Mani <manisandro@gmail.com> - 2.5.3-3
- Rebuild (icu)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Sat Jun 22 2019 Sandro Mani <manisandro@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Mon Jun 03 2019 Sandro Mani <manisandro@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Mon May 27 2019 Sandro Mani <manisandro@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Mon Apr 15 2019 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Thu Jan 31 2019 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Sat Nov 24 2018 Sandro Mani <manisandro@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Thu Nov 08 2018 Sandro Mani <manisandro@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Mon Nov 05 2018 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sun Oct 28 2018 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Mon Sep 10 2018 Sandro Mani <manisandro@gmail.com> - 1.8.8-1
- Update to 1.8.8

* Thu Aug 09 2018 Sandro Mani <manisandro@gmail.com> - 1.8.7-1
- Update to 1.8.7

* Thu Aug 02 2018 Sandro Mani <manisandro@gmail.com> - 1.8.5-1
- Update to 1.8.5

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 1.8.4-1
- Update to 1.8.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Sandro Mani <manisandro@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Thu Jun 14 2018 Sandro Mani <manisandro@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue May 29 2018 Sandro Mani <manisandro@gmail.com> - 1.7.6-1
- Update to 1.7.6

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.4.8-1
- Update to 1.4.8

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 1.3.2-2
- Rebuilt for mingw-icu 57

* Sun Oct 16 2016 Kalev Lember <klember@redhat.com> - 1.3.2-1
- Update to 1.3.2

* Wed Aug 10 2016 Kalev Lember <klember@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 1.2.7-1
- Update to 1.2.7

* Sat Apr  9 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2
- Make freetype an optional runtime dependency instead of a hard dependency (using delay load)
- Perform verbose make

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.40-1
- Update to 0.9.40
- Use license macro for the COPYING file

* Wed Dec 31 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.37-2
- Added Requires: mingw{32,64}-glib2-static tags to the -static subpackages

* Wed Dec 31 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.37-1
- Update to 0.9.37

* Sat Nov 15 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.34-1
- Update to 0.9.34

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.28-1
- Update to 0.9.28

* Sat Mar 29 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.27-1
- Update to 0.9.27

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.25-1
- Update to 0.9.25

* Wed Nov 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.24-1
- Update to 0.9.24

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.20-1
- Update to 0.9.20

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.18-4
- Rebuilt for icu 50

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.18-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sat Jun 15 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.18-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 09 2013 Kalev Lember <kalevlember@gmail.com> - 0.9.18-1
- Update to 0.9.18

* Thu May  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.16-1
- Update to 0.9.16

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.9-3
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Wed Jan 02 2013 Erik van Pienbroek <erik-fedora@vanpienbroek.nl> - 0.9.9-2
- Rebuilt against mingw-icu 49

* Mon Dec 24 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9
- Fix compatibility with WinXP (FreeDesktop Bug #55494)

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.7-1
- Update to 0.9.7

* Sun Aug 26 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.3-1
- Initial release

