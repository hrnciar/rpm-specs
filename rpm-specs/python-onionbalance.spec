%global pypi_name OnionBalance
%global pkgname onionbalance
%global sum Load-balancing for Tor onion services

%global toruser toranon

Name:           python-%{pkgname}
Version:        0.2.0
Release:        2%{?dist}
Summary:        %{sum}

License:        GPLv3
URL:            https://onionbalance.readthedocs.io
Source0:        %pypi_source
Source1:        onionbalance.service
Source2:        onionbalance.tmpfiles
Source3:        onionbalance.logrotate
Source5:        onionbalance.torrc.example
Source6:        README.fedora

BuildArch: noarch

BuildRequires: systemd-units

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-stem >= 1.8
BuildRequires:  python3-PyYAML >= 4.2b1
BuildRequires:  python3-cryptography >= 2.5
BuildRequires:  python3-crypto >= 2.6.1
BuildRequires:  python3-future >= 0.14.3
BuildRequires:  python3-setproctitle >= 1.1.9

BuildRequires: systemd


%global _description %{expand:
OnionBalance provides load-balancing and redundancy for Tor
onion services by distributing requests to multiple back-end
Tor instances.}

%description %_description

%package -n python3-%{pkgname}
Summary:   %{sum}
Requires:  python3-setuptools
Requires:  python3-stem >= 1.8
Requires:  python3-PyYAML >= 4.2b1
Requires:  python3-crypto
Requires:  python3-cryptography >= 2.5
Requires:  python3-future >= 0.14.3
Requires:  python3-setproctitle >= 1.1.9
%{?python_provide:%python_provide python3-%{pkgname}}
Requires: tor
Requires: logrotate
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

install -d        %{buildroot}/etc/logrotate.d
install -d        %{buildroot}/%{_sysconfdir}/%{pkgname}
install -d        %{buildroot}/%{_localstatedir}/log/%{pkgname}
install -d        %{buildroot}/%{_localstatedir}/lib/%{pkgname}
install -d -m 755 %{buildroot}/%{_unitdir}
install -d -m 755 %{buildroot}/%{_tmpfilesdir}

install -p -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{pkgname}.service
install -p -m 644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{pkgname}.conf
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{pkgname}.conf
%if 0%{?with_docs}
install -d -m 755 %{buildroot}/%{_mandir}/man1
cp docs/_build/man/%{pkgname}* %{buildroot}/%{_mandir}/man1/
%endif

install -p -m 644 %{SOURCE5} .
install -p -m 644 %{SOURCE6} .

%pre -n python3-%{pkgname}
getent passwd %{pkgname} >/dev/null || \
    useradd -r -g %{toruser} -d %{_localstatedir}/lib/%{pkgname} -s /sbin/nologin \
    -c "%{pkgname} daemon user" %{pkgname}
exit 0

%post -n python3-%{pkgname}
%systemd_post onionbalance.service

%preun -n python3-%{pkgname}
%systemd_preun onionbalance.service

%postun -n python3-%{pkgname}
%systemd_postun_with_restart onionbalance.service

%files -n python3-%{pkgname}
%doc README.rst
%doc README.fedora
%doc onionbalance.torrc.example
%license COPYING
%if 0%{?with_docs}
%doc docs/_build/html
%doc %attr(0644,root,root) %{_mandir}/man1/%{pkgname}*
%endif
%if 0%{?for_el7}
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_bindir}/%{pkgname}
%{_bindir}/%{pkgname}-config
%{_unitdir}/%{pkgname}.service
%{_tmpfilesdir}/%{pkgname}.conf
%dir %attr(0750,root,%{toruser}) %{_sysconfdir}/%{pkgname}
%dir %attr(0750,%{pkgname},%{toruser}) %{_localstatedir}/log/%{pkgname}
%dir %attr(0750,%{pkgname},%{toruser}) %{_localstatedir}/lib/%{pkgname}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{pkgname}.conf

%changelog
* Tue Jun 02 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.9

* Thu May 28 2020 Marcel Haerry <mh+fedora@scrit.ch> - 0.2.0-1
- Upgraded to 0.2.0 - new upstream - new HSv3 support
- Fixing build (bz#1792059)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Marcel Haerry <mh+fedora@scrit.ch - 0.1.8-10
- Fixing building on Python 3.8 (Fixes bz#1736518)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Marcel Haerry <mh+fedora@scrit.ch> - 0.1.8-6
- Fixed tmpfiles unit file

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Marcel Haerry <mh+fedora@scrit.ch> - 0.1.8-1
- latest upstream release (#1447661)

* Thu Feb 23 2017 Marcel Haerry <mh+fedora@scrit.ch> - 0.1.7-1
- latest upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Marcel Haerry <mh+fedora@scrit.ch> - 0.1.6-1
  initial release
