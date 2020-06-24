# Generated by rust2rpm 13
# * https://github.com/RReverser/serde-xml-rs/issues/101
%bcond_with check
%global debug_package %{nil}

%global crate serde-xml-rs

Name:           rust-%{crate}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Xml-rs based deserializer for Serde (compatible with 0.9+)

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/serde-xml-rs
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Xml-rs based deserializer for Serde (compatible with 0.9+).}

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
* Sat May 16 20:50:55 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 19:46:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-2
- Regenerate

* Sat Apr 27 09:30:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Initial package
