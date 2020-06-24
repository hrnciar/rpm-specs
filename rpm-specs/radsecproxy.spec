Summary:        Generic RADIUS proxy with RadSec support
Name:           radsecproxy
Version:        1.8.1
Release:        3%{?dist}
License:        BSD
URL:            https://radsecproxy.github.io/
Source0:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-210FA7FB28E45779777BAA1C5963D59C3D68633B.gpg
Source3:        %{name}.conf
Source4:        %{name}.service
Source5:        %{name}.logrotate
Source6:        %{name}.tmpfilesd
Patch0:         radsecproxy-1.8.1-paths.patch
Patch1:         radsecproxy-1.8.1-gcc10.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  nettle-devel
BuildRequires:  openssl-devel
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?rhel} > 6
BuildRequires:  systemd
%endif
%{?systemd_requires}
Requires(pre):  shadow-utils
Requires:       logrotate

%description
radsecproxy is a generic RADIUS proxy that in addition to usual RADIUS UDP
transport, also supports TLS (RadSec), as well as RADIUS over TCP and DTLS.
The aim is for the proxy to have sufficient features to be flexible, while
at the same time to be small, efficient and easy to configure.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch0 -p1 -b .paths
%patch1 -p1 -b .gcc10

%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_rundir},%{_localstatedir}/{lib,log}}/%{name}/
install -D -p -m 0640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
chmod 644 tools/*.sh

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "RADIUS proxy with RadSec support" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc AUTHORS ChangeLog radsecproxy.conf-example THANKS tools
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_bindir}/%{name}-conf
%{_bindir}/%{name}-hash
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-hash.1*
%{_mandir}/man5/%{name}.conf.5*
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/

%changelog
* Sun Feb 02 2020 Robert Scheck <robert@fedoraproject.org> 1.8.1-3
- Added patch to declare pthread_attr as extern in header file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Robert Scheck <robert@fedoraproject.org> 1.8.1-1
- Upgrade to 1.8.1

* Tue Sep 17 2019 Robert Scheck <robert@fedoraproject.org> 1.8.0-1
- Upgrade to 1.8.0 (#1753052)
- Initial spec file for Fedora and Red Hat Enterprise Linux
