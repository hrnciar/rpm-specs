# Generated by rust2rpm 15
# * Tests require internet and a token
%bcond_with check
%global debug_package %{nil}

%global crate fever_api

Name:           rust-%{crate}
Version:        0.2.7
Release:        1%{?dist}
Summary:        Rust implementation of the FEVER-API

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+
URL:            https://crates.io/crates/fever_api
Source:         %{crates_source}
# Initial patched metadata
# * Fixup deps, https://pagure.io/fedora-rust/rust2rpm/issue/109
Patch0:         fever_api-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of the FEVER-API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE
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
* Fri May 22 20:07:22 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Mon May 18 2020 Josh Stone <jistone@redhat.com> - 0.2.5-1
- Update to 0.2.5

* Thu May 14 09:11:41 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.2.3-1
- Initial package