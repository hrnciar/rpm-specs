# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate nix

Name:           rust-%{crate}0.17
Version:        0.17.0
Release:        1%{?dist}
Summary:        Rust friendly bindings to *nix APIs

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/nix
Source:         %{crates_source}
# Initial patched metadata
# * No dragonfly/freebsd
Patch0:         nix-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust friendly bindings to *nix APIs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md CONVENTIONS.md README.md
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
# Testing parts are not distributed
%cargo_test -- --doc
%endif

%changelog
* Sun Oct 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.17.0-1
- Initial compat package for nix 0.17
