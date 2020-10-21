%if 0%{?with_snapshot}
%global gitdate              20201013
%global portable_commit      dce7298652497d00442a6c7d595a4f9f0a43cf47
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       9c4b11c1c1baf41daf64436e73ce014c562a4aea
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        OpenBGPD Routing Daemon
Name:           openbgpd
Version:        6.8p0
Release:        1%{?with_snapshot:.git%{gitdate}}%{?dist}
# OpenBGPD itself is ISC but uses other source codes, breakdown:
# BSD: include/{sha2_openbsd,siphash,util,vis}.h and compat/{fmt_scaled,setproctitle,sha2,siphash,vis}.c
# BSD with advertising: include/net/pfkeyv2.h
# Public Domain: include/{endian,sha2,stdlib,string,unistd}.h and compat/{{explicit_bzero,getrtable}.c,chacha_private.h}
License:        ISC and BSD and BSD with advertising and Public Domain
URL:            http://www.openbgpd.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenBGPD/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-BA3DA14FEE657A6D7931C08EC755429BA6A969A8.gpg
%else
Source0:        https://github.com/openbgpd-portable/openbgpd-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/openbgpd-portable/openbgpd-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        openbgpd.service
Source4:        openbgpd.tmpfilesd
# Adjust path of Validated ROA Payloads (VRP) for rpki-client
Patch0:         openbgpd-6.7p0-rpki-client.patch
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bison
%endif
BuildRequires:  gcc
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
Requires(pre):  shadow-utils
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
Recommends:     rpki-client
%else
Requires:       rpki-client
%endif

%description
OpenBGPD is a free implementation of the Border Gateway Protocol (BGP),
Version 4. It allows ordinary machines to be used as routers exchanging
routes with other systems speaking the BGP protocol.

This is the portable version and it does not have the means to influence
kernel routing tables. It is only suitable for route servers/collectors.

%prep
%if !0%{?with_snapshot}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%else
%setup -q -n %{name}-portable-%{portable_commit}
tar xfz %{SOURCE1}
mv -f %{name}-openbsd-%{openbsd_commit} openbsd
./autogen.sh
%endif
%patch0 -p1 -b .rpki-client
touch -c -r bgpd.conf{.rpki-client,}

%build
%if 0%{?fedora} > 31
# https://github.com/openbgpd-portable/openbgpd-portable/issues/8
export CFLAGS="$RPM_OPT_FLAGS -fcommon"
%endif
%configure --with-privsep-user=bgpd
# Workaround until autoconf generated './configure' supports '--runstatedir=/run/bgpd' option
sed -e 's|^\(runstatedir =\).*|\1 %{_rundir}/bgpd|g' -i {.,compat,include,src/{bgpctl,bgpd}}/Makefile
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir}/empty,%{_rundir}}/bgpd/
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/bgpd.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf

%pre
getent group bgpd > /dev/null || %{_sbindir}/groupadd -r bgpd
getent passwd bgpd > /dev/null || %{_sbindir}/useradd -r -g bgpd -d %{_localstatedir}/empty/bgpd -s /sbin/nologin -c "Privilege-separated BGP" bgpd
exit 0

%post
%systemd_post bgpd.service

%preun
%systemd_preun bgpd.service

%postun
%systemd_postun_with_restart bgpd.service

%files
%license LICENSE
%doc AUTHORS README.md
%config(noreplace) %attr(0640,root,bgpd) %{_sysconfdir}/bgpd.conf
%dir %attr(0750,root,bgpd) %{_sysconfdir}/bgpd/
%{_unitdir}/bgpd.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/bgpctl
%{_sbindir}/bgpd
%{_mandir}/man5/bgpd.conf.5*
%{_mandir}/man8/bgpctl.8*
%{_mandir}/man8/bgpd.8*
%dir %attr(0755,root,root) %{_rundir}/bgpd/
%dir %attr(0711,root,root) %{_localstatedir}/empty/bgpd/

%changelog
* Tue Oct 20 2020 Robert Scheck <robert@fedoraproject.org> 6.8p0-1
- Upgrade to 6.8p0 (#1889826)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7p0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-2
- Changes to match the Fedora Packaging Guidelines (#1835023 #c2)

* Tue May 19 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-1
- Upgrade to 6.7p0

* Wed May 13 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-0.1.git20200512
- Upgrade to 6.7p0 (GIT 20200512)

* Thu Apr 30 2020 Robert Scheck <robert@fedoraproject.org> 6.6p0-1
- Upgrade to 6.6p0 (#1835023)
- Initial spec file for Fedora and Red Hat Enterprise Linux
