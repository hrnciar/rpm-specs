%global driver sx

Name:           indi-%{driver}
Version:        1.8.6
# Upstream provides one big tar including nonfree BLOBs for other drivers.
# Thus we have to generate a clean tar by ourself containing only
# the free driver to be packaged using
# ./indi-sx-generate-tarball.sh 1.3.1
Release:        1%{?dist}
Summary:        INDI driver providing support for Starlight Xpress devices

License:        GPLv2+
URL:            http://indilib.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  libusb-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
BuildRequires:  libindi = %{version}
BuildRequires:  libindi-devel = %{version}

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{version}
Requires:       udev

%description
INDI driver providing support for devices from Starlight Xpress. This includes
SX CCDs, SX wheel and SX Active Optics. 


%prep
%setup -q -n%{name}-%{version}
# For Fedora we want to put udev rules in %{_udevrulesdir}
sed -i 's|/lib/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README
%{_bindir}/indi_%{driver}_ao
%{_bindir}/indi_%{driver}_ccd
%{_bindir}/indi_%{driver}_wheel
%{_bindir}/%{driver}_ccd_test
%{_datadir}/indi/indi_%{driver}.xml
%{_udevrulesdir}/99-sx.rules


%changelog
* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 1.8.6-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.8.5-1
- new version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.8.1-1
- new version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 1.7.7-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.7.4-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Christian Dersch <lupinix@mailbox.org> - 1.7.4-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.7.2-1
- new version

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 1.6.2-3
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Christian Dersch <lupinix@mailbox.org> - 1.6.2-1
- new version

* Tue Jan 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.6.0-1
- new version

* Sat Oct 07 2017 Christian Dersch <lupinix@mailbox.org> - 1.5.0-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Christian Dersch <lupinix@mailbox.org> - 1.4.1-1
- new version

* Sun Feb 26 2017 Christian Dersch <lupinix@mailbox.org> - 1.4.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 1.3.1-1
- new version

* Sun Apr 03 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-5.20160403svn2711
- Update to svn 2711 to support new cameras

* Tue Mar 08 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-4.20160308svn2698
- Update to svn rev 2698 to add support for new cameras

* Fri Feb 19 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-3.20160202svn2675
- Added patch to fix compilation with GCC 6.x

* Thu Feb 11 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-2.20160202svn2675
- rebuilt

* Tue Feb 02 2016 Christian Dersch <lupinix@mailbox.org> - 1.2.0-1.20160202svn2675
- new version

* Mon Sep 07 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.1.0-1.20150907svn2392
- updated to libindi 1.1.0 tree

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4.20150227svn2049
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-3.20150227svn2049
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0.0-2.20150227svn2049
- updated to svn rev 2049 fixing a bug with some camera models

* Thu Feb 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0.0-1.20150226svn2046
- updated to libindi 1.0.0 tree

* Mon Nov 10 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-4.20141110svn1788
- used wrong release tag, fixed

* Mon Nov 10 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-1.20141110svn1788
- update to svn revision 1788 fixing a bug (dark frames with closed shutter on SXVR H18)

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-3.20141025svn1784
- removed checkout macro from changelog

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-2.20141025svn1784
- spec adjustments (consistently using udevrulesdir macro now)

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-1.20141025svn1784
- initial spec
