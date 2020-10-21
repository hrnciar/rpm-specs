# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate rand_xoshiro

Name:           rust-%{crate}
Version:        0.4.0
Release:        3%{?dist}
Summary:        Xoshiro, xoroshiro and splitmix64 random number generators

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rand_xoshiro
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Xoshiro, xoroshiro and splitmix64 random number generators.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 18:53:32 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Sun Aug 04 10:36:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 16:45:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Regenerate

* Sun Jun 09 17:05:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-2
- Regenerate

* Thu May 30 16:49:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Release 0.2.0

* Wed Mar 20 09:35:16 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Run tests in infrastructure

* Fri Mar 08 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
