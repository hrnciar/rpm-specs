# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate testing_logger

Name:           rust-%{crate}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Supports writing tests to verify `log` crate calls

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/testing_logger
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Supports writing tests to verify `log` crate calls.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
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
* Sun May 17 13:07:10 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.1-1
- Initial package
