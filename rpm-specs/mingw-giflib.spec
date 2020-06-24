%{?mingw_package_header}

%global pkgname giflib

Name:          mingw-%{pkgname}
Version:       5.2.1
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library
License:       MIT

BuildArch:     noarch
URL:           http://www.sourceforge.net/projects/%{pkgname}/
Source:        http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.gz
Source1:       CMakeLists.txt

BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc


%description
MinGW Windows giflib library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}
cp -a %{SOURCE1} .


%build
%mingw_cmake -DBUILD_STATIC_LIBS=1
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Don't ship manpages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgif-7.dll
%{mingw32_includedir}/gif_lib.h
%{mingw32_libdir}/libgif.dll.a

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libgif.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgif-7.dll
%{mingw64_includedir}/gif_lib.h
%{mingw64_libdir}/libgif.dll.a

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libgif.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 5.2.1-1
- Update to 5.2.1

* Mon Apr 01 2019 Sandro Mani <manisandro@gmail.com> - 5.1.9-1
- Update to 5.1.9

* Wed Mar 20 2019 Sandro Mani <manisandro@gmail.com> - 5.1.8-1
- Update to 5.1.8

* Mon Mar 11 2019 Sandro Mani <manisandro@gmail.com> - 5.1.7-1
- Update to 5.1.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 04 2016 Sandro Mani <manisandro@gmail.com> - 5.1.4-1
- Update to 5.1.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Sandro Mani <manisandro@gmail.com> - 5.0.5-4
- Add patch for heap overflow in giffix (CVE-2015-7555, #1293372)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Sandro Mani <manisandro@gmail.com> - 5.0.5-1
- Update to 5.0.5

* Sat Aug 10 2013 Sandro Mani <manisandro@gmail.com> - 5.0.4-2
- Fix descriptions

* Fri Aug 09 2013 Sandro Mani <manisandro@gmail.com> - 5.0.4-1
- Update to 5.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Sandro Mani <manisandro@gmail.com> - 4.1.6-2
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires

* Wed May 08 2013 Sandro Mani <manisandro@gmail.com> - 4.1.6-1
- Initial Fedora package
