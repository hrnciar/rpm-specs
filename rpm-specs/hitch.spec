# Checks may only be ran from a host with internet connection
%global runcheck	0

%global hitch_user	hitch
%global hitch_group	hitch
%global hitch_homedir	%{_sharedstatedir}/hitch
%global hitch_confdir	%{_sysconfdir}/hitch
%global hitch_datadir	%{_datadir}/hitch
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# A bug in the rhel7 builders? Looks like they set _pkgdocdir fedora style
# without version...?
%if 0%{?rhel} == 6 || 0%{?rhel} == 7
%global _pkgdocdir %{_docdir}/%{name}-%{version}
%endif

%global _hardened_build 1

Name:		hitch
Version:	1.5.2
Release:	3%{?dist}
Summary:	Network proxy that terminates TLS/SSL connections

License:	BSD
URL:		https://hitch-tls.org/
Source0:	https://hitch-tls.org/source/%{name}-%{version}%{?v_rc}.tar.gz

BuildRequires:	libev-devel
BuildRequires:	openssl-devel
BuildRequires:	openssl
BuildRequires:	pkgconfig
BuildRequires:	libtool
#BuildRequires:	python-docutils >= 0.6
Requires:	openssl

Patch0:		hitch.systemd.service.patch
Patch1:		hitch.initrc.redhat.patch

# Upstream commit 60e4da2
Patch100:       hitch-1.5.2_fix_gcc-10.patch

%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
%else
Requires(preun): initscripts
%endif

%description
hitch is a network proxy that terminates TLS/SSL connections and forwards the
unencrypted traffic to some backend. It is designed to handle 10s of thousands
of connections efficiently on multicore machines.

%prep
%setup -q -n %{name}-%{version}%{?v_rc}
%patch0
%patch1
%patch100 -p1

%build
#./bootstrap

%if 0%{?rhel} == 6
CFLAGS="%{optflags} -fPIE"
LDFLAGS=" -pie"
CPPFLAGS=" -I%{_includedir}/libev"
export LDFLAGS
export CPPFLAGS
%endif
export CFLAGS

# manpages are prebuilt, no need to build again
export RST2MAN=/bin/true

%configure --docdir=%_pkgdocdir

make %{?_smp_mflags}


%install
%make_install
sed   '
	s/user = .*/user = "%{hitch_user}"/g;
	s/group = .*/group = "%{hitch_group}"/g;
	s/backend = "\[127.0.0.1\]:8000"/backend = "[127.0.0.1]:6081"/g;
	$a\syslog = on
	$a\log-level = 1
	$a\# Add pem files to this directory
	$a\pem-dir = "/etc/pki/tls/private"
	' hitch.conf.example > hitch.conf

%if 0%{?fedora} 
	sed -i 's/^ciphers =.*/ciphers = "PROFILE=SYSTEM"/g' hitch.conf
%endif

rm -f %{buildroot}%{_datarootdir}/doc/%{name}/hitch.conf.example

install -p -D -m 0644 hitch.conf %{buildroot}%{_sysconfdir}/hitch/hitch.conf
install -d -m 0755 %{buildroot}%{hitch_homedir}
install -d -m 0755 %{buildroot}%{hitch_datadir}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
install -p -D -m 0644 hitch.service %{buildroot}%{_unitdir}/hitch.service
install -p -D -m 0644 limit.conf    %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service.d/limit.conf

%else
install -p -D -m 0755 hitch.initrc.redhat %{buildroot}%{_initrddir}/hitch
install -d -m 0755 %{buildroot}%{_localstatedir}/run/hitch
%endif

# check is not enabled by default, as it won't work on the koji builders, 
# nor on machines that can't reach the Internet. 
%check
%if 0%{?runcheck} == 1
make check
%endif

%pre
groupadd -r %{hitch_group} &>/dev/null ||:
useradd -r -g %{hitch_group} -s /sbin/nologin -d %{hitch_homedir} %{hitch_user} &>/dev/null ||:


%post
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%systemd_post hitch.service
%else
/sbin/chkconfig --add hitch
%endif

%preun
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%systemd_preun hitch.service
%else
if [ $1 -lt 1 ]; then
/sbin/service hitch stop > /dev/null 2>&1
/sbin/chkconfig --del hitch
fi
%endif


%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%postun
%systemd_postun_with_restart hitch.service
%endif


%files
%doc README.md
%doc CHANGES.rst
%doc hitch.conf.example
%doc docs/*
%if 0%{?rhel} == 6
%doc LICENSE
%else
%license LICENSE
%endif
%{_sbindir}/%{name}
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%dir %{_sysconfdir}/%{name}
%attr(0700,%hitch_user,%hitch_user) %dir %hitch_homedir
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/systemd/system/%{name}.service.d/limit.conf
%ghost %verify(not md5 size mtime)  /run/%{name}/%{name}.pid

%else
%{_initrddir}/%{name}
%attr(0755,%hitch_user,%hitch_user) %dir %{_localstatedir}/run/%{name}
%attr(0644,%hitch_user,%hitch_user) %ghost %verify(not md5 size mtime)	%{_localstatedir}/run/%{name}/%{name}.pid
%endif


%changelog
* Mon Feb 10 2020 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.2-3
- Added upstream patch for gcc-10.0.1, upstream issue 326

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.2-1
- New upstream release
- Removed patches merged upstream

* Tue Nov 26 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.1-1
- New upstream release
- Added a patch working around upstream bug #322
- Example config now sets debug-level=1 and logs to syslog

* Tue Nov 12 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.5.0-4
- Added support for epel8
- Added a systemd limit.conf with defaults LimitCORE=infinity, LimitNOFILE=10240
- Added pem-dir = "/etc/pki/tls/private" to the example config
- Changed systemd Type=forking matching the example config, fixes bz #1731420
- Simplified handling of the _docdir macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.5.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Ingvar Hagelund <ingvar@redpill-linpro.com>  - 1.4.8-1
- New upstream release 1.4.8, closes bz 1569501

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 04 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.6-4
- Rebuilt against openssl-1.0.2k for epel7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.6-1
- New upstream release
- Removed unnecessary fix for upstream bug #181

* Wed May 31 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> - 1.4.5-1
- New upstream release
- Had to add -Wno-error=strict-aliasing because of upstream bug #181

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.4-2
- More macros
- Use systemd's RuntimeDirectory instead of tmpfilesd
- hitch now owns its homedir, closing bz #1405948

* Thu Dec 22 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.4-1
- New upstream release
- Removed merged patch for openssl-1.1

* Thu Nov 17 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.3-1
- New upstream release
- Added upstream patch for openssl-1.1

* Thu Nov 17 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.2-1
- New upstream release
- Added new manpage for hitch.conf
- Updated sed edit of the example config to match values in the test suite
- Added a hack for un-fedora-styling _pkgdocdir on rhel7 builders

* Sat Sep 24 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.4.1-1
- New upstream release

* Tue Sep 13 2016 Ingvar Hagelund <ingvar@repdill-linpro.com> 1.4.0-1
- New upstream release

* Thu Aug 25 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.1-1
- New upstream release
- Fixes for beta3 ironed out upstream, so removed

* Mon Aug 08 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3.0-0.1.beta3
- New upstream beta release
- Manually build man page, BuildRequires python-docutils => 0.6
- Check suit now runs on el6 without patching

* Fri May 20 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.2.0-2
- Added missing check on upgrade/uninstall in postun script on epel6

* Mon Apr 25 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.2.0-1
- New upstream release
- Clean up test tree before build
- Removed no longer needed test patch 
- Rebased missing_curl_resolve_on_el6 test patch
- Added reload option to systemd service file and sysv initrc script
- Changed the default cipher to "PROFILE=SYSTEM" on fedora

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.1.1-1
- New upstream release
- Removed patches included upstream
- No need to rebuild the manpage, as the upstream distribution includes it

* Mon Nov 23 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.1.0-1
- New upstream release
- Use the _pkgdocdir macro to avoid docdir hacks for el6
- Added a patch from upstream that sets stronger ciphers as default

* Thu Oct 15 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.1-1
- New upstream release
- New Home and Source0 URLs
- Rebased patches
- Changed initrc and systemd start up scripts to match new binary name

* Tue Aug 04 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.5.1.beta5
- New upstream beta
- Dropped patch3 and patch5, they are fixed in upstream
- Rebased patch for curl on el6
- hitch no longer autocreates the default config, so use the provided example

* Tue Aug 04 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.3.beta4
- Much simpler patch for github issue #37

* Mon Aug 03 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.2.beta4
- Patching around upstream github issue #37

* Mon Aug 03 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.4.1.beta4
- New upstream beta
- Dropped setgroups patch as it has been accepted upstream
- Simple sed replace nobody for nogroup in test08

* Sun Jul 19 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.4.beta3
- Some more fixes for the fedora package review, ref Cicku

* Thu Jul 16 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.3.beta3
- Some more fixes for the fedora package review, ref Jeff Backus

* Fri Jun 26 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.2.beta3
- Added _hardened_build macro and PIE on el6

* Thu Jun 25 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.1.beta3
- Some fixes for the fedora package review, ref Sören Möller
- Now runs the test suite in check, adding BuildRequire openssl
- Added a patch that fixed missing cleaning running daemons from test suite
- Added a patch that made test07 run on older curl (epel6)
- Package owns /etc/hitch
- Added pidfile to systemd and tmpfiles.d configuration
- Added pidfile to redhat sysv init script

* Wed Jun 10 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.0.0-0.3.beta3
- Initial wrap for fedora

