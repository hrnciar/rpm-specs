# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate actix

Name:           rust-%{crate}
Version:        0.10.0~alpha.3
Release:        1%{?dist}
Summary:        Actor framework for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/actix
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Actor framework for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGES.md MIGRATION.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mailbox_assert-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mailbox_assert-devel %{_description}

This package contains library source intended for building other packages
which use "mailbox_assert" feature of "%{crate}" crate.

%files       -n %{name}+mailbox_assert-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+resolver-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+resolver-devel %{_description}

This package contains library source intended for building other packages
which use "resolver" feature of "%{crate}" crate.

%files       -n %{name}+resolver-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+trust-dns-proto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trust-dns-proto-devel %{_description}

This package contains library source intended for building other packages
which use "trust-dns-proto" feature of "%{crate}" crate.

%files       -n %{name}+trust-dns-proto-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+trust-dns-resolver-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trust-dns-resolver-devel %{_description}

This package contains library source intended for building other packages
which use "trust-dns-resolver" feature of "%{crate}" crate.

%files       -n %{name}+trust-dns-resolver-devel
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
* Thu May 14 19:45:44 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0~alpha.3-1
- Update to 0.10.0-alpha.3

* Wed Mar 25 18:05:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0~alpha.2-1
- Update to 0.10.0-alpha.2

* Sat Feb 29 06:59:32 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0~alpha.1-1
- Update to 0.10.0-alpha.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 09:09:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-4
- Update parking_lot to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 10:10:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-2
- Update dependencies

* Thu May 30 18:30:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-1
- Initial package