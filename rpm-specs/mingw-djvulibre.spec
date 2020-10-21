%{?mingw_package_header}

%global pkgname djvulibre

Name:          mingw-%{pkgname}
Version:       3.5.27
Release:       9%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       GPLv2+
URL:           http://djvu.sourceforge.net/
Source0:       http://downloads.sourceforge.net/djvu/%{pkgname}-%{version}.tar.gz
# Backport patch to fix missing dllexports
Patch0:        0001-Define-XXX_EXPORT-symbols-under-win32.patch
# Backport fix for CVE-2019-15142
# https://sourceforge.net/p/djvu/djvulibre-git/ci/970fb1
Patch1:        CVE-2019-15142.patch
# Backport fix for CVE-2019-15143
# https://sourceforge.net/p/djvu/djvulibre-git/ci/b1f4e1
Patch2:        CVE-2019-15143.patch
# Backport fix for CVE-2019-15144
# https://sourceforge.net/p/djvu/djvulibre-git/ci/e15d51
Patch3:        CVE-2019-15144.patch
# Backport fix for CVE-2019-15145
# https://sourceforge.net/p/djvu/djvulibre-git/ci/9658b0
Patch4:        CVE-2019-15145.patch
# Backport fix for CVE-2019-18804
# https://sourceforge.net/p/djvu/djvulibre-git/ci/c8bec6
Patch5:        CVE-2019-18804.patch


BuildRequires: automake autoconf libtool make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo

%description
%{summary}.


%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%mingw_configure
# Parallel build is broken
%mingw_make


%install
%{mingw_make} install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove shell scripts
rm -f %{buildroot}%{mingw32_bindir}/{any2djvu,djvudigital}
rm -f %{buildroot}%{mingw64_bindir}/{any2djvu,djvudigital}

# Remove data
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libdjvulibre-21.dll
%{mingw32_includedir}/libdjvu/
%{mingw32_libdir}/libdjvulibre.dll.a
%{mingw32_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libdjvulibre-21.dll
%{mingw64_includedir}/libdjvu/
%{mingw64_libdir}/libdjvulibre.dll.a
%{mingw64_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 3.5.27-7
- Backport fix for CVE-2019-15142
- Backport fix for CVE-2019-15143
- Backport fix for CVE-2019-15144
- Backport fix for CVE-2019-15145
- Backport fix for CVE-2019-18804

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.5.27-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 3.5.27-1
- Initial package
