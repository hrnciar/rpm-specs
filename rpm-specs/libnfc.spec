Name:             libnfc
Version:          1.7.1
Release:          15%{?dist}
Summary:          NFC SDK and Programmers API

License:          LGPLv3+
URL:              http://www.libnfc.org/
Source0:          http://libnfc.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:          README.fedora

BuildRequires:  gcc
BuildRequires:    pcsc-lite-devel
BuildRequires:    libusb-devel
BuildRequires:    doxygen
Requires:         systemd
Requires(post):   systemd
Requires(postun): systemd

%description
libnfc is the first free NFC SDK and Programmers API released under the
GNU Lesser General Public License. It provides complete transparency and
royalty-free use for everyone.

%package devel
Summary: Development libraries for libnfc
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The libnfc-devel package contains header files necessary for
developing programs using libnfc.

%package examples
Summary: Examples using libnfc
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
The libnfc-examples package contains examples demonstrating the functionality
of libnfc.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure --disable-static --with-drivers=all

# remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
doxygen

%install
make install DESTDIR=%{buildroot}
# remove *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# migrate udev rule to dynamic ACL management, classify the device as smartcard reader
sed -i 's/GROUP="plugdev"/ENV{ID_SMARTCARD_READER}="1"/' contrib/udev/42-pn53x.rules

# install udev rule
install -Dp -m 0644 contrib/udev/42-pn53x.rules %{buildroot}%{_prefix}/lib/udev/rules.d/42-pn53x.rules

# install module blacklist file as an example
install -Dp -m 0644 contrib/linux/blacklist-libnfc.conf %{buildroot}%{_datadir}/%{name}/blacklist-libnfc.conf

# fix typo in sample config file (reported upstream - issue 247)
sed -i 's/allow_intrusive_autoscan/allow_intrusive_scan/g' libnfc.conf.sample

# install sample config file
mkdir -p %{buildroot}%{_sysconfdir}/nfc/devices.d
install -p -m 0644 libnfc.conf.sample %{buildroot}%{_sysconfdir}/nfc/libnfc.conf

%post
/sbin/ldconfig
[ "$1" = 1 ] && udevadm control --reload
exit 0

%postun
/sbin/ldconfig
[ "$1" = 0 ] && udevadm control --reload
exit 0

%files
%doc COPYING README README.fedora AUTHORS ChangeLog
%dir %{_sysconfdir}/nfc
%dir %{_sysconfdir}/nfc/devices.d
%{_prefix}/lib/udev/rules.d/42-pn53x.rules
%config(noreplace) %{_sysconfdir}/nfc/libnfc.conf
%{_datadir}/%{name}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/nfc/
%{_libdir}/pkgconfig/*.pc
%doc doc/html

%files examples
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.7.1-4
- Migrated udev rule to dynamic ACL management
- Fixed udev rule location
- Added kernel modules blacklist file as an example (not enabled by default)
  Resolves: rhbz#1057285

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.7.1-1
- New version
  Resolves: rhbz#1076524

* Thu Oct 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.0-1
- Update to 1.7.0 final
- Cleanup and modernise spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-0.5.rc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.7.0-0.4.rc7
- packaged example configuration file
- packaged udev rule
- removed some trailing spaces

* Mon Apr 08 2013 F. Kooman <fkooman@tuxed.net> - 1.7.0-0.3.rc7
- update source to rc7 as well

* Mon Apr 08 2013 F. Kooman <fkooman@tuxed.net> - 1.7.0-0.2.rc7
- update to 1.7.0-rc7

* Wed Mar 20 2013 F. Kooman <fkooman@tuxed.net> - 1.7.0-0.1.rc6
- update to 1.7.0-rc6
- remove upstreamed usb enumeration patch
- explicitly enable all drivers

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 30 2012 F. Kooman <fkooman@tuxed.net> - 1.4.2-5
- fix patch

* Mon Jul 30 2012 F. Kooman <fkooman@tuxed.net> - 1.4.2-4
- added usb enumeration patch to fix RHBZ #832983, #843660

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 23 2011 F. Kooman <fkooman@tuxed.net> - 1.4.2-1
- update to 1.4.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 F. Kooman <fkooman@tuxed.net> - 1.4.1-1
- update to 1.4.1

* Thu Nov 25 2010 F. Kooman <fkooman@tuxed.net> - 1.4.0-1
- update to 1.4.0

* Wed Sep 29 2010 jkeating - 1.3.9-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 François Kooman <fkooman at tuxed net> 1.3.9-1
- update to 1.3.9

* Mon Apr 12 2010 François Kooman <fkooman at tuxed net> 1.3.4-1
- update to 1.3.4

* Mon Mar 8 2010 François Kooman <fkooman at tuxed net> 1.3.3-1
- update to 1.3.3

* Mon Feb 8 2010 François Kooman <fkooman at tuxed net> 1.3.2-1
- update to 1.3.2

* Wed Jan 20 2010 François Kooman <fkooman at tuxed net> 1.3.1-1
- update to 1.3.1

* Sat Jan 16 2010 François Kooman <fkooman at tuxed net> 1.3.0-1
- update to final version 1.3.0
- drop CMake for now as upstream does not include CMake build scripts
  in releases
- create API documentation using Doxygen

* Sat Oct 03 2009 François Kooman <fkooman at tuxed net> 1.3.0-0.1
- next version will be 1.3.0
- use better macro for mandir
- use name macro instead of "libnfc" in Requires and includedir

* Mon Sep 14 2009 François Kooman <fkooman at tuxed net> 1.2.2-0.1
- update to SVN snapshot
- use CMake instead of autotools

* Fri Aug 21 2009 François Kooman <fkooman at tuxed net> 1.2.1-1
- initial Fedora package

