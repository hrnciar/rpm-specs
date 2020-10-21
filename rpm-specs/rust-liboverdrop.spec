# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate liboverdrop

Name:           rust-%{crate}
Version:        0.0.2
Release:        4%{?dist}
Summary:        Configuration library, with directory overlaying and fragments dropins

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/liboverdrop
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Configuration library, with directory overlaying and fragments dropins.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYRIGHT LICENSE-APACHE-2.0 LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Robert Fairley <rfairley@redhat.com> - 0.0.2-1
- Update to 0.0.2

* Thu Jun 20 23:51:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.1-2
- Add docs

* Thu Jun 20 19:50:01 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.0.1-1
- Initial package (RHBZ#1720724)
- Also use rust2rpm 10 to generate specfile with dynamic DynamicBuildRequires
