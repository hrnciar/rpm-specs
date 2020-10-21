# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate slog-scope

Name:           rust-%{crate}
Version:        4.3.0
Release:        4%{?dist}
Summary:        Logging scopes for slog-rs

# Upstream license specification: MPL-2.0/MIT/Apache-2.0
License:        MPLv2.0 or MIT or ASL 2.0
URL:            https://crates.io/crates/slog-scope
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Logging scopes for slog-rs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE LICENSE-MPL2
%doc README.md CHANGELOG.md
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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 4.3.0-1
- Update to 4.3.0

* Sun Sep 08 09:16:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:10:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1-2
- Regenerate

* Sun Apr 28 07:54:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.1-1
- Initial package
