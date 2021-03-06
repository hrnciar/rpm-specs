# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate pure-rust-locales

Name:           rust-%{crate}
Version:        0.5.3
Release:        1%{?dist}
Summary:        Pure Rust locales imported directly from the GNU C Library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/pure-rust-locales
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure Rust locales imported directly from the GNU C Library. `LC_COLLATE` and
`LC_CTYPE` are not yet supported.}

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
* Fri Oct 09 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.3-1
- Update to version 0.5.3.

* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.2-1
- Initial package
