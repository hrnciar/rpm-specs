# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate libhandy

Name:           rust-%{crate}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Rust bindings for libhandy

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+
URL:            https://crates.io/crates/libhandy
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for libhandy.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v0_0_10-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v0_0_10-devel %{_description}

This package contains library source intended for building other packages
which use "v0_0_10" feature of "%{crate}" crate.

%files       -n %{name}+v0_0_10-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v0_0_6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v0_0_6-devel %{_description}

This package contains library source intended for building other packages
which use "v0_0_6" feature of "%{crate}" crate.

%files       -n %{name}+v0_0_6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v0_0_7-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v0_0_7-devel %{_description}

This package contains library source intended for building other packages
which use "v0_0_7" feature of "%{crate}" crate.

%files       -n %{name}+v0_0_7-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v0_0_8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v0_0_8-devel %{_description}

This package contains library source intended for building other packages
which use "v0_0_8" feature of "%{crate}" crate.

%files       -n %{name}+v0_0_8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v0_0_9-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v0_0_9-devel %{_description}

This package contains library source intended for building other packages
which use "v0_0_9" feature of "%{crate}" crate.

%files       -n %{name}+v0_0_9-devel
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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 17:08:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package