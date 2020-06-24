# Generated by rust2rpm 15
%bcond_without check
%global __cargo_skip_build 0

%global crate choosier

Name:           rust-%{crate}
Version:        0.1.0
Release:        3%{?dist}
Summary:        Choose your browser based on the URL given

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/choosier
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
BuildRequires:  /usr/bin/desktop-file-validate
%endif

%global _description %{expand:
Choose your browser based on the URL given.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# MIT or ASL 2.0
# MPLv2.0
License:        MPLv2.0 and (MIT or ASL 2.0)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.txt
%doc README.md examples
%{_bindir}/choosier
%{_datadir}/applications/choosier.desktop
%dir %{_sysconfdir}/choosier/
%ghost %config(noreplace) %{_sysconfdir}/choosier/choosier.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_datadir}/applications assets/choosier.desktop
mkdir -p %{buildroot}%{_sysconfdir}/choosier

%if %{with check}
%check
%cargo_test
desktop-file-validate %{buildroot}%{_datadir}/applications/choosier.desktop
%endif

%changelog
* Sun Jun 14 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.0-3
- Restore examples

* Sun Jun 14 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Tidy up installation

* Sun Jun 07 18:20:05 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.0-1
- Initial package