%global user_group ircd


Name:       ircd-ratbox
Version:    3.0.10
Release:    6%{?dist}
Summary:    Ircd-ratbox is an advanced, stable and fast ircd

License:    GPLv2

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool-ltdl-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd

%{?systemd_requires}
Requires(pre):  shadow-utils

URL:        https://www.ratbox.org/
Source0:    %{url}/download/%{name}-%{version}.tar.bz2
Source1:    ircd.service
Source2:    ircd.sysconfig
Source3:    ircd.fedora.conf
Source4:    ircd.logrotate
Source5:    ircd.tmpfiles.d.conf

Patch0000:  %{name}-3.0.10-gcc_format-security_fix.patch
Patch0001:  %{name}-3.0.10-crypt-null-pointer-dereference.patch
Patch0002:  %{name}-3.0.10-gnutls3.patch

Conflicts:  ircd-hybrid

%description
%{name} is an advanced, stable, fast ircd. It is an evolution where
ircd-hybrid left off around version 7-rc1. It supports the TS3 and TS5
protocols, and is used on EFnet and other IRC networks.


%package mkpasswd
Summary:    Password hash generator for ircd-ratbox
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description mkpasswd
Ircd-mkpasswd is a password hash generator for ircd-ratbox.


%prep
%autosetup -p 1

%{__sed} -i \
    -e 's|#servlink_path = "/usr/local/ircd/bin/servlink";|servlink_path = "%{_bindir}/servlink";|' \
    -e 's|/usr/local/ircd/modules|%{_datadir}/ircd/modules|g' \
    -e 's|/usr/local/ircd/etc/|%{_sysconfdir}/ircd|g' \
    -e 's|"logs/|"%{_var}/log|g' \
    doc/example.*conf

sed 's/-Werror//g' -i configure


%build
%configure \
    --with-helpdir=%{_datadir}/ircd \
    --with-moduledir=%{_datadir}/ircd/modules \
    --with-confdir=%{_sysconfdir}/ircd \
    --with-logdir=%{_var}/log/ircd \
    --enable-ipv6 \
    --enable-openssl \
    --enable-zlib \
    --with-nicklen=32 \
    --with-topiclen=350 \
    --enable-small-net \
    --enable-services
%make_build


%install
mkdir -p %{buildroot}%{_sysconfdir}/ircd \
         %{buildroot}/run/%{name} \
         %{buildroot}%{_var}/log/ircd
%make_install
install -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/ircd.service
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/ircd
install -D -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/ircd/ircd.conf
install -D -m664 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/ircd
install -D -m644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/ircd.conf
mv %{buildroot}%{_datadir}/ircd-old/modules %{buildroot}%{_datadir}/ircd/modules
rm -fr %{buildroot}%{_datadir}/ircd-old
find %{buildroot} -type f -name '*.la' -delete -print


%pre
getent group ircd  >/dev/null || groupadd -r ircd
getent passwd ircd >/dev/null || \
useradd -r -g ircd -d /run/%{name} -s /sbin/nologin \
    -c "%{name} user" ircd


%post
%systemd_post ircd.service


%preun
%systemd_preun ircd.service


%postun
%systemd_postun_with_restart ircd.service


%triggerun -- %{name} < 2.2.8-9
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply ircd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ircd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ircd >/dev/null 2>&1 || :
/bin/systemctl try-restart ircd.service >/dev/null 2>&1 || :


%files
%doc BUGS ChangeLog* INSTALL README.FIRST RELNOTES SVN-Access doc/*
%license CREDITS LICENSE
%{_bindir}/bantool
%{_bindir}/ircd
%{_bindir}/ratbox-sqlite3
%{_datadir}/ircd*
%{_libdir}/libcore.so*
%{_libdir}/libratbox.so*
%{_libexecdir}/%{name}
%dir %{_sysconfdir}/ircd
%config(noreplace) %{_sysconfdir}/ircd/*
%{_sysconfdir}/sysconfig/ircd
%{_unitdir}/ircd.service
%{_tmpfilesdir}/ircd.conf
%dir %attr(750,ircd,ircd) %{_var}/log/ircd
%dir %attr(750,ircd,ircd) /run/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/ircd


%files mkpasswd
%{_bindir}/ratbox-mkpasswd


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.10-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.10-2
- Re-add mkpasswd sub-package

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 3.0.11-1
- Update to 3.0.10 (#950360)
- Fix FTBFS (#1555892, #1604384)
- Modernize spec-file
- Drop mkpasswd package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.9-9
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Nils Philippsen <nils@redhat.com> - 2.2.9-1
- fix build with -Werror=format-security (#1037135)
- build hardened executables (#955164)

* Fri Feb 21 2014 Nils Philippsen <nils@redhat.com> - 2.2.9-1
- version 2.2.9
- remove obsolete offbyone patch
- use working upstream and source URLs
- tidy up inconsistent and trailing whitespace
- add tmpfile.d configuration and adapt systemd service file (#1030161)
- use systemd macros (#850170)
- don't list files twice, mark all configuration as %%config(noreplace)
- don't specify %%defattr and BuildRoot
- change ircd user home directory to /run/ircd-ratbox
- fix systemd requirements

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Lubomir Rintel <lkundrak@v3.sk> - 2.2.8-11
- Own ircd homedir, SELinux would disallow creating it during installation

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 2.2.8-9
- Migrate to systemd, BZ 789704.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.8-6
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.8-3
- rebuild with new openssl

* Wed Aug 27 2008 Marek Mahut <mmahut@fedoraproject.org> - 2.2.8-2
- Initial package build
