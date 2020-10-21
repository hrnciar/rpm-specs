# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate gl_generator

Name:           rust-%{crate}
Version:        0.14.0
Release:        3%{?dist}
Summary:        Code generators for creating bindings to the Khronos OpenGL APIs

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/gl_generator
Source:         %{crates_source}
Source1:        https://raw.githubusercontent.com/brendanzab/gl-rs/master/LICENSE

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Code generators for creating bindings to the Khronos OpenGL APIs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
# Licenses exist outside the crate in the repo's root
# https://github.com/brendanzab/gl-rs/pull/520
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

%package     -n %{name}+unstable_generator_utils-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_generator_utils-devel %{_description}

This package contains library source intended for building other packages
which use "unstable_generator_utils" feature of "%{crate}" crate.

%files       -n %{name}+unstable_generator_utils-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
cp -p %{SOURCE1} .
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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 20:43:12 CEST 2020 returntrip <stefano@figura.im> - 0.14.0-1
- Initial package