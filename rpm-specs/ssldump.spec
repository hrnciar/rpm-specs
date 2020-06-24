Summary:	An SSLv3/TLS network protocol analyzer
Name:		ssldump
Version:	0.9
Release:	0.21.b3%{?dist}
License:	BSD with advertising
URL:		http://ssldump.sourceforge.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}b3.tar.gz
Source1:	README.FEDORA
Patch0:		ssldump-0.9-openssl.patch
Patch1:		ssldump-0.9-libpcap.patch
Patch2:		ssldump-0.9-aes.patch
Patch3:		ssldump-0.9-cvs-20060619.patch
Patch4:		ssldump-0.9-table-stops.patch
Patch5:		ssldump-0.9-link_layer.patch
Patch6:		ssldump-0.9-pcap-vlan.patch
Patch7:		ssldump-0.9-tlsv12.patch
Patch8:		ssldump-0.9-ssl-enums.patch
Patch9:		ssldump-0.9-ciphersuites.patch
BuildRequires:	gcc, openssl-devel, libpcap-devel, autoconf, automake

%description
This program is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret them
as SSLv3/TLS traffic. When ssldump identifies SSLv3/TLS traffic, ssldump
decodes the records and displays them in a textual form to stdout. And if
provided with the appropriate keying material, ssldump will also decrypt
the connections and display the application data traffic. This program is
based on tcpdump, a network monitoring and data acquisition tool.

%prep
%setup -q -n %{name}-%{version}b3
%patch0 -p1 -b .openssl
%patch1 -p1 -b .libpcap
%patch2 -p1 -b .aes
%patch3 -p1 -b .cvs-20060619
%patch4 -p1 -b .table-stops
%patch5 -p1 -b .link_layer
%patch6 -p1 -b .pcap-vlan
%patch7 -p1 -b .tlsv12
%patch8 -p1 -b .ssl-enums
%patch9 -p1 -b .ciphersuites
cp -pf %{SOURCE1} .

# Rebuilding of configure file is needed for Patch1
autoconf --force

# Copying config.{guess,sub} is required for x86_64
cp -pf %{_datadir}/automake-*/config.{guess,sub} .

%build
%configure \
  --with-pcap-inc=%{_includedir} --with-pcap-lib=%{_libdir} \
  --with-openssl-inc=%{_includedir} --with-openssl-lib=%{_libdir}
%make_build

%install
%make_install BINDIR="$RPM_BUILD_ROOT%{_sbindir}" \
  MANDIR="$RPM_BUILD_ROOT%{_mandir}"

# Correct permissions
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1*

%files
%license COPYRIGHT
%doc ChangeLog CREDITS README README.FEDORA
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.21.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.20.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.19.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.18.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.17.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.16.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.15.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.14.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.13.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.12.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.11.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.10.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Robert Scheck <robert@fedoraproject.org> 0.9-0.9.b3
- Added a patch which adds further link layer offsets
- Added patch to include traffic with(out) the 802.1Q VLAN header
- Added patch for TLSv1.1/TLSv1.2 application data decrypt support
- Added a patch to update known cipher suites according to IANA
- Added patch with new cipher suites for application data decoding

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.8.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.7.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.5.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Robert Scheck <robert@fedoraproject.org> 0.9-0.4.b3
- Fixed wrong decoder table ends to avoid many segfaults (#747398)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.3.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 06 2010 Robert Scheck <robert@fedoraproject.org> 0.9-0.2.b3
- Added a patch to support AES cipher-suites (#248813 #c5)
- Added backporting patch from CVS 2006-06-19 (#248813 #c5)

* Sat Jan 23 2010 Robert Scheck <robert@fedoraproject.org> 0.9-0.1.b3
- Upgrade to 0.9b3
- Initial spec file for Fedora and Red Hat Enterprise Linux
