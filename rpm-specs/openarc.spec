%global systemd (0%{?fedora} >= 18) || (0%{?rhel} >= 7)
%global tmpfiles (0%{?fedora} >= 15) || (0%{?rhel} >= 7)

%global pre_rel Beta3

Summary: An open source library and milter for providing ARC service
Name: openarc
Version: 1.0.0
Release: %{?pre_rel:0.}8%{?pre_rel:.%pre_rel}%{?dist}
License: BSD and Sendmail
URL: https://github.com/trusteddomainproject/OpenARC

Source0: https://github.com/trusteddomainproject/OpenARC/archive/v%{version}%{?pre_rel:.%pre_rel}/%{name}-%{version}%{?pre_rel:.%pre_rel}.tar.gz

BuildRequires: libtool gcc
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(jansson)

# sendmail-devel renamed for F25+
%if 0%{?fedora} > 25
BuildRequires: sendmail-milter-devel
%else
BuildRequires: sendmail-devel
%endif

BuildRequires: autoconf
BuildRequires: automake

Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: libopenarc = %{version}-%{release}
Requires(pre): shadow-utils
%if %systemd
# Required for systemd
%{?systemd_requires}
BuildRequires: systemd
%else
# Required for SysV
Requires(post): chkconfig
Requires(preun): chkconfig, initscripts
%endif


%description
The Trusted Domain Project is a community effort to develop and maintain a
C library for producing ARC-aware applications and an open source milter for
providing ARC service through milter-enabled MTAs.

%package -n libopenarc
Summary: An open source ARC library

%description -n libopenarc
This package contains the library files required for running services built
using libopenarc.

%package -n libopenarc-devel
Summary: Development files for libopenarc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n libopenarc-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopenarc.

%prep
%autosetup -n OpenARC-rel-openarc-1-0-0-Beta3 -p1


%build
autoreconf --install
%configure --disable-static
%make_build

%install
%make_install
mkdir -p -m 0700 %{buildroot}%{_sysconfdir}/%{name}
mkdir -p -m 0750 %{buildroot}%{_rundir}/%{name}
rm -r %{buildroot}%{_prefix}/share/doc/openarc
rm %{buildroot}/%{_libdir}/*.la


cat > %{buildroot}%{_sysconfdir}/openarc.conf <<EOF
## See openarc.conf(5) or %{_docdir}/%{name}%{?rhel:-%{version}}/openarc.conf.sample for more
PidFile %{_rundir}/%{name}/%{name}.pid
Syslog  yes
UserID  openarc:openarc
Socket  local:%{_rundi}/%{name}/%{name}.sock
SignHeaders to,subject,message-id,date,from,mime-version,dkim-signature
PeerList %{_sysconfdir}/%{name}/PeerList
MilterDebug 6
EnableCoredumps yes

## After setting Mode to "sv", running
## opendkim-genkey -D %{_sysconfdir}/openarc -s key -d `hostname --domain`
## and putting %{_sysconfdir}/openarc
#Mode                    sv
#Canonicalization        relaxed/simple
#Domain                  example.com # change to domain
#Selector                key
#KeyFile                 %{_sysconfdir}/openarc/key.private
#SignatureAlgorithm rsa-sha256
EOF

# Don't sign or validate connections from localhost
cat > %{buildroot}%{_sysconfdir}/%{name}/PeerList <<EOF
127.0.0.1/32
[::1]/128
EOF
chmod 0640 %{buildroot}%{_sysconfdir}/%{name}/PeerList

%if %systemd
install -d -m 0755 %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/%{name}.service << 'EOF'
[Unit]
Description=Authenticated Receive Chain (ARC) Milter
Documentation=man:%{name}(8) man:%{name}.conf(5) http://www.trusteddomain.org/%{name}/
After=network.target nss-lookup.target syslog.target

[Service]
Type=forking
PIDFile=%{_rundir}/%{name}/%{name}.pid
EnvironmentFile=-%{_sysconfdir}/sysconfig/%{name}
ExecStart=/usr/sbin/%{name} $OPTIONS
ExecReload=/bin/kill -USR1 $MAINPID
User=%{name}
Group=%{name}
UMask=0007
ProtectSystem=strict
ProtectHome=true

[Install]
WantedBy=multi-user.target
EOF
%else
mkdir -p %{buildroot}%{_initrddir}
install -m 0755 contrib/init/redhat/%{name} %{buildroot}%{_initrddir}/%{name}
%endif

%if %{tmpfiles}
install -p -d %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
D %{_rundir}/%{name} 0750 %{name} %{name} -
EOF
%endif

%pre
if ! getent passwd %{name} >/dev/null 2>&1; then
    %{_sbindir}/useradd -M -d %{_localstatedir}/lib/%{name} -r -s /sbin/nologin %{name}
    if ! getent group %{name} >/dev/null; then
        %{_sbindir}/groupadd %{name}
        %{_sbindir}/usermod -g %{name} %{name}
    fi
    if getent group mail >/dev/null; then
        %{_sbindir}/usermod -G mail %{name}
    fi
fi
exit 0


%post

%if %systemd
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name} || :
%endif


%preun
%if %systemd
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
    service %{name} stop >/dev/null || :
    /sbin/chkconfig --del %{name} || :
fi
exit 0
%endif

%ldconfig_scriptlets -n libopenarc

%files
%license LICENSE LICENSE.Sendmail
%doc README RELEASE_NOTES %{name}/%{name}.conf.sample
%dir %attr(0755,root,%{name}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0644,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %attr(0440,%{name},%{name}) %{_sysconfdir}/%{name}/PeerList

%if %{tmpfiles}
%{_tmpfilesdir}/%{name}.conf
%else
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%endif

%if %{systemd}
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif
%{_mandir}/*/*
%{_sbindir}/*


%files -n libopenarc
%license LICENSE LICENSE.Sendmail
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.0

%files -n libopenarc-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Apr 21 2020 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.8.Beta3
- packaging suggestions from
  https://github.com/trusteddomainproject/OpenARC/pull/103#issuecomment-574367733
- use systemd service ProtectHome and ProtectSystem

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.7.Beta3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.0.0-0.7.Beta3
- Remove obsolete requirement for %%postun scriptlet

* Mon Dec  2 2019 Matt Domsch <mdomsch@fedoraproject.org> - 1.0.0-0.6.Beta3
- Upstream beta3
- Add dependency on janusson-devel, needed for new SealHeaderChecks config option

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.Beta2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Matt Domsch <matt@domsch.com - 1.0.0-0.1.Beta2
- Upstream beta2, drop merged patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.1.Beta1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.1.Beta1
- Upstream beta1

* Sat Sep 22 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.4.Beta0
- fix ownership of openarc.conf and PeerList files

* Sat Sep 22 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.3.Beta0
- replace header generation patch with upstream fix
- apply specfile fixes from https://github.com/trusteddomainproject/OpenARC/pull/103

* Mon Sep 10 2018 Matt Domsch <matt@domsch.com> 1.0.0-0.2.Beta0
- Own /etc/openarc/
- improve default config file, add default PeerList config

* Wed Jul 11 2018 Xavier Bachelot <xavier@bachelot.org> 1.0.0-0.1.Beta0
- Specfile clean up.
- Update to 1.0.0 beta 0.

* Sun Jul 23 2017  Matt Domsch <matt@domsch.com> 0.1.0-1
- update to Fedora Packaging Guidelines
