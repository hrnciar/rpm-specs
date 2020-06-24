# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate md-5

Name:           rust-%{crate}
Version:        0.9.0
Release:        1%{?dist}
Summary:        MD5 hash function

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/md-5
Source:         %{crates_source}
# Initial patched metadata
# * Update block-buffer to 0.9, https://github.com/RustCrypto/hashes/commit/d24f26b1650156b1da4fced389559cee17805910
Patch0:         md-5-fix-metadata.diff
Patch0001:      0001-Update-block-buffer-to-v0.9-164.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
MD5 hash function.}

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

%package     -n %{name}+asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+asm-devel %{_description}

This package contains library source intended for building other packages
which use "asm" feature of "%{crate}" crate.

%files       -n %{name}+asm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+md5-asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+md5-asm-devel %{_description}

This package contains library source intended for building other packages
which use "md5-asm" feature of "%{crate}" crate.

%files       -n %{name}+md5-asm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Sun Jun 21 17:38:18 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 21:07:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-2
- Regenerate

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Initial package
