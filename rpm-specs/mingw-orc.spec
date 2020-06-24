%{?mingw_package_header}

Name:           mingw-orc
Version:        0.4.27
Release:        6%{?dist}
Summary:        Cross compiled Oil Run-time Compiler

License:        BSD
URL:            http://code.entropywave.com/projects/orc/
Source0:        http://gstreamer.freedesktop.org/src/orc/orc-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.


# Mingw32
%package -n mingw32-orc
Summary: %{summary}

%description -n mingw32-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw32-orc-compiler
Summary:        Orc compiler
Requires:       mingw32-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw32-orc-compiler
The Orc compiler, to produce optimized code.

# Mingw64
%package -n mingw64-orc
Summary: %{summary}

%description -n mingw64-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw64-orc-compiler
Summary:        Orc compiler
Requires:       mingw64-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw64-orc-compiler
The Orc compiler, to produce optimized code.

%{?mingw_debug_package}


%prep
%setup -q -n orc-%{version}


%build
%mingw_configure \
    --enable-shared \
    --disable-static \
    --disable-gtk-doc
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT" INSTALL="install -p"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete
# Remove gtk documentation.
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc


# Mingw32
%files -n mingw32-orc
%license COPYING
%doc README
%{mingw32_bindir}/liborc-0.4-0.dll
%{mingw32_bindir}/liborc-test-0.4-0.dll
%{mingw32_bindir}/orc-bugreport.exe
%{mingw32_datadir}/aclocal/orc.m4
%{mingw32_includedir}/orc-0.4/
%{mingw32_libdir}/liborc-0.4.dll.a
%{mingw32_libdir}/liborc-test-0.4.dll.a
%{mingw32_libdir}/pkgconfig/orc-0.4.pc

%files -n mingw32-orc-compiler
%{mingw32_bindir}/orcc.exe

# Mingw64
%files -n mingw64-orc
%license COPYING
%doc README
%{mingw64_bindir}/liborc-0.4-0.dll
%{mingw64_bindir}/liborc-test-0.4-0.dll
%{mingw64_bindir}/orc-bugreport.exe
%{mingw64_datadir}/aclocal/orc.m4
%{mingw64_includedir}/orc-0.4/
%{mingw64_libdir}/liborc-0.4.dll.a
%{mingw64_libdir}/liborc-test-0.4.dll.a
%{mingw64_libdir}/pkgconfig/orc-0.4.pc

%files -n mingw64-orc-compiler
%{mingw64_bindir}/orcc.exe


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 0.4.27-1
- Update to 0.4.27

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Kalev Lember <klember@redhat.com> - 0.4.26-1
- Update to 0.4.26
- Don't set group tags

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 0.4.25-1
- Update to 0.4.25

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 0.4.24-1
- Update to 0.4.24
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 Michael Cronenworth <mike@cchtml.com> - 0.4.22-1
- Updated to 0.4.22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May  3 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.16-1
- Updated to 0.4.16

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul  4 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.14-2
- The package wasn't installable due to broken Requires tags. Fixed

* Fri May 13 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.14-1
- Updated to 0.4.14
- Updated to newer mingw instructions (with mingw64 support)

* Wed Dec 29 2010 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.11-1
- Initial mingw32-orc 0.4.11
- Based upon previous package in Fedora by Fabian Deutsch
