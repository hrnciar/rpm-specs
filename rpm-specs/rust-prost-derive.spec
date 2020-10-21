# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate prost-derive

Name:           rust-%{crate}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Protocol Buffers implementation for the Rust Language

# Upstream license specification: Apache-2.0
# https://github.com/danburkert/prost/issues/353
License:        ASL 2.0
URL:            https://crates.io/crates/prost-derive
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
# %license LICENSE
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
* Sun Aug 02 2020 Peter Robinson <pbrobinson@fedorapeople.org> - 0.6.1-1
- Initial package
