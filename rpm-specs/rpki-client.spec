%if 0%{?with_snapshot}
%global gitdate              20200518
%global portable_commit      9fd28531d42a31c6a362e6607363d796ea1c9b0d
%global portable_shortcommit %(c=%{portable_commit}; echo ${c:0:7})
%global openbsd_commit       24126e9d30629312790021d0537b2086f70c749c
%global openbsd_shortcommit  %(c=%{openbsd_commit}; echo ${c:0:7})
%endif

Summary:        RPKI client implementation
Name:           rpki-client
Version:        6.7p0
Release:        1%{?with_snapshot:.git%{gitdate}}%{?dist}
License:        ISC
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
rpki-client is an implementation of RPKI (Resource Public Key
Infrastructure), specified by RFC 6480. It implements the client
side of RPKI, which is responsible for downloading, validating
and converting ROAs (Route Origin Authorisations) into VRPs
(Validated ROA Payloads). The client's output (VRPs) can be used
to perform BGP Origin Validation (RFC 6811).

The design focus of rpki-client is simplicity and security. To
wit, it implements RPKI components necessary for validating route
statements and omits superfluities (such as, for example, which
X509 certificate sections must be labelled "Critical").

%prep
%if !0%{?with_snapshot}
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
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
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "RPKI client" %{name}
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
* Mon May 18 2020 Robert Scheck <robert@fedoraproject.org> 6.7p0-1
- Upgrade to 6.7p0

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
