# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate liquid-lib

Name:           rust-%{crate}
Version:        0.20.2
Release:        2%{?dist}
Summary:        Liquid templating language for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/liquid-lib
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Liquid templating language for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deunicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deunicode-devel %{_description}

This package contains library source intended for building other packages
which use "deunicode" feature of "%{crate}" crate.

%files       -n %{name}+deunicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extra-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extra-devel %{_description}

This package contains library source intended for building other packages
which use "extra" feature of "%{crate}" crate.

%files       -n %{name}+extra-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+jekyll-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jekyll-devel %{_description}

This package contains library source intended for building other packages
which use "jekyll" feature of "%{crate}" crate.

%files       -n %{name}+jekyll-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+shopify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shopify-devel %{_description}

This package contains library source intended for building other packages
which use "shopify" feature of "%{crate}" crate.

%files       -n %{name}+shopify-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stdlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stdlib-devel %{_description}

This package contains library source intended for building other packages
which use "stdlib" feature of "%{crate}" crate.

%files       -n %{name}+stdlib-devel
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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.20.2-1
- Update to 0.20.2

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.20.1-1
- Update to 0.20.1

* Sun Mar 22 15:20:47 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.20.0-1
- Initial package
