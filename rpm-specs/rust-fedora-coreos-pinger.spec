# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate fedora-coreos-pinger

Name:           rust-%{crate}
Version:        0.0.4
Release:        7%{?dist}
Summary:        Telemetry service for Fedora CoreOS

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/fedora-coreos-pinger
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  systemd-rpm-macros

%global _description %{expand:
Telemetry service for Fedora CoreOS.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/fedora-coreos-pinger
%license LICENSE
%{_unitdir}/fedora-coreos-pinger.service
%dir %{_sysconfdir}/fedora-coreos-pinger
%dir %{_sysconfdir}/fedora-coreos-pinger/config.d
%attr(0775, fedora-coreos-pinger,fedora-coreos-pinger) %dir /run/fedora-coreos-pinger
%attr(0775, fedora-coreos-pinger,fedora-coreos-pinger) %dir /run/fedora-coreos-pinger/config.d
%dir %{_prefix}/lib/fedora-coreos-pinger
%dir %{_prefix}/lib/fedora-coreos-pinger/config.d
%{_prefix}/lib/fedora-coreos-pinger/config.d/10-default-enable.toml
%{_tmpfilesdir}/fedora-coreos-pinger.conf
%{_sysusersdir}/50-fedora-coreos-pinger.conf

%post        -n %{crate}
%systemd_post fedora-coreos-pinger.service

%preun       -n %{crate}
%systemd_preun fedora-coreos-pinger.service

%postun      -n %{crate}
%systemd_postun_with_restart fedora-coreos-pinger.service

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_unitdir} \
  dist/systemd/*.service
mkdir -p %{buildroot}%{_sysconfdir}/fedora-coreos-pinger/config.d
mkdir -p %{buildroot}/run/fedora-coreos-pinger/config.d
mkdir -p %{buildroot}%{_prefix}/lib/fedora-coreos-pinger/config.d
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/fedora-coreos-pinger/config.d \
  dist/config.d/*.toml
install -Dpm0644 -t %{buildroot}%{_sysusersdir} \
  dist/sysusers.d/*.conf
install -Dpm0644 -t %{buildroot}%{_tmpfilesdir} \
  dist/tmpfiles.d/*.conf

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Sep 23 2020 Kelvin Fan <kfan@redhat.com> - 0.0.4-7
- Remove unnecessary usage of systemd RPM macro in %pre

* Sun Aug 16 15:01:25 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.0.4-6
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 8 2020 Robert Fairley <rfairley@redhat.com> - 0.0.4-4
- Bump release to have latest build retagged into f32, so a Bodhi
  update for a non-modular build can be opened (https://github.com/coreos/fedora-coreos-tracker/issues/525)
- Regenerate using rust2rpm 15

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Robert Fairley <rfairley@redhat.com> - 0.0.4-1
- Initial import (#1728378)
