# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ipnetwork

Name:           rust-%{crate}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Library to work with IP CIDRs in Rust

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/ipnetwork
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to work with IP CIDRs in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.md
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

%package     -n %{name}+clippy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clippy-devel %{_description}

This package contains library source intended for building other packages
which use "clippy" feature of "%{crate}" crate.

%files       -n %{name}+clippy-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dev-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev-devel %{_description}

This package contains library source intended for building other packages
which use "dev" feature of "%{crate}" crate.

%files       -n %{name}+dev-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
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
* Tue Feb 11 14:59:45 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.16.0-1
- Update to 0.16.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:31:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-2
- Regenerate

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.1-1
- Initial package
