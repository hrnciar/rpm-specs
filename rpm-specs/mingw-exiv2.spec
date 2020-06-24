%{?mingw_package_header}

%global pkgname exiv2

Name:          mingw-%{pkgname}
Version:       0.27.2
Release:       4%{?dist}
Summary:       MinGW Windows %{pkgname} library
License:       GPLv2+
BuildArch:     noarch
URL:           http://www.exiv2.org/
Source0:       https://github.com/Exiv2/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz

# Fix undefined reference to BasicError<T>::setMsg
# (Some issue with dllexport/dllimport and a template specialization in a source
# file... So just moved the implementation out and made it inline.)
#Patch1:        exiv2_setMsg.patch

BuildRequires: cmake
BuildRequires: gettext

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gettext
BuildRequires: mingw32-expat
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gettext
BuildRequires: mingw64-expat
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake \
  -DEXIV2_ENABLE_NLS:BOOL=ON \
  -DEXIV2_BUILD_SAMPLES:BOOL=OFF \
  -DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON \
  -DICONV_ACCEPTS_CONST_INPUT=1

# Hack around double slashes install paths in generated po/cmake_install.cmake
# sed -i 's|//|/|g' build_win32/po/cmake_install.cmake
# sed -i 's|//|/|g' build_win64/po/cmake_install.cmake

%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install
%mingw_find_lang exiv2

rm -f %{buildroot}%{mingw32_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw32_datadir}/man/man1/exiv2.1
rm -f %{buildroot}%{mingw64_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw64_datadir}/man/man1/exiv2.1



%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.lang
%license COPYING
%{mingw32_bindir}/exiv2.exe
%{mingw32_bindir}/libexiv2.dll
%{mingw32_libdir}/libexiv2.dll.a
%{mingw32_libdir}/libexiv2-xmp.a
%{mingw32_libdir}/cmake/exiv2/
%{mingw32_libdir}/pkgconfig/exiv2.pc
%{mingw32_includedir}/exiv2/


%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.lang
%license COPYING
%{mingw64_bindir}/exiv2.exe
%{mingw64_bindir}/libexiv2.dll
%{mingw64_libdir}/libexiv2.dll.a
%{mingw64_libdir}/libexiv2-xmp.a
%{mingw64_libdir}/cmake/exiv2/
%{mingw64_libdir}/pkgconfig/exiv2.pc
%{mingw64_includedir}/exiv2/


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.27.2-4
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.27.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Jul 29 2019 Sandro Mani <manisandro@gmail.com> - 0.27.2-1
- Update to 0.27.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 0.27.1-1
- Update to 0.27.1

* Wed Apr 17 2019 Sandro Mani <manisandro@gmail.com> - 0.27-4
- Fix build against mingw-win-iconv-0.0.8

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 0.27-3
- Backport fix for CVE-2018-2009{6,7,8,9}

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Sandro Mani <manisandro@gmail.com> - 0.27-1
- Update to 0.27

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 0.26-1
- Update to 0.26

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 0.25-1
- Initial package
