# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate wayland-commons

Name:           rust-%{crate}
Version:        0.26.6
Release:        2%{?dist}
Summary:        Common types and structures used by wayland-client and wayland-server

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/wayland-commons
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Common types and structures used by wayland-client and wayland-server.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.txt
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
* Fri Jun 26 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.26.6-2
- Package license and docs

* Fri Jun 26 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.26.6-1
- Update to 0.26.6-1

* Fri May 22 14:29:32 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.26.5-1
- Initial package
