Name: indi-apogee
Version: 1.8.1
Release: 2%{?dist}
Summary: The INDI driver for Apogee Alta (U & E) line of CCDs

License: LGPLv2+
URL: http://indilib.org
# Upstream provides one big tar including nonfree BLOBs for other drivers.
# Thus we have to generate a clean tar by ourself containing only
# the free driver to be packaged using
# ./indi-apogee-generate-tarball.sh 1.3.1
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake libusb-devel cfitsio-devel zlib-devel
BuildRequires: libapogee-devel libnova-devel
BuildRequires: libindi = %{version}
BuildRequires: libindi-devel = %{version}

# We have to specify this requirement as the shared libraries are part of
# libindi-libs (which is what the dependency generator will find), but the
# driver also requires the binary indiserver, part of libindi package.
Requires:     libindi = %{version}

%description
The INDI (Instrument Neutral Distributed Interface) driver for Apogee 
Alta (U & E) line of CCDs.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING.LIB
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/indi/*

%changelog
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

* Tue Feb 02 2016 Christian Dersch <lupinix@mailbox.org> - 1.0-21
- Rebuild for libindi 1.2.0

* Mon Sep 07 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0-20
- rebuilt against libindi 1.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.0-18
- rebuilt against libindi 1.0.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-16
- rebuild (libnova)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> 1.0-14
- Rebuilt for new cfitsio (3.360)
- Fix bz #1037130 (format security error)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0-12
- EVR bump to build with cfitsio 3.350

* Sun Mar 24 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0-11
- EVR bump to build with cfitsio 3.340
- Removed some unused macros (buildroot, clean, etc)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 08 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0-6
- Added missing -lm in indi_apogeeu_ccd and indi_apogeeu_ccd. Fixes bz #564703

* Fri Jan 08 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0-5
- EVR bump, rebuilt with new libnova

* Tue Dec 22 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 1.0-4
- Adding libindi-devel to build requires

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Sergio Pascual <sergiopr at fedoraproject.org> -  1.0-1
- First version
