%{?mingw_package_header}

%global pkgname fribidi

Name:          mingw-%{pkgname}
Version:       1.0.10
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       LGPLv2+
BuildArch:     noarch
URL:           https://github.com/%{pkgname}/%{pkgname}
Source0:       https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.xz

# Drop bundled gnulib
Patch0:        fribidi-drop-bundled-gnulib.patch

BuildRequires: meson
BuildRequires: gcc

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_meson --default-library=both -Ddocs=false
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/fribidi.exe
%{mingw32_bindir}/libfribidi-0.dll
%{mingw32_includedir}/fribidi
%{mingw32_libdir}/libfribidi.dll.a
%{mingw32_libdir}/pkgconfig/fribidi.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libfribidi.a

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/fribidi.exe
%{mingw64_bindir}/libfribidi-0.dll
%{mingw64_includedir}/fribidi
%{mingw64_libdir}/libfribidi.dll.a
%{mingw64_libdir}/pkgconfig/fribidi.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libfribidi.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Sandro Mani <manisandro@gmail.com> - 1.0.10-1
- Update to 1.0.10

* Thu Mar 05 2020 Sandro Mani <manisandro@gmail.com> - 1.0.9-1
- Update to 1.0.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Sandro Mani <manisandro@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Sat Sep 28 2019 Sandro Mani <manisandro@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 1.0.5-1
- Initial package
