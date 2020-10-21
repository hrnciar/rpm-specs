# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate thiserror-impl

Name:           rust-%{crate}
Version:        1.0.21
Release:        1%{?dist}
Summary:        Implementation detail of the `thiserror` crate

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/thiserror-impl
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation detail of the `thiserror` crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.21-1
- Update to version 1.0.21.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 1.0.20-1
- Update to 1.0.20

* Fri May 22 2020 Josh Stone <jistone@redhat.com> - 1.0.19-1
- Update to 1.0.19

* Sat May 16 19:37:01 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 1.0.17-1
- Update to 1.0.17

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 1.0.16-1
- Update to 1.0.16

* Wed Apr 15 2020 Josh Stone <jistone@redhat.com> - 1.0.15-1
- Update to 1.0.15

* Mon Mar 30 08:08:24 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14

* Mon Mar 23 18:50:24 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.13-1
- Update to 1.0.13

* Sat Mar 21 07:19:25 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12

* Fri Feb 14 20:25:18 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.11-1
- Initial package
