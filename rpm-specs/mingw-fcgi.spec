%{?mingw_package_header}

%global pkgname fcgi

Name:           mingw-%{pkgname}
Version:        2.4.2
Release:        5%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        OML
URL:            https://fastcgi-archives.github.io/
Source0:        https://github.com/FastCGI-Archives/fcgi2/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


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
%autosetup -p1 -n %{pkgname}2-%{version}
# remove DOS End Of Line Encoding
sed -i 's/\r//' doc/fastcgi-prog-guide/ch2c.htm
# fix file permissions
chmod a-x include/fcgios.h libfcgi/os_unix.c


%build
autoreconf -ifv
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license LICENSE.TERMS
%{mingw32_bindir}/cgi-fcgi.exe
%{mingw32_bindir}/libfcgi-0.dll
%{mingw32_bindir}/libfcgi++-0.dll
%{mingw32_libdir}/libfcgi.dll.a
%{mingw32_libdir}/libfcgi++.dll.a
%{mingw32_libdir}/pkgconfig/fcgi.pc
%{mingw32_libdir}/pkgconfig/fcgi++.pc
%{mingw32_includedir}/*

%files -n mingw64-%{pkgname}
%license LICENSE.TERMS
%{mingw64_bindir}/cgi-fcgi.exe
%{mingw64_bindir}/libfcgi-0.dll
%{mingw64_bindir}/libfcgi++-0.dll
%{mingw64_libdir}/libfcgi.dll.a
%{mingw64_libdir}/libfcgi++.dll.a
%{mingw64_libdir}/pkgconfig/fcgi.pc
%{mingw64_libdir}/pkgconfig/fcgi++.pc
%{mingw64_includedir}/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.4.2-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Wed Jun 24 2015 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Initial package
