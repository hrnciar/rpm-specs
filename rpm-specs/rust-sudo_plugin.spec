# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate sudo_plugin

Name:           rust-%{crate}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Macros to easily write custom sudo plugins

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/sudo_plugin
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macros to easily write custom sudo plugins.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE
%doc CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Mar 26 09:20:50 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 09:48:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
