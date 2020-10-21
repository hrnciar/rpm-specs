Summary:          Gluster block storage utility
Name:             gluster-block
Version:          0.5
Release:          3%{?dist}
License:          GPLv2 or LGPLv3+
URL:              https://github.com/gluster/gluster-block
Source0:          https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:    pkgconfig(glusterfs-api)
BuildRequires:    pkgconfig(json-c)
BuildRequires:    help2man >= 1.36
BuildRequires:    libtirpc-devel
BuildRequires:    rpcgen
BuildRequires:    systemd
# tarball releases require running ./autogen.sh
BuildRequires:    automake, autoconf, libtool, git

Requires:         tcmu-runner >= 1.1.3
Requires:         targetcli >= 2.1.fb49
Requires:         python3-rtslib >= 2.1.fb69
Requires:         rpcbind

%{?systemd_requires}

%description
gluster-block is a CLI utility, which aims at making gluster backed block
storage creation and maintenance as simple as possible.

%prep
%autosetup -p 1

%build
echo %{version} > VERSION
./autogen.sh
%configure
%make_build

%install
%make_install
touch %{buildroot}%{_sharedstatedir}/gluster-block/gb_upgrade.status

%post
%systemd_post gluster-block-target.service
%systemd_post gluster-blockd.service

%preun
%systemd_preun gluster-block-target.service
%systemd_preun gluster-blockd.service

%postun
%systemd_postun_with_restart gluster-block-target.service
%systemd_postun_with_restart gluster-blockd.service

%files
%license COPYING-GPLV2 COPYING-LGPLV3
%doc README.md
%{_sbindir}/gluster-block
%{_sbindir}/gluster-blockd
%doc %{_mandir}/man8/gluster-block*.8*
%{_unitdir}/gluster-blockd.service
%{_unitdir}/gluster-block-target.service
%config(noreplace) %{_sysconfdir}/sysconfig/gluster-blockd
%config(noreplace) %{_sysconfdir}/logrotate.d/gluster-block
%{_libexecdir}/gluster-block
%dir %{_localstatedir}/log/gluster-block
%dir %{_sharedstatedir}/gluster-block
%ghost %{_sharedstatedir}/gluster-block/gb_upgrade.status
%config(noreplace) %{_sharedstatedir}/gluster-block/gluster-block-caps.info

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Niels de Vos <devos@fedoraproject.org> - 0.5-1
- Update to gluster-block 0.5

* Sat May 2 2020 Niels de Vos <devos@fedoraproject.org> - 0.4-8
- Use Python3 for rtslib (#1830514)

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.4-7
- Rebuild (json-c)

* Tue Apr 14 2020 Björn Esser <besser82@fedoraproject.org> - 0.4-6
- Rebuilt (glusterfs-7.4)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 3 2019 Niels de Vos <devos@fedoraproject.org> - 0.4-3
- Update runtime dependency versions for tcmu-runner, targetcli and rtslib

* Fri May 3 2019 Niels de Vos <devos@fedoraproject.org> - 0.4-2
- Correct the filename of the logrotate configuration

* Fri May 3 2019 Niels de Vos <devos@fedoraproject.org> - 0.4-1
- Update to version 0.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.3-5
- Add patch to build against libtirpc-devel instead glibc-rpc
- Add needed BR: rpcgen, libtirpc-devel

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.3-4
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.3-2
- Rebuilt for libjson-c.so.3

* Mon Nov 06 2017 Prasanna Kumar Kalever <prasanna.kalever@redhat.com> - 0.3-1
- Update to 0.3

* Wed Sep 13 2017 Niels de Vos <ndevos@redhat.com> - 0.2.1-2
- use pkgconfig for BuildRequires
- run setup in quiet mode
- run make_* macros instead of make commands in build/install section
- drop the INSTALL file from the documentation

* Fri Jun 30 2017 Niels de Vos <ndevos@redhat.com> - 0.2.1-1
- initial packaging, based on upstream .spec
- prevent ./autogen.sh'd need for git to determine the version
- added systemd macros in the scriptlets
