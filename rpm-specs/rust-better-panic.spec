# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate better-panic

Name:           rust-%{crate}
Version:        0.2.0
Release:        4%{?dist}
Summary:        Pretty panic backtraces inspired by Python's tracebacks

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/better-panic
Source:         %{crates_source}
# Initial patched metadata
# * Bump to syntect 4, https://github.com/mitsuhiko/better-panic/pull/7
Patch0:         better-panic-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pretty panic backtraces inspired by Python's tracebacks.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+syntect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syntect-devel %{_description}

This package contains library source intended for building other packages
which use "syntect" feature of "%{crate}" crate.

%files       -n %{name}+syntect-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Josh Stone <jistone@redhat.com> - 0.2.0-3
- Bump to syntect 4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 00:29:01 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
