# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tpm2-policy

Name:           rust-%{crate}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Specify and send TPM2 policies to satisfy object authorization

# Upstream license specification: EUPL-1.2
License:        EUPL-1.2
URL:            https://crates.io/crates/tpm2-policy
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Specify and send TPM2 policies to satisfy object authorization.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Thu Aug 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-1
- Initial package

* Mon Aug 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.0-1
 - Initial package
