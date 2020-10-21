# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate tokio-util

Name:           rust-%{crate}0.2
Version:        0.2.0
Release:        2%{?dist}
Summary:        Additional utilities for working with Tokio

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-util
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Additional utilities for working with Tokio.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+codec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+codec-devel %{_description}

This package contains library source intended for building other packages
which use "codec" feature of "%{crate}" crate.

%files       -n %{name}+codec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages
which use "full" feature of "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+udp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+udp-devel %{_description}

This package contains library source intended for building other packages
which use "udp" feature of "%{crate}" crate.

%files       -n %{name}+udp-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 22:54:46 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package
