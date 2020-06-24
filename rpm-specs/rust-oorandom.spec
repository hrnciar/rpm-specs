# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate oorandom

Name:           rust-%{crate}
Version:        11.1.2
Release:        1%{?dist}
Summary:        Tiny, robust PRNG implementation

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/oorandom
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Tiny, robust PRNG implementation.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 11.1.2-1
- Update to 11.1.2

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 11.1.1-1
- Update to 11.1.1

* Sat Feb 29 17:10:23 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 11.1.0-1
- Initial package