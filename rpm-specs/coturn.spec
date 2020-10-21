Name:           coturn
Version:        4.5.1.3
Release:        3%{?dist}
Summary:        TURN/STUN & ICE Server
License:        BSD
URL:            https://github.com/coturn/coturn/
Source0:        https://github.com/coturn/coturn/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        coturn.service
Source2:        coturn.tmpfilesd
Source3:        coturn.logrotate

BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  libevent-devel >= 2.0.0
BuildRequires:  make
BuildRequires:  mariadb-devel
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
Requires(pre):  shadow-utils
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     perl-interpreter
Recommends:     perl(DBI)
Recommends:     perl(HTTP::Request::Common)
Recommends:     perl(strict)
Recommends:     perl(warnings)
Recommends:     telnet
%else
Requires:       perl-interpreter
Requires:       perl(DBI)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       telnet
%endif
Provides:       turnserver = %{version}
%{?systemd_requires}

%description
The Coturn TURN Server is a VoIP media traffic NAT traversal server and gateway.
It can be used as a general-purpose network traffic TURN server/gateway, too.

This implementation also includes some extra features. Supported RFCs:

TURN specs:
- RFC 5766 - base TURN specs
- RFC 6062 - TCP relaying TURN extension
- RFC 6156 - IPv6 extension for TURN
- Experimental DTLS support as client protocol.

STUN specs:
- RFC 3489 - "classic" STUN
- RFC 5389 - base "new" STUN specs
- RFC 5769 - test vectors for STUN protocol testing
- RFC 5780 - NAT behavior discovery support

The implementation fully supports the following client-to-TURN-server protocols:
- UDP (per RFC 5766)
- TCP (per RFC 5766 and RFC 6062)
- TLS (per RFC 5766 and RFC 6062); TLS1.0/TLS1.1/TLS1.2
- DTLS (experimental non-standard feature)

Supported relay protocols:
- UDP (per RFC 5766)
- TCP (per RFC 6062)

Supported user databases (for user repository, with passwords or keys, if
authentication is required):
- SQLite
- MySQL
- PostgreSQL
- Redis

Redis can also be used for status and statistics storage and notification.

Supported TURN authentication mechanisms:
- long-term
- TURN REST API (a modification of the long-term mechanism, for time-limited
  secret-based authentication, for WebRTC applications)

The load balancing can be implemented with the following tools (either one or a
combination of them):
- network load-balancer server
- DNS-based load balancing
- built-in ALTERNATE-SERVER mechanism.


%package        utils
Summary:        Coturn utils

%description    utils
This package contains the TURN client utils.


%package        client-libs
Summary:        TURN client static library

%description    client-libs
This package contains the TURN client static library.


%package        client-devel
Summary:        Coturn client development headers

%description    client-devel
This package contains the TURN client development headers.


%prep
%setup -q

# NOTE: Use Fedora Default Ciphers
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i \
    -e 's|#define DEFAULT_CIPHER_LIST "DEFAULT"|#define DEFAULT_CIPHER_LIST "PROFILE=SYSTEM"|g' \
    -e 's|/* "ALL:eNULL:aNULL:NULL" */|/* Fedora Defaults */|g' \
    src/apps/relay/mainrelay.h
sed -i \
    -e 's|*csuite = "ALL"; //"AES256-SHA" "DH"|*csuite = "PROFILE=SYSTEM"; // Fedora Defaults|g' \
    src/apps/uclient/mainuclient.c
%endif


%build
%configure \
    --confdir=%{_sysconfdir}/%{name} \
    --examplesdir=%{_docdir}/%{name} \
    --schemadir=%{_datadir}/%{name} \
    --manprefix=%{_datadir} \
    --docdir=%{_docdir}/%{name} \
    --turndbdir=%{_localstatedir}/lib/%{name} \
    --disable-rpath
%make_build


%install
%make_install
mkdir -p %{buildroot}{%{_sysconfdir}/pki/coturn/{public,private},{%{_rundir},%{_localstatedir}/{lib,log}}/%{name}}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/coturn.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/coturn.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
sed -i \
    -e "s|^syslog$|#syslog|g" \
    -e "s|^#*log-file=.*|log-file=/var/log/coturn/turnserver.log|g" \
    -e "s|^#*simple-log|simple-log|g" \
    -e "s|^#*cert=.*|#cert=/etc/pki/coturn/public/turn_server_cert.pem|g" \
    -e "s|^#*pkey=.*|#pkey=/etc/pki/coturn/private/turn_server_pkey.pem|g" \
    %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
touch -c -r examples/etc/turnserver.conf %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default
mv %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf.default %{buildroot}%{_sysconfdir}/%{name}/turnserver.conf
# NOTE: Removing sqlite db, certs and keys
rm %{buildroot}%{_localstatedir}/lib/%{name}/turndb
rm %{buildroot}%{_docdir}/%{name}/etc/{cacert,turn_{client,server}_{cert,pkey}}.pem
rm %{buildroot}%{_docdir}/%{name}/etc/coturn.service


%check
make test


%pre
getent group coturn >/dev/null || groupadd -r coturn
getent passwd coturn >/dev/null || \
    useradd -r -g coturn -d %{_datadir}/%{name} -s /sbin/nologin \
    -c "Coturn TURN Server daemon" coturn
exit 0


%post
%systemd_post coturn.service


%preun
%systemd_preun coturn.service


%postun
%systemd_postun_with_restart coturn.service


%files
%license LICENSE
%{_bindir}/turnserver
%{_bindir}/turnadmin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.redis
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/*.sh
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.*
%exclude %{_docdir}/%{name}/README.turnutils
%exclude %{_docdir}/%{name}/INSTALL
%exclude %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}/postinstall.txt
%dir %{_docdir}/%{name}/etc
%doc %{_docdir}/%{name}/etc/*
%dir %{_docdir}/%{name}/scripts
%dir %{_docdir}/%{name}/scripts/*
%{_docdir}/%{name}/scripts/*.sh
%{_docdir}/%{name}/scripts/readme.txt
%doc %{_docdir}/%{name}/scripts/*/*
# NOTE: These schema files are installed twice. Excluding copies in docs.
%exclude %doc %{_docdir}/%{name}/schema.mongo.sh
%exclude %doc %{_docdir}/%{name}/schema.sql
%exclude %doc %{_docdir}/%{name}/schema.stats.redis
%exclude %doc %{_docdir}/%{name}/schema.userdb.redis
%{_mandir}/man1/coturn.1.*
%{_mandir}/man1/turnserver.1.*
%{_mandir}/man1/turnadmin.1.*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/turnserver.conf
%dir %{_sysconfdir}/pki/%{name}
%dir %{_sysconfdir}/pki/%{name}/public
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/private
%{_unitdir}/coturn.service
%{_tmpfilesdir}/coturn.conf
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}


%files utils
%license LICENSE
%{_bindir}/turnutils_peer
%{_bindir}/turnutils_stunclient
%{_bindir}/turnutils_uclient
%{_bindir}/turnutils_oauth
%{_bindir}/turnutils_natdiscovery
%doc %{_docdir}/%{name}/README.turnutils
%{_mandir}/man1/turnutils.1.*
%{_mandir}/man1/turnutils_*.1.*


%files client-libs
%license LICENSE
%{_libdir}/libturnclient.a


%files client-devel
%license LICENSE
%dir %{_includedir}/turn
%{_includedir}/turn/*.h
%dir %{_includedir}/turn/client
%{_includedir}/turn/client/*


%changelog
* Sun Sep 27 2020 Christian Glombek <lorbus@fedoraproject.org> - 4.5.1.3-3
- Rebuilt for libevent 2.1.12 soname bump

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.3-1
- Update to 4.5.1.3

* Sat May 16 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.2-1
- Update to 4.5.1.2

* Mon Mar 23 2020 Robert Scheck <robert@fedoraproject.org> - 4.5.1.1-3
- Added upstream patch for CVE-2020-6061 (#1816159)
- Backported upstream patch for CVE-2020-6062 (#1816163)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Robert Scheck <robert@fedoraproject.org> - 4.5.1.1-1
- Update to 4.5.1.1

* Fri Jul 26 2019 Robert Scheck <robert@fedoraproject.org> - 4.5.1.0-3
- Added patch to append only to log files rather to override always
- Relocate SQLite database to FHS conform /var/lib/coturn/turndb path
- Include default log file directory with logrotate configuration
- Provide /run/coturn and correct PID file handling (#1705146)
- Ensure private keys for SSL certs can be only read by coturn user
- Ensure /etc/coturn/turnserver.conf can be only read by coturn user
- Correct subpackage licensing as per Fedora Packaging Guidelines

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Christian Glombek <lorbus@fedoraproject.org> - 4.5.1.0-1
- Initial Fedora Package
- Update to 4.5.1.0
- Introduce consistent naming, rename service to coturn
- Add configure, make and systemd macros
- Remove dependencies on mariadb, mysql, postgresql and sqlite
- Forked from https://github.com/coturn/coturn/blob/af674368d120361603342ff4ff30b44f147a38ff/rpm/turnserver.spec
