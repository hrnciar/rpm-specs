%{?mingw_package_header}

%global pkgname libcharset

# libcharset is distributed with libiconv
%global iconv_ver 1.14

Name:          mingw-%{pkgname}
Version:       1.4.0
Summary:       MinGW Windows libcharset library
Release:       6%{?dist}

BuildArch:     noarch
License:       LGPLv2+
URL:           http://www.haible.de/bruno/packages-libcharset.html
Source0:       ftp://ftp.gnu.org/pub/gnu/libiconv/libiconv-%{iconv_ver}.tar.gz

BuildRequires: automake autoconf libtool libtool-ltdl-devel bison flex

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc


%description
MinGW Windows libcharset library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows libcharset library

%description -n mingw32-%{pkgname}
MinGW Windows libcharset library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows libcharset library

%description -n mingw64-%{pkgname}
MinGW Windows libcharset library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n libiconv-%{iconv_ver}


%build
(
cd libcharset
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}
)


%install
(
cd libcharset
%mingw_make install DESTDIR=%{buildroot}
)

find %{buildroot} -name *.la -delete


%files -n mingw32-%{pkgname}
%license libcharset/COPYING.LIB
%{mingw32_bindir}/libcharset-1.dll
%{mingw32_includedir}/*.h
%{mingw32_libdir}/libcharset.dll.a
%{mingw32_libdir}/charset.alias

%files -n mingw64-%{pkgname}
%license libcharset/COPYING.LIB
%{mingw64_bindir}/libcharset-1.dll
%{mingw64_includedir}/*.h
%{mingw64_libdir}/libcharset.dll.a
%{mingw64_libdir}/charset.alias


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon May 11 2015 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Initial package
