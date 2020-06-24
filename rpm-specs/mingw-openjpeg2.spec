%{?mingw_package_header}

%global pkgname openjpeg2

Name:           mingw-%{pkgname}
Version:        2.3.1
Release:        7%{?dist}
Summary:        MinGW Windows %{pkgname} library

# windirent.h is MIT, the rest is BSD
License:        BSD and MIT
BuildArch:      noarch
URL:            https://github.com/uclouvain/openjpeg
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}/openjpeg-%{version}.tar.gz

# Rename tool names to avoid conflicts with openjpeg-1.x
Patch0:         openjpeg2_opj2.patch
# Backport patch for CVE 2020-6851
# https://github.com/uclouvain/openjpeg/issues/1228
Patch1:         openjpeg2_CVE-2020-6851.patch
# Backport patch for CVE 2020-8112
# https://github.com/uclouvain/openjpeg/pull/1232/commits/05f9b91e60debda0e83977e5e63b2e66486f7074
Patch2:         openjpeg2_CVE-2020-8112.patch



BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-lcms2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-lcms2


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
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


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n openjpeg-%{version}

# Remove all third party libraries just to be sure
find thirdparty/ -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} \;


%build
%mingw_cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_PKGCONFIG_FILES=ON .
%mingw_make VERBOSE=1 %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

# Delete files to exclude from package
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libopenjp2.dll
%{mingw32_libdir}/libopenjp2.dll.a
%{mingw32_includedir}/openjpeg-2.3/
%{mingw32_libdir}/openjpeg-2.3/
%{mingw32_libdir}/pkgconfig/libopenjp2.pc

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/opj2_compress.exe
%{mingw32_bindir}/opj2_decompress.exe
%{mingw32_bindir}/opj2_dump.exe

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libopenjp2.dll
%{mingw64_libdir}/libopenjp2.dll.a
%{mingw64_includedir}/openjpeg-2.3/
%{mingw64_libdir}/openjpeg-2.3/
%{mingw64_libdir}/pkgconfig/libopenjp2.pc

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/opj2_compress.exe
%{mingw64_bindir}/opj2_decompress.exe
%{mingw64_bindir}/opj2_dump.exe


%changelog
* Thu Feb 13 2020 Sandro Mani <manisandro@gmail.com> - 2.3.1-7
- Backport patch for CVE 2020-8112

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Sandro Mani <manisandro@gmail.com> - 2.3.1-5
- Backport patch for CVE 2020-6851

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.3.1-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Oct 02 2019 Sandro Mani <manisandro@gmail.com> - 2.3.1-3
- Fix unbundling 3rd party libraries (#1757822)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- Update to 2.3.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Sandro Mani <manisandro@gmail.com> - 2.3.0-6
- Backport patches for CVE-2018-18088, CVE-2018-6616

* Sat Oct 06 2018 Sandro Mani <manisandro@gmail.com> - 2.3.0-4
- Add openjpeg2_opj2.patch from native openjpeg2 package (#1636669)

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.3.0-3
- Backport patch for CVE-2018-5785 (#1537758)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 05 2017 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-3
- Backport more security fixes, including for CVE-2017-14041 and CVE-2017-14040

* Thu Aug 31 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Backport patch for CVE-2017-12982

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Sandro Mani <manisandro@gmail.com> - 2.1.2-3
- Add patch for CVE-2016-9580 (#1405128) and CVE-2016-9581 (#1405135)

* Thu Dec 08 2016 Sandro Mani <manisandro@gmail.com> - 2.1.2-2
- Add patch for CVE-2016-9572 (#1402714) and CVE-2016-9573 (#1402711)

* Wed Sep 28 2016 Sandro Mani <manisandro@gmail.com> - 2.1.2-1
- Update to 2.1.2
- Fixes: CVE-2016-7445

* Fri Sep 09 2016 Sandro Mani <manisandro@gmail.com> - 2.1.1-3
- Backport: Add sanity check for tile coordinates (#1374337)

* Fri Sep 09 2016 Sandro Mani <manisandro@gmail.com> - 2.1.1-2
- Backport fixes for CVE-2016-7163

* Wed Jul 06 2016 Sandro Mani <manisandro@gmail.com> - 2.1.1-1
- Update to 2.1.1
- Fixes: CVE-2016-3183, CVE-2016-3181, CVE-2016-3182, CVE-2016-4796, CVE-2016-4797, CVE-2015-8871

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Initial package
