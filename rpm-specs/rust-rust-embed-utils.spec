# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rust-embed-utils

Name:           rust-%{crate}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Utilities for rust-embed

# Upstream license specification: MIT
# https://github.com/pyros2097/rust-embed/pull/107
License:        MIT
URL:            https://crates.io/crates/rust-embed-utils
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Utilities for rust-embed.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-embed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-embed-devel %{_description}

This package contains library source intended for building other packages
which use "debug-embed" feature of "%{crate}" crate.

%files       -n %{name}+debug-embed-devel
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
* Tue May 12 16:57:19 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 5.0.0-1
- Initial package
