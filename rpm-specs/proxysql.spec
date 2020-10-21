Summary:       A high-performance MySQL proxy
Name:          proxysql
Version:       2.0.13
Release:       1%{?dist}
URL:           http://www.proxysql.com/
# The entire source code is GPLv3+ except deps/re2 and deps/jemalloc which is BSD
# and deps/mariadb-connector-c which is LGPLv2+
License:       GPLv3+ and LGPLv2+ and BSD

BuildRequires: openssl-devel, libev-devel, perl
BuildRequires: cmake, gcc-c++, libcurl-devel, pcre-devel
BuildRequires: systemd
BuildRequires: libconfig-devel, lz4-devel
BuildRequires: libdaemon-devel
BuildRequires: sqlite-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: libtool
BuildRequires: automake

Suggests: mariadb, community-mysql

# Build in other architectures aside from x86 is not yet supported due to some
# use of assembly code, but is on the upstream roadmap to support them.
# https://github.com/sysown/proxysql/issues/977
ExcludeArch:   %{arm} %{power64} s390x aarch64

Provides:      bundled(jemalloc) = 5.2.0
Provides:      bundled(mariadb-connector-c) = 3.0.2
Provides:      bundled(re2) = 20180701

# Added bundled libraries from v2.0.7
Provides:      bundled(clickhouse-cpp)
Provides:      bundled(cityhash) = 1.1.1
Provides:      bundled(libhttpserver) = 0.18.1
Provides:      bundled(libmicrohttpd) = 0.9.55

# There is inconsistency between name and URL of file
Source0:       https://github.com/sysown/proxysql/archive/%{name}-%{version}.tar.gz
Source1:       proxysql.service
Source2:       proxysql.1

# The upstream code bundles 15 libraries: libconfig, libdaemon, sqlite3, re2,
# mariadb-connector-c, pcre, clickhouse-cpp, lz4, cityhash, microhttpd, curl
# ev, coredumper, libssl and jemalloc.
# This patch de-bundles 8 of these libraries: libconfig, libdaemon and sqlite3,
# libsl, pcre, curl, lz4, ev
# The remaining libraries are not de-bundled due to different reasons (mainly
# being patched, more info here: https://bugzilla.redhat.com/show_bug.cgi?id=1457929).
# Other remaining libraries are not maintained in Fedora (clickhouse-cpp,
# cityhash, google-coredumper)

# Patch provides debundling bundled libraries
Patch0: proxysql_debundle.patch
Patch1: libinjection_python2_to_3.patch
%description
ProxySQL is a high performance, high availability, protocol aware proxy for
MySQL and forks (like Percona Server and MariaDB).

%prep
%setup -q
%patch0 -p1
rm -rf deps/libconfig deps/libdaemon deps/sqlite3

# Remove sources of debundled libraries from v2.0.7
rm -rf deps/libssl deps/pcre deps/curl deps/lz4 deps/libev

%build
%global _configure :
%configure help
export CPPFLAGS=$CXXFLAGS
%make_build

%install
install -p -D -m 0755 src/proxysql %{buildroot}%{_bindir}/proxysql
install -p -D -m 0640 etc/proxysql.cnf %{buildroot}%{_sysconfdir}/proxysql.cnf
install -p -D -m 0755 tools/proxysql_galera_checker.sh %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_checker.sh
install -p -D -m 0755 tools/proxysql_galera_writer.pl %{buildroot}%{_datadir}/%{name}/tools/proxysql_galera_writer.pl
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 README.md %{buildroot}%{_docdir}/proxysql/README.md
install -p -D -m 0644 RUNNING.md %{buildroot}%{_docdir}/proxysql/RUNNING.md
install -p -D -m 0644 FAQ.md %{buildroot}%{_docdir}/proxysql/FAQ.md
install -p -D -m 0644 doc/release_notes/*.md -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 doc/internal/*.txt -t %{buildroot}%{_docdir}/proxysql
install -p -D -m 0644 %{SOURCE2} %{buildroot}/%{_mandir}/man1/%{name}.1
install -d -m 0755 %{buildroot}%{_sharedstatedir}/proxysql

%pre
/usr/sbin/groupadd -r proxysql >/dev/null 2>&1 || :
/usr/sbin/useradd  -g proxysql -r -d /var/lib/proxysql -s /sbin/nologin \
    -c "ProxySQL" proxysql >/dev/null 2>&1 || :

%post
%systemd_post proxysql.service

%preun
%systemd_preun proxysql.service

%postun
%systemd_postun_with_restart proxysql.service

%files
%{_bindir}/*
%{_unitdir}/*
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/*
%license LICENSE
%defattr(-,proxysql,proxysql,-)
%{_sharedstatedir}/%{name}
%defattr(-,proxysql,root,-)
%config(noreplace) %{_sysconfdir}/%{name}.cnf

%changelog
* Tue Aug 04 2020 Filip Januš <fjanus@redhat.com> - 2.0.13-1
- Rebase onto version 2.0.13
- Add new patch to port bundled libinjection to python 3
- Fix debundle patch, new bundled library (libhttpserver) - new dependencies
- Remove bundled google-coredumper

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Lukas Javorsky <ljavorsk@redhat.com> - 2.0.9-4
- Add mariadb and mysql client to suggests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Filip Januš <fjanus@redhat.com> - 2.0.9-2
- .service file path fix

* Tue Nov 19 2019 Filip Januš <fjanus@redhat.com> - 2.0.9-1
- Upstream released ProxySQL 2.0.9
- Patch0 was modified - lib/Makefile was modified

* Tue Oct 15 2019 Filip Januš <fjanus@redhat.com> - 2.0.8-1
- Upstream released ProxySQL 2.0.8

* Mon Sep 23 2019 Filip Januš <fjanus@redhat.com> - 2.0.7-1
- Updated to ProxySQL 2.0.7
- De-bundled new libraries (Update patch)
- Fix path to doc
- Fix man page path (bug #1722350)

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 1.3.7-11
- Build-require zlib-devel (bug #1727136)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 1.3.7-8
- Rebuild for new libconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Augusto Caringi <acaringi@redhat.com> 1.3.7-5
- Made install commands in install section compatible with epel7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017  Augusto Caringi <acaringi@redhat.com> 1.3.7-2
- Fixed build flags through exporting CPPFLAGS variable
- Remove unused bundled libraries
- Fixed configuration file ownership
- Replaced default login shell of proxysql user from /bin/false to /sbin/nologin

* Wed Jun 14 2017  Augusto Caringi <acaringi@redhat.com> 1.3.7-1
- Updated to ProxySQL 1.3.7
- De-bundled some libraries
- Added man page
- Updated license field
- Adopted proxysql user/group
- Improvements in spec file

* Tue May 16 2017  Augusto Caringi <acaringi@redhat.com> 1.3.6-1
- Initial build
