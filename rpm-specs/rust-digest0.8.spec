# Generated by rust2rpm 15
%bcond_with check
%global debug_package %{nil}

%global crate digest

Name:           rust-%{crate}0.8
Version:        0.8.1
Release:        1%{?dist}
Summary:        Traits for cryptographic hash functions

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/digest
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Traits for cryptographic hash functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+blobby-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blobby-devel %{_description}

This package contains library source intended for building other packages
which use "blobby" feature of "%{crate}" crate.

%files       -n %{name}+blobby-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dev-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev-devel %{_description}

This package contains library source intended for building other packages
which use "dev" feature of "%{crate}" crate.

%files       -n %{name}+dev-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Wed Jun 24 11:21:37 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Initial package