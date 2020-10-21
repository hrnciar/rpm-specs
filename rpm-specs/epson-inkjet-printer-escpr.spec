# The lsb release used in the tarball name
%global lsb 1lsb3.2
# Not defined on el6
%{!?_cups_serverbin: %global _cups_serverbin %(/usr/bin/cups-config --serverbin)}

Name:           epson-inkjet-printer-escpr
Summary:        Drivers for Epson inkjet printers
Epoch:          1
Version:        1.7.7
Release:        1.%{lsb}%{?dist}
License:        GPLv2+
URL:            http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX
# Download address is garbled on web page
Source0:        https://download3.ebz.epson.net/dsc/f/03/00/10/49/18/f3016be6120a7271a6d9cb64872f817bce1920b8/epson-inkjet-printer-escpr-%{version}-%{lsb}.tar.gz
# Patch from Arch Linux
# https://aur.archlinux.org/packages/epson-inkjet-printer-escpr/
Patch1:         epson-inkjet-printer-escpr-filter.patch

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  chrpath
BuildRequires:  libtool
BuildRequires:  cups-devel
BuildRequires:  libjpeg-devel

# All current Fedoras
%if 0%{?fedora} >= 21
# For automatic detection of printer drivers
BuildRequires:  python3-cups
# For dir ownership
Requires:       cups-filesystem
%endif

# Red Hat Enterprise 7
%if 0%{?rhel} >= 7
# For automatic detection of printer drivers
BuildRequires:  python-cups
# For dir ownership
Requires:       cups-filesystem
%endif

# Red Hat Enterprise 6
%if 0%{?rhel} == 6
# No automatic detection on RHEL6
# For dir ownership
Requires:       cups
%endif

%description
This package contains drivers for Epson Inkjet printers that use 
the New Generation Epson Printer Control Language.

For a detailed list of supported printers, please refer to
http://avasys.jp/english/linux_e/

%prep
%setup -q 
%patch1 -p1 -b .filter
# Fix permissions
find . -name \*.h -exec chmod 644 {} \;
find . -name \*.c -exec chmod 644 {} \;
for f in README README.ja COPYING AUTHORS NEWS; do
 chmod 644 $f
done

%build
autoreconf -i
%configure --disable-static --enable-shared --disable-rpath
# SMP make doesn't work
#make %{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot} CUPS_PPD_DIR=%{_datadir}/ppd/Epson
# Get rid of .la files
rm -f %{buildroot}%{_libdir}/*.la
# Compress ppd files
for ppd in %{buildroot}%{_datadir}/ppd/Epson/epson-inkjet-printer-escpr/*.ppd; do
 gzip $ppd
done
# Get rid of rpath
chrpath --delete %{buildroot}%{_cups_serverbin}/filter/epson-escpr
# Copy documentation
cp -a README README.ja COPYING AUTHORS NEWS ..

# Get rid of .so file, since no headers are installed.
rm %{buildroot}%{_libdir}/libescpr.so

%ldconfig_scriptlets

%files
%doc README README.ja COPYING AUTHORS NEWS
%{_cups_serverbin}/filter/epson-*
%{_datadir}/ppd/Epson/
%{_libdir}/libescpr.so.*

%changelog
* Mon Jul 27 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.7.7-1.1lsb3.2
- Update to 1.7.7.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-4.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.41-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.41-1.1lsb3.2
- Update to 1.6.41.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.30-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.30-1.1lsb3.2
- Update to 1.6.30.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.20-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.20-1.1lsb3.2
- Update to 1.6.20.

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.6.17-4.1lsb3.2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.17-3.1lsb3.2
- Added gcc buildrequires.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.17-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.17-1.1lsb3.2
- Update to 1.6.17.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.13-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.13-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.13-1.1lsb3.2
- Update to 1.6.13.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.10-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.10-2.1lsb3.2
- Fix FTBFS in rawhide.
- Add patch that fixes crashes (BZ #1400346).

* Thu Nov 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.6.10-1.1lsb3.2
- Update to 1.6.10.

* Sun Apr 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.5.2-3.1lsb3.2
- Roll back to 1.5.2 due to serious bug in 1.6.x series.

* Sun Apr 24 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.6.5-1.1lsb3.2
- Update to 1.6.5.

* Thu Mar 31 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.6.4-1.1lsb3.2
- Make sure driver provides are autodetected (BZ #1323033).
- Update to 1.6.4.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.2-1.1lsb3.2
- Update to 1.5.2.

* Tue Aug 11 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.5.0-1.1lsb3.2
- Update to 1.5.0.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Orion Poplawski <orion@cora.nwra.com> - 1.4.3-1.1lsb3.2
- Update to 1.4.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-1.1lsb3.2
- Added BR: python-cups (BZ #1049528).
- Update to 1.3.1.

* Sun Nov 03 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3.0-1.1lsb3.2
- Update to 1.3.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1.1lsb3.2
- Update to 1.2.3
- spec cleanup

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1.1lsb3.2
- Update to 1.1.1.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.1lsb3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1lsb3.2
- Update to 1.1.0.

* Sun Aug 28 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-3.1lsb3.2
- No sense in shipping .so file without headers; dropped -devel.

* Wed Jul 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-2.1lsb3.2
- Get rid of rpath.

* Mon Jul 11 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-1.1lsb3.2
- First release.
