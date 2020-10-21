Name:		ufdbGuard
Version:	1.35.1
Release:	1%{?dist}
Summary:	A URL filter for squid
URL:		https://www.urlfilterdb.com/
License:	GPLv2

Source0:	https://www.urlfilterdb.com/files/downloads/%{name}-%{version}.tar.gz
Source1:	ufdbGuard.service
Source2:	ufdbGuard.logrotate

%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without tmpfiles
%else
%bcond_with    tmpfiles
%endif

BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: perl-interpreter 
BuildRequires: gcc
%if %{?rhel:7}%{!?rhel:0}
%{?systemd_requires}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif
BuildRequires: openssl-devel
Requires(pre): shadow-utils
Requires: logrotate

%description
ufdbGuard is a free URL filter for Squid with additional features like
SafeSearch enforcement for a large number of search engines, safer HTTPS 
visits and dynamic detection of proxies (URL filter circumventors).

ufdbGuard supports free and commercial URL databases that can be
downloaded from various sites and vendors.
You can also make your own URL database for ufdbGuard.

%prep
%setup -q

iconv -c --to-code=UTF-8 CHANGELOG > CHANGELOG.new
mv CHANGELOG.new CHANGELOG

%build
INSTALL_PROGRAM=./install-sh %configure \
	--with-ufdb-user=ufdb \
	--prefix=%{_prefix} \
	--with-ufdb-bindir=%{_sbindir} \
	--with-ufdb-piddir=%{_localstatedir}/run/ufdbguard \
	--with-ufdb-mandir=%{_mandir} \
	--with-ufdb-images_dir=%{_sharedstatedir}/ufdbguard/images \
	--with-ufdb-logdir=%{_localstatedir}/log/ufdbguard \
	--with-ufdb-samplesdir=%{_sharedstatedir}/ufdbguard/samples \
	--with-ufdb-config=%{_sysconfdir}/ufdbguard \
	--with-ufdb-dbhome=%{_sharedstatedir}/ufdbguard/blacklists \
	--with-ufdb-imagesdir=%{_sharedstatedir}/ufdbguard/images

%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}%{_sysconfdir}/ufdbguard
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
%make_install INSTALL="../install-sh -c"
for i in $(find doc/ -type f -name '*.1'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man1/
done
for i in $(find doc/ -type f -name '*.8'); do
    install -p -D -m 0644 $i %{buildroot}%{_mandir}/man8/
done

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/ufdbGuard.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/ufdbGuard

rm -rf %{buildroot}%{_sysconfdir}/rc.d/init.d/ufdb

#remove sysinit file
rm -rf %{buildroot}%{_sysconfdir}/init.d

#remove ufdbsignal as it's setuid.
rm -f %{buildroot}%{_sbindir}/ufdbsignal

mkdir -p %{buildroot}%{_var}/run/ufdbguard
%if %{with tmpfiles}
# Setup tmpfiles.d config for the above
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
echo 'd /var/run/ufdbguard 0750 ufdb ufdb -' > \
    %{buildroot}/usr/lib/tmpfiles.d/ufdbGuard.conf
%endif


%pre
getent group ufdb >/dev/null || groupadd -r ufdb
getent passwd ufdb >/dev/null || \
    useradd -r -g ufdb -d /var/lib/ufdbguard -s /sbin/nologin \
    -c "ufdbGuard URL filter" ufdb
exit 0

%post
%systemd_post ufdbGuard.service

%preun
%systemd_preun ufdbGuard.service

%postun
%systemd_postun_with_restart ufdbGuard.service


%files
%license COPYING GPL
%doc README CHANGELOG CREDITS
%config(noreplace) %{_sysconfdir}/sysconfig/ufdbguard
%config(noreplace) %dir %{_sysconfdir}/ufdbguard/
%config(noreplace) %{_sysconfdir}/ufdbguard/*
%config(noreplace) %{_sysconfdir}/logrotate.d/ufdbGuard
%{_sbindir}/*
%{_mandir}/man1/ufdb*
%{_mandir}/man8/ufdb*
%dir %{_sharedstatedir}/ufdbguard/
%attr(-, ufdb, ufdb) %dir %{_localstatedir}/log/ufdbguard/
%{_sharedstatedir}/ufdbguard/*
%{_unitdir}/ufdbGuard.service
%attr(-, ufdb, ufdb) %dir %{_var}/run/ufdbguard/
%if %{with tmpfiles}
%config(noreplace) %{_tmpfilesdir}/ufdbGuard.conf
%endif

%changelog
* Thu Oct 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.35.1-1
- 1.35.1

* Wed Sep 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-3
- Correct logrotate configure.

* Fri Aug 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-2
- Correct sysconfig file placement.
- Fix tmpfiles config.

* Mon Aug 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.6-1
- 1.34.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.5-2
- Review fixes.

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.34.5-1
- Initial package.
