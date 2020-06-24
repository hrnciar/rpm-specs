%global _hardened_build 1
%global snapshot 0

Summary: Opportunistically encrypt TCP connections
Name: tcpcrypt
Version: 0.5
Release: 2%{?dist}
License: BSD
Url: http://tcpcrypt.org/
Source0: http://tcpcrypt.org//%{name}-%{version}.tar.gz
SOURCE1: tmpfiles-tcpcrypt.conf
SOURCE2: tcpcryptd.service
SOURCE3: tcpcryptd-firewall
SOURCE4: tcpcrypt-firewalld.xml
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:  gcc
BuildRequires: openssl-devel libnetfilter_queue-devel libcap-devel
BuildRequires: libnetfilter_conntrack-devel libpcap-devel
BuildRequires: libtool autoconf automake
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(pre): shadow-utils
# we need to require it to install our file
Requires: firewalld

%description
Provides a protocol that attempts to encrypt (almost) all of your
network traffic. Unlike other security mechanisms, Tcpcrypt works out
of the box: it requires no configuration, no changes to applications,
and your network connections will continue to work even if the remote
end does not support

%package devel
Summary: Development package that includes the tcpcrypt header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The devel package contains the tcpcrypt library and the include files

%package libs
Summary: Libraries used by tcpcryptd server and tcpcrypt-aware applications

%description libs
Contains libraries used by tcpcryptd server and tcpcrypt-aware applications

%prep
%autosetup

%build
sh bootstrap.sh
%configure --disable-static --disable-rpath
%make_build

%install
%make_install
install -m 0755 %{SOURCE3} %{buildroot}/%{_bindir}
rm %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d/ %{buildroot}/run/tcpcryptd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/tcpcrypt.conf
mkdir -p %{buildroot}%{_unitdir}
install -m 0755 %{SOURCE2} %{buildroot}/%{_unitdir}/tcpcryptd.service
# install firewalld policy needed for tracking and marking packets
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_prefix}/lib/firewalld/services/tcpcryptd.xml

%files libs
%doc README.markdown
%license LICENSE
%{_libdir}/libtcpcrypt.so.*

%files
%doc README.markdown
%license LICENSE
%{_bindir}/tcnetstat
%{_bindir}/tcpcryptd
%{_bindir}/tcpcryptd-firewall
%{_bindir}/tcs
%{_mandir}/man8/*
%attr(0644,root,root) %{_tmpfilesdir}/tcpcrypt.conf
%attr(0644,root,root) %{_unitdir}/tcpcryptd.service
%attr(0644,root,root) %{_prefix}/lib/firewalld/services/tcpcryptd.xml
%attr(0755,tcpcryptd,tcpcryptd) %dir /run/tcpcryptd

%files devel
%{_libdir}/libtcpcrypt.so
%dir %{_includedir}/tcpcrypt
%{_includedir}/tcpcrypt/*.h

%ldconfig_scriptlets libs

%pre
getent group tcpcryptd >/dev/null || groupadd -r tcpcryptd
getent passwd tcpcryptd >/dev/null || \
useradd -r -g tcpcryptd -d /var/run/tcpcryptd -s /sbin/nologin \
-c "tcpcrypt daemon account" tcpcryptd || exit 0

%post
%systemd_post tcpcryptd.service

%preun
%systemd_preun tcpcryptd.service

%postun
%systemd_postun_with_restart tcpcryptd.service

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.5-1
- Update to 0.5 plus spec cleanup and modernization

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 06 2016 Paul Wouters <pwouters@redhat.com> - 0.4-1
- Updated to 0.4
- Resolves: rhbz#1213128 wrong user tcpcrypt
- Resolves: rhbz#1312703 Package systemd ExecStartPre/ExecStopPost script broken

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.5.bb990b1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.4.bb990b1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Paul Wouters <pwouters@redhat.com> - 0.4-0.3.bb990b1b
- fix groupadd
- remove rm -rf buildroot in install target

* Thu Jan 29 2015 Paul Wouters <pwouters@redhat.com> - 0.4-0.2.bb990b1b
- Bundle tcpcrypd-firewall to start/stop the custom firewall rules
- Use macros for tmpfiles
- updated service file

* Mon Jan 19 2015 Paul Wouters <pwouters@redhat.com> - 0.4-0.1.bb990b1b
- Update to latest git, fix versioning

* Mon Aug 25 2014 Paul Wouters <pwouters@redhat.com> - 0-3.cacd9789
- Enabled autoconf Buildrequires for snapshot release

* Wed Aug 20 2014 Paul Wouters <pwouters@redhat.com> - 0-2.cacd9789
- Updated to latest git, removed patched merged upstream
- Added systemd service file
- Removed no longer needed rpath fixes

* Fri Aug 08 2014 Paul Wouters <pwouters@redhat.com> - 0-1.c8b7efa
- Patch for missing-call-to-chdir-with-chroot and missing-call-to-setgroups
- Remove RPATH

* Thu Jul 24 2014 Paul Wouters <pwouters@redhat.com> - 0-0.c8b7efa
- Initial package for review

