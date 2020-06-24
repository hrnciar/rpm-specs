%{!?_rundir:%global _rundir %%{_localstatedir}/run}

Summary: A client for signing certificates with an ACME server
Name: dehydrated
Version: 0.6.5
Release: 3%{?dist}
License: MIT
URL: https://github.com/lukas2511/dehydrated
Source0: https://github.com/lukas2511/dehydrated/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: dehydrated.tmpfiles
Requires: openssl
Requires: curl
Requires: sed
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: systemd
%endif
BuildArch: noarch

%description
This is a client for signing certificates with an ACME-server (currently
only provided by Let's Encrypt) implemented as a relatively simple bash-
script. Dehydrated supports both ACME v1 and the new ACME v2 including
support for wildcard certificates!

Current features:
* Signing of a list of domains
* Signing of a CSR
* Renewal if a certificate is about to expire or SAN (subdomains) changed
* Certificate revocation

%prep
%setup -q

%build
: nothing to do

%install
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/accounts
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/archive
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/certs
mkdir -p %{buildroot}%{_sysconfdir}/dehydrated/conf.d
mkdir -p %{buildroot}%{_rundir}/dehydrated
%if 0%{?fedora} || 0%{?rhel} >= 7
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/dehydrated.conf
%endif
sed \
    -e 's|^#LOCKFILE="\${BASEDIR}/lock"|LOCKFILE="%{_rundir}/dehydrated/lock"|' \
    -e 's|^#CONFIG_D=|CONFIG_D="\${BASEDIR}/conf.d"|' \
    -e 's|^#HOOK=|HOOK="\${BASEDIR}/hook.sh"|' \
    -e 's|^#PRIVATE_KEY_RENEW="yes"|PRIVATE_KEY_RENEW="no"|' \
    docs/examples/config >%{buildroot}%{_sysconfdir}/dehydrated/config
install -p docs/examples/hook.sh %{buildroot}%{_sysconfdir}/dehydrated/
install -D -p -m 0755 dehydrated %{buildroot}%{_bindir}/dehydrated
install -D -p -m 0644 docs/man/dehydrated.1 %{buildroot}%{_mandir}/man1/dehydrated.1
rm -rf docs/man/

%post
if [ ! -f %{_sysconfdir}/cron.d/dehydrated ]; then
    echo "$(($RANDOM % 60)) $(($RANDOM % 6)) * * $(($RANDOM % 7)) root test -s %{_sysconfdir}/dehydrated/domains.txt && %{_bindir}/dehydrated --cron" \
	>%{_sysconfdir}/cron.d/dehydrated
fi
umask=$(umask)
umask 027
if [ -z "$(ls %{_sysconfdir}/dehydrated/conf.d/*.sh 2>/dev/null)" ]; then
    touch %{_sysconfdir}/dehydrated/conf.d/local.sh
fi
if [ ! -e %{_sysconfdir}/dehydrated/domains.txt ]; then
    touch %{_sysconfdir}/dehydrated/domains.txt
fi
umask ${umask} || :

%files
%doc README.md docs/*
%license LICENSE
%attr(0644,root,root) %ghost %{_sysconfdir}/cron.d/dehydrated
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/dehydrated/config
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/dehydrated/hook.sh
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/accounts
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/archive
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/certs
%attr(0750,root,root) %dir %{_sysconfdir}/dehydrated/conf.d
%attr(0640,root,root) %ghost %{_sysconfdir}/dehydrated/conf.d/local.sh
%attr(0640,root,root) %ghost %{_sysconfdir}/dehydrated/domains.txt
%attr(0750,root,root) %dir %{_rundir}/dehydrated
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_tmpfilesdir}/dehydrated.conf
%endif
%{_bindir}/dehydrated
%{_mandir}/man1/dehydrated.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Paul Wouters <pwouters@redhat.com> - 0.6.5-1
- Resolves: rhbz#1723766 Updated to 0.6.5

* Tue Jun 25 2019 Robert Scheck <robert@fedoraproject.org> - 0.6.4-1
- Upgrade to 0.6.4 (#1723766)
- Update source link

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Robert Scheck <robert@fedoraproject.org> - 0.6.2-1
- Resolves: rhbz#1572609 Updated to 0.6.2

* Sat Mar 31 2018 Robert Scheck <robert@fedoraproject.org> - 0.6.1-1
- Resolves: rhbz#1554153 Updated to 0.6.1 with ACME v2 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Paul Wouters <pwouters@redhat.com> - 0.5.0-1
- Resolves: rhbz#1534189 dehydrated-0.5.0 is available

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Paul Wouters <pwouters@redhat.com> - 0.4.0-5
- Include license with proper macros

* Mon Mar 20 2017 Paul Wouters <pwouters@redhat.com> - 0.4.0-4
- Set PRIVATE_KEY_RENEW=no so pubkeys are re-used, allowing TLSA DNS records

* Sat Mar 18 2017 Tuomo Soini <tis@foobar.fi> - 0.4.0-3
- Fix file mode of crontab entry

* Sat Mar 18 2017 Kim B. Heino <b@bbbs.net> - 0.4.0-2
- Add archive directory, cleanup

* Sat Mar 18 2017 Tuomo Soini <tis@foobar.fi> - 0.4.0-1
- Initial build
