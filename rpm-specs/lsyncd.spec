%global _hardened_build 1
%global commit0 cce7db5ebd352690917792848c2aea92c08efdd5
%global gittag0 release-2.2.2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		lsyncd
Version:	2.2.2
Release:	11%{?dist}
Summary:	File change monitoring and synchronization daemon
License:	GPLv2+
URL:		https://github.com/axkibe/lsyncd
Source0:	https://github.com/axkibe/%{name}/archive/%{gittag0}.tar.gz#/release-%{version}.tar.gz

Patch0:		docpath.patch

Source1:	lsyncd.service
Source2:	lsyncd.init
Source3:	lsyncd.sysconfig
Source4:	lsyncd.logrotate
Source5:	lsyncd.conf

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	lua-devel >= 5.1.3
BuildRequires:	asciidoc
BuildRequires:	cmake
BuildRequires:  systemd
Requires:	lua
Requires:	rsync
%{?systemd_requires}

%description
Lsyncd watches a local directory trees event monitor interface (inotify).
It aggregates and combines events for a few seconds and then spawns one
(or more) process(es) to synchronize the changes. By default this is
rsync.

Lsyncd is thus a light-weight live mirror solution that is comparatively
easy to install not requiring new file systems or block devices and does
not hamper local file system performance.

%prep
%autosetup -n %{name}-%{gittag0}

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -d -m 0755 %{buildroot}%{_var}/log/%{name}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/lsyncd
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/lsyncd
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/lsyncd.service

%check
ctest -V %{?_smp_mflags}

%post
%systemd_post lsyncd.service

%preun
%systemd_preun lsyncd.service

%postun
%systemd_postun_with_restart lsyncd.service

%files
%license COPYING
%doc ChangeLog examples
%doc %{_mandir}/man1/lsyncd.1.*
%config(noreplace) %{_sysconfdir}/lsyncd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/lsyncd
%config(noreplace) %{_sysconfdir}/logrotate.d/lsyncd
%{_bindir}/lsyncd
%dir %{_var}/log/%{name}
%{_unitdir}/lsyncd.service

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.2.2-6
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Jason Taylor <jtfas90@gmail.com> - 2.2.2-1
- updated to latest upstream (resolves #1415295)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Jason Taylor <jtfas90@gmail.com> - 2.2.1-1
- updated to latest upstream (resolves #1383855)
- updated lsyncd.service (resolves #1369274 #1383855)
- updated to github home page and source

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 18 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.1.5-7
- Remove unnecessary service restart in logrotate (Troy C., #915873)
- Enable hardening (#955203)

* Tue Nov 18 2014 Lubomir Rintel <lkundrak@v3.sk> - 2.1.5-6
- Fix bad shell argument escaping

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.5-4
- No prelink on aarch64/ppc64le

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 2.1.5-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Wed Oct  9 2013 Martin Langhoff <martin@laptop.org> - 2.1.5-1
- New upstream version
- adds rsync options: bwlimit, timeout
- several upstream fixes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Paul Wouters <pwouters@redhat.com> - 2.1.4-3
- Comment out the LSYNCD_OPTIONS options per default, it accidentally
  caused the options from the initscript/systemd service to ignored

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Paul Wouters <pwouters@redhat.com> - 2.1.4-1
- Merged in changes of rhbz#805849
- Fixed URL/Source
- Upgraded systemd macros

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 2.0.4-1
- Initial packaging
