%{?mingw_package_header}

Name:           mingw-libvirt-glib
Version:        3.0.0
Release:        3%{?dist}
Summary:        MinGW Windows libvirt-glib virtualization library

License:        LGPLv2+
URL:            http://libvirt.org/
Source0:        ftp://libvirt.org/libvirt/glib/libvirt-glib-%{version}.tar.gz

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libvirt >= 0.9.10
BuildRequires:  mingw64-libvirt >= 0.9.10
BuildRequires:  intltool
BuildRequires:  pkgconfig

BuildArch:      noarch

%package -n mingw32-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw32-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw32-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library

Requires: pkgconfig

%package -n mingw64-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library

Requires: pkgconfig

%description
MinGW Windows libvirt-glib virtualization library.

%description -n mingw32-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw32-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw32-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.


%description -n mingw64-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw64-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw64-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.

%{?mingw_debug_package}

%prep
%setup -q -n libvirt-glib-%{version}


%build
%mingw_configure \
    --enable-introspection=no

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libvirt-gconfig-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libvirt-glib-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libvirt-gobject-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libvirt-gconfig-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libvirt-glib-1.0.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libvirt-gobject-1.0.a

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/gtk-doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/gtk-doc

%mingw_find_lang libvirt-glib

%files -n mingw32-libvirt-glib -f mingw32-libvirt-glib.lang
%doc README COPYING AUTHORS ChangeLog NEWS
%{mingw32_bindir}/libvirt-glib-1.0-0.dll

%{mingw32_libdir}/libvirt-glib-1.0.dll.a
%{mingw32_libdir}/libvirt-glib-1.0.la

%{mingw32_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw32_includedir}/libvirt-glib-1.0
%dir %{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h

%files -n mingw64-libvirt-glib -f mingw64-libvirt-glib.lang
%doc README COPYING AUTHORS ChangeLog NEWS
%{mingw64_bindir}/libvirt-glib-1.0-0.dll

%{mingw64_libdir}/libvirt-glib-1.0.dll.a
%{mingw64_libdir}/libvirt-glib-1.0.la

%{mingw64_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw64_includedir}/libvirt-glib-1.0
%dir %{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h



%files -n mingw32-libvirt-gconfig
%{mingw32_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw32_libdir}/libvirt-gconfig-1.0.dll.a
%{mingw32_libdir}/libvirt-gconfig-1.0.la

%{mingw32_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw32_includedir}/libvirt-gconfig-1.0
%dir %{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h

%files -n mingw64-libvirt-gconfig
%{mingw64_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw64_libdir}/libvirt-gconfig-1.0.dll.a
%{mingw64_libdir}/libvirt-gconfig-1.0.la

%{mingw64_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw64_includedir}/libvirt-gconfig-1.0
%dir %{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h



%files -n mingw32-libvirt-gobject
%{mingw32_bindir}/libvirt-gobject-1.0-0.dll

%{mingw32_libdir}/libvirt-gobject-1.0.dll.a
%{mingw32_libdir}/libvirt-gobject-1.0.la

%{mingw32_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw32_includedir}/libvirt-gobject-1.0
%dir %{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h

%files -n mingw64-libvirt-gobject
%{mingw64_bindir}/libvirt-gobject-1.0-0.dll

%{mingw64_libdir}/libvirt-gobject-1.0.dll.a
%{mingw64_libdir}/libvirt-gobject-1.0.la

%{mingw64_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw64_includedir}/libvirt-gobject-1.0
%dir %{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 3.0.0-3
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Daniel P. Berrangé <berrange@redhat.com> - 3.0.0-1
- Update to 3.0.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Daniel P. Berrangé <berrange@redhat.com> - 2.0.0-1
- Update to 2.0.0 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov  4 2016 Daniel P. Berrange <berrange@redhat.com> - 1.0.0-1
- Update to 1.0.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
