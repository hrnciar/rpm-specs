# For deep debugging we need to build binaries with extra debug info
%bcond_with     debug

Name:           mariadb-connector-c
Version:        3.1.8
Release:        1%{?with_debug:.debug}%{?dist}
Summary:        The MariaDB Native Client library (C driver)
License:        LGPLv2+
Source:         https://downloads.mariadb.org/interstitial/connector-c-%{version}/%{name}-%{version}-src.tar.gz
Source2:        my.cnf
Source3:        client.cnf
Url:            http://mariadb.org/
# More information: https://mariadb.com/kb/en/mariadb/building-connectorc-from-source/

Patch1:         testsuite.patch

Requires:       %{_sysconfdir}/my.cnf
BuildRequires:  zlib-devel cmake openssl-devel gcc-c++
# Remote-IO plugin
BuildRequires:  libcurl-devel
# auth_gssapi_client plugin
BuildRequires:  krb5-devel

%description
The MariaDB Native Client library (C driver) is used to connect applications
developed in C/C++ to MariaDB and MySQL databases.



%package devel
Summary:        Development files for mariadb-connector-c
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel zlib-devel
BuildRequires:  multilib-rpm-config

%description devel
Development files for mariadb-connector-c.
Contains everything needed to build against libmariadb.so >=3 client library.



%package test
Summary:        Testsuite files for mariadb-connector-c
Requires:       %{name} = %{version}-%{release}
Requires:       cmake
Recommends:     mariadb-server

%description test
Testsuite files for mariadb-connector-c.
Contains binaries and a prepared CMake ctest file.
Requires running MariaDB / MySQL server with create database "test".



%package config
Summary:        Configuration files for packages that use /etc/my.cnf as a configuration file
BuildArch:      noarch
Obsoletes:      mariadb-config <= 3:10.3.8-4

%description config
This package delivers /etc/my.cnf that includes other configuration files
from the /etc/my.cnf.d directory and ships this directory as well.
Other packages should only put their files into /etc/my.cnf.d directory
and require this package, so the /etc/my.cnf file is present.



%prep
%setup -q -n %{name}-%{version}-src
%patch1 -p1

# Remove unsused parts
rm -r win zlib win-iconv examples



%build
%{set_build_flags}

# Override all optimization flags when making a debug build
%{?with_debug: CFLAGS="$CFLAGS -O0 -g"}
CXXFLAGS="$CFLAGS"
export CFLAGS CXXFLAGS

# https://jira.mariadb.org/browse/MDEV-13836:
#   The server has (used to have for ages) some magic around the port number.
#   If it's 0, the default port value will use getservbyname("mysql", "tcp"), that is, whatever is written in /etc/services.
#   If it's a positive number, say, 3306, it will be 3306, no matter what /etc/services say.
#   I don't know if that behavior makes much sense, /etc/services wasn't supposed to be a system configuration file.

# The INSTALL_* macros have to be specified relative to CMAKE_INSTALL_PREFIX
# so we can't use %%{_datadir} and so forth here.

%cmake . \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DCMAKE_SYSTEM_PROCESSOR="%{_arch}" \
\
       -DMARIADB_UNIX_ADDR=%{_sharedstatedir}/mysql/mysql.sock \
       -DMARIADB_PORT=3306 \
\
       -DWITH_EXTERNAL_ZLIB=YES \
       -DWITH_SSL=OPENSSL \
       -DWITH_MYSQLCOMPAT=ON \
       -DPLUGIN_CLIENT_ED25519=DYNAMIC \
\
       -DINSTALL_LAYOUT=RPM \
       -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
       -DINSTALL_BINDIR="bin" \
       -DINSTALL_LIBDIR="%{_lib}" \
       -DINSTALL_INCLUDEDIR="include/mysql" \
       -DINSTALL_PLUGINDIR="%{_lib}/mariadb/plugin" \
       -DINSTALL_PCDIR="%{_lib}/pkgconfig" \
\
       -DWITH_UNITTEST=ON

#cmake ./ -LAH

%make_build



%install
%make_install

%multilib_fix_c_header --file %{_includedir}/mysql/mariadb_version.h

# Remove static linked libraries and symlinks to them
rm %{buildroot}%{_libdir}/lib*.a

# Add a compatibility symlinks
ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h

# Install config files
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/my.cnf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/my.cnf.d/client.cnf



%check
# Check the generated configuration on the actual machine
%{buildroot}%{_bindir}/mariadb_config

# Run the unit tests
# - don't run mytap tests
# - ignore the testsuite result for now. Enable tests now, fix them later.
# Note: there must be a database called 'test' created for the testcases to be run
pushd unittest/libmariadb/
ctest || :
popd



%files
%{_libdir}/libmariadb.so.3

%dir %{_libdir}/mariadb
%dir %{_libdir}/mariadb/plugin
%{_libdir}/mariadb/plugin/*

%doc README
%license COPYING.LIB



%files devel
# Binary which provides compiler info for software compiling against this library
%{_bindir}/mariadb_config
%{_bindir}/mysql_config

# Symlinks to the versioned library
%{_libdir}/libmariadb.so
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so

# Pkgconfig
%{_libdir}/pkgconfig/libmariadb.pc

# Header files
%dir %{_includedir}/mysql
%{_includedir}/mysql/*



%files config
%dir %{_sysconfdir}/my.cnf.d
%config(noreplace) %{_sysconfdir}/my.cnf
%config(noreplace) %{_sysconfdir}/my.cnf.d/client.cnf



%files test
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/libcctap.so



# Opened issues on the upstream tracker:
#   https://jira.mariadb.org/browse/CONC-293
#      DESCRIPTION: add mysql_config and mariadb_config man page
#      IN_PROGRESS: upsteam plans to add it to 3.1 release
#   https://jira.mariadb.org/browse/CONC-410
#      DESCRIPTION: Fix pkgconfig file - overlinking issues
#      IN_PROGRESS: PR submitted, problem consulted & explained, waiting on upstream response
#   https://jira.mariadb.org/browse/CONC-436
#      DESCRIPTION: Make testsuite independent / portable
#      NEW:         PR submitted, problem explained, waiting on upstream response

# Coverity Scan results from 3.0.10 release:
#   https://jira.mariadb.org/browse/CONC-234
#      DESCRIPTION: Covscan report
#      TODO:        Check atleast the important issues

# Downstream issues:
#   Start running this package testsuite at the build time
#      It requires a running MariaDB server
#         mariadb-server package pulls in mariadb-connector-c as a dependency
#         Need to ensure, that the testsuite is ran against the newly build library, instead of the one from the pulled package
#      Need to ensure, that the testsuite will also run properly on 'fedpkg local' buid, not damaging the host machine

%changelog
* Thu May 14 2020 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.8-1
- Rebase to 3.1.8

* Mon Mar 16 2020 Michal Schorm <mschorm@redhat.com> - 3.1.7-2
- Rebase to 3.1.7 latest git
  Fix for: https://jira.mariadb.org/browse/CONC-441

* Mon Feb 03 2020 Michal Schorm <mschorm@redhat.com> - 3.1.7-1
- Rebase to 3.1.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.6-1
- Rebase to 3.1.6

* Tue Nov 12 2019 Michal Schorm <mschorm@redhat.com> - 3.1.5-1
- Rebase to 3.1.5

* Sun Nov 03 2019 Michal Schorm <mschorm@redhat.com> - 3.1.4-2
- Fix for #1624533

* Wed Sep 18 2019 Lukas Javorsky <ljavorsk@redhat.com> - 3.1.4-1
- Rebase to 3.1.4

* Wed Sep 11 2019 Michal Schorm <mschorm@redhat.com> - 3.1.3-3
- Enable building of the ed25519 client plugin.
  It won't be shipped anymore by 'mariadb-server'

* Mon Aug 19 2019 Michal Schorm <mschorm@redhat.com> - 3.1.3-2
- Extract the prepared testsuite to the standalone subpackage so it can be run outside of the buildroot

* Fri Aug 02 2019 Michal Schorm <mschorm@redhat.com> - 3.1.3-1
- Rebase to 3.1.3 version
- Patch upstreamed
- Remove glob from library version, as per Fedora Packaging Guidelines

* Fri Jul 19 2019 Michal Schorm <mschorm@redhat.com> - 3.1.2-2
- Use macro to set build flags

* Fri Jul 12 2019 Michal Schorm <mschorm@redhat.com> - 3.1.2-1
- Rebase to 3.1 version
- Disabling the ED25519 plugin
- Plugindir patch upstreamed
- Added debug build switch

* Tue May 21 2019 Michal Schorm <mschorm@redhat.com> - 3.0.10-2
- Fix overlinking issues

* Wed May 15 2019 Michal Schorm <mschorm@redhat.com> - 3.0.10-1
- Rebase to 3.0.10
- Remove scriplet; no longer needed

* Fri Mar 29 2019 Michal Schorm <mschorm@redhat.com> - 3.0.9-3
- Add "zlib-devel" requirement in "-devel" subpackage. MariaDB requires
  linking with "-lz", which will fail without the zlib library
- Related: #1693966

* Mon Feb 18 2019 Michal Schorm <mschorm@redhat.com> - 3.0.9-2
- Fix plugindir issues
  Resolves: #1624533

* Mon Feb 18 2019 Michal Schorm <mschorm@redhat.com> - 3.0.9-1
- Rebase to 3.0.9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Michal Schorm <mschorm@redhat.com> - 3.0.8-1
- Rebase to 3.0.8

* Mon Nov 19 2018 Michal Schorm <mschorm@redhat.com> - 3.0.7-1
- Rebase to 3.0.7

* Tue Sep 04 2018 Michal Schorm <mschorm@redhat.com> - 3.0.6-2
- Fix parallel installability of x86_64 and i686 devel package

* Fri Aug 03 2018 Michal Schorm <mschorm@redhat.com> - 3.0.6-1
- Rebase to 3.0.6

* Tue Jul 17 2018 Honza Horak <hhorak@redhat.com> - 3.0.5-3
- Add -config sub-package that delivers system-wide /etc/my.cnf and
  /etc/my.cnf.d directory, that other packages should use
  This package also obsoletes mariadb-config

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Michal Schorm <mschorm@redhat.com> - 3.0.5-1
- Rebase to 3.0.5

* Thu Apr 26 2018 Michal Schorm <mschorm@redhat.com> - 3.0.4-1
- Rebase to 3.0.4

* Mon Apr 23 2018 Michal Schorm <mschorm@redhat.com> - 3.0.3-4
- Further fix of the '--plugindir' output from the config binary
  Realted: #1569159

* Wed Mar 21 2018 Richard W.M. Jones <rjones@redhat.com> - 3.0.3-3
- Fix plugin install directory (INSTALL_PLUGINDIR not PLUGIN_INSTALL_DIR).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Michal Schorm <mschorm@redhat.com> - 3.0.3-1
- Rebase to 3.0.3

* Mon Nov 27 2017 Honza Horak <hhorak@redhat.com> - 3.0.2-21
- Remove unneeded dependency on xmlto

* Tue Nov 14 2017 Pavel Raiskup <praiskup@redhat.com> - 3.0.2-19
- drop misleading provides

* Wed Nov 08 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-19
- Move the scriptlet to the correct package

* Thu Nov 02 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-18
- Fix typo in require

* Wed Nov 01 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-17
- Use correct require for OpenSSL

* Wed Nov 01 2017 Merlin Mathesius <mmathesi@redhat.com> - 3.0.2-16
- Correct typo in spec file conditional

* Tue Oct 31 2017 Merlin Mathesius <mmathesi@redhat.com> - 3.0.2-15
- Cleanup spec file conditionals

* Tue Oct 31 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-14
- Remove Requires for openssl. Managed by RPM.

* Mon Oct 30 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-13
- Update scriplet dealing with symlinks as Guidelines suggests
  Related: #1501933

* Thu Oct 26 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-12
- Move library directly to libdir, don't create any symlinks to directories
- Update scritplets, so they only check for old symlinks to directories
  Related: #1501933
- Add 'Conflicts' with mariadb package on F<28
  Related: #1506441

* Mon Oct 09 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-11
- Fix ldconfig path

* Wed Oct 04 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-10
- Add scriptlets to handle errors in /usr/lib64/ created by older versions
  of mariadb and mariadb-connector-c pakages

* Wed Sep 20 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-9
- Add symlinks so more packages will build succesfully
- Change libdir from .../lib64/mariadb to mysql
  Related: #1497234

* Wed Sep 13 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-7
- Move header files to the same location, as they would be in mariadb-server
- Add provides "libmysqlclient.so"

* Tue Sep 05 2017 Honza Horak <hhorak@redhat.com> - 3.0.2-5
- Remove a symlink /usr/lib64/mysql that conflicts with mariadb-libs

* Mon Aug 14 2017 Honza Horak <hhorak@redhat.com> - 3.0.2-4
- Add compatibility symlinks

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Michal Schorm <mschorm@redhat.com> - 3.0.2-1
- Rebase to version 3.0.2
- Library libmariadb.so.3 introduced
- Plugin Remote-IO enabled

* Wed Jun 07 2017 Michal Schorm <mschorm@redhat.com> - 2.3.3-1
- Rebase to version 2.3.3
- Patch dropped, solved by upstream; https://jira.mariadb.org/browse/CONC-231

* Tue Feb 07 2017 Michal Schorm <mschorm@redhat.com> - 2.3.2-2
- Fix based on output from RPMLint in previous version

* Tue Jan 24 2017 Michal Schorm <mschorm@redhat.com> - 2.3.2-1
- Rebase to version 2.3.2, patch needed (fixed by upstream in later versions)
- Plugin dir moved from /libdir/plugin to /libdir/mariadb/plugin

* Thu Oct 27 2016 Michal Schorm <mschorm@redhat.com> - 2.3.1-3
- Fixed ownership of {_libdir}/mariadb (this dir must me owned by package)
- Fixed ownership of {_sysconfigdir}/ld.so.conf.d (this dir must me owned by package)
- Fixed redundnace on lines with {_sysconfigdir}/ld.so.conf.d
- Fixed ownership of {_bindir} (only one program is owned, so let's be accurate)
- Some comments added, for me and future maintainers

* Mon Oct 17 2016 Michal Schorm <mschorm@redhat.com> - 2.3.1-2
- Fixed ownership of {_libdir}/mariadb directory and cosmetic specfile changes

* Tue Sep 13 2016 Michal Schorm <mschorm@redhat.com> - 2.3.1-1
- Rebase to version 2.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Matej Mužila <mmuzila@redhat.com> - 2.1.0-1
- Rebase to version 2.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Matej Mužila <mmuzila@redhat.com> - 2.0.0-2
- Fixed html IDs in documentation

* Tue Aug 26 2014 Matej Mužila <mmuzila@redhat.com> - 2.0.0-2
- Initial version for 2.0.0