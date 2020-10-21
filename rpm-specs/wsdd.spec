Name:           wsdd
Version:        0.6.1
Release:        3%{?dist}
Summary:        Web Services Dynamic Discovery host daemon
License:        MIT 
URL:            https://github.com/christgau/wsdd 
Source0:        https://github.com/christgau/wsdd/archive/v%{version}/wsdd-%{version}.tar.gz
Source1:        wsdd.service
Source2:        wsdd.xml
Source3:        wsdd-http.xml
Source4:        wsdd.sysconfig
BuildArch:      noarch
BuildRequires:  systemd
Requires(pre):  shadow-utils


%description
wsdd implements a Web Service Discovery host daemon. This enables (Samba)
hosts, like your local NAS device, to be found by Web Service Discovery Clients
like Windows.


%prep
%autosetup


%install
install -pDm644 %{S:1} %{buildroot}%{_unitdir}/wsdd.service
install -pDm644 %{S:2} %{buildroot}%{_usr}/lib/firewalld/services/wsdd.xml
install -pDm644 %{S:3} %{buildroot}%{_usr}/lib/firewalld/services/wsdd-http.xml
install -pDm644 %{S:4} %{buildroot}%{_sysconfdir}/sysconfig/wsdd
install -pDm644 man/wsdd.1 %{buildroot}%{_mandir}/man1/wsdd.1
install -pDm755 src/wsdd.py %{buildroot}%{_bindir}/wsdd


%pre
getent group wsdd >/dev/null || groupadd -r wsdd
getent passwd wsdd >/dev/null || \
    useradd -r -g wsdd -d / -s /sbin/nologin \
    -c "%{summary}" wsdd
exit 0

%post
%systemd_post wsdd.service

%preun
%systemd_preun wsdd.service

%postun
%systemd_postun_with_restart wsdd.service

%files
%{_unitdir}/wsdd.service
%{_usr}/lib/firewalld/services/wsdd.xml
%{_usr}/lib/firewalld/services/wsdd-http.xml
%config(noreplace) %{_sysconfdir}/sysconfig/wsdd
%{_bindir}/wsdd
%{_mandir}/man1/wsdd.1*
%license LICENSE
%doc AUTHORS README.md


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Sam P <survient@fedoraproject.org> - 0.6.1-2
- Added fixes from rh#1858858

* Mon Jul 13 2020 Sam P <survient@fedoraproject.org> - 0.6.1-1
- Updated to upstream latest release

* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 0.5-2
- Removed unnecessary build dependency

* Thu Feb 20 2020 Sam P <survient@fedoraproject.org> - 0.5-1
- Updated to latest upstream release

* Wed Dec 11 2019 Sam P <survient@fedoraproject.org> - 0.4-2
- Added systemd unit scriptlet sections

* Tue Nov 19 2019 Sam P <survient@fedoraproject.org> - 0.4-1
- Initial package
