%define rsyslog_statedir %{_sharedstatedir}/rsyslog
%define rsyslog_pkidir %{_sysconfdir}/pki/rsyslog
%define rsyslog_docdir %{_docdir}/rsyslog
#due to multiple failures of extensive testbench on various archs
#and module requirements of certain tests need to have it disabled,
#tests execution possible locally on properly set up workstation
%global want_testbench 0

Summary: Enhanced system logging and kernel message trapping daemon
Name: rsyslog
Version: 8.2008.0
Release: 2%{?dist}
License: (GPLv3+ and ASL 2.0)
URL: http://www.rsyslog.com/
Source0: http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
Source1: http://www.rsyslog.com/files/download/rsyslog/%{name}-doc-%{version}.tar.gz
Source2: rsyslog.conf
Source3: rsyslog.sysconfig
Source4: rsyslog.log
Source5: rsyslog.service

BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: dos2unix
BuildRequires: flex
BuildRequires: libgcrypt-devel
BuildRequires: libfastjson-devel >= 0.99.8
BuildRequires: libestr-devel >= 0.1.9
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: pkgconfig
BuildRequires: python3-docutils
# make sure systemd is in a version that isn't affected by rhbz#974132
BuildRequires: systemd-devel >= 204-8
BuildRequires: zlib-devel
BuildRequires: qpid-proton-c-devel

Requires: logrotate >= 3.5.2
Requires: bash >= 2.0
%{?systemd_ordering}

Provides: syslog
Obsoletes: sysklogd < 1.5-11

%package crypto
Summary: Encryption support
Requires: %name = %version-%release

%package doc
Summary: HTML documentation for rsyslog
BuildArch: noarch

%package elasticsearch
Summary: ElasticSearch output module for rsyslog
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%package hiredis
Summary: Redis support for rsyslog
Requires: %name = %version-%release
BuildRequires: hiredis-devel

%package mmjsonparse
Summary: JSON enhanced logging support
Requires: %name = %version-%release

%package mmnormalize
Summary: Log normalization support for rsyslog
Requires: %name = %version-%release
BuildRequires: libestr-devel liblognorm-devel >= 1.0.2

%package mmaudit
Summary: Message modification module supporting Linux audit format
Requires: %name = %version-%release

%package mmsnmptrapd
Summary: Message modification module for snmptrapd generated messages
Requires: %name = %version-%release

%package libdbi
Summary: Libdbi database support for rsyslog
Requires: %name = %version-%release
BuildRequires: libdbi-devel

%package mysql
Summary: MySQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: mariadb-connector-c-devel

%package mongodb
Summary: MongoDB support for rsyslog
Requires: %name = %version-%release
BuildRequires: mongo-c-driver-devel snappy-devel cyrus-sasl-devel

%package pgsql
Summary: PostgresSQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: libpq-devel

%package rabbitmq
Summary: RabbitMQ support for rsyslog
Requires: %name = %version-%release
BuildRequires: librabbitmq-devel >= 0.2

%package gssapi
Summary: GSSAPI authentication and encryption support for rsyslog
Requires: %name = %version-%release
BuildRequires: krb5-devel

%package relp
Summary: RELP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: librelp-devel >= 1.2.16

%package gnutls
Summary: TLS protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: gnutls-devel

%package snmp
Summary: SNMP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: net-snmp-devel

%package udpspoof
Summary: Provides the omudpspoof module
Requires: %name = %version-%release
BuildRequires: libnet-devel

%package omamqp1
Summary: Provides the omamqp1 module
Requires: %name = %version-%release
BuildRequires: qpid-proton-c-devel

%package kafka
Summary: Provides the omkafka module
Requires: %name = %version-%release
BuildRequires: librdkafka-devel

%package mmkubernetes
Summary: Provides the mmkubernetes module
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%description crypto
This package contains a module providing log file encryption and a
command line tool to process encrypted logs.

%description doc
This subpackage contains documentation for rsyslog.

%description elasticsearch
This module provides the capability for rsyslog to feed logs directly into
Elasticsearch.

%description hiredis
This module provides output to Redis.

%description mmjsonparse
This module provides the capability to recognize and parse JSON enhanced
syslog messages.

%description mmnormalize
This module provides the capability to normalize log messages via liblognorm.

%description mmaudit
This module provides message modification supporting Linux audit format
in various settings.

%description mmsnmptrapd
This message modification module takes messages generated from snmptrapd and
modifies them so that they look like they originated from the read originator.

%description libdbi
This module supports a large number of database systems via
libdbi. Libdbi abstracts the database layer and provides drivers for
many systems. Drivers are available via the libdbi-drivers project.

%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

%description mongodb
The rsyslog-mongodb package contains a dynamic shared object that will add
MongoDB database support to rsyslog.

%description pgsql
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.

%description rabbitmq
This module allows rsyslog to send messages to a RabbitMQ server.

%description gssapi
The rsyslog-gssapi package contains the rsyslog plugins which support GSSAPI
authentication and secure connections. GSSAPI is commonly used for Kerberos
authentication.

%description relp
The rsyslog-relp package contains the rsyslog plugins that provide
the ability to receive syslog messages via the reliable RELP
protocol.

%description gnutls
The rsyslog-gnutls package contains the rsyslog plugins that provide the
ability to receive syslog messages via upcoming syslog-transport-tls
IETF standard protocol.

%description snmp
The rsyslog-snmp package contains the rsyslog plugin that provides the
ability to send syslog messages as SNMPv1 and SNMPv2c traps.

%description udpspoof
This module is similar to the regular UDP forwarder, but permits to
spoof the sender address. Also, it enables to circle through a number
of source ports.

%description omamqp1
The omamqp1 output module can be used to send log messages via an AMQP
1.0-compatible messaging bus.

%description kafka
The rsyslog-kafka package provides module for Apache Kafka output.

%description mmkubernetes
The rsyslog-mmkubernetes package provides module for adding kubernetes
container metadata.

%prep
# set up rsyslog-doc sources
%setup -q -a 1 -T -c
rm -r LICENSE README.md source build/objects.inv
mv build doc
# set up rsyslog sources
%setup -q -D

autoreconf -iv

%build
%ifarch sparc64
#sparc64 need big PIE
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpie"
%endif
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"

# the hiredis-devel package doesn't provide a pkg-config file
export HIREDIS_CFLAGS=-I/usr/include/hiredis
export HIREDIS_LIBS="-L%{_libdir} -lhiredis"
%configure \
	--prefix=/usr \
	--disable-static \
%if %{want_testbench}
	--enable-testbench \
%endif
	--enable-elasticsearch \
	--enable-clickhouse \
	--enable-generate-man-pages \
	--enable-gnutls \
	--enable-gssapi-krb5 \
	--enable-imdiag \
	--enable-imdocker \
	--enable-imfile \
	--enable-imjournal \
	--enable-improg \
	--enable-impstats \
	--enable-imptcp \
	--enable-libdbi \
	--enable-mail \
	--enable-mmanon \
	--enable-mmaudit \
	--enable-mmcount \
	--enable-mmkubernetes \
	--enable-mmjsonparse \
	--enable-mmnormalize \
	--enable-mmsnmptrapd \
	--enable-mysql \
	--enable-omamqp1 \
	--enable-omhiredis \
	--enable-omhttp \
	--enable-omjournal \
	--enable-ommongodb \
	--enable-omprog \
	--enable-omrabbitmq \
	--enable-omstdout \
	--enable-omudpspoof \
	--enable-omuxsock \
	--enable-pgsql \
	--enable-pmaixforwardedfrom \
	--enable-pmcisconames \
	--enable-pmlastmsg \
	--enable-pmsnare \
	--enable-relp \
	--enable-snmp \
	--enable-unlimited-select \
	--enable-usertools \
	--enable-omkafka

make V=1

%check
make V=1 check

%install
make V=1 DESTDIR=%{buildroot} install

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m 700 %{buildroot}%{rsyslog_statedir}
install -d -m 700 %{buildroot}%{rsyslog_pkidir}
install -d -m 755 %{buildroot}%{rsyslog_docdir}/html

install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/rsyslog.conf
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/rsyslog
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/rsyslog.service
install -p -m 644 plugins/ommysql/createDB.sql %{buildroot}%{rsyslog_docdir}/mysql-createDB.sql
install -p -m 644 plugins/ompgsql/createDB.sql %{buildroot}%{rsyslog_docdir}/pgsql-createDB.sql
dos2unix tools/recover_qi.pl
install -p -m 644 tools/recover_qi.pl %{buildroot}%{rsyslog_docdir}/recover_qi.pl
install -p -m 644 contrib/mmkubernetes/*.rulebase %{buildroot}%{rsyslog_docdir}
# extract documentation
cp -r doc/* %{buildroot}%{rsyslog_docdir}/html
# get rid of libtool libraries
rm -f %{buildroot}%{_libdir}/rsyslog/*.la
# imdiag and liboverride is only used for testing
rm -f %{buildroot}%{_libdir}/rsyslog/imdiag.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname.so

%post
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done
%systemd_post rsyslog.service

%preun
%systemd_preun rsyslog.service

%postun
%systemd_postun_with_restart rsyslog.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS ChangeLog README.md
%{rsyslog_docdir}
%exclude %{rsyslog_docdir}/html
%exclude %{rsyslog_docdir}/mysql-createDB.sql
%exclude %{rsyslog_docdir}/pgsql-createDB.sql
%dir %{_libdir}/rsyslog
%dir %{_sysconfdir}/rsyslog.d
%dir %{rsyslog_statedir}
%dir %{rsyslog_pkidir}
%{_sbindir}/rsyslogd
%{_mandir}/man5/rsyslog.conf.5.gz
%{_mandir}/man8/rsyslogd.8.gz
%{_unitdir}/rsyslog.service
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
%config(noreplace) %{_sysconfdir}/logrotate.d/rsyslog
# plugins
%{_libdir}/rsyslog/imdocker.so
%{_libdir}/rsyslog/imfile.so
%{_libdir}/rsyslog/imjournal.so
%{_libdir}/rsyslog/imklog.so
%{_libdir}/rsyslog/immark.so
%{_libdir}/rsyslog/improg.so
%{_libdir}/rsyslog/impstats.so
%{_libdir}/rsyslog/imptcp.so
%{_libdir}/rsyslog/imtcp.so
%{_libdir}/rsyslog/imudp.so
%{_libdir}/rsyslog/imuxsock.so
%{_libdir}/rsyslog/lmnet.so
%{_libdir}/rsyslog/lmnetstrms.so
%{_libdir}/rsyslog/lmnsd_ptcp.so
%{_libdir}/rsyslog/lmregexp.so
%{_libdir}/rsyslog/lmtcpclt.so
%{_libdir}/rsyslog/lmtcpsrv.so
%{_libdir}/rsyslog/lmzlibw.so
%{_libdir}/rsyslog/mmanon.so
%{_libdir}/rsyslog/mmcount.so
%{_libdir}/rsyslog/mmexternal.so
%{_libdir}/rsyslog/omclickhouse.so
%{_libdir}/rsyslog/omhttp.so
%{_libdir}/rsyslog/omjournal.so
%{_libdir}/rsyslog/ommail.so
%{_libdir}/rsyslog/omprog.so
%{_libdir}/rsyslog/omstdout.so
%{_libdir}/rsyslog/omtesting.so
%{_libdir}/rsyslog/omuxsock.so
%{_libdir}/rsyslog/pmaixforwardedfrom.so
%{_libdir}/rsyslog/pmcisconames.so
%{_libdir}/rsyslog/pmlastmsg.so
%{_libdir}/rsyslog/pmsnare.so
%{_libdir}/rsyslog/fmhttp.so
%{_libdir}/rsyslog/fmhash.so

%files crypto
%{_bindir}/rscryutil
%{_mandir}/man1/rscryutil.1.gz
%{_libdir}/rsyslog/lmcry_gcry.so

%files doc
%doc %{rsyslog_docdir}/html

%files elasticsearch
%{_libdir}/rsyslog/omelasticsearch.so

%files hiredis
%{_libdir}/rsyslog/omhiredis.so

%files libdbi
%{_libdir}/rsyslog/omlibdbi.so

%files mmaudit
%{_libdir}/rsyslog/mmaudit.so

%files mmjsonparse
%{_libdir}/rsyslog/mmjsonparse.so

%files mmnormalize
%{_libdir}/rsyslog/mmnormalize.so

%files mmsnmptrapd
%{_libdir}/rsyslog/mmsnmptrapd.so

%files mysql
%doc %{rsyslog_docdir}/mysql-createDB.sql
%{_libdir}/rsyslog/ommysql.so

%files mongodb
%{_bindir}/logctl
%{_libdir}/rsyslog/ommongodb.so

%files pgsql
%doc %{rsyslog_docdir}/pgsql-createDB.sql
%{_libdir}/rsyslog/ompgsql.so

%files rabbitmq
%{_libdir}/rsyslog/omrabbitmq.so

%files gssapi
%{_libdir}/rsyslog/lmgssutil.so
%{_libdir}/rsyslog/imgssapi.so
%{_libdir}/rsyslog/omgssapi.so

%files relp
%{_libdir}/rsyslog/imrelp.so
%{_libdir}/rsyslog/omrelp.so

%files gnutls
%{_libdir}/rsyslog/lmnsd_gtls.so

%files snmp
%{_libdir}/rsyslog/omsnmp.so

%files udpspoof
%{_libdir}/rsyslog/omudpspoof.so

%files omamqp1
%{_libdir}/rsyslog/omamqp1.so

%files kafka
%{_libdir}/rsyslog/omkafka.so

%files mmkubernetes
%{_libdir}/rsyslog/mmkubernetes.so
%doc %{rsyslog_docdir}/k8s_filename.rulebase
%doc %{rsyslog_docdir}/k8s_container_name.rulebase

%changelog
* Fri Sep 18 2020 Attila Lakatos <alakatos@redhat.com> - 8.2008.0-2
- rebuild package

* Thu Sep 17 2020 Attila Lakatos <alakatos@redhat.com> - 8.2008.0-1
- rebase to upstream version 8.2008.0
  resolves: rhbz#1829092
  resolves: rhbz#1823862
  resolves: rhbz#1876773
- add service file back(upstream does not ship it anymore)

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 8.2002.0-5
- Rebuilt for new net-snmp release

* Thu Aug 20 2020 Attila Lakatos <alakatos@redhat.com> - 8.2002.0-4
- enable configuration reload in the service
  resolves: rhbz#1868636

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2002.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2002.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Jiri Vymazal <jvymazal@redhat.com> - 8.2002.0-1
- rebase to upstream version 8.2002.0
  resolves: rhbz#1807097

* Mon Feb 03 2020 Jiri Vymazal <jvymazal@redhat.com> - 8.2001.0-1
- rebase to upstream version 8.2001.0
  resolves: rhbz#1790731

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1911.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1911.0-1
- rebase to upstream version 8.1911.0
  resolves: rhbz#1771468

* Thu Oct 17 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1910.0-1
- rebase to upstream version 8.1910.0
  resolves: rhbz#1743537

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1907.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1907.0-1
- rebase to upstream version 8.1905.0
  resolves: rhbz#1716391

* Mon May 13 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1904.0-1
- rebase to upstream version 8.1904.0
  resolves: rhbz#1668473

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Bogdan Dobrelya <bdobreli@redhat.com> - 8.39.0-2
- Use systemd_ordering macro

* Wed Dec 05 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.39.0-1
- rebase to upstream version 8.39.0
  resolves: rhbz#1649081
  resolves: rhbz#1615014

* Wed Oct 10 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.38.0-1
- rebase to upstream version 8.38.0
  resolves: rhbz#1632432
  resolves: rhbz#1627944

* Fri Aug 10 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.37.0-1
- added mmkubernetes rulebases as doc files
  resolves: rhbz#1614440

* Wed Aug 08 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.37.0-1
- rebase to upstream version 8.37.0
  resolves: rhbz#1612079
  resolves: rhbz#1598217
  resolves: rhbz#1544139
- dropped needless libee dependency
- bumped librelp dependency to actually needed version

* Wed Jul 25 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-3
- fixed a typo in commented-out part of default conf + reordered it
  resolves: rhbz#1579592

* Tue Jul 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 8.36.0-3
- Rebuild for unannounced net-snmp soversion bump.
- Use python3-docutils because rst2man has moved there.

* Mon Jul 23 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-2
- added gcc to buildrequires following f29 system-wide change

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-1
- rebase to 8.36.0
  - removed stdlog dependency as upstream is going to drop it
- following upstream naming of pidfile
- removed needless conditionals

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 8.35.0-4
- rebuild with libbson and libmongc 1.10.2 (soname back to 0)

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 8.35.0-3
- rebuild with libbson and libmongc 1.10.0

* Thu May 17 2018 Radovan Sroka <rsroka@redhat.com> - 8.35.0-2
- rebase to 8.35.0

* Thu Apr 05 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.34.0-1
- rebase to 8.34.0
- added mmkubernetes module
- added fmhttp module
- finished converting rsyslog config to new syntax
- dropped obsolete defattr statements from spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.32.0-1
- rebase to 8.32.0
- now requires higher version of libfastjson

* Thu Dec 14 2017 Radovan Sroka <rsroka@redhat.com> - 8.31.0-2
- added also cyrus-sasl-devel dependency

* Thu Dec 14 2017 Radovan Sroka <rsroka@redhat.com> - 8.31.0-1
- update to 8.31.0
- removed upstreamed patches
- added dependecies mongo-c-driver-devel snappy-devel
- removed depricated dependecies libmongo-client
- mongodb plugin now uses new driver with TLS,...

* Tue Nov 28 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.30.0-4
- changed rsyslog-doc to noarch

* Mon Nov 20 2017 Radovan Sroka <rsoka@redhat.com> - 8.30.0-4
- rebuild due to libqpid-proton.so

* Wed Oct 25 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-3
- rebuild

* Wed Oct 25 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-2
- imjournal didn't work at all
- added imjournal patch for rhbz#1505853

* Mon Oct 23 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-1
- rebase to 8.30.0
- added patch that resolves imgssapi compilation errors

* Mon Oct 9 2017 Marek Tamaskovic <mtamasko@redhat.com> - 8.29.0-4
- mysql-devel changed for mariadb-connector-c-devel
  resolves: rhbz#1493695
- repaired changelog

* Tue Aug 15 2017 Radovan Sroka <rsroka@redhat.com> - 8.29.0-2
- rebuild, bumped release number

* Tue Aug 15 2017 Marek Tamaskovic <mtamasko@redhat.com> - 8.29.0-1
- rebase to 8.29.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Radovan Sroka <rsroka@redhat.com> - 8.27.0-1
- dropped patch2 (upstreamed)
- rebase to 8.27.0

* Tue Apr 18 2017 Radovan Sroka <rsroka@redhat.com> - 8.26.0-1
- rebase to 8.26.0
- added doc patch rhbz#1436113
- dropped chdir patch, https://github.com/rsyslog/rsyslog/pull/1420
- moved dependency libgcrypt to rsyslog core

* Wed Mar 01 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.25.0-2
- rebased doc subpackage to 8.25.0 as well
- dropped upstreamed doc patch

* Tue Feb 28 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.25.0-1
- rebase to 8.25.0 upstream source version

* Mon Feb 27 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-7
- forced rebuild because of libqpid-proton rebase

* Mon Feb 20 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-6
- fixed typo in chdir location
  resolves: rhbz#1422542
- updated one more directive in default config
  resolves: rhbz#1419625

* Fri Feb 17 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-5
- new default config, using RainerScript wherever possible
  resolves: rhbz#1419625
- updated testbench guard as testbench now needs explicit configuration
  see: rhbz#1211194
- added patch to make chdir call after chroot
  resolves: rhbz#1422542

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-3
- new kafka sub-package, adding omkafka module
  see: rhbz#1418720

* Mon Jan 16 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-2
- reverted symlink to syslog.service - not needed
  see: rhbz#1343132

* Fri Jan 13 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-1
- rsyslog rebase to 8.24
- changed name of created file in logrotate.d to non-generic one
  resolves: rhbz1269244
- added symlink to syslog.service
  resolves: rhbz1343132
- added documentation for recover_qi
  resolves: rhbz1286707
- changed default .conf added imuxsock, seqfault is not present anymore
  https://github.com/rsyslog/rsyslog/pull/1289

* Tue Dec 20 2016 Radovan Sroka <rsroka@redhat.com> - 8.23.0-2
- added forgoten patch rsyslog-8.23.0-msg_c_nonoverwrite_merge.patch

* Tue Dec 20 2016 Radovan Sroka <rsroka@redhat.com> - 8.23.0-1
- rebase to 8.23.0
- change build requires from libfastjson to libfastjson-devel

* Thu Nov 10 2016 Tomas Sykora <tosykora@redhat.com> 8.22.0-1
- rebase to 8.22.0
  - added omamqp1 subpackage
  - changed BuildRequires from json-c to libfastjson

* Wed Oct 05 2016 Radovan Sroka <rsroka@redhat.com> 8.21.0-1
- rebase to 8.21.0
- dropped rsyslog-8.12.0-gnutls-detection.patch
- dropped rsyslog-8.8.0-immutable-json-props.patch
  - remove from specs but nor from git
  - could be useful in future

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Tomas Heinrich <theinric@redhat.com> 8.12.0-2
- rebuild for soname bump in hiredis-0.13.2

* Tue Sep 1 2015 Radovan Sroka <rsroka@redhat.com> 8.12.0-1
- rebase to 8.12.0
  - drop patches merged upstream
- resolve detection of the new GnuTLS package
  - add autoconf to BuildRequires
- add --enable-generate-man-pages to configure parameters;
  the rscryutil man page isn't generated without it
  https://github.com/rsyslog/rsyslog/pull/469

* Wed Jun 24 2015 Tomas Heinrich <theinric@redhat.com> 8.10.0-1
- rebase to 8.10.0
- drop patches merged upstream
- use the right macro to specify the default pidfile
  resolves: rhbz#1224972
- make logrotate tolerate missing log files
  resolves: rhbz#1205889
- set the default service umask to 0066
  resolves: rhbz#1228192
- use systemctl for sending SIGHUP to the service
  related: rhbz#1224972
- add a patch to prevent a crash on empty messages
  resolves: rhbz#1224538
- add a patch to fix several default parameters for message queues
  resolves: rhbz#1205696
- add a patch to fix the storage size for a configuration option

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Remi Collet <remi@fedoraproject.org> 8.8.0-3
- rebuild for new librabbitmq

* Fri Mar 20 2015 Tomas Heinrich <theinric@redhat.com> 8.8.0-2
- add a patch to fix default syslog priority assigned to journal
  messages which have none

* Thu Mar 19 2015 Tomas Heinrich <theinric@redhat.com> 8.8.0-1
- rebase to 8.8.0
  resolves: rhbz#1069690
  - drop patches merged upstream
  - version the dependency on liblognorm-devel
  - enable mmcount, mmexternal modules,
    remove imdiag, omruleset and pmrfc3164sd modules
    resolves: rhbz#1156359
- add dos2unix to build requirements
- make the build process more verbose
- in accordance with an upstream change, the rsyslog service is now
  restarted automatically upon failure
- adjust the default configuration file for the removal of
  /etc/rsyslog.d/listen.conf by the systemd package
  resolves: rhbz#1116864
- disable the imklog module by default; kernel messages are read from journald
  resolves: rhbz#1083564
- if there is no saved position in the journal, log only messages that are
  received after rsyslog is started; this is a safety measure to prevent
  excessive resource utilization
- use documentation from the standalone rsyslog-docs project
- move documentation from all subpackages into a single directory
- mark the recover_qi.pl script as documentation

* Tue Oct 07 2014 Tomas Heinrich <theinric@redhat.com> 7.4.10-5
- fix CVE-2014-3634

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Tom Callaway <spot@fedoraproject.org> - 7.4.10-3
- fix license handling
- fix build against latest json-c

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Tomas Heinrich <theinric@redhat.com> 7.4.10-1
- rebase to 7.4.10
  - drop patches merged upstream
  - add a build dependency on liblogging-stdlog

* Thu Apr 24 2014 Tomas Mraz <tmraz@redhat.com> - 7.4.8-2
- Rebuild for new libgcrypt

* Mon Feb 10 2014 Tomas Heinrich <theinric@redhat.com> 7.4.8-1
- rebase to 7.4.8
- drop patch4, merged upstream
  rsyslog-7.4.7-bz1030044-remove-ads.patch
- add an explicit requirement on the version of libestr
- drop the "v5" string from the conf file as it's misleading
- add rsyslog-7.4.8-omjournal-warning.patch to fix
  a condition for issuing a warning in omjournal
- add rsyslog-7.4.8-dont-link-libee.patch to prevent
  linking the main binary with libee
- replace rsyslog-7.3.15-imuxsock-warning.patch
  with rsyslog-7.4.8-imuxsock-wrn.patch
- link to libhiredis explicitly
- add a patch to prevent message loss in imjournal
  rsyslog-7.4.8-bz1026804-imjournal-message-loss.patch
- move the rscryutil man page to the crypto subpackage

* Sun Feb 09 2014 Lubomir Rintel <lkundrak@v3.sk> 7.4.7-3
- Fixed 32-bit PowerPC build

* Mon Jan 27 2014 Tomas Heinrich <theinric@redhat.com> 7.4.7-2
- rebuild for libdbi-0.9.0-1

* Mon Jan 06 2014 Tomas Heinrich <theinric@redhat.com> 7.4.7-1
- rebase to 7.4.7
- install the rsyslog-recover-qi.pl tool
- fix a typo in a package description
- add missing defattr directives
- add a patch to remove references to Google ads in the html docs
  rsyslog-7.4.7-bz1030044-remove-ads.patch
  Resolves: #1030044
- add a patch to allow numeric specification of UIDs/GUIDs
  rsyslog-7.4.7-numeric-uid.patch
- change the installation prefix to "/usr"
  Resolves: #1032577

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Tomas Heinrich <theinric@redhat.com> 7.4.2-1
- rebase to 7.4.2
  most importantly, this release fixes a potential vulnerability,
  see http://www.lsexperts.de/advisories/lse-2013-07-03.txt
  the impact should be low as only those using the omelasticsearch
  plugin with a specific configuration are exposed

* Mon Jun 17 2013 Tomas Heinrich <theinric@redhat.com> 7.4.1-1
- rebase to 7.4.1
  this release adds code that somewhat mitigates damage in cases
  where large amounts of messages are received from systemd
  journal (see rhbz#974132)
- regenerate patch 0
- drop patches merged upstream: 4..8
- add a dependency on the version of systemd which resolves the bug
  mentioned above
- update option name in rsyslog.conf

* Wed Jun 12 2013 Tomas Heinrich <theinric@redhat.com> 7.4.0-1
- rebase to 7.4.0
- drop autoconf automake libtool from BuildRequires
- depends on systemd >= 201 because of the sd_journal_get_events() api
- add a patch to prevent a segfault in imjournal caused by a bug in
  systemd journal
- add a patch to prevent an endless loop in the ratelimiter
- add a patch to prevent another endless loop in the ratelimiter
- add a patch to prevent a segfault in imjournal for undefined state file
- add a patch to correctly reset state in the ratelimiter

* Tue Jun 04 2013 Tomas Heinrich <theinric@redhat.com> 7.3.15-1.20130604git6e72fa6
- rebase to an upstream snapshot, effectively version 7.3.15
  plus several more changes
- drop patches 3, 4 - merged upstream
- add a patch to silence warnings emitted by the imuxsock module
- drop the imkmsg plugin
- enable compilation of additional modules
  imjournal, mmanon, omjournal, omrabbitmq
- new subpackages: crypto, rabbitmq
- add python-docutils and autoconf to global BuildRequires
- drop the option for backwards compatibility from the
  sysconfig file - it is no longer supported
- call autoreconf to prepare the snapshot for building
- switch the local message source from imuxsock to imjournal
  the imuxsock module is left enabled so it is easy to swich back to
  it and because systemd drops a file into /etc/rsyslog.d which only
  imuxsock can parse

* Wed Apr 10 2013 Tomas Heinrich <theinric@redhat.com> 7.3.10-1
- rebase to 7.3.10
- add a patch to resolve #950088 - ratelimiter segfault, merged upstream
  rsyslog-7.3.10-ratelimit-segv.patch
- add a patch to correct a default value, merged upstream
  rsyslog-7.3.10-correct-def-val.patch
- drop patch 5 - fixed upstream

* Thu Apr 04 2013 Tomas Heinrich <theinric@redhat.com> 7.3.9-1
- rebase to 7.3.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Tomas Heinrich <theinric@redhat.com> 7.2.5-2
- update a line in rsyslog.conf for the new syntax

* Sun Jan 13 2013 Tomas Heinrich <theinric@redhat.com> 7.2.5-1
- upgrade to upstream version 7.2.5
- update the compatibility mode in sysconfig file

* Mon Dec 17 2012 Tomas Heinrich <theinric@redhat.com> 7.2.4-2
- add a condition to disable several subpackages

* Mon Dec 10 2012 Tomas Heinrich <theinric@redhat.com> 7.2.4-1
- upgrade to upstream version 7.2.4
- remove trailing whitespace

* Tue Nov 20 2012 Tomas Heinrich <theinric@redhat.com> 7.2.2-1
- upgrade to upstream version 7.2.2
  update BuildRequires
- remove patches merged upstream
  rsyslog-5.8.7-sysklogd-compat-1-template.patch
  rsyslog-5.8.7-sysklogd-compat-2-option.patch
  rsyslog-5.8.11-close-fd1-when-forking.patch
- add patch from Milan Bartos <mbartos@redhat.com>
  rsyslog-7.2.1-msg_c_nonoverwrite_merge.patch
- remove the rsyslog-sysvinit package
- clean up BuildRequires, Requires
- remove the 'BuildRoot' tag
- split off a doc package
- compile additional modules (some of them in separate packages):
  elasticsearch
  hiredis
  mmjsonparse
  mmnormalize
  mmaudit
  mmsnmptrapd
  mongodb
- correct impossible timestamps in older changelog entries
- correct typos, trailing spaces, etc
- s/RPM_BUILD_ROOT/{buildroot}/
- remove the 'clean' section
- replace post* scriptlets with systemd macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Tomas Heinrich <theinric@redhat.com> 5.8.11-2
- update systemd patch: remove the 'ExecStartPre' option

* Wed May 23 2012 Tomas Heinrich <theinric@redhat.com> 5.8.11-1
- upgrade to new upstream stable version 5.8.11
- add impstats and imptcp modules
- include new license text files
- consider lock file in 'status' action
- add patch to update information on debugging in the man page
- add patch to prevent debug output to stdout after forking
- add patch to support ssl certificates with domain names longer than 128 chars

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> 5.8.7-2
- libnet rebuild.

* Mon Jan 23 2012 Tomas Heinrich <theinric@redhat.com> 5.8.7-1
- upgrade to new upstream version 5.8.7
- change license from 'GPLv3+' to '(GPLv3+ and ASL 2.0)'
  http://blog.gerhards.net/2012/01/rsyslog-licensing-update.html
- use a specific version for obsoleting sysklogd
- add patches for better sysklogd compatibility (taken from upstream)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Tomas Heinrich <theinric@redhat.com> 5.8.6-1
- upgrade to new upstream version 5.8.6
- obsolete sysklogd
  Resolves: #748495

* Tue Oct 11 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-3
- modify logrotate configuration to omit boot.log
  Resolves: #745093

* Tue Sep 06 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-2
- add systemd-units to BuildRequires for the _unitdir macro definition

* Mon Sep 05 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-1
- upgrade to new upstream version (CVE-2011-3200)

* Fri Jul 22 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-3
- move the SysV init script into a subpackage
- Resolves: 697533

* Mon Jul 11 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-2
- rebuild for net-snmp-5.7 (soname bump in libnetsnmp)

* Mon Jun 27 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-1
- upgrade to new upstream version 5.8.2

* Mon Jun 13 2011 Tomas Heinrich <theinric@redhat.com> 5.8.1-2
- scriptlet correction
- use macro in unit file's path

* Fri May 20 2011 Tomas Heinrich <theinric@redhat.com> 5.8.1-1
- upgrade to new upstream version
- correct systemd scriptlets (#705829)

* Mon May 16 2011 Bill Nottingham <notting@redhat.com> - 5.7.9-3
- combine triggers (as rpm will only execute one) - fixes upgrades (#699198)

* Tue Apr 05 2011 Tomas Heinrich <theinric@redhat.com> 5.7.10-1
- upgrade to new upstream version 5.7.10

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 5.7.9-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Fri Mar 18 2011 Tomas Heinrich <theinric@redhat.com> 5.7.9-1
- upgrade to new upstream version 5.7.9
- enable compilation of several new modules,
  create new subpackages for some of them
- integrate changes from Lennart Poettering
  to add support for systemd
  - add rsyslog-5.7.9-systemd.patch to tweak the upstream
    service file to honour configuration from /etc/sysconfig/rsyslog

* Fri Mar 18 2011 Dennis Gilmore <dennis@ausil.us> - 5.6.2-3
- sparc64 needs big PIE

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Tomas Heinrich <theinric@redhat.com> 5.6.2-1
- upgrade to new upstream stable version 5.6.2
- drop rsyslog-5.5.7-remove_include.patch; applied upstream
- provide omsnmp module
- use correct name for lock file (#659398)
- enable specification of the pid file (#579411)
- init script adjustments

* Wed Oct 06 2010 Tomas Heinrich <theinric@redhat.com> 5.5.7-1
- upgrade to upstream version 5.5.7
- update configuration and init files for the new major version
- add several directories for storing auxiliary data
- add ChangeLog to documentation
- drop unlimited-select.patch; integrated upstream
- add rsyslog-5.5.7-remove_include.patch to fix compilation

* Tue Sep 07 2010 Tomas Heinrich <theinric@redhat.com> 4.6.3-2
- build rsyslog with PIE and RELRO

* Thu Jul 15 2010 Tomas Heinrich <theinric@redhat.com> 4.6.3-1
- upgrade to new upstream stable version 4.6.3

* Wed Apr 07 2010 Tomas Heinrich <theinric@redhat.com> 4.6.2-1
- upgrade to new upstream stable version 4.6.2
- correct the default value of the OMFileFlushOnTXEnd directive

* Thu Feb 11 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-6
- modify rsyslog-4.4.2-unlimited-select.patch so that
  running autoreconf is not needed
- remove autoconf, automake, libtool from BuildRequires
- change exec-prefix to nil

* Wed Feb 10 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-5
- remove '_smp_mflags' make argument as it seems to be
  producing corrupted builds

* Mon Feb 08 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-4
- redefine _libdir as it doesn't use _exec_prefix

* Thu Dec 17 2009 Tomas Heinrich <theinric@redhat.com> 4.4.2-3
- change exec-prefix to /

* Wed Dec 09 2009 Robert Scheck <robert@fedoraproject.org> 4.4.2-2
- run libtoolize to avoid errors due mismatching libtool version

* Thu Dec 03 2009 Tomas Heinrich <theinric@redhat.com> 4.4.2-1
- upgrade to new upstream stable version 4.4.2
- add support for arbitrary number of open file descriptors

* Mon Sep 14 2009 Tomas Heinrich <theinric@redhat.com> 4.4.1-2
- adjust init script according to guidelines (#522071)

* Thu Sep 03 2009 Tomas Heinrich <theinric@redhat.com> 4.4.1-1
- upgrade to new upstream stable version

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.2.0-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Tomas Heinrich <theinric@redhat.com> 4.2.0-1
- upgrade

* Mon Apr 13 2009 Tomas Heinrich <theinric@redhat.com> 3.21.11-1
- upgrade

* Tue Mar 31 2009 Lubomir Rintel <lkundrak@v3.sk> 3.21.10-4
- Backport HUPisRestart option

* Wed Mar 18 2009 Tomas Heinrich <theinric@redhat.com> 3.21.10-3
- fix variables' type conversion in expression-based filters (#485937)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Tomas Heinrich <theinric@redhat.com> 3.21.10-1
- upgrade

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 3.21.9-3
- rebuild for dependencies

* Wed Jan 07 2009 Tomas Heinrich <theinric@redhat.com> 3.21.9-2
- fix several legacy options handling
- fix internal message output (#478612)

* Mon Dec 15 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.9-1
- update is fixing $AllowedSender security issue

* Mon Sep 15 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.3-4
- use RPM_OPT_FLAGS
- use same pid file and logrotate file as syslog-ng (#441664)
- mark config files as noreplace (#428155)

* Mon Sep 01 2008 Tomas Heinrich <theinric@redhat.com> 3.21.3-3
- fix a wrong module name in the rsyslog.conf manual page (#455086)
- expand the rsyslog.conf manual page (#456030)

* Thu Aug 28 2008 Tomas Heinrich <theinric@redhat.com> 3.21.3-2
- fix clock rollback issue (#460230)

* Wed Aug 20 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.3-1
- upgrade to bugfix release

* Wed Jul 23 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.0-1
- upgrade

* Mon Jul 14 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.9-2
- adjust default config file

* Fri Jul 11 2008 Lubomir Rintel <lkundrak@v3.sk> 3.19.9-1
- upgrade

* Wed Jun 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-3
- rebuild because of new gnutls

* Fri Jun 13 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-2
- do not translate Oopses (#450329)

* Fri Jun 13 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-1
- upgrade

* Wed May 28 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.4-1
- upgrade

* Mon May 26 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.3-1
- upgrade to new upstream release

* Wed May 14 2008 Tomas Heinrich <theinric@redhat.com> 3.16.1-1
- upgrade

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-5
- prevent undesired error description in legacy
  warning messages

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-4
- adjust symbol lookup method to 2.6 kernel

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-3
- fix segfault of expression based filters

* Mon Apr 07 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-2
- init script fixes (#441170,#440968)

* Fri Apr 04 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-1
- upgrade

* Tue Mar 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.4-1
- upgrade

* Wed Mar 19 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.3-1
- upgrade
- fix some significant memory leaks

* Tue Mar 11 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.1-2
- init script fixes (#436854)
- fix config file parsing (#436722)

* Thu Mar 06 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.1-1
- upgrade

* Wed Mar 05 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.0-1
- upgrade

* Mon Feb 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.11.5-1
- upgrade

* Fri Feb 01 2008 Peter Vrabec <pvrabec@redhat.com> 3.11.0-1
- upgrade to the latests development release
- provide PostgresSQL support
- provide GSSAPI support

* Mon Jan 21 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-7
- change from requires sysklogd to conflicts sysklogd

* Fri Jan 18 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-6
- change logrotate file
- use rsyslog own pid file

* Thu Jan 17 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-5
- fixing bad descriptor (#428775)

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-4
- rename logrotate file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-3
- fix post script and init file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-2
- change pid filename and use logrotata script from sysklogd

* Tue Jan 15 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-1
- upgrade to stable release
- spec file clean up

* Wed Jan 02 2008 Peter Vrabec <pvrabec@redhat.com> 1.21.2-1
- new upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.19.11-2
- Rebuild for deps

* Thu Nov 29 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.11-1
- new upstream release
- add conflicts (#400671)

* Mon Nov 19 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.10-1
- new upstream release

* Wed Oct 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.6-3
- remove NUL character from recieved messages

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-2
- fix message suppression (303341)

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-1
- upstream bugfix release

* Tue Aug 28 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.2-1
- upstream bugfix release
- support for negative app selector, patch from
  theinric@redhat.com

* Fri Aug 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.0-1
- new upstream release with MySQL support(as plugin)

* Wed Aug 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.1-1
- upstream bugfix release

* Mon Aug 06 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.0-1
- new upstream release

* Thu Aug 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.6-1
- upstream bugfix release

* Mon Jul 30 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.5-1
- upstream bugfix release
- fix typo in provides

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 1.17.2-4
- rebuild for toolchain bug

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-3
- take care of sysklogd configuration files in %%post

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-2
- use EVR in provides/obsoletes sysklogd

* Mon Jul 23 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-1
- upstream bug fix release

* Fri Jul 20 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.1-1
- upstream bug fix release
- include html docs (#248712)
- make "-r" option compatible with sysklogd config (248982)

* Tue Jul 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.0-1
- feature rich upstream release

* Thu Jul 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-2
- use obsoletes and hadle old config files

* Wed Jul 11 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-1
- new upstream bugfix release

* Tue Jul 10 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.0-1
- new upstream release introduce capability to generate output
  file names based on templates

* Tue Jul 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.2-1
- new upstream bugfix release

* Mon Jul 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.1-1
- new upstream release with IPv6 support

* Tue Jun 26 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-3
- add BuildRequires for zlib compression feature

* Mon Jun 25 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-2
- some spec file adjustments.
- fix syslog init script error codes (#245330)

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-1
- new upstream release

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-2
- some spec file adjustments.

* Mon Jun 18 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-1
- upgrade to new upstream release

* Wed Jun 13 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-2
- DB support off

* Tue Jun 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-1
- new upstream release based on redhat patch

* Fri Jun 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-2
- rsyslog package provides its own kernel log. daemon (rklogd)

* Mon Jun 04 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-1
- Initial rpm build
