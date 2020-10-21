# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate vte_generate_state_changes

Name:           rust-%{crate}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Proc macro for generating VTE state changes

# Upstream license specification: Apache-2.0 OR MIT
# https://github.com/alacritty/vte/pull/66
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/vte_generate_state_changes
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Proc macro for generating VTE state changes.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Thu Aug 27 16:49:48 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.1-1
- Initial package
