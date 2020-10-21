%{?mingw_package_header}

Name:           mingw-hamlib
Version:        3.3
Release:        2%{?dist}
Summary:        Run-time library to control radio transceivers and receivers

License:        GPLv2+ and LGPLv2+
URL:            http://hamlib.sourceforge.net
Source0:        http://downloads.sourceforge.net/hamlib/hamlib-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libusbx

BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-binutils


%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.


%package -n mingw32-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win32

%description -n mingw32-hamlib


%package -n mingw64-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win64

%description -n mingw64-hamlib


%{?mingw_debug_package}


%prep
%autosetup -n hamlib-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

find %{buildroot} -name "*.la" -delete

rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_datadir}/{doc,info,man}
rm -f %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw64_datadir}/{doc,info,man}


%files -n mingw32-hamlib
%{mingw32_bindir}/libhamlib-2.dll
%{mingw32_bindir}/libhamlib++-2.dll
%{mingw32_libdir}/libhamlib.dll.a
%{mingw32_libdir}/libhamlib++.dll.a
%{mingw32_libdir}/pkgconfig/hamlib.pc
%{mingw32_includedir}/hamlib/
%{mingw32_datadir}/aclocal/


%files -n mingw64-hamlib
%{mingw64_bindir}/libhamlib-2.dll
%{mingw64_bindir}/libhamlib++-2.dll
%{mingw64_libdir}/libhamlib.dll.a
%{mingw64_libdir}/libhamlib++.dll.a
%{mingw64_libdir}/pkgconfig/hamlib.pc
%{mingw64_includedir}/hamlib/
%{mingw64_datadir}/aclocal/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Nov 21 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3-1
- Update to 3.3.

* Tue Jul  4 2017 Richard Shaw <hobbes1069@gmail.com> - 3.1-1
- Initial packaging.
