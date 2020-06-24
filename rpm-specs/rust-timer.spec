# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate timer

Name:           rust-%{crate}
Version:        0.2.0
Release:        5%{?dist}
Summary:        Simple timer to schedule execution of closures

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/timer
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple timer. Use it to schedule execution of closures after a delay or at a
given timestamp.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 18:41:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Regenerate

* Tue Apr 23 15:05:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-2
- Run tests in infrastructure

* Sun Apr 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
