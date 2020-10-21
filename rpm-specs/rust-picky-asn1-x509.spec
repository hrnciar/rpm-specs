# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate picky-asn1-x509

Name:           rust-%{crate}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Provides ASN1 types defined by X.509 related RFCs

# Upstream license specification: MIT OR Apache-2.0
# https://github.com/Devolutions/picky-rs/issues/56
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/picky-asn1-x509
Source:         %{crates_source}
# Initial patched metadata
Patch0:         picky-asn1-x509-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Provides ASN1 types defined by X.509 related RFCs.}

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
* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.2-1
- Update to 0.3.2

* Tue Sep 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-1
- Initial package
