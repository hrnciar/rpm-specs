# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate magic-crypt

Name:           rust-%{crate}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Library to encrypt/decrpyt strings, files, or data, using DES or AES

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/magic-crypt
Source:         %{crates_source}
# Initial patched metadata
# * Drop digest 0.7 since we patch tiger-digest
Patch0:         magic-crypt-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
MagicCrypt is a Java/PHP/NodeJS/Rust library to encrypt/decrpyt strings, files,
or data, using Data Encryption Standard(DES) or Advanced Encryption
Standard(AES) algorithms. It supports CBC block cipher mode, PKCS5 padding and
64, 128, 192 or 256-bits key length.}

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
# It is used for tiger-digest, but we patch it to use new digest
sed -i \
  -e "s/digest_old::FixedOutput as OldFixedOutput/digest::FixedOutput/" \
  -e "/digest_old/d" \
  src/ciphers/aes192.rs
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
* Sun May 31 10:13:38 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Mon May 25 13:06:10 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Fri May 15 09:24:19 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 3.0.0-1
- Initial package
