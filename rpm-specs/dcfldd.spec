%global         real_version 1.3.4-1

Name:           dcfldd
Version:        1.3.4.1
Release:        21%{?dist}
Summary:        Improved dd, useful for forensics and security

#Whole dcfldd is licensed as GPLv2+
#sha1.c sha1.h BSD Type license - Allan Saddi <allan@saddi.com>
#sha2.c sha2.h BSD Type license - Aaron D. Gifford <me@aarongifford.com>
#md5.c Copyright RSA
# Note that we are using the RSA MD5 code without license.
# See: https://fedoraproject.org/wiki/Licensing:FAQ#MD5
License:        GPLv2+ and BSD and Copyright Only
URL:            http://dcfldd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{real_version}.tar.gz


BuildRequires:  gcc
%description
dcfldd is an enhanced version of GNU dd with features useful for forensics
and security. dcfldd has the following additional features:

   * Hashing on-the-fly - dcfldd can hash the input data as it is being
     transferred, helping to ensure data integrity.
   * Status output - dcfldd can update the user of its progress in terms of
     the amount of data transferred and how much longer operation will take.
   * Flexible disk wipes - dcfldd can be used to wipe disks quickly
     and with a known pattern if desired.
   * Image/wipe Verify - dcfldd can verify that a target drive is a
     bit-for-bit match of the specified input file or pattern.
   * Multiple outputs - dcfldd can output to multiple files or disks at
     the same time.
   * Split output - dcfldd can split output to multiple files with more
     configuration possibilities than the split command.
   * Piped output and logs - dcfldd can send all its log data and output
     to commands as well as files.

%prep
%setup -q -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%files
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_mandir}/man1/dcfldd.1*
%{_bindir}/dcfldd

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Michal Ambroz <rebus at, seznam.cz> - 1.3.4.1-4
- fix license tag acording the license analysis done by
- terjeros@phys.ntnu.no and tcallawa@redhat.com

* Sun Apr 18 2010 Michal Ambroz <rebus at, seznam.cz> - 1.3.4.1-3
- incorporate changes as suggested by terjeros@phys.ntnu.no

* Sun Apr 11 2010 Michal Ambroz <rebus at, seznam.cz> - 1.3.4.1-2
- rebuild for Fedora 12

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 1.3.4.1-1 - +/
- Initial package. (using DAR)