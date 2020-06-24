# Generated by rust2rpm 13
# * Tests implicitly use pin-project
%bcond_with check
%global debug_package %{nil}

%global crate pin-project-internal

Name:           rust-%{crate}
Version:        0.4.22
Release:        1%{?dist}
Summary:        Internal crate to support pin_project - do not use directly

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/pin-project-internal
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Internal crate to support pin_project - do not use directly.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.4.22-1
- Update to 0.4.22

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.4.20-1
- Update to 0.4.20

* Fri Jun 05 2020 Josh Stone <jistone@redhat.com> - 0.4.19-1
- Update to 0.4.19

* Mon May 18 2020 Josh Stone <jistone@redhat.com> - 0.4.17-1
- Update to 0.4.17

* Mon May 11 2020 Josh Stone <jistone@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Thu May 07 2020 Josh Stone <jistone@redhat.com> - 0.4.13-1
- Update to 0.4.13

* Mon May 04 2020 Josh Stone <jistone@redhat.com> - 0.4.10-1
- Update to 0.4.10

* Tue Apr 14 2020 Josh Stone <jistone@redhat.com> - 0.4.9-1
- Update to 0.4.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.4.8-1
- Update to 0.4.8

* Fri Dec 13 21:10:21 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.6-1
- Initial package
