# Generated by rust2rpm 13
# * Many dev-deps are missing
%bcond_with check
%global debug_package %{nil}

%global crate ahash

Name:           rust-%{crate}
Version:        0.3.8
Release:        1%{?dist}
Summary:        Non-cryptographic hash function using AES-NI for high performance

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/ahash
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Non-cryptographic hash function using AES-NI for high performance.}

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
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+compile-time-rng-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compile-time-rng-devel %{_description}

This package contains library source intended for building other packages
which use "compile-time-rng" feature of "%{crate}" crate.

%files       -n %{name}+compile-time-rng-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+const-random-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const-random-devel %{_description}

This package contains library source intended for building other packages
which use "const-random" feature of "%{crate}" crate.

%files       -n %{name}+const-random-devel
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
* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.3.8-1
- Update to 0.3.8

* Sat May 16 19:38:42 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Wed May 06 2020 Josh Stone <jistone@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Josh Stone <jistone@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Fri Dec 20 20:04:40 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.18-1
- Initial package