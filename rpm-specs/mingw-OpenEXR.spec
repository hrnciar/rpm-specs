%{?mingw_package_header}

%global pkgname OpenEXR

Name:          mingw-%{pkgname}
Version:       2.4.1
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:       https://github.com/openexr/openexr/archive/v%{version}/openexr-%{version}.tar.gz
# don't autogenerate headers (would require wine BR)
Patch0:        openexr_autogen-headers.patch
# Remove libsuffix from library names in pc file, the autotools build does not add them
Patch1:        openexr_pc-libsuffix.patch

# Backport patch for CVE-2020-15306
# https://github.com/AcademySoftwareFoundation/openexr/pull/738
Patch2:        CVE-2020-15306.patch
# Backport patch for CVE-2020-15305
# https://github.com/AcademySoftwareFoundation/openexr/pull/730
Patch3:        CVE-2020-15305.patch
# Backport patch for CVE-2020-15304
# https://github.com/AcademySoftwareFoundation/openexr/pull/727
Patch4:        CVE-2020-15304.patch

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-ilmbase = %{version}
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-ilmbase = %{version}
BuildRequires: mingw64-zlib

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
%autosetup -p1 -n openexr-%{version}


%build
# Native IlmBase build to be able to build b44ExpLogTable and dwaLookups natively...
pushd IlmBase
./bootstrap
%configure
%make_build
popd

pushd OpenEXR
./bootstrap
%mingw_configure

# Generate these natively to avoid having to BR wine
g++ %{optflags} -o IlmImf/b44ExpLogTable IlmImf/b44ExpLogTable.cpp -I ../IlmBase/Half/ -L ../IlmBase/Half/.libs -lHalf
LD_LIBRARY_PATH=../IlmBase/Half/.libs ./IlmImf/b44ExpLogTable > ./IlmImf/b44ExpLogTable.h

g++ %{optflags} -o IlmImf/dwaLookups IlmImf/dwaLookups.cpp -I ../IlmBase/Half/ -L ../IlmBase/Half/.libs -lHalf -Ibuild_win32/config -I ../IlmBase/IlmThread/ -I ../IlmBase/config -I ./IlmImf -I ../IlmBase/Imath -I ../IlmBase/Iex -L ../IlmBase/IlmThread/.libs/ -lIlmThread -lpthread
LD_LIBRARY_PATH=../IlmBase/Half/.libs:../IlmBase/IlmThread/.libs ./IlmImf/dwaLookups > ./IlmImf/dwaLookups.h

%mingw_make %{?_smp_mflags}
popd


%install
pushd OpenEXR
%mingw_make install DESTDIR=%{buildroot}
popd

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Don't install doc
rm -rf %{buildroot}%{mingw32_docdir}/openexr
rm -rf %{buildroot}%{mingw64_docdir}/openexr


%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/libIlmImf-2_4-24.dll
%{mingw32_bindir}/libIlmImfUtil-2_4-24.dll
#dir %%{mingw32_includedir}/OpenEXR => It is owned by mingw32-ilmbase, which is a dependency
%{mingw32_includedir}/OpenEXR/*.h
%{mingw32_libdir}/libIlmImf.dll.a
%{mingw32_libdir}/libIlmImfUtil.dll.a
%{mingw32_libdir}/pkgconfig/OpenEXR.pc
%{mingw32_datadir}/aclocal/openexr.m4

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libIlmImf.a
%{mingw32_libdir}/libIlmImfUtil.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/libIlmImf-2_4-24.dll
%{mingw64_bindir}/libIlmImfUtil-2_4-24.dll
#dir %%{mingw64_includedir}/OpenEXR => It is owned by mingw32-ilmbase, which is a dependency
%{mingw64_includedir}/OpenEXR/*.h
%{mingw64_libdir}/libIlmImf.dll.a
%{mingw64_libdir}/libIlmImfUtil.dll.a
%{mingw64_libdir}/pkgconfig/OpenEXR.pc
%{mingw64_datadir}/aclocal/openexr.m4

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libIlmImf.a
%{mingw64_libdir}/libIlmImfUtil.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Sandro Mani <manisandro@gmail.com> - 2.4.1-2
- Backport patches for CVE-2020-15306, CVE-2020-15305, CVE-2020-15304

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

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1
- Fixes: CVE-2017-9110, CVE-2017-9111, CVE-2017-9112, CVE-2017-9113, CVE-2017-9114, CVE-2017-9115, CVE-2017-9116

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-5
- Improve openexr-2.2.0_aligned-malloc.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 14 2014 Sandro Mani <manisandro@gmail.com> - 2.1.0-2
- Add LICENSE to doc
- Add patch to replace obsolete configure.ac macros

* Fri Dec 27 2013 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Initial package
