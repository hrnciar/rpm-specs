# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate crypto-mac

Name:           rust-%{crate}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Trait for Message Authentication Code (MAC) algorithms

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/crypto-mac
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Trait for Message Authentication Code (MAC) algorithms.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+blobby-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blobby-devel %{_description}

This package contains library source intended for building other packages
which use "blobby" feature of "%{crate}" crate.

%files       -n %{name}+blobby-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dev-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev-devel %{_description}

This package contains library source intended for building other packages
which use "dev" feature of "%{crate}" crate.

%files       -n %{name}+dev-devel
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
* Sun Jun 21 10:04:50 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 0.7.0-5
- Bump generic-array to 0.13

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:21:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-2
- Regenerate

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Initial package
