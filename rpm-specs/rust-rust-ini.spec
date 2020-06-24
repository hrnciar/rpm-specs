# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate rust-ini

Name:           rust-%{crate}
Version:        0.13.0
Release:        6%{?dist}
Summary:        Ini configuration file parsing library in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rust-ini
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Ini configuration file parsing library in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.rst
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 21:33:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-4
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.13.0-2
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.2-3
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.1-1
- Initial package