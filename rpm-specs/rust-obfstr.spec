# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate obfstr

Name:           rust-%{crate}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Compiletime string literal obfuscation for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/obfstr
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compiletime string literal obfuscation for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license license.txt
%doc readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages
which use "rand" feature of "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unsafe_static_str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unsafe_static_str-devel %{_description}

This package contains library source intended for building other packages
which use "unsafe_static_str" feature of "%{crate}" crate.

%files       -n %{name}+unsafe_static_str-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 17:44:52 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.1-1
- Initial package
