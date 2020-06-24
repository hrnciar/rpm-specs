# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate time-macros

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Procedural macros for the time crate

# Upstream license specification: MIT OR Apache-2.0
# https://github.com/time-rs/time/pull/206
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/time-macros
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Procedural macros for the time crate.}

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
* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.1.0-1
- Initial package