# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rust_decimal

Name:           rust-%{crate}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Decimal Implementation written in pure Rust suitable for financial calculations

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rust_decimal
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Decimal Implementation written in pure Rust suitable for financial
calculations.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md VERSION.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+byteorder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+byteorder-devel %{_description}

This package contains library source intended for building other packages
which use "byteorder" feature of "%{crate}" crate.

%files       -n %{name}+byteorder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytes-devel %{_description}

This package contains library source intended for building other packages
which use "bytes" feature of "%{crate}" crate.

%files       -n %{name}+bytes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+diesel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+diesel-devel %{_description}

This package contains library source intended for building other packages
which use "diesel" feature of "%{crate}" crate.

%files       -n %{name}+diesel-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+postgres-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+postgres-devel %{_description}

This package contains library source intended for building other packages
which use "postgres" feature of "%{crate}" crate.

%files       -n %{name}+postgres-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-float-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-float-devel %{_description}

This package contains library source intended for building other packages
which use "serde-float" feature of "%{crate}" crate.

%files       -n %{name}+serde-float-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-pg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-pg-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-pg" feature of "%{crate}" crate.

%files       -n %{name}+tokio-pg-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-postgres-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-postgres-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-postgres" feature of "%{crate}" crate.

%files       -n %{name}+tokio-postgres-devel
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
* Wed May 20 09:07:19 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Fri May 08 2020 Josh Stone <jistone@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Apr 15 2020 Josh Stone <jistone@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Mon Mar 23 06:53:16 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Feb 28 19:14:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Tue Feb 11 09:58:57 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:34:29 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Initial package