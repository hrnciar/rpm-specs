Summary:           Tiny IPv4 and IPv6 SIP redirect server written in Perl
Summary(de):       Ein winziger, in Perl geschriebener, SIP Redirekt-Server
Name:              sip-redirect
Version:           0.2.0
Release:           12%{?dist}
License:           GPLv2+
URL:               https://ftp.robert-scheck.de/linux/%{name}/
Source:            https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
BuildArch:         noarch
Requires:          logrotate
%if 0%{?rhel} > 6 || 0%{?fedora} > 16
Requires:          perl(Socket) >= 1.95
%else
Requires:          perl(Socket6)
%endif
Requires(pre):     shadow-utils
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
BuildRequires:     perl-generators
BuildRequires:     systemd
%else
Requires(post):    /sbin/chkconfig
Requires(preun):   /sbin/service, /sbin/chkconfig
Requires(postun):  /sbin/service
%endif

%description
sip-redirect is a tiny SIP redirect server written in Perl. It is IPv4 and
IPv6 capable, but the IPv6 support is optional. The RFC 3261 was the base for
this simple and very configurable implementation. There is neither TCP nor
multicast support programmed in.

%description -l de
sip-redirect ist ein winziger, in Perl geschriebener, SIP Redirekt-Server. Er
unterstützt IPv4 und IPv6, aber der IPv6-Support ist optional. Als Grundlage
für diese einfache und sehr konfigurierbare Implementation wurde die RFC 3261
verwendet. Es wurde keine Unterstützung für TCP und für Multicast eingebaut.

%prep
%setup -q

%build

%install
%make_install

%pre
getent group sip > /dev/null || %{_sbindir}/groupadd -r sip
getent passwd sip > /dev/null || %{_sbindir}/useradd -r -g sip -d / -s /sbin/nologin -c "SIP redirect server" sip
exit 0

%post
touch %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chown sip:sip %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chmod 640 %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%else
/sbin/chkconfig --add %{name}

%preun
if [ $1 -eq 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ne 0 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi
%endif

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/rc.d/init.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(0640,sip,sip) %{_localstatedir}/log/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Robert Scheck <robert@fedoraproject.org> 0.2.0-9
- Corrected systemd scriptlets usage (#1716388)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 29 2014 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.1.2-9
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.1.2-3
- Rebuild against rpm 4.6

* Thu Nov 06 2008 Robert Scheck <robert@fedoraproject.org> 0.1.2-2
- Changes to match with Fedora Packaging Guidelines (#443675)

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 0.1.2-1
- Upgrade to 0.1.2

* Wed Oct 25 2006 Robert Scheck <robert@fedoraproject.org> 0.1.1-1
- Upgrade to 0.1.1

* Sat Jul 08 2006 Robert Scheck <robert@fedoraproject.org> 0.1.0-1
- Upgrade to 0.1.0
- Initial spec file for Fedora Core and Red Hat Enterprise Linux
