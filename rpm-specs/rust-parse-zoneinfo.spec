# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate parse-zoneinfo

Name:           rust-%{crate}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Parse zoneinfo files from the IANA database

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/parse-zoneinfo
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parse zoneinfo files from the IANA database.}

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 21:40:52 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Tue Nov 05 23:25:26 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Initial package
