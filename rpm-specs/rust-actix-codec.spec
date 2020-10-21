# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate actix-codec

Name:           rust-%{crate}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Codec utilities for working with framed protocols

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/actix-codec
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Codec utilities for working with framed protocols.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGES.md
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
* Mon Sep 21 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.0-1
- Update to version 0.3.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 11:29:27 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 19:55:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-2
- Regenerate

* Fri May 31 09:15:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Initial package
