%{?mingw_package_header}

%global pkgname libgta

Name:          mingw-%{pkgname}
Version:       1.0.9
Release:       5%{?dist}
Summary:       MinGW Windows GTA library

License:       LGPLv2+
BuildArch:     noarch
URL:           http://gta.nongnu.org
Source0:       https://marlam.de/gta/releases/%{pkgname}-%{version}.tar.xz

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-zlib
BuildRequires: mingw32-xz-libs

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-zlib
BuildRequires: mingw64-xz-libs

%description
MinGW Windows GTA library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GTA library

%description -n mingw32-%{pkgname}
MinGW Windows GTA library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GTA library

%description -n mingw64-%{pkgname}
MinGW Windows GTA library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make_install DESTDIR=%{buildroot}

# Remove documentation
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgta-0.dll
%{mingw32_includedir}/gta/
%{mingw32_libdir}/libgta.dll.a
%{mingw32_libdir}/pkgconfig/gta.pc
%{mingw32_datadir}/libgta/

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgta-0.dll
%{mingw64_includedir}/gta/
%{mingw64_libdir}/libgta.dll.a
%{mingw64_libdir}/pkgconfig/gta.pc
%{mingw64_datadir}/libgta/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.0.9-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Sandro Mani <manisandro@gmail.com> - 1.0.9-1
- Update to 1.0.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 1.0.8-1
- Update to 1.8.0

* Thu Apr 23 2015 Sandro Mani <manisandro@gmail.com> - 1.0.7-1
- Initial package
