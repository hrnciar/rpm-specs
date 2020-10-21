# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate instant

Name:           rust-%{crate}
Version:        0.1.6
Release:        1%{?dist}
Summary:        Partial replacement for std::time::Instant that works on WASM too

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/instant
Source:         %{crates_source}
# Initial patched metadata
# * Remove wasm dependencies
Patch0:         instant-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Partial replacement for std::time::Instant that works on WASM too.}

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

%package     -n %{name}+now-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+now-devel %{_description}

This package contains library source intended for building other packages
which use "now" feature of "%{crate}" crate.

%files       -n %{name}+now-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages
which use "time" feature of "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
rm tests/wasm.rs
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
* Tue Aug 25 16:17:36 PDT 2020 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Initial package