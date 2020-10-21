# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate jobserver

Name:           rust-%{crate}
Version:        0.1.21
Release:        2%{?dist}
Summary:        Implementation of the GNU make jobserver for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/jobserver
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of the GNU make jobserver for Rust.}

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
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 0.1.21-1
- Update to 0.1.21

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.1.19-1
- Update to 0.1.19

* Fri Nov 15 2019 Josh Stone <jistone@redhat.com> - 0.1.17-1
- Update to 0.1.17

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.1.11-6
- Adapt to new packaging

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-5
- Rebuild to trigger tests

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-4
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-2
- Bump tokio-process to 0.2

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Tue Mar 13 2018 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Initial package
