# Tarfile created using git
# git clone https://github.com/ptpd/ptpd.git
# git archive --format=tar --prefix=ptpd-2.3.1/ 235e9b4 | xz > ptpd-2.3.1-235e9b4.tar.xz

%global gitshort 235e9b4

Name:    ptpd
Version: 2.3.1
Release: 16%{?gitshort:.%{gitshort}}%{?dist}
Summary: PTPd implements the Precision Time protocol (PTP) as defined by the IEEE 1588
License: BSD
URL:     https://github.com/ptpd/ptpd/wiki

Source0: %{name}-%{version}-%{gitshort}.tar.xz
Source1: ptpd2.service
Source2: ptpd2
Source3: ptpd2.conf

# The definition of EVP_MD_CTX conflicts with the one from openssl which is
# pulled in by the new vesion of net-snmp.
Patch0:  patch-conflicting-typedef

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: libpcap-devel
BuildRequires: net-snmp-devel
BuildRequires: libtool autoconf automake

%description
The PTP daemon (PTPd) implements the Precision Time protocol (PTP) as defined
by the relevant IEEE 1588 standard. PTP was developed to provide very precise
time coordination of LAN connected computers.

PTPd is a complete implementation of the IEEE 1588 specification for a standard
(non-boundary) clock. PTPd has been tested with and is known to work properly
with other IEEE 1588 implementations.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure --enable-statistics --with-max-unicast-destinations=512
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_mandir}/man{5,8}
mkdir -p %{buildroot}%{_datadir}/snmp/mibs
mkdir -p %{buildroot}%{_datadir}/ptpd
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_localstatedir}/log

install -pm 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}
install -pm 755 src/ptpd2 %{buildroot}%{_bindir}
install -pm 644 src/ptpd2.8 %{buildroot}%{_mandir}/man8/
install -pm 644 src/ptpd2.conf.5 %{buildroot}%{_mandir}/man5/
install -pm 644 doc/PTPBASE-MIB.txt %{buildroot}%{_datadir}/snmp/mibs
install -pm 644 src/leap-seconds.list %{buildroot}%{_datadir}/ptpd
# have to create the below, else ptpd will not log drift
touch %{buildroot}%{_localstatedir}/log/ptpd2_kernelclock.drift

%post
%systemd_post ptpd2.service

%preun
%systemd_preun ptpd2.service

%postun
%systemd_postun_with_restart ptpd2.service

%files
%license COPYRIGHT
%doc ChangeLog README.md
%config(noreplace) %{_sysconfdir}/sysconfig/ptpd2
%config(noreplace) %{_sysconfdir}/ptpd2.conf
%config %{_localstatedir}/log/ptpd2_kernelclock.drift
%{_bindir}/*
%{_unitdir}/*
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_datadir}/snmp/mibs/*
%{_datadir}/ptpd/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-16.235e9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-15.235e9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-14.235e9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.3.1-13
- Rebuild for unannounced net-snmp soversion bump.
- Quick patch to fix build failure with new net-snmp.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12.235e9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.1-11.235e9b4
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10.235e9b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.1-9.235e9b4
- Move to git snapshot to fix FTBFS due to net-snmp changes
- Spec cleanup, use %%license
- Update upstream URLs

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.3.1-8
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.1-3
- Rebuilt for rpm 4.12.90

* Sat Jul 11 2015 Jon Kent <jon.kent at, gmail.com> - 2.3.1-2
- Removed redundant configure options

* Tue Jul 07 2015 Jon Kent <jon.kent at, gmail.com> - 2.3.1-1
- update with latest upstream

* Mon Jul 06 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.3.0-6
- Fix broken make invocation (F23FTBFS RHBZ#1239803).

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.0-3
- As per packaging guidelines build on all arches

* Tue Jun 10 2014 Jon Kent - 2.3.0-2
- restricted Arch to i686 and x86_64

* Sun Jun 08 2014 Jon Kent - 2.3.0-1
- Updates to ptpd 2.3.0 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Jon Kent <jon.kent at, gmail.com> - 2.2.0-7
- various enhancement and corrections as request in bugzilla 1100256

* Fri Aug 09 2013 Jon Kent <jon.kent at, gmail.com> - 2.2.0-6
- Removed version from doc directory creation as per pkg standards for fc20

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Jon Kent <jon.kent at, gmail.com> 2.2.0-4
- added noreplace to sysconfig/ptpd2

* Tue May 14 2013 Jon Kent <jon.kent at, gmail.com> 2.2.0-3
- corrected sysconfig and systemd file names

* Fri May 10 2013 Jon Kent <jon.kent at, gmail.com> 2.2.0-2
- correct systemd script and init script to use ptpd2

* Tue Mar 26 2013 Jon Kent <jon.kent at, gmail.com> 2.2.0-1
- added systemd startup
- binary name has changed to ptpd2, spec modified to reflect this

* Fri Mar 22 2013 Jon Kent <jon.kent at, gmail.com> 2.2.0-1
- new upstream version of ptpd

* Wed Dec 01 2010 Jon Kent <jon.kent at, gmail.com> 1.1.0-2
- Cleaned up description
- Moved docs to use %%doc tag
- Cleaned up %%build section
- Cleaned up the src and init/sysconfig extraction

* Sun Nov 21 2010 Jon Kent <jon.kent at, gmail.com> 1.1.0-1
- First release of ptpd for Fedora

