# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate alphanumeric-sort

Name:           rust-%{crate}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Sort order for files and folders whose names contain numerals

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/alphanumeric-sort
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
This crate can help you sort order for files and folders whose names contain
numerals.}

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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Mon Jun 15 2020 Josh Stone <jistone@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Fri May 22 2020 Josh Stone <jistone@redhat.com> - 1.0.13-1
- Update to 1.0.13

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 1.0.12-1
- Update to 1.0.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 11:06:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Sun Jul 28 18:28:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 07:54:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.6-1
- Initial package
