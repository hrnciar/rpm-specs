%{?mingw_package_header}

%global pkgname uriparser

Name:           mingw-%{pkgname}
Version:        0.9.4
Release:        2%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        BSD
URL:            https://uriparser.github.io/
Source0:        https://github.com/%{pkgname}/%{pkgname}/releases/download/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DURIPARSER_BUILD_TESTS=OFF -DURIPARSER_BUILD_DOCS=OFF
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/uriparse.exe
%{mingw32_bindir}/lib%{pkgname}-1.dll
%{mingw32_includedir}/%{pkgname}/
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw32_libdir}/cmake/%{pkgname}-%{version}/

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/uriparse.exe
%{mingw64_includedir}/%{pkgname}/
%{mingw64_bindir}/lib%{pkgname}-1.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_libdir}/pkgconfig/lib%{pkgname}.pc
%{mingw64_libdir}/cmake/%{pkgname}-%{version}/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Tue Apr 23 2019 Sandro Mani <manisandro@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Sandro Mani <manisandro@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Sat Oct 27 2018 Sandro Mani <manisandro@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Tue Aug 21 2018 Sandro Mani <manisandro@gmail.com> - 0.8.6-1
- Update to 0.8.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Sandro Mani <manisandro@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 0.8.4-1
- Initial package
