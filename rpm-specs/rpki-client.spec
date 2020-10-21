%if 0%{?with_snapshot}
%global gitdate              20201011
%global portable_commit      927f4a597d25c244e292570c6edd65064425507e
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       f865ccea0af41e99c3c13fbfbee3fdca6362e193
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        RPKI validator to support BGP Origin Validation
Name:           rpki-client
Version:        6.8p0
Release:        1%{?with_snapshot:.git%{gitdate}}%{?dist}
# rpki-client itself is ISC but uses other source codes, breakdown:
# BSD: include/{sys/{queue,tree},sha2_openbsd}.h and src/main.c
# Public Domain: include/{sys/{types,_null},sha2,unistd,string,stdlib,poll}.h and compat/explicit_bzero.c
License:        ISC and BSD and Public Domain
URL:            https://www.rpki-client.org/
%if !0%{?with_snapshot}
Source0:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/rpki-client/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-B5B6416FEA6DDA05EA562A9FCB987F2783972FF9.gpg
%else
Source0:        https://github.com/rpki-client/rpki-client-portable/archive/%{portable_commit}/%{name}-portable-%{version}-%{portable_shortcommit}.tar.gz
Source1:        https://github.com/rpki-client/rpki-client-openbsd/archive/%{openbsd_commit}/%{name}-openbsd-%{version}-%{openbsd_shortcommit}.tar.gz
%endif
Source3:        TALs.md
%if !0%{?with_snapshot}
BuildRequires:  gnupg2
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires:  gcc
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel >= 1.1.0
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  rsync
Requires:       rsync
Requires(pre):  shadow-utils

%description
The OpenBSD rpki-client is a free, easy-to-use implementation of the
Resource Public Key Infrastructure (RPKI) for Relying Parties (RP) to
facilitate validation of the Route Origin of a BGP announcement. The
program queries the RPKI repository system, downloads and validates
Route Origin Authorisations (ROAs) and finally outputs Validated ROA
Payloads (VRPs) in the configuration format of OpenBGPD, BIRD, and
also as CSV or JSON objects for consumption by other routing stacks.

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
cp -pf %{SOURCE3} .

%build
%configure \
%if 0%{?rhel} && 0%{?rhel} < 8
  --with-openssl=openssl11 \
%endif
  --with-user=%{name} \
  --with-tal-dir=%{_sysconfdir}/pki/tals \
  --with-base-dir=%{_localstatedir}/cache/%{name} \
  --with-output-dir=%{_localstatedir}/lib/%{name}
%make_build

%install
%make_install

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "OpenBSD RPKI validator" %{name}
exit 0

%files
%license LICENSE
%doc AUTHORS README.md TALs.md
%{_sbindir}/%{name}
%{_sysconfdir}/pki/tals/
%{_mandir}/man8/%{name}.8*
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/lib/%{name}/

%changelog
* Tue Oct 20 2020 Robert Scheck <robert@fedoraproject.org> 6.8p0-1
- Upgrade to 6.8p0 (#1889618)

* Wed Jul 29 2020 Robert Scheck <robert@fedoraproject.org> 6.7p1-1
- Upgrade to 6.7p1 (#1861137)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7p0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-1
- Upgrade to 6.7p0 (#1837150)

* Sun Apr 19 2020 Robert Scheck <robert@fedoraproject.org> 6.6p2-1
- Upgrade to 6.6p2

* Tue Apr 14 2020 Robert Scheck <robert@fedoraproject.org> 6.6p1-1
- Upgrade to 6.6p1

* Sun Apr 05 2020 Robert Scheck <robert@fedoraproject.org> 0.3.0-2
- Apply fixes from upstream (rebase to commit 87683e9)

* Mon Feb 24 2020 Robert Scheck <robert@fedoraproject.org> 0.3.0-1
- Upgrade to 0.3.0 (#1806049)
- Install bundled Trust Anchor Locators (TALs)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jun 19 2019 Robert Scheck <robert@fedoraproject.org> 0.2.0-1
- Upgrade to 0.2.0 (#1745770)
- Initial spec file for Fedora and Red Hat Enterprise Linux
