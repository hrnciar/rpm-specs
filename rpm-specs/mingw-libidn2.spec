
%?mingw_package_header

Name:           mingw-libidn2
Version:        2.3.0
Release:        2%{?dist}
Summary:        MinGW Windows Internationalized Domain Name 2008 support library

# The distribution contains only GPLv3 copying for some reason. Pointed
# on the upstream ML: https://lists.gnu.org/archive/html/help-libidn/2016-11/msg00020.html
License:        ( LGPLv3+ and GPLv2 ) and GPLv3+
URL:            https://www.gnu.org/software/libidn/#libidn2
Source0:        https://ftp.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz.sig
Source2:	gpgkey-A26704281CB27DBC98614B2D5841646D08302DB6A2670428.gpg

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  pkgconfig


%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892 and 5893 for internationalized domain names (IDN).
It is a standalone library, without any dependency on libidn.

# Win32
%package -n mingw32-libidn2
Summary:        MinGW Windows IDN 2008 library the win32 target
Requires:       pkgconfig

%description -n mingw32-libidn2
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892 and 5893 for internationalized domain names (IDN).
It is a standalone library, without any dependency on libidn.

%package -n mingw32-libidn2-static
Summary:        Static version of the MinGW Windows IDN 2008 library
Requires:       mingw32-libidn2 = %{version}-%{release}

%description -n mingw32-libidn2-static
Static version of the MinGW Windows IDN 2008 library.

# Win64
%package -n mingw64-libidn2
Summary:        MinGW Windows IDN 2008 library the win64 target
Requires:       pkgconfig

%description -n mingw64-libidn2
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892 and 5893 for internationalized domain names (IDN).
It is a standalone library, without any dependency on libidn.

%package -n mingw64-libidn2-static
Summary:        Static version of the MinGW Windows IDN 2008 library
Requires:       mingw64-libidn2 = %{version}-%{release}

%description -n mingw64-libidn2-static
Static version of the MinGW Windows IDN 2008 library.


%?mingw_debug_package


%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q -n libidn2-%{version}


%build
%mingw_configure --disable-nls --enable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove documentation which duplicates native Fedora package.
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man*
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man*


# The .def file isn't interesting for other libraries/applications
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/libidn2-*.def
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/libidn2-*.def

# The executables are not useful in this build
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/idn2*.exe
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/lookup.exe
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/register.exe

rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/idn2*.exe
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/lookup.exe
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/register.exe

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-libidn2
%license COPYING
%{mingw32_bindir}/libidn2-*.dll
%{mingw32_libdir}/libidn2.dll.a
%{mingw32_libdir}/pkgconfig/libidn2.pc
%{mingw32_includedir}/*.h

%files -n mingw32-libidn2-static
%{mingw32_libdir}/libidn2.a

# Win64
%files -n mingw64-libidn2
%doc COPYING
%{mingw64_bindir}/libidn2-*.dll
%{mingw64_libdir}/libidn2.dll.a
%{mingw64_libdir}/pkgconfig/libidn2.pc
%{mingw64_includedir}/*.h

%files -n mingw64-libidn2-static
%{mingw64_libdir}/libidn2.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Robert Scheck <robert@fedoraproject.org> - 2.3.0-1
- New upstream release (#1764345, #1773229)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 13 2019 Fabiano Fidêncio <fidencio@redhat.com> - 2.2.0-1
- Update the sources accordingly to its native counter part, rhbz#1740792

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Nikos Mavrogiannopoulos <nmav@redhat.com> - 2.1.1a-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Robert Scheck <robert@fedoraproject.org> - 2.0.4-1
- New upstream release (#1486881, #1486882)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr  4 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 2.0.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Nikos Mavrogiannopoulos - 0.11-1
- Initial RPM release.
