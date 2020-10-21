
%if 0%{?fedora} || 0%{?rhel} > 7
# Explicity require python3 on Fedora to help track which packages 
# no longer need python2.
%global use_python3 1
%else
%global use_python3 0
%endif

Name:		acme-tiny
Version:	4.1.0
Release:	4%{?dist}
Summary:	Tiny auditable script to issue, renew Let's Encrypt certificates

License:	MIT
URL:		https://github.com/diafygi/%{name}
Source0:	https://github.com/diafygi/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	acme-tiny-sign.sh
Source2:	cert-check.py
Source3:	acme.conf
Source6:	acme-tiny.timer
Source7:	acme-tiny.service
Source8:	README-fedora.md
# simple script hook to kick services when cert is updated
Source9:	notify.sh

Requires(pre): shadow-utils
# systemd macros are not defined unless systemd is present
BuildRequires: systemd
%{?systemd_requires}
Requires: %{name}-core = %{version}-%{release}
BuildArch:	noarch
%if 0%{?fedora}
Suggests: httpd, mod_ssl, nginx
Enhances: httpd, mod_ssl, nginx
%endif

%description
This is a tiny, auditable script that you can throw on your server to issue and
renew Let's Encrypt certificates. Since it has to be run on your server and
have access to your private Let's Encrypt account key, I tried to make it as
tiny as possible (currently less than 200 lines). The only prerequisites are
python and openssl.  

Well, that and a web server - but then you only need this with a web server.
This package adds a simple directory layout and timer service that runs
acme_tiny on installed CSRs as the acme user for privilege separation.

%package core
Summary: core python module of acme-tiny
Requires:	openssl
%if 0%{?rhel} >= 5 && 0%{?rhel} < 7
# EL6 uses python2.6, which does not include argparse
Requires:	python-argparse
%endif
BuildArch: noarch

%description core
Includes only the core acme_tiny.py script and its dependencies.
Alternate frameworks that use acme_tiny.py can install this to avoid pulling in
unneeded packages.

%prep
%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE8} .
sed -i.orig -e '1,1 s,^.*python$,#!/usr/bin/python,' acme_tiny.py
%if %{use_python3}
sed -i.old -e '1,1 s/python$/python3/' *.py
%endif

%build

%install
mkdir -p %{buildroot}/var/www/challenges
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/acme/{private,csr,certs}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/notify.d
chmod 0700 %{buildroot}%{_sharedstatedir}/acme/private

install -m 0755 acme-tiny-sign.sh %{buildroot}%{_libexecdir}/%{name}/sign
install -m 0755 acme_tiny.py %{buildroot}%{_sbindir}/acme_tiny
ln -sf acme_tiny %{buildroot}%{_sbindir}/%{name}
ln -sf %{_libexecdir}/%{name}/sign %{buildroot}%{_sbindir}/acme-tiny-sign
install -m 0755 cert-check.py %{buildroot}%{_sbindir}/cert-check
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0755 %{SOURCE9} %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE6} %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE7} %{buildroot}%{_unitdir}

%pre
getent group acme > /dev/null || groupadd -r acme
getent passwd acme > /dev/null || /usr/sbin/useradd -g acme \
	-c "Tiny Auditable ACME Client" \
	-r -d %{_sharedstatedir}/acme -s /sbin/nologin acme
exit 0

%post
%systemd_post acme-tiny.service acme-tiny.timer

%postun
%systemd_postun_with_restart acme-tiny.service acme-tiny.timer

%preun
%systemd_preun acme-tiny.service acme-tiny.timer

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README-fedora.md
%attr(0755,acme,acme) /var/www/challenges
%attr(-,acme,acme) %{_sharedstatedir}/acme
%{_libexecdir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/acme.conf
%{_unitdir}/*
%{_sbindir}/acme-tiny-sign
%{_sbindir}/cert-check
%{_sbindir}/%{name}
%{_sysconfdir}/%{name}

%files core
%license LICENSE
%doc README.md
%{_sbindir}/acme_tiny

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr  9 2020 Stuart D. Gathman <stuart@gathman.org> 4.1.0-3
- Update README-fedora.md to describe notify.sh
- Apply selected changes from Marcel Metz <mmetz@adrian-broher.net>:
- Use openssl x509 -checkend parameter to determine certificate expiration
- Remove Let's Encrypt intermediate certificate
- Remove cron job used on non systemd systems

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 Tim Jackson <rpm@timj.co.uk> - 4.1.0-1
- Update to 4.1.0

* Fri Oct 11 2019 Stuart D. Gathman <stuart@gathman.org> 4.0.4-5
- Add generic notify script for incron

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Stuart D. Gathman <stuart@gathman.org> 4.0.4-1
- Official upstream release! BZ#1560531
- Move acme_tiny.py to acme-tiny-core subpackage BZ#1438181

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4.20170516gitaf025f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Stuart D. Gathman <stuart@gathman.org> 0.2-3.20170616gitaf025f5
- BZ#1507333 EL6 missing python-argparse dependency
- BZ#1515781 Agreement updated.
- BZ#1409345 Unwritable certs silently skipped

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2.20170516gitaf025f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul  6 2017 Stuart D. Gathman <stuart@gathman.org> 0.2-1.20170616gitaf025f5
- BZ#1468045 Update to new upstream version
- BZ#1409686 Message.getallmatchingheaders() is broken in python3.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20160810git5a7b4e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-11.20160810git5a7b4e7
- Rebuild for Python 3.6

* Mon Aug 22 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-10.20160810git5a7b4e7
- Fix cert writable check in sign script
- More tips in README-fedora.md

* Mon Aug 22 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-9.20160810git5a7b4e7
- Use %%{systemd_requires}
- Remove unneeded cronie, python dependencies
- Add acme-tiny.timer to systemd scriptlets
- Add README-fedora.md
- acme_tiny: Fix --chain patch for python2.6 (el6)
- acme_tiny: Suppress traceback on error

* Sun Aug 21 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-8
- Add use_systemd flag to use systemd timer and enable on Fedora and epel7
- Enable use_python3 flag for Fedora (but not epel7).

* Sat Aug 20 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-7
- sign: Actually use the new --chain flag
- cron: Make days to expiration explicit
- spec: Set file modes with install
- acme.conf: mark as config

* Fri Aug 19 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-6
- Python3 fixes for cert-check
- acme-tiny: Update patch to leave default behavior unchanged
- make /var/lib/acme readable by all except private

* Thu Aug 11 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-5
- sign: Use tmp output to avoid wiping existing cert on error
- acme_tiny: get intermediate cert from acme protocol

* Thu Aug 11 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-4
- Fix path of acme_tiny and make days explicit in sign script
- Add crontab

* Wed Aug 10 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-3
- Add global acme httpd conf
- Append intermediate certs, add current lets-encrypt intermediate cert

* Tue Aug  9 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-2
- add private, csr, certs directories
- add sign script suitable for cron

* Mon Aug  8 2016 Stuart D. Gathman <stuart@gathman.org> 0.1-1
- Initial RPM
