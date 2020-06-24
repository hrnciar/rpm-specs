# Generated by rust2rpm 15
%if 0%{?__isa_bits} == 32
# https://github.com/sgrif/pq-sys/issues/32
%bcond_with check
%else
%bcond_without check
%endif
%global debug_package %{nil}

%global crate pq-sys

Name:           rust-%{crate}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Auto-generated rust bindings for libpq

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pq-sys
Source:         %{crates_source}
# Initial patched metadata
# * No windows
# * pkg-config by default
Patch0:         pq-sys-fix-metadata.diff
Patch0001:      0001-Enforce-pkg-config-feature.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Auto-generated rust bindings for libpq.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libpq)

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

%package     -n %{name}+pkg-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg-config-devel %{_description}

This package contains library source intended for building other packages
which use "pkg-config" feature of "%{crate}" crate.

%files       -n %{name}+pkg-config-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libpq)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jun 17 17:49:57 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.4.6-1
- Initial package
