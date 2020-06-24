# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate psm

Name:           rust-%{crate}
Version:        0.1.9
Release:        1%{?dist}
Summary:        Portable Stack Manipulation: stack manipulation and introspection routines

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/psm
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Portable Stack Manipulation: stack manipulation and introspection routines.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.mkd
%license LICENSE-APACHE LICENSE-MIT
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Thu May 07 2020 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 15:14:15 PST 2019 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Initial package
