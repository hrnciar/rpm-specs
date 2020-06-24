# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate pnet_base

Name:           rust-%{crate}
Version:        0.26.0
Release:        1%{?dist}
Summary:        Fundamental base types and code used by pnet

# Upstream license specification: MIT/Apache-2.0
# https://github.com/libpnet/libpnet/issues/371
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pnet_base
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fundamental base types and code used by pnet.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Sat May 16 20:41:17 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0

* Tue Feb 11 14:50:34 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.25.0-1
- Update to 0.25.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 10:14:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-3
- Regenerate

* Tue Apr 16 09:02:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- Fixes in packaging

* Wed Apr 10 2019 Sayan Chowdhury <sayanchowdhury@fedoraproject.org> - 0.22.0-1
- Initial package