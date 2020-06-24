%{?mingw_package_header}

%global pkgname ilmbase

Name:          mingw-%{pkgname}
Version:       2.4.1
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:       https://github.com/openexr/openexr/archive/v%{version}/openexr-%{version}.tar.gz

# use win32 threads
Patch0:        ilmbase-2.2.0_win32-threads.patch
# replace obsolete configure.ac macros
Patch1:        ilmbase-2.2.0_obsolete-macros.patch
# Remove libsuffix from library names in pc file, the autotools build does not add them
Patch2:        ilmbase_pc-libsuffix.patch

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++

%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
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


%{?mingw_debug_package}


%prep
%autosetup -p1 -n openexr-%{version}


%build
pushd IlmBase
./bootstrap
%mingw_configure

# Generate these natively to avoid having BR wine
g++ %{optflags} -o Half/eLut Half/eLut.cpp
g++ %{optflags} -o Half/toFloat Half/toFloat.cpp
./Half/eLut > ./Half/eLut.h
./Half/toFloat > ./Half/toFloat.h

%mingw_make %{?_smp_mflags}
popd


%install
pushd IlmBase
%mingw_make install DESTDIR=%{buildroot}
popd

# Delete *.la files
find %{buildroot} -name '*.la' -delete


%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/libHalf-2_4-24.dll
%{mingw32_bindir}/libIex-2_4-24.dll
%{mingw32_bindir}/libIexMath-2_4-24.dll
%{mingw32_bindir}/libIlmThread-2_4-24.dll
%{mingw32_bindir}/libImath-2_4-24.dll
%dir %{mingw32_includedir}/OpenEXR
%{mingw32_includedir}/OpenEXR/*.h
%{mingw32_libdir}/libHalf.dll.a
%{mingw32_libdir}/libIex.dll.a
%{mingw32_libdir}/libIexMath.dll.a
%{mingw32_libdir}/libIlmThread.dll.a
%{mingw32_libdir}/libImath.dll.a
%{mingw32_libdir}/pkgconfig/IlmBase.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libHalf.a
%{mingw32_libdir}/libIex.a
%{mingw32_libdir}/libIexMath.a
%{mingw32_libdir}/libIlmThread.a
%{mingw32_libdir}/libImath.a

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/libHalf-2_4-24.dll
%{mingw64_bindir}/libIex-2_4-24.dll
%{mingw64_bindir}/libIexMath-2_4-24.dll
%{mingw64_bindir}/libIlmThread-2_4-24.dll
%{mingw64_bindir}/libImath-2_4-24.dll
%dir %{mingw64_includedir}/OpenEXR
%{mingw64_includedir}/OpenEXR/*.h
%{mingw64_libdir}/libHalf.dll.a
%{mingw64_libdir}/libIex.dll.a
%{mingw64_libdir}/libIexMath.dll.a
%{mingw64_libdir}/libIlmThread.dll.a
%{mingw64_libdir}/libImath.dll.a
%{mingw64_libdir}/pkgconfig/IlmBase.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libHalf.a
%{mingw64_libdir}/libIex.a
%{mingw64_libdir}/libIexMath.a
%{mingw64_libdir}/libIlmThread.a
%{mingw64_libdir}/libImath.a


%changelog
* Wed Feb 12 2020 Sandro Mani <manisandro@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.3.0-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 2.2.0-7
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 26 2013 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Initial package
