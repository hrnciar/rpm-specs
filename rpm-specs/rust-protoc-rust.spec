# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate protoc-rust

Name:           rust-%{crate}
Version:        2.14.0
Release:        1%{?dist}
Summary:        Protoc --rust_out=.. available as API

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/protoc-rust
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Protoc --rust_out=... available as API. protoc needs to be in $PATH, protoc-
gen-run does not.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.txt
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
* Wed Apr 15 2020 Josh Stone <jistone@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Fri Mar 27 07:55:43 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.12.0-1
- Update to 2.12.0

* Mon Mar 02 2020 Josh Stone <jistone@redhat.com> - 2.10.2-1
- Update to 2.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Josh Stone <jistone@redhat.com> - 2.10.1-1
- Update to 2.10.1

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 2.10.0-1
- Update to 2.10.0

* Mon Nov 11 14:45:34 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.1-1
- Initial package
