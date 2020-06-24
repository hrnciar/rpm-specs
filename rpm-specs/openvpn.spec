%define _hardened_build 1
#define prerelease rc22

# Build conditionals
# tests_long - Enabled by default, enables long running tests in %%check
%bcond_without tests_long

Name:              openvpn
Version:           2.4.9
Release:           1%{?prerelease:.%{prerelease}}%{?dist}
Summary:           A full-featured SSL VPN solution
URL:               https://community.openvpn.net/
Source0:           https://build.openvpn.net/downloads/releases/%{name}-%{version}%{?prerelease:_%{prerelease}}.tar.xz
Source1:           https://build.openvpn.net/downloads/releases/%{name}-%{version}%{?prerelease:_%{prerelease}}.tar.xz.asc
Source2:           roadwarrior-server.conf
Source3:           roadwarrior-client.conf
# Upstream signing key
Source6:           gpgkey-F554A3687412CFFEBDEFE0A312F5F7B42F2B01E7.gpg
Patch1:            0001-Change-the-default-cipher-to-AES-256-GCM-for-server-.patch
Patch50:           openvpn-2.4-change-tmpfiles-permissions.patch
License:           GPLv2
BuildRequires:     gnupg2
BuildRequires:     gcc
BuildRequires:     systemd-devel
BuildRequires:     lzo-devel
BuildRequires:     lz4-devel
BuildRequires:     openssl-devel
BuildRequires:     pkcs11-helper-devel >= 1.11
BuildRequires:     pam-devel
BuildRequires:     libselinux-devel
# For the perl_default_filter macro
BuildRequires:     perl-macros
BuildRequires:     systemd
%{?systemd_requires}
# For /sbin/ip.
BuildRequires:     iproute
Requires:          iproute
Requires(pre):     /usr/sbin/useradd

# Filter out the perl(Authen::PAM) dependency.
# No perl dependency is really needed at all.
%{?perl_default_filter}

%description
OpenVPN is a robust and highly flexible tunneling application that uses all
of the encryption, authentication, and certification features of the
OpenSSL library to securely tunnel IP networks over a single UDP or TCP
port.  It can use the Marcus Franz Xaver Johannes Oberhumers LZO library
for compression.

%package devel
Summary:           Development headers and examples for OpenVPN plug-ins

%description devel
OpenVPN can be extended through the --plugin option, which provides
possibilities to add specialized authentication, user accounting,
packet filtering and related features.  These plug-ins need to be
written in C and provides a more low-level and information rich access
to similar features as the various script-hooks.


%prep
gpgv2 --quiet --keyring %{SOURCE6} %{SOURCE1} %{SOURCE0}
%setup -q -n %{name}-%{version}%{?prerelease:_%{prerelease}}
%patch1 -p1 -b .ch_default_cipher
%patch50 -p1

sed -i -e 's,%{_datadir}/openvpn/plugin,%{_libdir}/openvpn/plugin,' doc/openvpn.8

# %%doc items shouldn't be executable.
find contrib sample -type f -perm /100 \
    -exec chmod a-x {} \;

%build
%configure \
    --enable-iproute2 \
    --with-crypto-library=openssl \
    --enable-pkcs11 \
    --enable-selinux \
    --enable-systemd \
    --enable-x509-alt-username \
    --enable-async-push \
    --docdir=%{_pkgdocdir} \
    SYSTEMD_UNIT_DIR=%{_unitdir} \
    TMPFILES_DIR=%{_tmpfilesdir} \
    IPROUTE=/sbin/ip
%{__make}

%check
# Test Crypto:
./src/openvpn/openvpn --genkey --secret key
./src/openvpn/openvpn --cipher aes-128-cbc --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-256-cbc --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-128-gcm --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-256-gcm --test-crypto --secret key

%if %{with tests_long}
# Randomize ports for tests to avoid conflicts on the build servers.
cport=$[ 50000 + ($RANDOM % 15534) ]
sport=$[ $cport + 1 ]
sed -e 's/^\(rport\) .*$/\1 '$sport'/' \
    -e 's/^\(lport\) .*$/\1 '$cport'/' \
    < sample/sample-config-files/loopback-client \
    > %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client
sed -e 's/^\(rport\) .*$/\1 '$cport'/' \
    -e 's/^\(lport\) .*$/\1 '$sport'/' \
    < sample/sample-config-files/loopback-server \
    > %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server

pushd sample
# Test SSL/TLS negotiations (runs for 2 minutes):
../src/openvpn/openvpn --config \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client &
../src/openvpn/openvpn --config \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server
wait
popd

rm -f %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server
%endif

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f
mkdir -p -m 0750 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/client $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/server
cp %{SOURCE2} %{SOURCE3} sample/sample-config-files/

# Create some directories the OpenVPN package should own
mkdir -m 0750 -p $RPM_BUILD_ROOT%{_rundir}/%{name}-{client,server}
mkdir -m 0770 -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

# Package installs into %%{_pkgdocdir} directly
# Add various additional files
cp -a AUTHORS ChangeLog contrib sample distro/systemd/README.systemd $RPM_BUILD_ROOT%{_pkgdocdir}

# Remove some files which does not really belong here
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/sample/Makefile{,.in,.am}
rm -f  $RPM_BUILD_ROOT%{_pkgdocdir}/contrib/multilevel-init.patch
rm -rf $RPM_BUILD_ROOT%{_pkgdocdir}/sample/sample-keys

%pre
getent group openvpn &>/dev/null || groupadd -r openvpn
getent passwd openvpn &>/dev/null || \
    /usr/sbin/useradd -r -g openvpn -s /sbin/nologin -c OpenVPN \
        -d /etc/openvpn openvpn

%post
%systemd_post openvpn-client@\*.service
%systemd_post openvpn-server@\*.service

%preun
%systemd_preun openvpn-client@\*.service
%systemd_preun openvpn-server@\*.service

%postun
%systemd_postun_with_restart openvpn-client@\*.service
%systemd_postun_with_restart openvpn-server@\*.service
%systemd_postun_with_restart openvpn@\*.service

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/README.IPv6
%exclude %{_pkgdocdir}/README.mbedtls
%exclude %{_pkgdocdir}/sample/sample-plugins
%{_mandir}/man8/%{name}.8*
%{_sbindir}/%{name}
%{_libdir}/%{name}/
%{_unitdir}/%{name}-client@.service
%{_unitdir}/%{name}-server@.service
%{_tmpfilesdir}/%{name}.conf
%config %dir %{_sysconfdir}/%{name}/
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/client
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/server
%attr(0750,-,openvpn) %{_rundir}/%{name}-client
%attr(0750,-,openvpn) %{_rundir}/%{name}-server
%attr(0770,openvpn,openvpn) %{_sharedstatedir}/%{name}

%files devel
%{_pkgdocdir}/sample/sample-plugins
%{_includedir}/openvpn-plugin.h
%{_includedir}/openvpn-msg.h


%changelog
* Sun Apr 19 2020 David Sommerseth <dazo@eurephia.org> - 2.4.9-1
- Update to upstream OpenVPN 2.4.9

* Wed Feb 12 2020 David Sommerseth <dazo@eurephia.org> - 2.4.8-3
- Rebuilt to be linked against latest lzo (RHBZ#1802299)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 1 2019 David Sommerseth <dazo@eurephia.org> - 2.4.8-1
- Updating to upstream OpenVPN 2.4.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 David Sommerseth <dazo@eurephia.org> - 2.4.7-1
- Updating to upstream OpenVPN 2.4.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 6 2018 David Sommerseth <dazo@eurephia.org> - 2.4.6-3
- Enable the asynchronous push feature, which can improve connect speeds with slow authentication backends

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 David Sommerseth <dazo@eurephia.org> - 2.4.6-1
- Updating to upstream, openvpn-2.4.6

* Thu Mar 1 2018 David Sommerseth <dazo@eurephia.org> - 2.4.5-1
- Updating to upstream, openvpn-2.4.5
- Package upstream ChangeLog, which contains a bit more details than Changes.rst
- Cleaned up spec file further, removed Group: tag, trimmed changelog section,
  added gcc to BuildRequires.
- Excluded not relevant file, README.mbedtls
- Package upstream version of README.systemd
- Fix wrong group owner of /etc/openvpn/{client,server} (rhbz#1526743)
- Changed crypto self-test to test AES-{128,256}-{CBC,GCM} instead of only BF-CBC (deprecated)
- Change /run/openvpn-{client,server} permissions to be 0750 instead of 0710, with group set to openvpn

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.4-2
- Fix systemd executions/requirements

* Tue Sep 26 2017 David Sommerseth <dazo@eurephia.org> - 2.4.4-1
- Update to upstream openvpn-2.4.4
- Includes fix for possible stack overflow if --key-method 1 is used {CVE-2017-12166}

* Fri Aug  4 2017 David Sommerseth <dazo@eurephia.org> - 2.4.3-4
- Change to AES-GCM as the default cipher for server configurations (rhbz#1479270)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 David Sommerseth <dazo@eurephia.org> - 2.4.3-1
- Updating to upstream openvpn-2.4.3
- Fix remotely-triggerable ASSERT() on malformed IPv6 packet {CVE-2017-7508}
- Prevent two kinds of stack buffer OOB reads and a crash for invalid input data {CVE-2017-7520}
- Fix potential double-free in --x509-alt-username {CVE-2017-7521}
- Fix remote-triggerable memory leaks {CVE-2017-7521}
- Ensure OpenVPN systemd services are restarted upon upgrades
- Verify PGP signature of source tarball as part of package building
- Build against system lz4 library

* Fri May 12 2017 David Sommerseth <dazo@eurephia.org> - 2.4.2-2
- Install and take ownership of /run/openvpn-{client,server} (rhbz#1444601)
- Install and take ownership of /var/lib/openvpn (rhbz#922786)

* Thu May 11 2017 David Sommerseth <dazo@eurephia.org> - 2.4.2-1
- Updating to upstream openvpn-2.4.2
- Switching back to OpenSSL, using compat-openssl10 (rhbz#1443749, rhbz#1432125, rhbz#1440468)
- Re-enabling --enable-x509-alt-username (rhbz#1443942)
- Add --enable-selinux
- Build with lz4 library from Fedora

* Wed Mar 29 2017 David Sommerseth <dazo@eurephia.org> - 2.4.1-3
- Splitting out -devel files into a separate package
- Removed several contrib and sample files which makes is not
  strictly needed in this package.
- build: Enable tests runs by default, long running tests can
  be disabled with "--without tests_long"
- build: Removed defined %%{plugins} macro not in use

* Fri Mar 24 2017 David Sommerseth <dazo@eurephia.org> - 2.4.1-2
- Various cleanups
- Use systemd-rpm macros (rhbz #850257)
- Removed the deprecated openvpn@.service unit.  Replaced by openvpn-{client,server}@.service
- Added README.systemd describing new systemd unit files

* Thu Mar 23 2017 David Sommerseth <dazo@eurephia.org> - 2.4.1-1
- Updating to upstream release, v2.4.1
- Added mbed TLS patch to allow RSA keys down to 1024 bits plus SHA1
  and RIPE-160 hasing algorithms (based on OpenVPN 3 legacy profile)
- Removed no-functional ./configure options
- Use upstream tmfiles.d/openvpn
- Package newer openvpn-client/server@.service unit files

* Thu Feb 09 2017 Jon Ciesla <limburgher@gmail.com> 2.4.0-2
- Move to mbedtls to resolve FTBFS.
- Dropped, re-add once openvpn supports openssl 1.1.x
-    --enable-pkcs11 \
-    --enable-x509-alt-username \

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> 2.4.0-1
- 2.4.0.

