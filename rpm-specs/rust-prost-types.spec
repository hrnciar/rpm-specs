# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate prost-types

Name:           rust-%{crate}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Protocol Buffers implementation for the Rust Language

# Upstream license specification: Apache-2.0
# https://github.com/danburkert/prost/issues/353
License:        ASL 2.0
URL:            https://crates.io/crates/prost-types
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Protocol Buffers implementation for the Rust Language.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Tue Aug 25 15:49:48 BST 2020 Peter Robinson <pbrobinson@gmail.com> - 0.6.1-1
- Initial package