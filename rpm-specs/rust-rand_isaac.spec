# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate rand_isaac

Name:           rust-%{crate}
Version:        0.2.0
Release:        3%{?dist}
Summary:        ISAAC random number generator

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rand_isaac
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
ISAAC random number generator.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE COPYRIGHT
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 04 10:33:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 09:22:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-6
- Regenerate

* Sun Jun 09 15:07:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-5
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-4
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Run tests in infrastructure

* Fri Nov 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
