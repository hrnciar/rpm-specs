# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate size

Name:           rust-%{crate}
Version:        0.1.2
Release:        3%{?dist}
Summary:        Units and formatting for file sizes in base2 and base10

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/size
Source:         %{crates_source}
# Part of https://github.com/neosmart/prettysize-rs/commit/e4f25aed974deb318493b2cc9c0c9e4b480c1d4c, fixes FTBFS
Patch0001:      0001-Update-to-Rust-2018-and-add-rustfmt-config.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Units and formatting for file sizes in base2 and base10.}

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 15:09:52 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.2-1
- Initial package
