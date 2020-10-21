%{?mingw_package_header}

%global pkgname libmng

Name:          mingw-%{pkgname}
Version:       2.0.3
Release:       11%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       zlib
BuildArch:     noarch
URL:           http://www.libmng.com/
Source0:       http://download.sourceforge.net/sourceforge/%{pkgname}/%{pkgname}-%{version}.tar.gz
# Add -no-undefined to linker flags
Patch0:        libmng_no-undefined.patch
# Replace deprecated configure.ac macro
Patch1:        libmng_deprecated-macro.patch

BuildRequires: libtool autoconf automake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-zlib

%description
MinGW Windows %{pkgname} library


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
%setup -q -n %{pkgname}-%{version}
%patch0 -p1
%patch1 -p1

# Delete pre-built library
rm -f bcb/win32dll/libmng.dll

%build
# Hack to stop configure complaining about already configured source tree
rm -f config.status
./bootstrap.sh
# Hack for rhbz#1214506
sed -i 's|-specs=/usr/lib/rpm/redhat/redhat-hardened-ld||g' ltmain.sh

%mingw_configure
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=%{buildroot} install

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Delete man pages
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libmng-2.dll
%{mingw32_includedir}/libmng*.h
%{mingw32_libdir}/libmng.dll.a
%{mingw32_libdir}/pkgconfig/libmng.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libmng.a

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libmng-2.dll
%{mingw64_includedir}/libmng*.h
%{mingw64_libdir}/libmng.dll.a
%{mingw64_libdir}/pkgconfig/libmng.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libmng.a

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Sandro Mani <manisandro@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 12 2014 Sandro Mani <manisandro@gmail.com> - 2.0.2-2
- Delete pre-built library
- Add patch to fix deprecated configure.ac macro
- Only install LICENSE in %%doc

* Fri Dec 27 2013 Sandro Mani <manisandro@gmail.com> - 2.0.2-1
- Initial package
