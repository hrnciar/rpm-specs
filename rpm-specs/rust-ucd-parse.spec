# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ucd-parse

Name:           rust-%{crate}
Version:        0.1.8
Release:        1%{?dist}
Summary:        Library for parsing data files in the Unicode character database

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/ucd-parse
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for parsing data files in the Unicode character database.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Fri Mar 13 2020 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Sun Sep 08 09:19:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 08:42:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package