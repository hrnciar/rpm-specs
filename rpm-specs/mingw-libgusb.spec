%{?mingw_package_header}

Name:           mingw-libgusb
Version:        0.2.11
Release:        6%{?dist}
Summary:        GLib wrapper around libusb1 for MinGW

License:        LGPLv2+
URL:            https://gitorious.org/gusb/
Source0:        http://people.freedesktop.org/~hughsient/releases/libgusb-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-libusbx >= 1.0.19
BuildRequires:  mingw64-libusbx >= 1.0.19
BuildRequires:  mingw32-glib2 >= 2.38.0
BuildRequires:  mingw64-glib2 >= 2.38.0
BuildRequires:  gobject-introspection-devel

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

This is the MinGW version of this library.

%package -n mingw32-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig

%description -n mingw32-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw32-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw32-libgusb = %{version}-%{release}

%description -n mingw32-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig

%description -n mingw64-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw64-libgusb = %{version}-%{release}

%description -n mingw64-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%{?mingw_debug_package}


%prep
%setup -q -n libgusb-%{version}


%build
%mingw_configure                        \
        --disable-vala                  \
        --disable-introspection         \
        --disable-gtk-doc
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-libgusb
%license COPYING
%doc AUTHORS README NEWS
%{mingw32_bindir}/gusbcmd.exe
%{mingw32_bindir}/libgusb-2.dll
%{mingw32_includedir}/gusb-1/
%{mingw32_libdir}/libgusb.dll.a
%{mingw32_libdir}/pkgconfig/gusb.pc

%files -n mingw32-libgusb-static
%{mingw32_libdir}/libgusb.a

%files -n mingw64-libgusb
%license COPYING
%doc AUTHORS README NEWS
%{mingw64_bindir}/gusbcmd.exe
%{mingw64_bindir}/libgusb-2.dll
%{mingw64_includedir}/gusb-1/
%{mingw64_libdir}/libgusb.dll.a
%{mingw64_libdir}/pkgconfig/gusb.pc

%files -n mingw64-libgusb-static
%{mingw64_libdir}/libgusb.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 0.2.11-1
- Update to 0.2.11

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 0.2.10-1
- Update to 0.2.10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 0.2.9-1
- Update to 0.2.9
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 09 2015 Richard Hughes <richard@hughsie.com> 0.2.4-1
- New upstream version
- Add new API for various client programs
- Don't filter out hub devices when getting the device list
- Make the platform ID persistent across re-plug

* Wed Nov 26 2014 Richard Hughes <richard@hughsie.com> - 0.2.3-1
- Initial packaging
