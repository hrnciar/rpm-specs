# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate paste-impl

Name:           rust-%{crate}
Version:        0.1.18
Release:        2%{?dist}
Summary:        Implementation detail of the `paste` crate

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/paste-impl
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation detail of the `paste` crate.}

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 08:58:44 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.18-1
- Update to 0.1.18

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.1.17-1
- Update to 0.1.17

* Wed Jun 03 07:26:30 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.16-1
- Update to 0.1.16

* Sun May 31 10:25:43 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15

* Tue May 26 2020 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Sun May 24 12:42:47 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13

* Mon May 04 2020 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Wed Apr 01 2020 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Sat Mar 28 07:15:03 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Mon Mar 23 18:48:53 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Sun Feb 23 10:24:23 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 15:12:43 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 09:52:37 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.4-1
- Initial package
