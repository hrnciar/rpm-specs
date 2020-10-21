Summary:	Scalable, accurate, flexible and efficient network probing
Name:		unicornscan
Version:	0.4.7
Release:	23%{?dist}
License:	GPLv2+
URL:		http://www.unicornscan.org/
Source0:	http://www.unicornscan.org/releases/%{name}-%{version}-2.tar.bz2
Source1:	unicornscan.conf
Source2:	unicornscan-README.fedora
Source3:	unicornscan-web-README.fedora
Patch0:		unicornscan-0.4.7-lib64.patch
Patch1:		unicornscan-0.4.7-geoip.patch
Patch2:		unicornscan-0.4.7-config.patch
Patch3:		unicornscan-0.4.7-gcc5.patch
Patch4:		unicornscan-0.4.7-ldflags.patch
Requires(pre):	shadow-utils
BuildRequires:	gcc-c++
BuildRequires:	flex, bison, libpcap-devel, libtool-ltdl-devel
BuildRequires:	libdnet-devel, GeoIP-devel, libpq-devel

%description
Unicornscan is an attempt at a user-land distributed TCP/IP stack. It is
intended to provide a researcher a superior interface for introducing a
stimulus into and measuring a response from a TCP/IP enabled device or
network. Although it currently has hundreds of individual features, a main
set of abilities include: Asynchronous stateless TCP scanning with all
variations of TCP flags, asynchronous stateless TCP banner grabbing,
asynchronous protocol specific UDP scanning (sending enough of a signature
to elicit a response), active and passive remote OS, application and
component identification by analyzing responses, PCAP file logging and
filtering, relational database output, custom module support, customized
data-set views.

%package web
Summary:	Web-based front-end for unicornscan database results
Requires:	%{name} = %{version}-%{release}, php-pgsql, httpd
BuildArch:	noarch

%description web
Unicornscan provides support to write results into a database. And with the
web-based front-end for unicornscan, which is written in PHP, these results
can be easily interpreted and visualized.

%prep
%setup -q
%patch0 -p1 -b .lib64
%patch1 -p1 -b .geoip
%patch2 -p1 -b .config
%patch3 -p1 -b .gcc5
%patch4 -p1 -b .ldflags

cp -pf %{SOURCE2} README.fedora
cp -pf %{SOURCE3} www-front-end/README.fedora

%build
# This package has an embedded copy of libtool which is apparently too old
# to properly handle LTO, particularly when building shared libraries.  This
# results in a failure to pass -fPIC when building the shared library and
# that in turn cause a link failure when LTO is enabled.
# Disable LTO for now
%define _lto_cflags %{nil}

# - _GNU_SOURCE is required for "ucred" from <bits/socket.h> via <sys/socket.h>
# - Use classical non-SELinux permission schema once SELinux Reference Policy is
#   including unicornscan support directly, maybe with Fedora 13 and/or RHEL 6
# - MySQL support is only available in ./configure as inside broken and disabled
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure --localstatedir=%{_localstatedir}/lib --with-pgsql --with-listen-user=%{name}
%make_build

%install
%make_install

# Remove the static library files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.a

# Correct permissions and timestamps
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/*
touch -c -r etc/modules.conf.config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.conf

# Install web files into destination
cp -af www-front-end $RPM_BUILD_ROOT%{_datadir}/%{name}/
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/attic
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{config.php.config,README.fedora,TODO}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/{session.sql,.htaccess}

# Move configuration file to its place
mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/config.php $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/web.php
touch -c -r www-front-end/config.php.config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/web.php
ln -sf ../../..%{_sysconfdir}/%{name}/web.php $RPM_BUILD_ROOT%{_datadir}/%{name}/config.php

# Install the apache configuration file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Create temporary directory for packaging
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/web/

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Unicornscan User" %{name}
exit 0

%files
%license LICENSE
%doc AUTHORS README README.database README.fedora README.security
%doc THANKS TODO UDP_PAYLOADS_NEEDED docs/Unicornscan-Getting_Started.pdf
%doc src/output_modules/database/sql/pgsql_schema.sql src/parse/example_confs
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/modules.conf
%config(noreplace) %{_sysconfdir}/%{name}/oui.txt
%config(noreplace) %{_sysconfdir}/%{name}/payloads.conf
%config(noreplace) %{_sysconfdir}/%{name}/ports.txt
%config(noreplace) %{_sysconfdir}/%{name}/unicorn.conf
%{_bindir}/fantaip
%{_bindir}/unibrow
%{_bindir}/unicfgtst
%{_bindir}/%{name}
%{_bindir}/us
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
# *.la files are referenced by the shared objects and required
%{_libdir}/%{name}/modules/httpexp.la
%{_libdir}/%{name}/modules/httpexp.so
%{_libdir}/%{name}/modules/http.la
%{_libdir}/%{name}/modules/http.so
%{_libdir}/%{name}/modules/ntalk.la
%{_libdir}/%{name}/modules/ntalk.so
%{_libdir}/%{name}/modules/osdetect.la
%{_libdir}/%{name}/modules/osdetect.so
%{_libdir}/%{name}/modules/pgsqldb.la
%{_libdir}/%{name}/modules/pgsqldb.so
%{_libdir}/%{name}/modules/rdns.la
%{_libdir}/%{name}/modules/rdns.so
%{_libdir}/%{name}/modules/sip.la
%{_libdir}/%{name}/modules/sip.so
%{_libdir}/%{name}/modules/upnp.la
%{_libdir}/%{name}/modules/upnp.so
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/unilisten
%{_libexecdir}/%{name}/unisend
%{_mandir}/man1/%{name}.1*
%dir %{_localstatedir}/lib/%{name}

%files web
%doc www-front-end/README.fedora www-front-end/lib/session.sql
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(640,apache,apache) %{_sysconfdir}/%{name}/web.php
%{_datadir}/%{name}
%attr(-,apache,apache) %dir %{_localstatedir}/lib/%{name}/web

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeff Law  <law@redhat.com> - 0.4.7-22
- Disable LTO

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Robert Scheck <robert@fedoraproject.org> 0.4.7-18
- Add missing linking to -lGeoIP (#1623468)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 0.4.7-11
- Added patch to make rebuilding with GCC 5 working

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 05 2009 Robert Scheck <robert@fedoraproject.org> 0.4.7-2
- Added unicornscan-web subpackage (#538190 #c3, Robert E. Lee)
- Updated the patch for 64 bit support in configure (#538190 #c6)

* Tue Nov 17 2009 Robert Scheck <robert@fedoraproject.org> 0.4.7-1
- Upgrade to 0.4.7
- Initial spec file for Fedora and Red Hat Enterprise Linux (spec
  file is based on a try by Robert E. Lee and Manuel Wolfshant)
