Name:           libphidget
Version:        2.1.8.20140319
Release:        15%{?dist}
Summary:        Drivers and API for Phidget devices

License:        LGPLv3
URL:            http://www.phidgets.com
Source0:        http://www.phidgets.com/downloads/libraries/libphidget_%{version}.tar.gz

Patch0:         libphidget-2.1.8.javadir.patch

# Needed because Makefile.am is patched
BuildRequires:  libtool
BuildRequires:  autoconf

BuildRequires:  avahi-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  libusb-devel
BuildRequires:  gawk

Requires:       udev
Requires:       avahi-compat-libdns_sd

%description
Phidgets are a set of "plug and play" building blocks for low cost USB 
sensing and control from your PC.  All the USB complexity is taken care 
of by the robust libphidget API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        java
Summary:        Java bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       java-headless >= 1:1.6.0
Requires:       jpackage-utils

%description    java
The %{name}-java package contains java bindings for the 
libphidget API.

%prep
%setup -q
%patch0 -p0 -b .javadir
# These headers are supplied by the avahi-compat-libdns_sd-devel package
# We can get rid of the bundled ones
rm -rf linux/avahi-*
rm -rf include/dns_sd.h

%build
autoreconf -i
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
make %{?_smp_mflags}
make phidget.jar

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_datadir}/libphidget/examples
install -p -m 0644 examples/*c $RPM_BUILD_ROOT%{_datadir}/libphidget/examples
install -p -m 0644 examples/README $RPM_BUILD_ROOT%{_datadir}/libphidget/examples
mkdir -p -m 0755 $RPM_BUILD_ROOT/lib/udev/rules.d
install -p -m 0644 udev/99-phidgets.rules $RPM_BUILD_ROOT/lib/udev/rules.d/99-phidgets.rules

%ldconfig_scriptlets


%files
%doc COPYING AUTHORS README
%{_libdir}/*.so.*
/lib/udev/rules.d/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/libphidget

%files java
%{_jnidir}/phidget.jar

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.1.8.20140319-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8.20140319-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20140319-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20140319-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20140319-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <rmattes@fedoraproject.org> - 2.1.8.20140319-1
- Update to release 2.1.8-20140319
- Rename phidget21.jar to phidget.jar, install to jnidir (rhbz#1022135)

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.1.8.20121218-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20121218-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20121218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Rich Mattes <richmattes@gmail.com> - 2.1.8.20121218-1
- Update to 2.1.8.20121218

* Sun Oct 28 2012 Rich Mattes <richmattes@gmail.com> - 2.1.8.20120912-1
- Update to 2.1.8.20120912

* Sun Sep 02 2012 Rich Mattes <richmattes@gmail.com> - 2.1.8.20120716-1
- Update to 2.1.8.20120716

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20120514-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 2.1.8.20120514-1
- Update to 2.1.8-20120514

* Mon Jan 23 2012 Rich Mattes <richmattes@gmail.com> - 2.1.8.20120123-1
- Update to 2.1.8-20120123
- Move udev rule to /lib/udev (/etc/udev is for sysadmins)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8.20111121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Rich Mattes <richmattes@gmail.com> - 2.1.8.20111121-1
- Update to 2.1.8-20111121

* Wed Jun 29 2011 Rich Mattes <richmattes@gmail.com> - 2.1.8.20110615-1
- Update to 2.1.8.20110615

* Wed May 11 2011 Rich Mattes <richmattes@gmail.com> - 2.1.8.20110322-1
- Update to 2.1.8.20110322

* Mon Mar 14 2011 Rich Mattes <richmattes@gmail.com> - 2.1.8.20110310-1
- Update to 2.1.8.20110310

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7.20101222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Rich Mattes <richmattes@gmail.com> - 2.1.7-20101222-1
- Update to version 2.1.7-20101222

* Tue Dec 14 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20101103-2
- Remove dependencies on bundled avahi headers
- Add explicit runtime requirement for avahi dns_sd

* Tue Dec 14 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20101103-1
- Update to latest version

* Fri Oct 01 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20100621-5
- Disable zeroconf runtime linking

* Mon Sep 27 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20100621-4
- Bump release to maintain upgrade path

* Tue Sep 21 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20100621-3
- Split java bindings into separate -java subpackage

* Mon Sep 20 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20100621-2
- Enable zeroconf
- Enable jni 
- Install udev rules

* Sun Sep 19 2010 Rich Mattes <richmattes@gmail.com> - 2.1.7.20100621-1
- Initial build
