# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate no-panic

Name:           rust-%{crate}
Version:        0.1.14
Release:        3%{?dist}
Summary:        Attribute macro to require that the compiler prove a function can't ever panic

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/no-panic
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Attribute macro to require that the compiler prove a function can't ever panic.}

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
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Thu Apr 09 2020 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Mon Aug 26 05:27:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Thu May 09 08:27:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Initial package
