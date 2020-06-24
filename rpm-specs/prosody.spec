%if 0%{?fedora} > 19 && 0%{?fedora} <= 30
%global lua_version 5.1
%else
%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%endif

%global sslcert    %{_sysconfdir}/pki/%{name}/localhost.crt
%global sslkey     %{_sysconfdir}/pki/%{name}/localhost.key

Summary:           Flexible communications server for Jabber/XMPP
Name:              prosody
Version:           0.11.5
Release:           1%{?dist}
License:           MIT
URL:               https://prosody.im/
Source0:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz
Source1:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz.asc
Source2:           gpgkey-32A9EDDE3609931EB98CEAC315907E8E7BDD6BFE.gpg
Source3:           prosody.init
Source4:           prosody.logrotate-init
Source5:           prosody.service
Source6:           prosody.logrotate-service
Source7:           prosody.tmpfilesd
Source8:           prosody-localhost.cfg.lua
Source9:           prosody-example.com.cfg.lua
Patch0:            prosody-0.11.0-config.patch
Patch1:            prosody-0.11.4-lua53.patch
BuildRequires:     gcc, libidn-devel, openssl-devel
BuildRequires:     gnupg2
Requires:          %{_bindir}/openssl
Requires(pre):     shadow-utils
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
Requires(post):    systemd, %{_bindir}/openssl
Requires(preun):   systemd
Requires(postun):  systemd
BuildRequires:     systemd
%else
Requires(post):    /sbin/chkconfig, %{_bindir}/openssl
Requires(preun):   /sbin/service, /sbin/chkconfig
Requires(postun):  /sbin/service
%endif
%if 0%{?fedora} > 19 && 0%{?fedora} <= 30
Requires:          compat-lua, lua-filesystem-compat, lua5.1-bitop
Requires:          lua-expat-compat, lua-socket-compat, lua-sec-compat
BuildRequires:     compat-lua, compat-lua-devel
%else
%if 0%{?rhel} > 6 || 0%{?fedora} > 15
Requires:          lua(abi) = %{lua_version}
%else
Requires:          lua >= %{lua_version}
%endif
Requires:          lua-filesystem, lua-expat, lua-socket, lua-sec
%if 0%{?rhel} >= 6 && 0%{?rhel} <= 7
Requires:          lua-bitop
%endif
BuildRequires:     lua, lua-devel
%endif

%description
Prosody is a flexible communications server for Jabber/XMPP written in Lua.
It aims to be easy to use, and light on resources. For developers it aims
to be easy to extend and give a flexible system on which to rapidly develop
added functionality, or prototype new protocols.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch0 -p1 -b .config
%patch1 -p1 -b .lua53

%build
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
%if 0%{?fedora} > 19 && 0%{?fedora} <= 30
  --lua-version=%{lua_version} \
  --with-lua-include=%{_includedir}/lua-%{lua_version} \
%endif
  --add-cflags="$RPM_OPT_FLAGS" \
%if 0%{?rhel} > 6 || 0%{?fedora}
  --add-ldflags="$RPM_LD_FLAGS" \
%else
  --add-ldflags="$RPM_LD_FLAGS -lrt" \
%endif
  --no-example-certs
make %{?_smp_mflags}

# Make prosody-migrator
make -C tools/migration %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_localstatedir}/{lib,log}/%{name}}/
make DESTDIR=$RPM_BUILD_ROOT install

# Install prosody-migrator
make -C tools/migration DESTDIR=$RPM_BUILD_ROOT install

# Install ejabberd2prosody
install -p -m 755 tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
sed -e 's@;../?.lua@;%{_libdir}/%{name}/util/?.lua;%{_libdir}/%{name}/?.lua;@' \
%if 0%{?fedora} > 19 && 0%{?fedora} <= 30
  -e '1s@ lua$@ lua-%{lua_version}@' \
%endif
  -i $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
touch -c -r tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
install -p -m 644 tools/erlparse.lua $RPM_BUILD_ROOT%{_libdir}/%{name}/util/

# Move certificates directory and symlink it
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs/ $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs

# Install systemd/tmpfiles or initscript files
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
install -D -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT/run/%{name}/
%else
install -D -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
install -D -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}/
sed -e 's@/run@%{_localstatedir}/run@' -i $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/prosody.cfg.lua
%endif

# Keep configuration file timestamp
touch -c -r prosody.cfg.lua.dist.config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/prosody.cfg.lua

# Install virtual host configuration
install -D -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/localhost.cfg.lua
install -D -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/example.com.cfg.lua

# Fix permissions for rpmlint
chmod 755 $RPM_BUILD_ROOT%{_libdir}/%{name}/util/*.so

# Fix incorrect end-of-line encoding
sed -e 's/\r//g' -i doc/stanza.txt doc/session.txt doc/roster_format.txt

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "Prosody XMPP Server" %{name}
exit 0

%post
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

if [ ! -f %{sslkey} ]; then
  umask 077
  %{_bindir}/openssl genrsa 4096 > %{sslkey} 2> /dev/null
  chown root:%{name} %{sslkey}
  chmod 640 %{sslkey}
fi

if [ ! -f %{sslcert} ]; then
  FQDN=`hostname`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi

  %{_bindir}/openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj "/C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  chmod 644 %{sslcert}
fi

%preun
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ne 0 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi
%endif

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS CHANGES HACKERS README doc/*
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}-migrator
%{_bindir}/ejabberd2prosody
%{_libdir}/%{name}/
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/pki/%{name}/*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.cfg.lua
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/*.cfg.lua
%attr(0750,root,%{name}) %{_sysconfdir}/%{name}/certs
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?rhel} > 6 || 0%{?fedora} > 17
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755,%{name},%{name}) /run/%{name}/
%else
%{_sysconfdir}/rc.d/init.d/%{name}
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/run/%{name}/
%endif
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%{_mandir}/man1/%{name}*.1*

%changelog
* Mon Apr 06 2020 Robert Scheck <robert@fedoraproject.org> 0.11.5-1
- Upgrade to 0.11.5 (#1816855)

* Mon Feb 10 2020 Robert Scheck <robert@fedoraproject.org> 0.11.4-1
- Upgrade to 0.11.4 (#1792635)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Robert Scheck <robert@fedoraproject.org> 0.11.3-1
- Upgrade to 0.11.3 (#1756953)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Robert Scheck <robert@fedoraproject.org> 0.11.2-1
- Upgrade to 0.11.2

* Thu Nov 29 2018 Robert Scheck <robert@fedoraproject.org> 0.11.1-1
- Upgrade to 0.11.1

* Mon Nov 19 2018 Robert Scheck <robert@fedoraproject.org> 0.11.0-1
- Upgrade to 0.11.0

* Sun Aug 19 2018 Robert Scheck <robert@fedoraproject.org> 0.10.2-3
- Don't attempt to reload during logrotate if prosody is stopped

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Robert Scheck <robert@fedoraproject.org> 0.10.2-1
- Upgrade to 0.10.2 (#1584801)
- Changed log rotation from weekly/52 to local system defaults

* Tue May 15 2018 Robert Scheck <robert@fedoraproject.org> 0.10.1-1
- Upgrade to 0.10.1 (#1578371)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Robert Scheck <robert@fedoraproject.org> 0.10.0-1
- Upgrade to 0.10.0 (#1497877)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Robert Scheck <robert@fedoraproject.org> 0.9.12-1
- Upgrade to 0.9.12 (#1412102)

* Mon Nov 07 2016 Robert Scheck <robert@fedoraproject.org> 0.9.11-1
- Upgrade to 0.9.11 (#1391802)

* Sun Apr 17 2016 Robert Scheck <robert@fedoraproject.org> 0.9.10-3
- Added runtime requirement to %%{_bindir}/openssl (#1319227)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Robert Scheck <robert@fedoraproject.org> 0.9.10-1
- Upgrade to 0.9.10 (#1302463)

* Tue Jan 12 2016 Robert Scheck <robert@fedoraproject.org> 0.9.9-2
- Added upstream patch to open /dev/urandom read-only

* Fri Jan 08 2016 Robert Scheck <robert@fedoraproject.org> 0.9.9-1
- Upgrade to 0.9.9 (#1296983, #1296984)

* Sun Sep 27 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-6
- Fixed shebang for ejabberd2prosody
- Backported support for IPv6 DNS servers (#1256677)

* Sun Aug 23 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-5
- Start after network-online.target not network.target (#1256062)

* Wed Jul 15 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-4
- Change default CA paths to /etc/pki/tls/certs(/ca-bundle.crt)

* Wed Jul 01 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-3
- Fixed the wrong logrotate configuration to not use a wildcard

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 18 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-1
- Upgrade to 0.9.8 (#1152126)

* Sat Feb 14 2015 Robert Scheck <robert@fedoraproject.org> 0.9.7-1
- Upgrade to 0.9.7 (#985563, #1152126)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jan Kaluza <jkaluza@redhat.com> - 0.9.4-2
- add missing lua-socket-compat dependency

* Fri May 30 2014 Jan Kaluza <jkaluza@redhat.com> - 0.9.4-1
- update to version 0.9.4
- build with luajit

* Wed Sep 11 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.1-1
- Update to 0.9.1

* Thu Aug 22 2013 Matěj Cepl <mcepl@redhat.com> - 0.9.0-1
- Final upstream release.

* Wed Aug 07 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.5.rc5
- Update to 0.9.0rc5

* Fri Jun 21 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.4.rc4
- Update to 0.9.0rc4

* Fri Jun 21 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.3.rc3
- Update to 0.9.0rc3

* Fri Jun 07 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.2.rc2
- Update to 0.9.0rc2

* Wed May 15 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.0-0.1.beta1
- update to 0.9.0beta1, rebuild for lua 5.2

* Sat Apr 27 2013 Robert Scheck <robert@fedoraproject.org> - 0.8.2-9
- Apply wise permissions to %%{_sysconfdir}/%%{name} (#955384)
- Apply wise permissions to default SSL certificates (#955380)
- Do not ship %%{_sysconfdir}/%%{name}/certs by default (#955385)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 27 2012 Johan Cwiklinski <johan At x-tnd DOt be> 0.8.2-7
- Use systemd-rpm macros, bz #850282

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-5
- Missing rhel %%ifs
- Change the way SSL certificate is generated

* Sun May 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-4
- ghost %%{_localstatedir}/run/%%{name}

* Sun May 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-3
- Add missing requires
- Add rhel %%ifs

* Mon Mar 05 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-2
- Switch to systemd for Fedora >= 15, keep sysv for EPEL builds
- Remove some macros that should not be used

* Thu Jun 23 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-1.trashy
- 0.8.2

* Tue Jun 7 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.1-1.trashy
- 0.8.1

* Sun May 8 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-3.trashy
- tmpfiles.d configuration for F-15

* Sat Apr 16 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-2.trashy
- Now requires lua-dbi

* Fri Apr 8 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-1.trashy
- 0.8.0

* Sun Jan 23 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-4.trashy
- Redefine _initddir and _sharedstatedir marcos for EL-5

* Sat Dec 11 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-3
- Apply ssl patch before sed on libdir; to avoid a patch context issue 
  building on i686 

* Sat Sep 11 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-2
- No longer ships default ssl certificates, generates one at install

* Wed Jul 14 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-1
- Update to 0.7.0

* Wed Apr 28 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.6.2-1
- Update to 0.6.2

* Thu Dec 31 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 0.6.1-1
- Initial packaging
