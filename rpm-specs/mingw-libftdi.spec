%?mingw_package_header

%global name1 libftdi
Name:           mingw-%{name1}
Version:        1.4
Release:        2%{?dist}
Summary:        MinGW library to program and control the FTDI USB controller

License:        LGPLv2 and GPLv2
URL:            http://www.intra2net.com/de/produkte/opensource/ftdi/
Source0:        http://www.intra2net.com/en/developer/%{name1}/download/%{name1}1-%{version}.tar.bz2
# Swig requirements have changed in newer versions of CMake.
# This has been reported to the mailing list
Patch0:         libftdi-cmake_swig.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw32-libconfuse
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-libconfuse
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  swig

%description
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw32-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw32-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw64-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw64-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{name1}1-%{version}


%build
%mingw_cmake .

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT/%{mingw32_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw32_datadir}/doc/libftdi1/example.conf
rm -f $RPM_BUILD_ROOT/%{mingw64_datadir}/doc/libftdi1/example.conf
rm -rf $RPM_BUILD_ROOT/build_win32/doc/html
rm -rf $RPM_BUILD_ROOT/build_win64/doc/html
rm -rf $RPM_BUILD_ROOT/build_win32/examples
rm -rf $RPM_BUILD_ROOT/build_win64/examples


%files -n mingw32-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw32_bindir}/ftdi_eeprom.exe      
%{mingw32_bindir}/libftdi1-config
%{mingw32_bindir}/libftdi1.dll
%{mingw32_bindir}/libftdipp1.dll
%{mingw32_includedir}/libftdi1
%{mingw32_libdir}/libftdi1.dll.a
%{mingw32_libdir}/libftdipp1.dll.a
%{mingw32_libdir}/cmake/libftdi1
%{mingw32_libdir}/pkgconfig/libftdi1.pc
%{mingw32_libdir}/pkgconfig/libftdipp1.pc

%files -n mingw64-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw64_bindir}/ftdi_eeprom.exe      
%{mingw64_bindir}/libftdi1-config
%{mingw64_bindir}/libftdi1.dll
%{mingw64_bindir}/libftdipp1.dll
%{mingw64_includedir}/libftdi1
%{mingw64_libdir}/libftdi1.dll.a
%{mingw64_libdir}/libftdipp1.dll.a
%{mingw64_libdir}/cmake/libftdi1
%{mingw64_libdir}/pkgconfig/libftdi1.pc
%{mingw64_libdir}/pkgconfig/libftdipp1.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.4-1
- update to 1.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 06 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-3
- fix license tag

* Fri Oct 06 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-2
- drop example and documentation
- properly include license files
- modernize spec files, remove obsolete constructs

* Wed Jan 25 2017 Thomas Sailer <thomas.sailer@axsem.com> - 1.3-1
- Initial Specfile
