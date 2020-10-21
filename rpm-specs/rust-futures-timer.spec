# Generated by rust2rpm 13
# * Circular dep with async-std
%bcond_with check
%global debug_package %{nil}

%global crate futures-timer

Name:           rust-%{crate}
Version:        3.0.2
Release:        2%{?dist}
Summary:        Timeouts for futures

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/futures-timer
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Timeouts for futures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+gloo-timers-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gloo-timers-devel %{_description}

This package contains library source intended for building other packages
which use "gloo-timers" feature of "%{crate}" crate.

%files       -n %{name}+gloo-timers-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+send_wrapper-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+send_wrapper-devel %{_description}

This package contains library source intended for building other packages
which use "send_wrapper" feature of "%{crate}" crate.

%files       -n %{name}+send_wrapper-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 07:14:30 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Mon Feb 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Package unretirement

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
