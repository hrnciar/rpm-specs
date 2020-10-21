# Generated by rust2rpm 9
%bcond_with check
%global debug_package %{nil}

%global crate brotli-sys

Name:           rust-%{crate}
Version:        0.3.2
Release:        4%{?dist}
Summary:        Raw bindings to libbrotli

# Upstream license specification: MIT/Apache-2.0
# https://github.com/alexcrichton/brotli2-rs/issues/28
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/brotli-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(cc/default) >= 1.0.0 with crate(cc/default) < 2.0.0)
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)

%global _description %{expand:
Raw bindings to libbrotli.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(brotli) = 0.6.0

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 09:32:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Initial package
