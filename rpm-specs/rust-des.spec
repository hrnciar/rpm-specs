# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate des

Name:           rust-%{crate}
Version:        0.4.0
Release:        1%{?dist}
Summary:        DES and Triple DES (3DES, TDES) block ciphers implementation

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/des
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
DES and Triple DES (3DES, TDES) block ciphers implementation.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
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
* Mon Jun 22 08:15:06 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu May 14 08:24:10 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
