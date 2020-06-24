%global driver gphoto

Name:           indi-%{driver}
Version:        1.8.1
Release:        3%{?dist}
Summary:        INDI driver providing support for gPhoto

License:        LGPLv2+
URL:            http://indilib.org/
# Upstream provides one big tar including nonfree BLOBs for other drivers.
# Thus we have to generate a clean tar by ourself containing only
# the free driver to be packaged using
# ./indi-gphoto-generate-tarball.sh 1.3.1
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cfitsio-devel
BuildRequires:	cmake
BuildRequires:	dcraw
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:  LibRaw-devel
BuildRequires:  libtiff-devel
BuildRequires:	libusb-devel
BuildRequires:  systemd
BuildRequires:	zlib-devel
BuildRequires:  libindi = %{version}
BuildRequires:  libindi-devel = %{version}

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:       libindi = %{version}

Requires:       dcraw

%description
INDI driver using gPhoto to add support for many cameras to INDI.
This includes many DSLR, e.g. Canon or Nikon.


%prep
%setup -q -n%{name}-%{version}
# For Fedora we want to put udev rules in %{_udevrulesdir}
sed -i 's|/lib/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt

%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%license COPYING.LIB
%doc AUTHORS README
%{_bindir}/indi_*_ccd
%{_datadir}/indi/indi_gphoto.xml
%{_udevrulesdir}/*.rules

%changelog
* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-3
- Rebuild for new LibRaw

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

* Thu Jul 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.7.2-3
- Rebuilt for LibRaw soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.7.2-1
- new version

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 1.6.2-4
- rebuilt for cfitsio 3.420 (so version bump)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.2-3
- Escape macros in %%changelog

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

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 1.3.1-2
- Rebuild for new LibRaw.

* Thu Dec 15 2016 Christian Dersch <lupinix@mailbox.org> - 1.3.1-1
- new version

* Tue Feb 02 2016 Christian Dersch <lupinix@fedoraproject.org> - 1.2.0-1.20160202svn2675
- updated to libindi 1.2.0 tree

* Mon Sep 07 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.1.0-1.20150907svn2392
- updated to libindi 1.1.0 tree

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3.20150226svn2046
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-2.20150226svn2046
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0.0-1.20150226svn2046
- updated to libindi 1.0.0 tree

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.9-5.20141015svn1783
- Rebuild (libgpohoto2)

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-4.20141015svn1783
- fixed wrong macro usage

* Sat Oct 25 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-3.20141015svn1783
- added patch forcing cmake to honor compiler flags, required for useful debuginfo
- removed INSTALL from %%doc section

* Wed Oct 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-2.20141015svn1783
- small spec fix

* Wed Oct 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-1.20141015svn1783
- initial spec
