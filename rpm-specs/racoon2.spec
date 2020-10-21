%global _hardened_build 1

Name:           racoon2
Version:        20100526a
Release:        44%{?dist}
Summary:        An implementation of key management system for IPsec
License:        BSD
URL:            http://www.racoon2.wide.ad.jp/
Source0:        http://ftp.racoon2.wide.ad.jp/pub/%{name}/%{name}-%{version}.tgz
Patch0:         %{name}-autotools.patch
Patch1:         %{name}-init.patch
Patch2:         %{name}-functions-shebang.patch
Patch3:         %{name}-configfiles.patch
Patch4:         %{name}-getopt.patch
# 1/4 Adapt to OpenSSL 1.1.1, bug #1606070, taken from a fork at
# <https://github.com/zoulasc/racoon2>
Patch5:         %{name}-20100526a-Make-unmodified-argument-const.patch
# 2/4 Adapt to OpenSSL 1.1.1, bug #1606070, taken from a fork at
# <https://github.com/zoulasc/racoon2>
Patch6:         %{name}-20100526a-Adjust-for-openssl-1.1.patch
# 3/4 Adapt to OpenSSL 1.1.1, bug #1606070, taken from a fork at
# <https://github.com/zoulasc/racoon2>
Patch7:         %{name}-20100526a-Adjust-for-OpenSSL-v1.1.patch
# 4/4 Adapt to OpenSSL 1.1.1, bug #1606070, taken from a fork at
# <https://github.com/zoulasc/racoon2>
Patch8:         %{name}-20100526a-Fix-for-OpenSSL-1.1.patch
# Stop including unused sysctl.h that was removed from glibc-2.32,
# bug # #1856775, <https://github.com/zoulasc/racoon2>
Patch9:         %{name}-20100526a-Linux-does-not-need-sysctl.h.patch
BuildRequires:  byacc
BuildRequires:  coreutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  sed
Requires(post): pwgen
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
%endif
%description
The Racoon2 project is a joint effort which provides an implementation of key
management system for IPsec. The implementation is called Racoon2, a successor
of Racoon, which was developed by the KAME project. It supports IKEv1, IKEv2,
and KINK protocols. It works on FreeBSD, NetBSD, Linux, and Mac OS X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

sed -i '/yyget_leng/d' lib/cftoken.l

%build
# --disable-kinkd: KINK must be disabled unless krb5 is compiled --with-crypto-impl=builtin
# because kinkd uses krb5's internal crypto functions that are not compiled otherwise.
# --disable-pedant: Racoon2 doesn't compile with pedantic compiler.
%configure --disable-kinkd --disable-pedant 
# racoon2 tends to misconfigure the spmd subtree
( cd spmd && %configure )
make %{?_smp_mflags}
sed -i 's/\t/    /' samples/*.conf
# Disable spmd.pwd generation
echo "#!/bin/sh" > pskgen/autogen.spmd.pwd

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# Rename binaries and manpages
for name in spmd spmdctl iked pskgen; do
    mv %{buildroot}%{_sbindir}/{,%{name}-}$name
    mv %{buildroot}%{_mandir}/man8/{,%{name}-}$name.8
done
# Delete initscripts first
rm %{buildroot}%{_initddir}/*
# Install systemd units or initscripts
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
install -m 755 -t %{buildroot}%{_sbindir} %{name}
install -d %{buildroot}%{_unitdir}
install -m 644 -t %{buildroot}%{_unitdir} %{name}.service
%else
install -m 755 %{name}.sysvinit %{buildroot}%{_initddir}/%{name}
%endif

%files
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/psk
%dir %{_sysconfdir}/%{name}/cert
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%config(noreplace) %{_sysconfdir}/%{name}/local-test.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/transport_ike.conf
%config(noreplace) %{_sysconfdir}/%{name}/transport_kink.conf
%config(noreplace) %{_sysconfdir}/%{name}/tunnel_ike.conf
%config(noreplace) %{_sysconfdir}/%{name}/tunnel_ike_natt.conf
%config(noreplace) %{_sysconfdir}/%{name}/tunnel_kink.conf
%config(noreplace) %{_sysconfdir}/%{name}/vals.conf
%dir %{_sysconfdir}/%{name}/hook
%{_sysconfdir}/%{name}/hook/child-down
%{_sysconfdir}/%{name}/hook/child-rekey
%{_sysconfdir}/%{name}/hook/child-up
%{_sysconfdir}/%{name}/hook/child-up.d/00childup_sample
%config(noreplace) %{_sysconfdir}/%{name}/hook/functions
%{_sysconfdir}/%{name}/hook/ikesa-down
%{_sysconfdir}/%{name}/hook/ikesa-rekey
%{_sysconfdir}/%{name}/hook/ikesa-up
%{_sysconfdir}/%{name}/hook/ikesa-up.d/00ikesaup_sample
%{_sysconfdir}/%{name}/hook/migration
%{_sysconfdir}/%{name}/hook/ph1-down
%{_sysconfdir}/%{name}/hook/ph1-up
%{_sbindir}/%{name}-iked
%{_sbindir}/%{name}-pskgen
%{_sbindir}/%{name}-spmd
%{_sbindir}/%{name}-spmdctl
%dir %{_var}/run/%{name}
%{_mandir}/man8/%{name}-iked.8.gz
%{_mandir}/man8/%{name}-pskgen.8.gz
%{_mandir}/man8/%{name}-spmd.8.gz
%{_mandir}/man8/%{name}-spmdctl.8.gz
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%else
%{_initddir}/%{name}
%endif

%post
if [ ! -e "%{_sysconfdir}/%{name}/spmd.pwd" ]; then
    pwgen > %{_sysconfdir}/%{name}/spmd.pwd
    chmod 600 %{_sysconfdir}/%{name}/spmd.pwd
fi
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

%preun
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ] ; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%systemd_postun_with_restart apache-httpd.service 
%else
%endif

%changelog
* Thu Sep 17 2020 Petr Pisar <ppisar@redhat.com> - 20100526a-44
- Stop including unused sysctl.h that was removed from glibc-2.32 (bug #1856775)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-43
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Petr Pisar <ppisar@redhat.com> - 20100526a-39
- Add missing build dependencies (bug #1606070)
- Adapt to OpenSSL 1.1.1 (bug #1606070)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20100526a-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Pavel Šimerda <psimerda@redhat.com> - 20100526a-28
- #995743 - avoid recently added dependency

* Wed Feb 19 2014 Pavel Šimerda <psimerda@redhat.com> - 20100526a-27
- #995745 - /etc/racoon2/psk and /etc/racoon2/cert references in vals.conf are not created
- #995743 - racoon2-genpsk missing dependancies

* Mon Feb 17 2014 Pavel Šimerda <psimerda@redhat.com> - 20100526a-26
- #955458 - hardened build
- fix build failure by reconfiguring spmd subdirectory

* Mon Feb 17 2014 Pavel Šimerda <psimerda@redhat.com> - 20100526a-25
- #914426 - fix build failure affecting Fedora >= 18

* Tue Jan 07 2014 Pavel Šimerda <psimerda@redhat.com> - 20100526a-24
- #850290 - use systemd-rpm macros

* Thu Sep 12 2013 Pavel Šimerda <psimerda@redhat.com> - 20100526a-23
- prefix init script daemon names with /racoon2-/ (#1006613, patch by Grant Hammond)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20100526a-21
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Pavel Šimerda <psimerda@redhat.com> - 20100526a-19
- Fix racoon2 script to call prefixed binaries

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100526a-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-17
- Prefix binaries with racoon2-

* Tue Feb 14 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-16
- Fixed systemd dependencies
- Switched to a single systemd unit or single initscript

* Tue Feb 14 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-15
- Expand tabs in config files for better readability

* Mon Feb 13 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-14
- rebuilt

* Sat Jan 21 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-13
- Added rm at the beginning of install section
- Changed conditionals to versioned ones

* Sun Jan 15 2012 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-12
- Removed sysvinit subpackage
- Added conditionals to handle different init systems
- Changed initrd macro to initd
- Marked functions as config file

* Fri Dec 30 2011 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-11
- Removed -fno-strict-aliasing
- Removed -D_GNU_SOURCE=1
- Added rationale for --disable-kinkd and --disable-pedant
- Removed @prefix@ from configuration files (patch)

* Thu Dec 29 2011 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-10
- Added pwgen dependency
- Moved various inline fixes from specfile to patches
- Fixed racoon2 configuration path (/etc/racoon2)

* Wed Dec 07 2011 Pavel Šimerda <pavlix@pavlix.net> - 20100526a-9
- Incorporated more rpmlint feedback
- Directories are now specified by macros
- Added systemd scriptlets
- Added needed /var/run/racoon2 directory
- Added directories to files section

* Wed Nov 09 2011 pavlix - 20100526a-8
- Incorporated rpmlint feedback

* Wed Nov 09 2011 pavlix - 20100526a-7
- Experimental build for packaging
