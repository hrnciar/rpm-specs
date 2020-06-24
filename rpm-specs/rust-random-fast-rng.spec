# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate random-fast-rng

Name:           rust-%{crate}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rust library for Blazing fast non cryptographic random number generator

# Upstream license specification: MIT/Apache-2.0
# https://github.com/elichai/random-rs/issues/2
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/random-fast-rng
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust library for Blazing fast non cryptographic random number generator.}

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

%package     -n %{name}+doc-comment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-comment-devel %{_description}

This package contains library source intended for building other packages
which use "doc-comment" feature of "%{crate}" crate.

%files       -n %{name}+doc-comment-devel
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
* Wed Feb 12 10:16:36 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package