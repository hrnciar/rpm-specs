# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate alacritty_terminal

Name:           rust-%{crate}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Library for writing terminal emulators

# Upstream license specification: Apache-2.0
# License PR: https://github.com/alacritty/alacritty/pull/4316
License:        ASL 2.0
URL:            https://crates.io/crates/alacritty_terminal
Source:         %{crates_source}
# Initial patched metadata:
# - Bump nix and parking_lot deps [0]
# - Remove windows and macos targets
# [0]: https://github.com/alacritty/alacritty/commit/67db9b2
Patch0:         alacritty_terminal-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for writing terminal emulators.}

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

%package     -n %{name}+bench-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bench-devel %{_description}

This package contains library source intended for building other packages
which use "bench" feature of "%{crate}" crate.

%files       -n %{name}+bench-devel
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
* Fri Oct 16 15:49:54 CEST 2020 returntrip <stefano@figura.im> - 0.10.0-1
- Initial package
