# Run tests in check section
%bcond_without check

# https://github.com/Yubico/yubihsm-connector
%global goipath         github.com/Yubico/yubihsm-connector
Version:                2.2.0
%global tag             %{version}

%gometa

%global common_description %{expand:
Backend to talk to YubiHSM 2}

Name:           yubihsm-connector
Release:        2%{?dist}
Summary:        YubiHSM Connector

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        %{gosource}.sig
Source2:        gpgkey-D7CE1455.gpg

%{?systemd_requires}
Requires(pre):  shadow-utils
BuildRequires:  systemd-rpm-macros
#BuildRequires:  git
BuildRequires:  golang(github.com/google/gousb)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/kardianos/service)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/sirupsen/logrus/hooks/syslog)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  gnupg2
Recommends:     yubihsm-shell

%description
%{common_description}

%gopkg

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%goprep

%build
export GO111MODULE=off
sed -i "s| -mod=vendor||" main.go
go generate
%gobuild -o %{gobuilddir}/bin/yubihsm-connector %{goipath}

%install
install -Dpm 0755 %{gobuilddir}/bin/yubihsm-connector %{buildroot}%{_bindir}/yubihsm-connector
install -Dpm 0644  deb/yubihsm-connector.yaml %{buildroot}%{_sysconfdir}/yubihsm-connector.yaml
install -Dpm 0644  deb/yubihsm-connector.service %{buildroot}%{_unitdir}/yubihsm-connector.service
install -Dpm 0644  deb/70-yubihsm-connector.rules %{buildroot}%{_udevrulesdir}/70-yubihsm-connector.rules

%if %{with check}
%check
%gocheck
%endif

%pre
getent group yubihsm-connector >/dev/null || groupadd -r yubihsm-connector
getent passwd yubihsm-connector >/dev/null || \
    useradd -r -g yubihsm-connector -M -s /sbin/nologin \
    -c "YubiHSM connector account" yubihsm-connector \
    --system
exit 0

%post
%systemd_post yubihsm-connector.service

%preun
%systemd_preun yubihsm-connector.service

%postun
%systemd_postun_with_restart yubihsm-connector.service

%files
%license LICENSE
%{_bindir}/yubihsm-connector
%config(noreplace) %{_sysconfdir}/yubihsm-connector.yaml
%{_unitdir}/yubihsm-connector.service
%{_udevrulesdir}/70-yubihsm-connector.rules

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Jakub Jelen <jjelen@redhat.com> - 2.2.0-1
- New upstream release (#1788637)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#1788637)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-2
- Update to latest Go macros

* Thu Jan 31 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.0-1
- First package for Fedora
