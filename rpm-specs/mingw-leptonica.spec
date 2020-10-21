%{?mingw_package_header}

%global pkgname leptonica

Name:          mingw-%{pkgname}
Version:       1.80.0
Release:       1%{?dist}
Summary:       MinGW Windows Leptonica library

License:       Leptonica
BuildArch:     noarch
URL:           https://github.com/danbloomberg/leptonica
Source0:       https://github.com/DanBloomberg/leptonica/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libpng
BuildRequires: mingw32-zlib
BuildRequires: mingw32-giflib
BuildRequires: mingw32-libwebp

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libpng
BuildRequires: mingw64-zlib
BuildRequires: mingw64-giflib
BuildRequires: mingw64-libwebp


%description
MinGW Windows Leptonica library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows Leptonica library

%description -n mingw32-%{pkgname}
MinGW Windows Leptonica library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows Leptonica library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows Leptonica library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows Leptonica library

%description -n mingw64-%{pkgname}
MinGW Windows Leptonica library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows Leptonica library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows Leptonica library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
autoreconf -ifv
%mingw_configure
%mingw_make_build


%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Delete *.exe files
rm -rf %{buildroot}%{mingw32_bindir}/*.exe
rm -rf %{buildroot}%{mingw64_bindir}/*.exe


%files -n mingw32-%{pkgname}
%license leptonica-license.txt
%doc README.html version-notes.html
%{mingw32_bindir}/liblept-5.dll
%{mingw32_includedir}/leptonica/
%{mingw32_libdir}/liblept.dll.a
%{mingw32_libdir}/pkgconfig/lept.pc
%{mingw32_libdir}/cmake/LeptonicaConfig-version.cmake
%{mingw32_libdir}/cmake/LeptonicaConfig.cmake

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/liblept.a
%{mingw32_libdir}/libleptonica.a

%files -n mingw64-%{pkgname}
%license leptonica-license.txt
%doc README.html version-notes.html
%{mingw64_bindir}/liblept-5.dll
%{mingw64_includedir}/leptonica/
%{mingw64_libdir}/liblept.dll.a
%{mingw64_libdir}/pkgconfig/lept.pc
%{mingw64_libdir}/cmake/LeptonicaConfig-version.cmake
%{mingw64_libdir}/cmake/LeptonicaConfig.cmake

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/liblept.a
%{mingw64_libdir}/libleptonica.a


%changelog
* Thu Jul 30 2020 Sandro Mani <manisandro@gmail.com> - 1.80.0-1
- Update to 1.80.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.79.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.79.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 04 2020 Sandro Mani <manisandro@gmail.com> - 1.79.0-1
- Update to 1.79.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.78.0-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.78.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Sandro Mani <manisandro@gmail.com> - 1.78.0-1
- Update to 1.78.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sandro Mani <manisandro@gmail.com> - 1.77.0-1
- Update to 1.77.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.76.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Sandro Mani <manisandro@gmail.com> - 1.76.0-1
- Update to 1.76.0

* Thu Feb 22 2018 Sandro Mani <manisandro@gmail.com> - 1.75.3-1
- Update to 1.75.3

* Mon Feb 12 2018 Sandro Mani <manisandro@gmail.com> - 1.75.2-1
- Update to 1.75.2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Sandro Mani <manisandro@gmail.com> - 1.74.4-1
- Update to 1.74.4

* Sun Jun 11 2017 Sandro Mani <manisandro@gmail.com> - 1.74.3-1
- Update to 1.74.3

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 1.74.2-2
- Backport 069bbc0897e8b939e93db8730b3f10b18e9d0885

* Tue May 30 2017 Sandro Mani <manisandro@gmail.com> - 1.74.2-1
- Update to 1.74.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.74.1-2
- Rebuild (libwebp)

* Tue Jan 03 2017 Sandro Mani <manisandro@gmail.com> - 1.74.1-1
- Update to 1.74.1

* Sun Dec 25 2016 Sandro Mani <manisandro@gmail.com> - 1.74.0-1
- Update to 1.74.0

* Wed May 04 2016 Sandro Mani <manisandro@gmail.com> - 1.73-3
- Rebuild (giflib)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 1.73-1
- Update to 1.73

* Mon Dec 28 2015 Sandro Mani <manisandro@gmail.com> - 1.72-3
- Rebuild (libwebp)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Sandro Mani <manisandro@gmail.com> - 1.72-1
- Update to 1.72

* Wed Aug 13 2014 Sandro Mani <manisandro@gmail.com> - 1.71-1
- Update to 1.71

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.69-6
- Rebuilt with libwebp 0.4.0

* Fri Aug 09 2013 Sandro Mani <manisandro@gmail.com> - 1.69-5
- Patch for and rebuild against giflib 5.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.69-3
- Rebuild against libpng 1.6

* Sun May 19 2013 Sandro Mani <manisandro@gmail.com> - 1.69-2
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires

* Wed May 08 2013 Sandro Mani <manisandro@gmail.com> - 1.69-1
- Initial Fedora package
