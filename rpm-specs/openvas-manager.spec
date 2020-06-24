Name:		openvas-manager
Version:	9.0.1
Release:	1%{?dist}
Summary:	Manager Module for the Open Vulnerability Assessment System (OpenVAS)

License:	GPLv2+
URL:		https://github.com/greenbone/gvmd
#		https://github.com/greenbone/gvmd/releases
Source0:	https://github.com/greenbone/gvmd/archive/v%{version}.tar.gz#/gvmd-%{version}.tar.gz
Source1:	https://github.com/greenbone/gvmd/releases/download/v%{version}/gvmd-%{version}.tar.gz.asc

# The authenticator public key obtained from release 7.0.0
# gpg2 -vv openvas-7.0.0.tar.gz.sig
# gpg2 --search-key 9823FAA60ED1E580
# wget https://www.greenbone.net/GBCommunitySigningKey.asc
# gpg2 --import GBCommunitySigningKey.asc
# gpg2 --list-public-keys 9823FAA60ED1E580
# gpg2 --export --export-options export-minimal 8AE4BE429B60A59B311C2E739823FAA60ED1E580 > gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg
Source2:        gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg


%global         common_desc  %{expand
The OpenVAS Manager is the central service that consolidates plain vulnerability
scanning into a full vulnerability management solution. The Manager controls the
Scanner via OTP and itself offers the XML-based, stateless OpenVAS Management 
Protocol (OMP). All intelligence is implemented in the Manager so that it is
possible to implement various lean clients that will behave consistently e.g. 
with regard to filtering or sorting scan results. The Manager also controls 
a SQL database (sqlite-based) where all configuration and scan result data is 
centrally stored. }


Source3:	%{name}.logrotate
Source4:	%{name}.sysconfig
%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
Source5:	%{name}.service
%else
Source6:	%{name}.initd
%endif

# Put certs to /etc/pki as suggested by http://fedoraproject.org/wiki/PackagingDrafts/Certificates
# Not reported upstream as it is RedHat/Fedora specific
Patch1:		%{name}-01-pki.patch
#Patch2:	%%{name}-02-gpgerror.patch

# Replace _BSD_SOURCE and _SVID_SOURCE with _DEFAULT_SOURCE otherwise build fails with Werror
Patch3:		%{name}-03-bsdsource.patch

Patch4:		%{name}-04-doxygen_full.patch

Patch5:		%{name}-05-postgresql.patch

BuildRequires:  gcc
BuildRequires:	openvas-libraries-devel >= %{version}
BuildRequires:	cmake >= 2.6.0
BuildRequires:	glib2-devel
BuildRequires:	sqlite-devel
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libuuid-devel
BuildRequires:	libpcap-devel
BuildRequires:	libksba-devel
BuildRequires:	gpgme-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig
BuildRequires:	xmltoman
BuildRequires:	libxslt
BuildRequires:	libical-devel
BuildRequires:	libpq-devel
BuildRequires:	postgresql-server-devel


%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
BuildRequires:	systemd
Requires(post):	systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
%endif

Requires:	logrotate
Requires:	/usr/bin/xsltproc



%description
%{common_desc}


%package doc
Summary:        Development documentation for %{name}
BuildRequires:  graphviz

%description doc
%{common_desc}
You can find documentation for development of %{name} under file://%{_docdir}/%{name}-doc.
It can be used with a browser.

%prep
#check signature
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%autosetup -p 1 -n gvmd-%{version}

#Fix encoding issues
iconv -f Windows-1250 -t utf-8 < CHANGELOG.md > CHANGELOG.md.utf8
mv CHANGELOG.md.utf8 CHANGELOG.md

%build
export CFLAGS="$RPM_OPT_FLAGS -Werror=unused-but-set-variable -lgpg-error"

%if 0%{?fedora} >= 30
# disable warnings -> error for stringop-truncation for now
export CFLAGS="${CFLAGS} -Wno-error=stringop-truncation"
%endif
mkdir build
cd build
%cmake -DLOCALSTATEDIR:PATH=%{_var} -DLIBDIR:PATH=%{_libdir} ..
make %{?_smp_mflags} VERBOSE=1
make doc
#make doc-full

%install
cd build
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Config directory
mkdir -p %{buildroot}/%{_sysconfdir}/gvm
chmod 755 %{buildroot}/%{_sysconfdir}/gvm

# Log direcotry
mkdir -p %{buildroot}/%{_var}/log/gvm
touch %{buildroot}%{_var}/log/gvm/gvmd.log

# Runtime lib directory
mkdir -p %{buildroot}/%{_var}/lib/gvm/mgr

# gnupg directory
mkdir -p %{buildroot}/%{_var}/lib/gvm/gnupg

# Install log rotation stuff
install -m 644 -Dp %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

# Install sysconfig configration
install -Dp -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
# Install systemd
install -Dp -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/%{name}.service
%else
# Install startup script
install -Dp -m 755 %{SOURCE6} %{buildroot}/%{_initddir}/%{name}
%endif

# Fix permissions on templates
chmod -R a+r %{buildroot}%{_datadir}/gvm/gvmd
find %{buildroot}%{_datadir}/gvm/gvmd -name generate | xargs chmod 755

# Clean installed doc directory
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# change to python3
sed -i 's|#!/usr/bin/env python[23]*|#!/usr/bin/python3|g' %{buildroot}/%{_datadir}/gvm/gvmd/global_alert_methods/5b39c481-9137-4876-b734-263849dd96ce/report-convert.py

# Remove wrong "doc" docdir
rm -rf %{buildroot}%{_datadir}/doc/gvm


%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
#Post scripts for systemd
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%else
#Post scripts for systemv initd
%post
# This adds the proper /etc/rc*.d links for the script
if [ "$1" -eq 1 ] ; then
	/sbin/chkconfig --add openvas-manager
fi

%preun
if [ "$1" -eq 0 ] ; then
	/sbin/service openvas-manager stop >/dev/null 2>&1
	/sbin/chkconfig --del openvas-manager
fi

%postun
# only for upgrades not erasure
if [ "$1" -eq 1 ] ; then
	/sbin/service openvas-manager condrestart  >/dev/null 2>&1
fi
%endif

%files
# INSTALL file contains post-installation guide for whole openvas
%doc CHANGELOG.md README.md INSTALL.md
%license COPYING
%doc doc/user-scap-data-HOWTO doc/report-format-HOWTO doc/about-cert-feed.txt doc/icalendar-schedules build/doc/example-gvm-manage-certs.conf build/doc/gmp.html
%doc report_formats
%config(noreplace) %{_sysconfdir}/logrotate.d/openvas-manager
%dir %{_sysconfdir}/gvm
%dir %{_var}/lib/gvm
%dir %{_var}/lib/gvm/mgr
%dir %{_var}/log/gvm
%dir %{_datadir}/gvm
%dir %{_var}/lib/gvm/gnupg
%dir %{_datadir}/gvm/scap
%dir %{_datadir}/gvm/cert
%config(noreplace) %{_sysconfdir}/gvm/gvmd_log.conf
%config(noreplace) %{_sysconfdir}/gvm/pwpolicy.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif
%{_bindir}/gvm-manage-certs
%{_sbindir}/gvmd
%{_sbindir}/greenbone-scapdata-sync
%{_sbindir}/greenbone-certdata-sync
%{_sbindir}/gvm-portnames-update
%{_sbindir}/gvm-migrate-to-postgres
%{_libdir}/libgvm-pg-server.so
%{_libdir}/libgvm-pg-server.so.9
%{_libdir}/libgvm-pg-server.so.%{version}
%{_mandir}/man1/gvm-manage-certs.1*
%{_mandir}/man8/gvmd.8*
%{_mandir}/man8//greenbone-certdata-sync.8*
%{_mandir}/man8/greenbone-scapdata-sync.8*
%{_mandir}/man8/gvm-migrate-to-postgres.8*
%{_mandir}/man8/gvm-portnames-update.8*
%{_datadir}/gvm/gvmd
%{_datadir}/gvm/scap/*
%{_datadir}/gvm/cert/*
%{_datadir}/gvm/gvm-lsc-rpm-creator.sh
%{_datadir}/gvm/gvm-lsc-deb-creator.sh
%ghost %{_var}/log/gvm/gvmd.log



%files doc
%doc build/doc/generated/html/*

%changelog
* Sat May 23 2020 josef radinger <cheese@nosuchhost.net> - 9.0.1-1
- bump version
- dont hardcode library-version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Michal Ambroz <rebus at, seznam.cz> - 9.0.0-1
- bump to 9.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-6
- rebuild against new libraries

* Mon Feb 04 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-5
- add -Wno-error=stringop-truncation" for fc30 (rawhide) for now
- switch to python3 on >= fc30
- have a larger DOT_GRAPH_MAX_NODES (patch4)

* Sun Feb 03 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-4
- add subpackage doc for developers.
- add libxslt to BuildRequires


* Sun Feb 03 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-3
- fix cmake-macro

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-1
- bump version
- new source-url
- no more Changelog
- cleanup spec-file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Michal Ambroz <rebus at, seznam.cz> - 7.0.2-1
- bump to 7.0.2

* Wed Apr 19 2017 Michal Ambroz <rebus at, seznam.cz> - 7.0.1-1
- bump version to OpenVAS-9

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 6.0.9-2
- Rebuild for gpgme 1.18

* Mon Sep 05 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.9-1
- bump version to 6.0.9

* Fri Apr 29 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.8-2
- sync spec-files across fedora versions

* Fri Apr 29 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.8-1
- bump version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 josef radinger <cheese@nosuchhost.net> - 6.0.7-1
- bump version
- small cleanups in spec-file

* Tue Sep 29 2015 josef radinger <cheese@nosuchhost.net> - 6.0.6-1
- bump version

* Wed Sep 16 2015 josef radinger <cheese@nosuchhost.net> - 6.0.5-2
- add gnupg-directory

* Wed Jul 15 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.5-1
- bump to OpenVas-8 version 6.0.5
- 1254456 - fix logrotate script

* Wed Jul 15 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.4-1
- bump to OpenVas-8 version 6.0.4

* Mon Jun 29 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-4
- rebuild for F22

* Sat Jun 20 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-3
- fix the options in the /etc/sysconfig

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-1
- bump to OpenVas-8 version 6.0.3

* Sat Apr 04 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.9-1
- bump to OpenVas-7 version 5.0.9

* Sat Dec 06 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.7-1
- bump to OpenVas-7 version 5.0.7

* Fri Nov 07 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.5-2
- remove sysvinit subpackage as it is not needed anymore
- call setgroups before giving up rights with setuid

* Tue Nov 04 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.5-1
- bump to OpenVas-7 version 5.0.5

* Fri Sep 12 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.4-1
- bump to OpenVas-7 version 5.0.4

* Tue Sep 02 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-1
- bump to OpenVas-7 version 5.0.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.2-1
- bump to OpenVas-7 version 5.0.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.1-1
- Update spec file
- Update to latest upstream release 5.0.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-4.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Michal Ambroz <rebus at, seznam.cz> - 4.0-3.beta5
- bump to OpenVas-6 version 4.0+beta5

* Tue Mar 12 2013 Michal Ambroz <rebus at, seznam.cz> - 4.0-2.beta4
- rebuilt with new GnuTLS

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-1.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Michal Ambroz <rebus at, seznam.cz> - 4.0-0.beta4
- bump to OpenVas-6 version 4.0+beta4

* Mon Oct 15 2012 Michal Ambroz <rebus at, seznam.cz> - 3.0.4-1
- bump OpenVas-5 (openvas-manager 3.0.4)

* Sat Aug 25 2012 Michal Ambroz <rebus at, seznam.cz> - 2.0.5-1
- bugfix release
- changed post scriptlets to macros for Fedora 18+

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Michal Ambroz <rebus at, seznam.cz> - 2.0.4-3
- migrate init scripts from sysvinit to systemd

* Mon Jan 23 2012 Michal Ambroz <rebus at, seznam.cz> - 2.0.4-2
- fix checking for the existence of the certificates in initscript

* Mon Jan 09 2012 Michal Ambroz <rebus at, seznam.cz> - 2.0.4-1
- new upstream version 2.0.4

* Wed Apr 06 2011 Michal Ambroz <rebus at, seznam.cz> - 2.0.2-4
- dependencies for F15

* Wed Mar 30 2011 Michal Ambroz <rebus at, seznam.cz> - 2.0.2-3
- implement changes based on package review

* Wed Mar 30 2011 Michal Ambroz <rebus at, seznam.cz> - 2.0.2-2
- implement changes based on package review

* Mon Mar 28 2011 Michal Ambroz <rebus at, seznam.cz> - 2.0.2-1
- initial spec for openvas-manager based on openvas-scanner
