%{?mingw_package_header}

%global pkgname podofo

Name:          mingw-%{pkgname}
Version:       0.9.6
Release:       17%{?dist}
Summary:       MinGW Windows %{pkgname} library

# The library is licensed under the LGPL.
# The tests and tools which are included in PoDoFo are licensed under the GPL.
# See the files COPYING and COPYING.LIB for details, see COPYING.exception.
License:       GPLv2+ and LGPLv2+ with exceptions
BuildArch:     noarch
URL:           http://podofo.sourceforge.net
Source0:       http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.gz
# Fix failure to detect FreeType
Patch0:        podofo-0.9.4-freetype.patch
# Don't try to copy non-existent testdata directory
Patch1:        podofo-cmake.patch
# Fix pkg-config file
Patch2:        podofo_pkgconfig.patch

# Backport patch for CVE-2018-5783
# https://sourceforge.net/p/podofo/code/1949
Patch10:        podofo_CVE-2018-5783.patch
# Backport patch for CVE-2018-11254
# https://sourceforge.net/p/podofo/code/1941
Patch11:        podofo_CVE-2018-11254.patch
# Backport patch for CVE-2018-11255
# https://sourceforge.net/p/podofo/code/1952
Patch12:        podofo_CVE-2018-11255.patch
# Backport patch for CVE-2018-11256
# https://sourceforge.net/p/podofo/code/1938
Patch13:        podofo_CVE-2018-11256.patch
# Backport patch for CVE-2018-12982
# https://sourceforge.net/p/podofo/code/1948
Patch14:        podofo_CVE-2018-12982.patch
# Backport patch for CVE-2018-14320
# https://sourceforge.net/p/podofo/code/1953
Patch15:        podofo_CVE-2018-14320.patch
# Backport patch for CVE-2018-19532
# https://sourceforge.net/p/podofo/code/1950
Patch16:        podofo_CVE-2018-19532.patch
# Backport patch for CVE-2018-20751
# https://sourceforge.net/p/podofo/code/1954
Patch17:        podofo_CVE-2018-20751.patch
# Backport patch for CVE-2019-9199
# https://sourceforge.net/p/podofo/code/1971/
Patch18:        podofo_CVE-2019-9199.patch
# Backport patch for CVE-2019-9687
# https://sourceforge.net/p/podofo/code/1969
Patch19:        podofo_CVE-2019-9687.patch

# Downstream patch for CVE-2019-20093
# https://sourceforge.net/p/podofo/tickets/75/
Patch20:        podofo_CVE-2019-20093.patch
# Proposed patch for CVE-2018-12983
# https://sourceforge.net/p/podofo/tickets/23/
Patch21:        podofo_CVE-2018-12983.diff

# https://sourceforge.net/p/podofo/tickets/101/
Patch22:        podofo_maxbytes.patch


BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-fontconfig
BuildRequires: mingw32-freetype
BuildRequires: mingw32-libidn
BuildRequires: mingw32-libjpeg
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-openssl
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-fontconfig
BuildRequires: mingw64-freetype
BuildRequires: mingw64-libidn
BuildRequires: mingw64-libjpeg
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-openssl
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


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-tools
Tools for the MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-tools
Tools for the MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DPODOFO_BUILD_SHARED=1
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Don't install manpages
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license COPYING.LIB COPYING.exception
%{mingw32_bindir}/libpodofo.dll
%{mingw32_libdir}/libpodofo.dll.a
%{mingw32_libdir}/pkgconfig/libpodofo.pc
%{mingw32_includedir}/podofo/

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING.LIB COPYING.exception
%{mingw64_bindir}/libpodofo.dll
%{mingw64_libdir}/libpodofo.dll.a
%{mingw64_libdir}/pkgconfig/libpodofo.pc
%{mingw64_includedir}/podofo/

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-16
- Add podofo_maxbytes.patch

* Thu Jul 02 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-15
- Backport proposed patch for CVE-2018-12983

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Sandro Mani <manisandro@gmail.com> - 0.9.6-13
- Add patch for CVE-2019-20093

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-12
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 27 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-11
- Rebuild (libidn)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-9
- Fix pkg-config file

* Wed Mar 13 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-8
- Backport security fixes: CVE-2019-9199, CVE-2019-9687

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 0.9.6-7
- Backport security fix for CVE-2018-20751

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-5
- Backport security fixes:
   CVE-2018-5783, CVE-2018-11254, CVE-2018-11255, CVE-2018-11256,
   CVE-2018-12982, CVE-2018-14320, CVE-2018-19532

* Fri Aug 24 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-4
- Fix FTBFS due to cmake attempting to copy non-existent directory

* Fri Aug 24 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.6-3
- Rebuild for new mingw-openssl.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 0.9.6-1
- Update to 0.9.6

* Fri Jun 15 2018 Sandro Mani <manisandro@gmail.com> - 0.9.5-6
- Backport security fixes (taken from debian package):
   CVE-2017-7380, CVE-2017-7381, CVE-2017-7382, CVE-2017-7383, CVE-2017-5852,
   CVE-2017-5853, CVE-2017-6844, CVE-2017-5854, CVE-2017-5855, CVE-2017-5886,
   CVE-2018-8000, CVE-2017-6840, CVE-2017-6842, CVE-2017-6843, CVE-2017-6845,
   CVE-2017-6847, CVE-2017-6848, CVE-2017-7378, CVE-2017-7379, CVE-2017-7994,
   CVE-2017-8054, CVE-2017-8378, CVE-2017-8787, CVE-2018-5295, CVE-2018-5308

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-4
- Enable OpenSSL support

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-2
- Drop -std=c++98 from CXXFLAGS

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Sun Oct 02 2016 Sandro Mani <manisandro@gmail.com> - 0.9.4-2
- Fix typo ${pkgname} -> %%{pkgname}

* Sun Sep 18 2016 Sandro Mani <manisandro@gmail.com> - 0.9.4-1
- Initial package
