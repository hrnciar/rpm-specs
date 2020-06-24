# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate subtle

Name:           rust-%{crate}
Version:        2.2.3
Release:        1%{?dist}
Summary:        Pure-Rust traits and utilities for constant-time cryptographic implementations

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/subtle
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure-Rust traits and utilities for constant-time cryptographic implementations.}

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

%package     -n %{name}+i128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages
which use "i128" feature of "%{crate}" crate.

%files       -n %{name}+i128-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
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
* Mon Jun 01 14:04:55 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 13:44:49 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Sat Sep 28 08:43:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Sat Aug 03 14:56:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:52:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-2
- Regenerate

* Tue Apr 30 08:34:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Initial package