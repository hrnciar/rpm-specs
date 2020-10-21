%{?mingw_package_header}

Name:           mingw-usbredir
Version:        0.8.0
Release:        5%{?dist}
Summary:        MinGW USB network redirection protocol libraries

License:        LGPLv2+
URL:            http://spice-space.org/page/UsbRedir
Source0:        http://spice-space.org/download/usbredir/usbredir-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-libusbx >= 1.0.9
BuildRequires:  mingw64-libusbx >= 1.0.9

%description
The usbredir libraries allow USB devices to be used on remote and/or virtual
hosts over TCP.  The following libraries are provided:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the USB host side of a usbredir connection.
All that an application wishing to implement a USB host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n mingw32-usbredir
Summary:        MinGW USB network redirection protocol libraries
Requires:       pkgconfig

%description -n mingw32-usbredir
This package contains the header files and libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw32-usbredir-static
Summary:        MinGW USB network redirection protocol static libraries
Requires:       mingw32-usbredir = %{version}-%{release}

%description -n mingw32-usbredir-static
This package contains the static libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw64-usbredir
Summary:        MinGW USB network redirection protocol libraries
Requires:       pkgconfig

%description -n mingw64-usbredir
This package contains the header files and libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw64-usbredir-static
Summary:        MinGW USB network redirection protocol static libraries
Requires:       mingw64-usbredir = %{version}-%{release}

%description -n mingw64-usbredir-static
This package contains the static libraries needed to develop
applications that use usbredir with MinGW.

%{?mingw_debug_package}


%prep
%setup -q -n usbredir-%{version}

%build
%mingw_configure
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-usbredir
%doc ChangeLog COPYING.LIB README TODO
%{mingw32_bindir}/libusbredirhost-1.dll
%{mingw32_bindir}/libusbredirparser-1.dll
%{mingw32_libdir}/libusbredirhost.dll.a
%{mingw32_libdir}/libusbredirparser.dll.a
%{mingw32_includedir}/usbredirfilter.h
%{mingw32_includedir}/usbredirhost.h
%{mingw32_includedir}/usbredirparser.h
%{mingw32_includedir}/usbredirproto.h
%{mingw32_libdir}/pkgconfig/libusbredirhost.pc
%{mingw32_libdir}/pkgconfig/libusbredirparser-0.5.pc

%files -n mingw32-usbredir-static
%{mingw32_libdir}/libusbredirhost.a
%{mingw32_libdir}/libusbredirparser.a

%files -n mingw64-usbredir
%doc ChangeLog COPYING.LIB README TODO
%{mingw64_bindir}/libusbredirhost-1.dll
%{mingw64_bindir}/libusbredirparser-1.dll
%{mingw64_libdir}/libusbredirhost.dll.a
%{mingw64_libdir}/libusbredirparser.dll.a
%{mingw64_includedir}/usbredirfilter.h
%{mingw64_includedir}/usbredirhost.h
%{mingw64_includedir}/usbredirparser.h
%{mingw64_includedir}/usbredirproto.h
%{mingw64_libdir}/pkgconfig/libusbredirhost.pc
%{mingw64_libdir}/pkgconfig/libusbredirparser-0.5.pc

%files -n mingw64-usbredir-static
%{mingw64_libdir}/libusbredirhost.a
%{mingw64_libdir}/libusbredirparser.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Victor Toso <victortoso@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-3
- Bump to be higher than F-24

* Mon Nov  7 2016 Victor Toso <victortoso@redhat.com> - 0.7.1-1
- Rebuilt for F26 (rawhide)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.7.1-1
- Update to upstream 0.7.1 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.6-2
- Fix some C symbols export

* Tue Jul  9 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.6-1
- Update to upstream 0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.5.2-1
- Update to upstream 0.5.2

* Mon May 21 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.3-1
- Initial Fedora MinGW package
