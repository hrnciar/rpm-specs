Name:          libusbg
Version:       0.2.0
Release:       8%{?dist}
Summary:       Library for USB gadget-configfs userspace functionality
License:       LGPLv2+

URL:           https://github.com/libusbgx/libusbgx
Source0:       https://github.com/libusbgx/libusbgx/archive/%{name}x-v%{version}.tar.gz
Patch0:        libusbgx-fix-inc.patch

BuildRequires: doxygen
BuildRequires: gcc gcc-c++
BuildRequires: libtool autoconf automake
BuildRequires: libconfig-devel

%description
libusbg is a C library encapsulating the kernel USB gadget-configfs
userspace API functionality.

It provides routines for creating and parsing USB gadget devices using
the configfs API. Currently, all USB gadget configfs functions that can
be enabled in kernel release 3.11 (Linux for Workgroups!) are supported.

%package utils
Summary: Utilities for USB gadget devices
License: GPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for USB gadget devices

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}x-%{name}x-v%{version}
%patch0 -p1 -b .inc

%build
autoreconf -vif
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LGPL
%doc README AUTHORS ChangeLog
%{_libdir}/*.so.*

%files utils
%doc COPYING
%{_bindir}/gadget*
%{_bindir}/show*

%files devel
%{_includedir}/usbg
%{_libdir}/pkgconfig/libusbgx.pc
%{_libdir}/*.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0.2.0-4
- Rebuild for new libconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-2
- Add sys/sysmacros.h include fix patch

* Tue Apr  3 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-1
- New 0.2.0 release
- New upstream, package cleanups

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.0-5
- Use %%license

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.0-2
- Enable check

* Thu Jan 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.0-1
- Initial package
